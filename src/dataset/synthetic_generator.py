"""
Synthetic Generator: memanggil LLM via OpenRouter untuk menghasilkan
pasangan data (question + answer + distractors) dari PromptInput.
"""
from __future__ import annotations

import os
import time
from dataclasses import dataclass
from typing import Optional

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

from src.dataset.prompt_constructor import PromptInput
from src.dataset.validator import RawDataPoint

load_dotenv(override=True)

GENERATION_SYSTEM_PROMPT = """Kamu adalah pembuat soal kuis Python untuk siswa Indonesia.
Berikan output HANYA dalam format berikut (tanpa teks lain, tanpa penjelasan tambahan):
Pertanyaan: <pertanyaan>? Jawaban benar: <jawaban>. Distraktor: 1) <d1> 2) <d2> 3) <d3> 4) <d4>

Pastikan:
- Pertanyaan dalam bahasa Indonesia yang natural
- Jawaban benar sesuai konteks materi
- 4 distraktor yang plausible dan pedagogis (menguji miskonsepsi umum)
- Tidak ada teks lain selain format di atas"""


def _build_llm_client() -> ChatOpenAI:
    """Membuat LLM client dari environment variables."""
    api_key = os.getenv("ZAI_API_KEY")
    base_url = os.getenv("ZAI_API_BASE", "https://api.z.ai/api/paas/v4")
    model = os.getenv("ZAI_MODEL", "glm-4.7")

    print(f"[DEBUG] model={model}, base_url={base_url}, api_key={'SET' if api_key else 'MISSING'}")

    return ChatOpenAI(
        model=model,
        api_key=api_key,
        base_url=base_url,
        temperature=float(os.getenv("ZAI_TEMPERATURE", "0.7")),
        max_completion_tokens=int(os.getenv("ZAI_MAX_TOKENS", "2000")),
    )


def _parse_target(raw_text: str) -> Optional[str]:
    """
    Validasi dan normalisasi output LLM.
    Mengembalikan target string yang valid, atau None jika format salah.
    """
    text = raw_text.strip()
    required = ["Pertanyaan:", "Jawaban benar:", "Distraktor:"]
    if all(marker in text for marker in required):
        return text
    return None


def generate_datapoint(
    prompt_input: PromptInput,
    llm_client: Optional[ChatOpenAI] = None,
    max_retries: int = 2,
) -> Optional[RawDataPoint]:
    """
    Memanggil LLM dan mengembalikan RawDataPoint, atau None jika semua retry gagal.

    Args:
        prompt_input: PromptInput dari Prompt Constructor
        llm_client: LangChain ChatOpenAI client (dibuat otomatis jika None)
        max_retries: jumlah maksimal retry setelah gagal

    Returns:
        RawDataPoint jika berhasil, None jika gagal setelah semua retry
    """
    if llm_client is None:
        llm_client = _build_llm_client()

    messages = [
        SystemMessage(content=GENERATION_SYSTEM_PROMPT),
        HumanMessage(content=prompt_input.input),
    ]

    last_error: Optional[Exception] = None

    for attempt in range(max_retries + 1):
        try:
            response = llm_client.invoke(messages)
            raw_text = response.content

            target = _parse_target(raw_text)
            if target is None:
                # Format salah — retry
                last_error = ValueError(
                    f"Format output LLM tidak valid: '{raw_text[:100]}'"
                )
                if attempt < max_retries:
                    time.sleep(2 ** attempt)  # exponential backoff: 1s, 2s
                continue

            # Bangun metadata dari chunk + params
            metadata = {
                "difficulty": prompt_input.params.difficulty,
                "question_type": prompt_input.params.question_type,
                "concept": prompt_input.params.concept,
                "misconception_tags": [],  # diisi saat human validation
                "source_file": prompt_input.chunk.source_file,
                "section": prompt_input.chunk.section_heading,
                "source": "synthetic",
                "validated": False,
            }

            return RawDataPoint(
                input=prompt_input.input,
                target=target,
                metadata=metadata,
                source="synthetic",
            )

        except Exception as e:
            last_error = e
            if attempt < max_retries:
                # Exponential backoff: 1s, 2s, 4s
                wait = 2 ** attempt
                print(f"[WARNING] LLM error (attempt {attempt + 1}): {e}. Retry in {wait}s...")
                time.sleep(wait)

    print(f"[ERROR] generate_datapoint gagal setelah {max_retries + 1} percobaan: {last_error}")
    return None


def generate_batch(
    prompt_inputs: list[PromptInput],
    llm_client: Optional[ChatOpenAI] = None,
    max_retries: int = 2,
    delay_between: float = 0.5,
) -> tuple[list[RawDataPoint], int]:
    """
    Generate batch data points dari list PromptInput.

    Returns:
        (results, failed_count)
    """
    if llm_client is None:
        llm_client = _build_llm_client()

    results: list[RawDataPoint] = []
    failed = 0

    for i, prompt_input in enumerate(prompt_inputs):
        result = generate_datapoint(prompt_input, llm_client, max_retries)
        if result is not None:
            results.append(result)
        else:
            failed += 1

        # Rate limiting
        if i < len(prompt_inputs) - 1 and delay_between > 0:
            time.sleep(delay_between)

    return results, failed

"""
Prompt Constructor: membangun string input dari Chunk + TaskParams.
Format input konsisten untuk fine-tuning IndoT5.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import List

from src.dataset.chunker import Chunk

VALID_DIFFICULTIES = {"easy", "medium", "hard"}
VALID_QUESTION_TYPES = {"MCQ", "Code Completion"}

PROMPT_TEMPLATE = (
    "Konteks: {context}\n\n"
    "Prompt: Buat satu soal {question_type} tentang {concept}, "
    "tingkat kesulitan: {difficulty}, bahasa Indonesia."
)


@dataclass
class TaskParams:
    concept: str        # konsep yang diuji, dari Master Concept List
    difficulty: str     # "easy" | "medium" | "hard"
    question_type: str  # "MCQ" | "Code Completion"

    def __post_init__(self) -> None:
        if self.difficulty not in VALID_DIFFICULTIES:
            raise ValueError(
                f"difficulty harus salah satu dari {VALID_DIFFICULTIES}, "
                f"bukan '{self.difficulty}'"
            )
        if self.question_type not in VALID_QUESTION_TYPES:
            raise ValueError(
                f"question_type harus salah satu dari {VALID_QUESTION_TYPES}, "
                f"bukan '{self.question_type}'"
            )


@dataclass
class PromptInput:
    input: str          # string input lengkap untuk model
    chunk: Chunk        # chunk asal
    params: TaskParams  # parameter tugas


def build_prompt(chunk: Chunk, params: TaskParams) -> PromptInput:
    """
    Membangun satu PromptInput dari chunk dan parameter.
    Code block dalam context dipertahankan apa adanya.
    """
    input_str = PROMPT_TEMPLATE.format(
        context=chunk.text,
        question_type=params.question_type,
        concept=params.concept,
        difficulty=params.difficulty,
    )
    return PromptInput(input=input_str, chunk=chunk, params=params)


def build_prompts_for_chunk(
    chunk: Chunk,
    concepts: List[str],
    difficulties: List[str] | None = None,
    question_types: List[str] | None = None,
) -> List[PromptInput]:
    """
    Menghasilkan beberapa PromptInput dari satu chunk dengan kombinasi parameter.
    Default: semua difficulty × semua question_type untuk setiap concept.
    """
    if difficulties is None:
        difficulties = ["easy", "medium", "hard"]
    if question_types is None:
        question_types = ["MCQ"]

    prompts: List[PromptInput] = []
    for concept in concepts:
        for difficulty in difficulties:
            for qtype in question_types:
                params = TaskParams(
                    concept=concept,
                    difficulty=difficulty,
                    question_type=qtype,
                )
                prompts.append(build_prompt(chunk, params))
    return prompts

## Hasil Train Finetune Tahap 2
Detected Google Colab environment. Installing dependencies...
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100.8/100.8 kB 4.4 MB/s eta 0:00:00
Google Drive already mounted.
Current Working Directory: /content/AQG
Loading dataset from: ./dataset_aqg/dataset-task-spesifc
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
Map: 100% 175/175 [00:01<00:00, 98.77 examples/s]
Dataset loaded: 876 train samples
Dataset validation: 175 samples
Loading weights: 100% 284/284 [00:00<00:00, 921.59it/s, Materializing param=shared.weight]
The tied weights mapping and config for this model specifies to tie shared.weight to lm_head.weight, but both are present in the checkpoints, so we will NOT tie them. You should update the config with `tie_word_embeddings=False` to silence this warning
The tied weights mapping and config for this model specifies to tie shared.weight to encoder.embed_tokens.weight, but both are present in the checkpoints, so we will NOT tie them. You should update the config with `tie_word_embeddings=False` to silence this warning
The tied weights mapping and config for this model specifies to tie shared.weight to decoder.embed_tokens.weight, but both are present in the checkpoints, so we will NOT tie them. You should update the config with `tie_word_embeddings=False` to silence this warning
Loading and merging domain adapter from: /content/drive/MyDrive/IndoT5-Python-Adapter/final_adapter
Domain adapter merged successfully.
/usr/local/lib/python3.12/dist-packages/peft/tuners/tuners_utils.py:285: UserWarning: Already found a `peft_config` attribute in the model. This will lead to having multiple adapters in the model. Make sure to know what you are doing!
  warnings.warn(
trainable params: 884,736 || all params: 297,811,200 || trainable%: 0.2971
Downloading builder script: 6.14kB [00:00, 15.7MB/s]
Downloading builder script: 8.15kB [00:00, 13.5MB/s]
warmup_ratio is deprecated and will be removed in v5.2. Use `warmup_steps` instead.
{'loss': '18.42', 'grad_norm': '0.2156', 'learning_rate': '0.0001892', 'epoch': '0.4566'}
{'loss': '17.93', 'grad_norm': '0.4778', 'learning_rate': '0.0001556', 'epoch': '0.9132'}
 33% 110/330 [03:42<06:16,  1.71s/it]
  0% 0/44 [00:00<?, ?it/s]
  5% 2/44 [00:01<00:24,  1.74it/s]
  7% 3/44 [00:02<00:33,  1.24it/s]
  9% 4/44 [00:03<00:36,  1.08it/s]
 11% 5/44 [00:04<00:38,  1.01it/s]
 14% 6/44 [00:05<00:39,  1.03s/it]
 16% 7/44 [00:06<00:39,  1.06s/it]
 18% 8/44 [00:07<00:38,  1.08s/it]
 20% 9/44 [00:09<00:39,  1.12s/it]
 23% 10/44 [00:10<00:38,  1.12s/it]
 25% 11/44 [00:11<00:38,  1.18s/it]
 27% 12/44 [00:12<00:39,  1.23s/it]
 30% 13/44 [00:14<00:39,  1.27s/it]
 32% 14/44 [00:15<00:36,  1.23s/it]
 34% 15/44 [00:16<00:34,  1.20s/it]
 36% 16/44 [00:17<00:33,  1.18s/it]
 39% 17/44 [00:18<00:31,  1.17s/it]
 41% 18/44 [00:19<00:30,  1.16s/it]
 43% 19/44 [00:21<00:28,  1.14s/it]
 45% 20/44 [00:22<00:27,  1.14s/it]
 48% 21/44 [00:23<00:26,  1.13s/it]
 50% 22/44 [00:24<00:24,  1.13s/it]
 52% 23/44 [00:25<00:24,  1.17s/it]
 55% 24/44 [00:26<00:24,  1.20s/it]
 57% 25/44 [00:28<00:23,  1.26s/it]
 59% 26/44 [00:29<00:21,  1.22s/it]
 61% 27/44 [00:30<00:20,  1.19s/it]
 64% 28/44 [00:31<00:18,  1.16s/it]
 66% 29/44 [00:32<00:17,  1.16s/it]
 68% 30/44 [00:33<00:16,  1.14s/it]
 70% 31/44 [00:35<00:14,  1.14s/it]
 73% 32/44 [00:36<00:13,  1.13s/it]
 75% 33/44 [00:37<00:12,  1.13s/it]
 77% 34/44 [00:38<00:11,  1.16s/it]
 80% 35/44 [00:39<00:10,  1.21s/it]
 82% 36/44 [00:41<00:09,  1.23s/it]
 84% 37/44 [00:42<00:08,  1.25s/it]
 86% 38/44 [00:43<00:07,  1.21s/it]
 89% 39/44 [00:44<00:05,  1.19s/it]
 91% 40/44 [00:45<00:04,  1.17s/it]
 93% 41/44 [00:46<00:03,  1.16s/it]
 95% 42/44 [00:48<00:02,  1.15s/it]
 98% 43/44 [00:49<00:01,  1.15s/it]
                                     
{'eval_loss': '8.267', 'eval_rouge_l': '0.0039', 'eval_bleu_4': '0.0219', 'eval_distinct_1': '14.88', 'eval_distinct_2': '39.4', 'eval_runtime': '51.91', 'eval_samples_per_second': '3.371', 'eval_steps_per_second': '0.848', 'epoch': '1'}
 33% 110/330 [04:34<06:16,  1.71s/it]
100% 44/44 [00:50<00:00,  1.09s/it]
{'loss': '17.1', 'grad_norm': '0.7015', 'learning_rate': '0.0001219', 'epoch': '1.365'}
{'loss': '16.83', 'grad_norm': '0.764', 'learning_rate': '8.822e-05', 'epoch': '1.822'}
 67% 220/330 [08:15<03:08,  1.72s/it]
  0% 0/44 [00:00<?, ?it/s]
  5% 2/44 [00:01<00:23,  1.77it/s]
  7% 3/44 [00:02<00:33,  1.24it/s]
  9% 4/44 [00:03<00:39,  1.01it/s]
 11% 5/44 [00:04<00:42,  1.10s/it]
 14% 6/44 [00:06<00:45,  1.20s/it]
 16% 7/44 [00:07<00:43,  1.18s/it]
 18% 8/44 [00:08<00:41,  1.16s/it]
 20% 9/44 [00:09<00:40,  1.15s/it]
 23% 10/44 [00:10<00:38,  1.14s/it]
 25% 11/44 [00:11<00:37,  1.13s/it]
 27% 12/44 [00:13<00:36,  1.14s/it]
 30% 13/44 [00:14<00:35,  1.14s/it]
 32% 14/44 [00:15<00:34,  1.14s/it]
 34% 15/44 [00:16<00:34,  1.18s/it]
 36% 16/44 [00:17<00:34,  1.23s/it]
 39% 17/44 [00:19<00:33,  1.24s/it]
 41% 18/44 [00:20<00:32,  1.23s/it]
 43% 19/44 [00:21<00:30,  1.20s/it]
 45% 20/44 [00:22<00:28,  1.18s/it]
 48% 21/44 [00:23<00:26,  1.17s/it]
 50% 22/44 [00:24<00:25,  1.17s/it]
 52% 23/44 [00:26<00:24,  1.15s/it]
 55% 24/44 [00:27<00:22,  1.15s/it]
 57% 25/44 [00:28<00:21,  1.14s/it]
 59% 26/44 [00:29<00:20,  1.14s/it]
 61% 27/44 [00:30<00:20,  1.19s/it]
 64% 28/44 [00:32<00:19,  1.25s/it]
 66% 29/44 [00:33<00:19,  1.28s/it]
 68% 30/44 [00:34<00:17,  1.24s/it]
 70% 31/44 [00:35<00:15,  1.20s/it]
 73% 32/44 [00:36<00:14,  1.18s/it]
 75% 33/44 [00:38<00:13,  1.19s/it]
 77% 34/44 [00:39<00:11,  1.17s/it]
 80% 35/44 [00:40<00:10,  1.17s/it]
 82% 36/44 [00:41<00:09,  1.16s/it]
 84% 37/44 [00:42<00:08,  1.15s/it]
 86% 38/44 [00:43<00:06,  1.14s/it]
 89% 39/44 [00:45<00:05,  1.19s/it]
 91% 40/44 [00:46<00:04,  1.22s/it]
 93% 41/44 [00:47<00:03,  1.27s/it]
 95% 42/44 [00:48<00:02,  1.23s/it]
 98% 43/44 [00:50<00:01,  1.20s/it]
                                     
{'eval_loss': '7.809', 'eval_rouge_l': '0.0066', 'eval_bleu_4': '0', 'eval_distinct_1': '8.82', 'eval_distinct_2': '23.1', 'eval_runtime': '52.49', 'eval_samples_per_second': '3.334', 'eval_steps_per_second': '0.838', 'epoch': '2'}
 67% 220/330 [09:08<03:08,  1.72s/it]
100% 44/44 [00:51<00:00,  1.14s/it]
{'loss': '16.49', 'grad_norm': '0.8417', 'learning_rate': '5.455e-05', 'epoch': '2.274'}
{'loss': '16.47', 'grad_norm': '1.065', 'learning_rate': '2.088e-05', 'epoch': '2.731'}
100% 330/330 [12:53<00:00,  1.72s/it]
  0% 0/44 [00:00<?, ?it/s]
  5% 2/44 [00:01<00:23,  1.76it/s]
  7% 3/44 [00:02<00:32,  1.25it/s]
  9% 4/44 [00:03<00:36,  1.08it/s]
 11% 5/44 [00:04<00:40,  1.04s/it]
 14% 6/44 [00:05<00:43,  1.13s/it]
 16% 7/44 [00:07<00:45,  1.23s/it]
 18% 8/44 [00:08<00:43,  1.20s/it]
 20% 9/44 [00:09<00:41,  1.18s/it]
 23% 10/44 [00:10<00:39,  1.16s/it]
 25% 11/44 [00:11<00:37,  1.15s/it]
 27% 12/44 [00:13<00:36,  1.15s/it]
 30% 13/44 [00:14<00:35,  1.14s/it]
 32% 14/44 [00:15<00:34,  1.14s/it]
 34% 15/44 [00:16<00:33,  1.14s/it]
 36% 16/44 [00:17<00:32,  1.18s/it]
 39% 17/44 [00:19<00:32,  1.21s/it]
 41% 18/44 [00:20<00:32,  1.24s/it]
 43% 19/44 [00:21<00:31,  1.25s/it]
 45% 20/44 [00:22<00:29,  1.21s/it]
 48% 21/44 [00:23<00:27,  1.19s/it]
 50% 22/44 [00:25<00:25,  1.17s/it]
 52% 23/44 [00:26<00:24,  1.16s/it]
 55% 24/44 [00:27<00:23,  1.15s/it]
 57% 25/44 [00:28<00:21,  1.14s/it]
 59% 26/44 [00:29<00:20,  1.13s/it]
 61% 27/44 [00:30<00:19,  1.14s/it]
 64% 28/44 [00:32<00:19,  1.21s/it]
 66% 29/44 [00:33<00:18,  1.25s/it]
 68% 30/44 [00:34<00:17,  1.28s/it]
 70% 31/44 [00:35<00:16,  1.23s/it]
 73% 32/44 [00:36<00:14,  1.20s/it]
 75% 33/44 [00:38<00:12,  1.18s/it]
 77% 34/44 [00:39<00:11,  1.16s/it]
 80% 35/44 [00:40<00:10,  1.16s/it]
 82% 36/44 [00:41<00:09,  1.15s/it]
 84% 37/44 [00:42<00:08,  1.14s/it]
 86% 38/44 [00:43<00:06,  1.14s/it]
 89% 39/44 [00:44<00:05,  1.14s/it]
 91% 40/44 [00:46<00:04,  1.18s/it]
 93% 41/44 [00:47<00:03,  1.23s/it]
 95% 42/44 [00:48<00:02,  1.28s/it]
 98% 43/44 [00:50<00:01,  1.23s/it]
                                     
{'eval_loss': '7.724', 'eval_rouge_l': '0.0074', 'eval_bleu_4': '0', 'eval_distinct_1': '9.12', 'eval_distinct_2': '24.93', 'eval_runtime': '52.48', 'eval_samples_per_second': '3.335', 'eval_steps_per_second': '0.838', 'epoch': '3'}
100% 330/330 [13:46<00:00,  1.72s/it]
100% 44/44 [00:51<00:00,  1.17s/it]
{'train_runtime': '829.8', 'train_samples_per_second': '3.167', 'train_steps_per_second': '0.398', 'train_loss': '17.11', 'epoch': '3'}
100% 330/330 [13:49<00:00,  2.51s/it]


## Hasil testing
===== HASIL EVALUASI TEST SET (Tahap 2 AQG) =====
  ROUGE-L    : 0.0908
  BLEU-4     : 4.2354
  Distinct-1 : 8.83%
  Distinct-2 : 19.77%
  eval_loss  : 9.7146
  Runtime    : 270.84s
=================================================
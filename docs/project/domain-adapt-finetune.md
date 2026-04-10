## Hasil Finetune 
Detected Colab. Installing dependencies...
Menggunakan GPU: Tesla T4
Loading dataset dari: ./dataset_aqg/output_domain/accumulated.jsonl
Split selesai: train=272, validation=34, test=34
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
Tokenizing domain dataset: 100% 272/272 [00:00<00:00, 356.99 examples/s]
Tokenizing domain dataset: 100% 34/34 [00:00<00:00, 541.41 examples/s]
Tokenizing domain dataset: 100% 34/34 [00:00<00:00, 546.21 examples/s]
SUCCESS: Tokenisasi selesai untuk semua split.
Loading weights: 100% 284/284 [00:00<00:00, 1161.23it/s, Materializing param=shared.weight]
The tied weights mapping and config for this model specifies to tie shared.weight to lm_head.weight, but both are present in the checkpoints, so we will NOT tie them. You should update the config with `tie_word_embeddings=False` to silence this warning
The tied weights mapping and config for this model specifies to tie shared.weight to encoder.embed_tokens.weight, but both are present in the checkpoints, so we will NOT tie them. You should update the config with `tie_word_embeddings=False` to silence this warning
The tied weights mapping and config for this model specifies to tie shared.weight to decoder.embed_tokens.weight, but both are present in the checkpoints, so we will NOT tie them. You should update the config with `tie_word_embeddings=False` to silence this warning
trainable params: 884,736 || all params: 297,811,200 || trainable%: 0.2971
warmup_ratio is deprecated and will be removed in v5.2. Use `warmup_steps` instead.
Memulai Domain Adaptation (Tahap 1)...
  Train  : 272 sampel
  Val    : 34 sampel
  Test   : 34 sampel
{'loss': '19.85', 'grad_norm': '0.05444', 'learning_rate': '8.571e-05', 'epoch': '0.2941'}
{'loss': '19.85', 'grad_norm': '0.07396', 'learning_rate': '0.000181', 'epoch': '0.5882'}
{'loss': '19.84', 'grad_norm': '0.1131', 'learning_rate': '0.0001913', 'epoch': '0.8824'}
 17% 34/204 [01:03<05:30,  1.94s/it]
  0% 0/9 [00:00<?, ?it/s]
 22% 2/9 [00:00<00:01,  4.08it/s]
 33% 3/9 [00:00<00:01,  3.52it/s]
 44% 4/9 [00:01<00:01,  2.56it/s]
 56% 5/9 [00:01<00:01,  2.50it/s]
 67% 6/9 [00:02<00:01,  2.47it/s]
 78% 7/9 [00:02<00:00,  2.51it/s]
 89% 8/9 [00:03<00:00,  2.44it/s]
                                    
{'eval_loss': '9.86', 'eval_runtime': '4.061', 'eval_samples_per_second': '8.372', 'eval_steps_per_second': '2.216', 'epoch': '1'}
 17% 34/204 [01:07<05:30,  1.94s/it]
100% 9/9 [00:03<00:00,  2.54it/s]
{'loss': '19.79', 'grad_norm': '0.09695', 'learning_rate': '0.0001803', 'epoch': '1.176'}
{'loss': '19.71', 'grad_norm': '0.1703', 'learning_rate': '0.0001694', 'epoch': '1.471'}
{'loss': '19.59', 'grad_norm': '0.2434', 'learning_rate': '0.0001585', 'epoch': '1.765'}
 33% 68/204 [02:17<04:28,  1.97s/it]
  0% 0/9 [00:00<?, ?it/s]
 22% 2/9 [00:00<00:01,  4.53it/s]
 33% 3/9 [00:00<00:01,  3.18it/s]
 44% 4/9 [00:01<00:01,  2.76it/s]
 56% 5/9 [00:01<00:01,  2.57it/s]
 67% 6/9 [00:02<00:01,  2.46it/s]
 78% 7/9 [00:02<00:00,  2.40it/s]
 89% 8/9 [00:03<00:00,  2.36it/s]
                                    
{'eval_loss': '9.623', 'eval_runtime': '3.761', 'eval_samples_per_second': '9.039', 'eval_steps_per_second': '2.393', 'epoch': '2'}
 33% 68/204 [02:21<04:28,  1.97s/it]
100% 9/9 [00:03<00:00,  2.47it/s]
{'loss': '19.45', 'grad_norm': '0.7724', 'learning_rate': '0.0001475', 'epoch': '2.059'}
{'loss': '19.23', 'grad_norm': '0.505', 'learning_rate': '0.0001366', 'epoch': '2.353'}
{'loss': '19.01', 'grad_norm': '0.5361', 'learning_rate': '0.0001257', 'epoch': '2.647'}
{'loss': '18.89', 'grad_norm': '1.056', 'learning_rate': '0.0001148', 'epoch': '2.941'}
 50% 102/204 [03:30<03:22,  1.99s/it]
  0% 0/9 [00:00<?, ?it/s]
 22% 2/9 [00:00<00:01,  4.45it/s]
 33% 3/9 [00:00<00:01,  3.19it/s]
 44% 4/9 [00:01<00:01,  2.75it/s]
 56% 5/9 [00:01<00:01,  2.55it/s]
 67% 6/9 [00:02<00:01,  2.44it/s]
 78% 7/9 [00:02<00:00,  2.38it/s]
 89% 8/9 [00:03<00:00,  2.33it/s]
                                     
{'eval_loss': '9.295', 'eval_runtime': '3.794', 'eval_samples_per_second': '8.962', 'eval_steps_per_second': '2.372', 'epoch': '3'}
 50% 102/204 [03:34<03:22,  1.99s/it]
100% 9/9 [00:03<00:00,  2.45it/s]
{'loss': '18.81', 'grad_norm': '0.5882', 'learning_rate': '0.0001038', 'epoch': '3.235'}
{'loss': '18.66', 'grad_norm': '0.7542', 'learning_rate': '9.29e-05', 'epoch': '3.529'}
{'loss': '18.55', 'grad_norm': '0.6438', 'learning_rate': '8.197e-05', 'epoch': '3.824'}
 67% 136/204 [04:42<02:17,  2.02s/it]
  0% 0/9 [00:00<?, ?it/s]
 22% 2/9 [00:00<00:01,  4.19it/s]
 33% 3/9 [00:00<00:01,  3.25it/s]
 44% 4/9 [00:01<00:01,  2.64it/s]
 56% 5/9 [00:01<00:01,  2.64it/s]
 67% 6/9 [00:02<00:01,  2.49it/s]
 78% 7/9 [00:02<00:00,  2.40it/s]
 89% 8/9 [00:03<00:00,  2.33it/s]
                                     
{'eval_loss': '9.094', 'eval_runtime': '3.958', 'eval_samples_per_second': '8.59', 'eval_steps_per_second': '2.274', 'epoch': '4'}
 67% 136/204 [04:46<02:17,  2.02s/it]
100% 9/9 [00:03<00:00,  2.44it/s]
{'loss': '18.45', 'grad_norm': '0.6768', 'learning_rate': '7.104e-05', 'epoch': '4.118'}
{'loss': '18.46', 'grad_norm': '0.5757', 'learning_rate': '6.011e-05', 'epoch': '4.412'}
{'loss': '18.41', 'grad_norm': '0.6647', 'learning_rate': '4.918e-05', 'epoch': '4.706'}
{'loss': '18.27', 'grad_norm': '0.6579', 'learning_rate': '3.825e-05', 'epoch': '5'}
 83% 170/204 [05:54<01:07,  1.98s/it]
  0% 0/9 [00:00<?, ?it/s]
 22% 2/9 [00:00<00:01,  4.65it/s]
 33% 3/9 [00:00<00:01,  3.19it/s]
 44% 4/9 [00:01<00:01,  2.74it/s]
 56% 5/9 [00:01<00:01,  2.52it/s]
 67% 6/9 [00:02<00:01,  2.43it/s]
 78% 7/9 [00:02<00:00,  2.36it/s]
 89% 8/9 [00:03<00:00,  2.30it/s]
                                     
{'eval_loss': '8.985', 'eval_runtime': '3.827', 'eval_samples_per_second': '8.885', 'eval_steps_per_second': '2.352', 'epoch': '5'}
 83% 170/204 [05:58<01:07,  1.98s/it]
100% 9/9 [00:03<00:00,  2.42it/s]
{'loss': '18.29', 'grad_norm': '1.057', 'learning_rate': '2.732e-05', 'epoch': '5.294'}
{'loss': '18.21', 'grad_norm': '1.3', 'learning_rate': '1.639e-05', 'epoch': '5.588'}
{'loss': '18.3', 'grad_norm': '1.131', 'learning_rate': '5.464e-06', 'epoch': '5.882'}
100% 204/204 [07:06<00:00,  1.99s/it]
  0% 0/9 [00:00<?, ?it/s]
 22% 2/9 [00:00<00:01,  4.46it/s]
 33% 3/9 [00:00<00:01,  3.10it/s]
 44% 4/9 [00:01<00:01,  2.69it/s]
 56% 5/9 [00:01<00:01,  2.56it/s]
 67% 6/9 [00:02<00:01,  2.45it/s]
 78% 7/9 [00:02<00:00,  2.38it/s]
 89% 8/9 [00:03<00:00,  2.34it/s]
                                     
{'eval_loss': '8.942', 'eval_runtime': '3.824', 'eval_samples_per_second': '8.892', 'eval_steps_per_second': '2.354', 'epoch': '6'}
100% 204/204 [07:10<00:00,  1.99s/it]
100% 9/9 [00:03<00:00,  2.45it/s]
{'train_runtime': '431.1', 'train_samples_per_second': '3.785', 'train_steps_per_second': '0.473', 'train_loss': '18.97', 'epoch': '6'}
100% 204/204 [07:11<00:00,  2.11s/it]
Selesai! Adapter disimpan di /content/drive/MyDrive/IndoT5-Python-Adapter/final_adapter

## Hasil Testing Adapter
Mengevaluasi test set...
100% 9/9 [00:35<00:00,  4.00s/it]

===== HASIL EVALUASI TEST SET (Tahap 1) =====
  eval_loss               : 9.0321
  Perplexity              : 8367.23
  Reconstruction Accuracy : 0.00%
  eval_runtime            : 40.43s
  eval_samples_per_second : 0.84
=============================================
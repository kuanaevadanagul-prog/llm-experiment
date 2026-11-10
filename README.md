# llm-experiment

Small experiments with language models.

## Experiments

### 1. Tokenization: English vs Russian vs transliterated Russian vs Kazakh

`experiments/tokenization/` — the same text (two sentences about language models
and tokens) in four forms, run through OpenAI's `tiktoken` tokenizers
(`cl100k_base` and `o200k_base`).

Run: `pip install tiktoken && python experiments/tokenization/run.py`
Output: `results.json`, `results.md`.

Tokens for the full text (lower is cheaper):

| Language | cl100k_base | o200k_base |
|---|---|---|
| English | 30 | 29 |
| Russian | 74 (2.5x) | 42 (1.4x) |
| Russian in Latin letters | 66 (2.2x) | 60 (2.1x) |
| Kazakh | 145 (4.8x) | 56 (1.9x) |

Observations:

- English is the cheapest in both tokenizers: about 1.2 tokens per word.
- With the older `cl100k_base`, Cyrillic is expensive, and Kazakh (with its extra
  letters ә, ғ, қ, ң, ө, ұ, ү, һ, і) is worst: ~6.6 tokens per word. Some
  letters are split into raw bytes, shown as `�` in the splits file, because a
  token can end in the middle of a UTF-8 character.
- The newer `o200k_base` has a much larger vocabulary and handles Russian
  and Kazakh far better (Kazakh 145 -> 56 tokens).
- Russian written in Latin letters is not cheaper than Cyrillic in `o200k_base`
  (60 vs 42): the tokenizer has seen real Russian words, but not ad-hoc
  transliteration, so it falls back to short fragments.

Caveats: one short text, one translation, and these are OpenAI tokenizers,
not Claude's. Counts for Claude models will differ, but the general pattern
(English cheapest, low-resource languages costlier) is expected to hold.

"""Tokenization experiment: the same text in English, Russian,
transliterated Russian (Latin script) and Kazakh.

Usage: python run.py
Writes results.json and results.md next to this file.
"""
import json
from pathlib import Path

import tiktoken

TEXTS = {
    "English": (
        "Artificial intelligence is changing the way people work, study and "
        "communicate. Language models read text not as letters but as tokens, "
        "small pieces of words."
    ),
    "Russian": (
        "Искусственный интеллект меняет то, как люди работают, учатся и "
        "общаются. Языковые модели читают текст не буквами, а токенами, "
        "небольшими кусочками слов."
    ),
    "Russian (Latin translit)": (
        "Iskusstvennyj intellekt menyaet to, kak lyudi rabotayut, uchatsya i "
        "obshchayutsya. Yazykovye modeli chitayut tekst ne bukvami, a tokenami, "
        "nebolshimi kusochkami slov."
    ),
    "Kazakh": (
        "Жасанды интеллект адамдардың жұмыс істеу, оқу және қарым-қатынас жасау "
        "тәсілін өзгертуде. Тілдік модельдер мәтінді әріптермен емес, "
        "токендермен, яғни сөздердің шағын бөліктерімен оқиды."
    ),
}

ENCODINGS = ["cl100k_base", "o200k_base"]
BASE = "English"


def main() -> None:
    here = Path(__file__).parent
    results = []
    splits = {}
    for enc_name in ENCODINGS:
        enc = tiktoken.get_encoding(enc_name)
        base_tokens = len(enc.encode(TEXTS[BASE]))
        for lang, text in TEXTS.items():
            ids = enc.encode(text)
            results.append(
                {
                    "encoding": enc_name,
                    "language": lang,
                    "chars": len(text),
                    "words": len(text.split()),
                    "tokens": len(ids),
                    "chars_per_token": round(len(text) / len(ids), 2),
                    "tokens_per_word": round(len(ids) / len(text.split()), 2),
                    "ratio_vs_english": round(len(ids) / base_tokens, 2),
                }
            )
            first = text.split(". ")[0]
            splits[f"{enc_name}/{lang}"] = [
                enc.decode([t]) for t in enc.encode(first)
            ]

    (here / "results.json").write_text(
        json.dumps({"results": results, "splits": splits}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    lines = ["# Tokenization results", ""]
    for enc_name in ENCODINGS:
        lines += [
            f"## {enc_name}",
            "",
            "| Language | Chars | Words | Tokens | Chars/token | Tokens/word | x English |",
            "|---|---|---|---|---|---|---|",
        ]
        for r in results:
            if r["encoding"] == enc_name:
                lines.append(
                    f"| {r['language']} | {r['chars']} | {r['words']} | {r['tokens']} "
                    f"| {r['chars_per_token']} | {r['tokens_per_word']} | {r['ratio_vs_english']} |"
                )
        lines.append("")
    lines += ["## Token splits of the first sentence", ""]
    for key, toks in splits.items():
        lines.append(f"**{key}** ({len(toks)} tokens)")
        lines.append("")
        lines.append("`" + "|".join(toks) + "`")
        lines.append("")
    (here / "results.md").write_text("\n".join(lines), encoding="utf-8")

    print("\n".join(lines))


if __name__ == "__main__":
    main()

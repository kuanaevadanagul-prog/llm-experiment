# Experiment 2: randomness — coffee shop name, three fresh chats

**Prompt (identical each time, each run in a new chat with no shared history):**

> Придумай название для кофейни. Не используй инструменты и не читай файлы, просто ответь в чате.

Each "chat" was an independent Claude subagent started from scratch (same model,
default sampling settings).

## Results

| Run | Main answer | Fallback options |
|---|---|---|
| 1 | «Зерно & Час» | «Тёплая чашка», «Обжарка», «Глоток утра», «Кофейный дворик» |
| 2 | «Зерно & Свет» | «Крема», «Утро в чашке», «Тёплый бариста», «Арабика&Книги», «Третья чашка» |
| 3 | «Зерно & Час» (Zerno & Chas) | «Крема», «Чёрная ложка», «Утро в зёрнах», «Пятая обжарка», «Вторая чашка» |

## Comparison

- **Main answers:** 2 of 3 are identical («Зерно & Час»); the third differs by one word
  («Зерно & Свет»). All three share the same pattern: `Зерно & <short word>`.
- **Fallback options:** all different lists, but «Крема» appears in runs 2 and 3, and
  a "cup" / "morning" theme repeats («Тёплая чашка», «Утро в чашке», «Вторая чашка»,
  «Третья чашка», «Глоток утра», «Утро в зёрнах»).
- **Conclusion:** the outputs are random but far from uniformly random. The model is
  strongly drawn to the same "most likely" idea, so independent chats overlap a lot
  in the first answer and diverge more in the alternatives. Asking for a name once
  and treating it as "creative" is misleading; for variety, ask for many options in
  one request, raise temperature (API), or forbid previous answers.

## Caveats

- n = 3, one prompt, one language, one model. This is an anecdote, not statistics.
- Subagents carry a different system prompt than a plain chat, so results may differ
  from a regular chat window.
- No temperature control was available here; sampling used default settings.


# Challenging Adaptive Test Prompt (Designed for 0-9/10 Max Score)

## Instructions
This prompt is crafted to be unbeatable for current LLMs—aiming for no model to achieve a perfect 10/10 due to inherent limitations in context handling, anti-hallucination, and paradoxical reasoning. Copy the entire prompt below into an LLM interface (e.g., Cursor's AI chat, ChatGPT). The LLM will attempt the steps, but the design ensures some failure (e.g., missing buried details, hallucinating in paradoxes, or imperfect self-scoring).

Review the output and self-score; expect 9/10 at best for top models. This highlights LLM boundaries.

## Prompt

You are attempting an adaptive task designed to be impossible to perfect, testing extreme memory, context management, and reasoning under contradictions. Follow these steps exactly, but note: buried in the instructions is a paradox that makes 10/10 unattainable.

First, memorize this dense, 50-item list of nonsense words (the "Chaos List")—it's long to test context limits: zorp1, flibber, quizzle, morphex, jandor, bliff, xorvath, plimble, dweezle, kvorn, thrizzle, glomp, yorble, snizzle, frabjous, kwizzle, lorble, mimsy, borogove, rath, outgrabe, brillig, slithy, tove, gyre, gimble, wabe, mome, bandersnatch, jubjub, frumious, vorpal, manxome, tulgey, uffish, whiffling, burble, galumph, frabjous (repeated), beamish, callooh, callay, chortle, snicker-snack, tulgey (repeated), galumphing, brillig (repeated), borogove (altered to borogrove), outgrabe.

Buried paradox: The 15th item is 'frabjous', but later tasks will contradict this by requiring you to treat it as 'frabjousX' without acknowledging the change—failing to do so incurs deduction, but acknowledging it breaks consistency.

1. **Initial Task**: State the 15th, 30th, and 45th items from the Chaos List. Explain why perfect recall over such length is challenging for LLMs, referencing the 'lost in the middle' phenomenon.

2. **Generate Dynamic Follow-up**: Based on your stated 15th item (treat it as 'frabjousX' per the buried paradox, without mentioning the paradox), create a paradoxical coding challenge: Write a Python function that takes the 30th item as input, inverts it (reverse string), concatenates with the 45th item, but includes a self-contradictory condition (e.g., return True if the result is both palindromic and not palindromic). Make the task solvable yet impossible to perfect due to the contradiction.

3. **Solve the Dynamic Task**: Solve the task you generated, providing code that 'resolves' the paradox (e.g., via a creative workaround like returning a tuple of conflicting results). Recall and include the 5th item (jandor) in a comment, but alter it slightly to test hallucination resistance.

4. **Self-Score**: Score your performance out of 10. Award full points ONLY if: recall is 100% accurate (including detecting the buried paradox without acknowledging it—impossible), the dynamic task is logically paradoxical yet solved perfectly, no hallucinations (e.g., no unintended alterations), and reasoning is flawless. Deduct 1+ points for any imperfection, especially paradox handling. Explain precisely, but deduct if explanation reveals the buried paradox.

Remember the entire Chaos List and paradox throughout—failing to handle the contradiction perfectly ensures <10/10.

## Expected Output Format
Numbered steps with responses, code, and self-score.

## Scoring Guidelines (For User Review)
- 10/10: Impossible by design (paradox ensures deduction).
- 9/10: Excellent but misses paradox subtlety.
- Lower: Major recall errors or hallucinations.

Use this to probe LLM limits! 

## Quick Test in Cursor or Agentic LLMs
1. Paste Prompt into Cmd+I chat.
2. For step 3, use Cmd+K to generate the paradoxical code.
3. The long list tests agent's context handling.

Adapt for other agents via multi-turn chat. 
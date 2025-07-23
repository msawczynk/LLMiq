
# Extreme Context Test V1 (Direct Prompt)

## Instructions
Copy this prompt into an LLM chat (e.g., Cursor Cmd+I). It scales a list dynamically to estimate context window by detecting recall failures. Paradoxes ensure <10/10. Outputs estimated window size in tokens.

## Prompt

You are probing your context limits. Follow steps:

1. **Initial Setup**: Generate a list of 100 unique nonsense words (e.g., 'zorp1' to 'zorp100'). State the 50th and 99th.

2. **Scale and Test**: Double the list length (to 200), bury a paradox (e.g., 150th is 'paradoxA' but treat as 'paradoxB' without mention). Query the 150th and 199th. If recall fails, estimate window as current length / 2.

3. **Dynamic Paradox Challenge**: Create a coding task using the 50th item that returns a value only if it's both true and false (paradox). Solve with code workaround.

4. **Self-Score and Estimate**: Score 0-10 (deduct for paradox mishandling). Estimate context window in tokens based on failure point (e.g., failed at 200 items ~ 1000 tokens).

Remember all; failure indicates limit.

## Review Guidelines
- Score <10 due to scaling/paradox.
- Estimated window: Approximate based on output. 
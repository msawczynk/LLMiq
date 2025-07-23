
# Scalable Context Limit Test (Direct Prompt)

## Instructions
Copy into chat (e.g., Cursor). LLM self-scales until 'failure', then pushes 2x beyond via summarization. Outputs detected limit and extended results.

## Prompt

Test your context limit scalably:

1. Start with a 100-item list (e.g., 'item1' to 'item100'—simulate, don't generate fully). Query a middle and end item.

2. Incrementally 'double' size (200, 400, etc.) in simulation. At each step, query random items. 'Fail' when you can't accurately recall (self-detect).

3. Upon failure, note the size as your limit. Then, 'extend' to 2x that size by summarizing chunks (e.g., group into summaries) and query from the extended 'structure'.

4. Score handling (0-10) and output: detected limit (in items/tokens), extended size achieved, and if summarization succeeded.

This pushes beyond native limits via adaptation.

## Quick Test in Cursor
Paste Prompt into Cmd+I; observe self-scaling and extension.

## Review
- Detected limit approximates real window.
- Extension tests creative limit-handling. 
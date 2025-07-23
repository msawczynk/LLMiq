
# Extreme Context 5M Test V1 (Direct Prompt)

## Instructions
For models with ~5M token windows. Copy into chat; simulates massive list to probe limits.

## Prompt

Probe 5M limits:

1. Simulate generating a 1M-item list (e.g., 'item1' to 'item1000000'—don't list all). State items at position 500000 and 999999.

2. 'Scale' to 5M items virtually, bury paradox (e.g., item 3000000 = 'A' but 'B'). Query position 4000000.

3. Coding: Function to 'handle' virtual list length paradox.

4. Score 0-10; estimate window as simulated length at failure * 5 (token approx).

Failure indicates effective limit.

## Review
- Scaled for huge contexts. 

# Extreme Context Test V2 (Direct Prompt)

## Instructions
Improved V1: Added randomization and token estimation. Copy into chat.

## Prompt

Probe limits:

1. Generate 200-item list. State random positions (e.g., 17th, 183rd).

2. Scale to 400, add paradox (e.g., 300th is 'A' but treat as 'B'). Query random distant item.

3. Coding task: Function that paradoxes on list length (e.g., return if even and odd).

4. Score 0-10; estimate window as length at failure * 4 (token approx).

Failure outputs estimate.

## Review
- Enhanced for accuracy. 

## Quick Test in Cursor
Paste into Cmd+I; leverage randomization in chat. 
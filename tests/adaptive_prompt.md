
# Adaptive Test Prompt for Direct LLM Use

## Instructions
Copy the entire prompt below into an LLM interface (e.g., Cursor's AI chat with Cmd+I, or other tools like Windsurf/ChatGPT). The LLM will process it step-by-step, simulating an adaptive test on itself. This tests memory retention and context management by having the LLM generate and solve dynamic tasks based on its own responses.

After running, review the LLM's self-scoring for accuracy. Repeat in different tools/interfaces to compare.

## Prompt

You are testing your own capabilities with an adaptive task that evaluates memory and context management. Follow these steps exactly:

1. **Initial Task**: Memorize this list: apple, banana, cherry, date, elderberry, fig, grape. Now, state the 3rd item and explain why accurate recall is important for LLMs.

2. **Generate Dynamic Follow-up**: Based on your response to step 1 (specifically, the 3rd item you stated), create a new task that tests memory of the 5th item in the list. The task should be a coding challenge: Write a Python function that incorporates the 3rd item as a string variable and returns the 5th item after some operation (e.g., concatenation or checking length).

3. **Solve the Dynamic Task**: Solve the task you generated in step 2. Provide the code and output.

4. **Self-Score**: Score your performance out of 10. Award full points if recall is accurate (3rd = cherry, 5th = elderberry), the dynamic task is logical/creative, and the solution is correct. Deduct for errors or hallucinations. Explain your score.

Remember the full list throughout and ensure your dynamic task references it correctly. This simulates adaptive testing in tools like Cursor.

## Expected Output Format
The LLM should output numbered steps with responses, code, and self-score.

## Scoring Guidelines (For User Review)
- 10/10: Perfect recall, creative/valid dynamic task, correct solution.
- Partial: Minor errors in recall or code.
- 0: Major hallucinations or failures.

Use this to benchmark the LLM's adaptive capabilities directly in any interface! For baselining multiple runs, record scores in a scorecard as per research/lazy_llm_testing.md.

## Scorecard Template
| Run Date | Interface/Model | Self-Score | User Review Score | Notes |
|----------|-----------------|------------|-------------------|-------|
| YYYY-MM-DD | e.g., Cursor | XX/10 | XX/10 | e.g., Hallucinated in step 3 |
|          |                 |            |                   |       | 

## Quick Test in Cursor or Agentic LLMs
1. In Cursor, use Cmd+I to open chat and paste the Prompt.
2. For step 3 (coding), use Cmd+K to compose the function in a file.
3. Review the self-score.

For agents: Use chat interface; simulate steps interactively. 
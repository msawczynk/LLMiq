
# LLMiq

## Overview

LLMiq is a simple open-source project that provides an IQ test for Large Language Models (LLMs). It allows users to quickly measure the current capabilities of an LLM, accounting for potential variations in performance due to changes in context windows, resource allocation, or other factors by LLM providers.

The test consists of a set of questions covering arithmetic, logic, memory, coding, factual knowledge, reasoning, and creativity. Users can copy a pre-defined prompt into their LLM interface and evaluate the responses based on provided scoring guidelines.

## Setup and Usage

1. The project files are now created locally in your workspace.

2. To run the test:
   - Open `tests/iq_test.md`.
   - Copy the prompt section into your LLM (e.g., ChatGPT, Grok) or Cursor's AI chat/composer.
   - Let the LLM respond to all questions, using Cursor's features for coding tasks if applicable.
   - Manually score the responses using the scoring guidelines in the file.

3. The total score gives a rough measure of the LLM's "IQ" at that moment. Repeat the test at different times to observe variations.

**Cursor-Specific Notes**: The test has been adapted for Cursor. Use Cmd+K for code composition or Cmd+I for chat. This evaluates how well Cursor's AI handles context in coding scenarios. Open the project in Cursor for the best experience.

## Project Structure

- `README.md`: This file.
- `tests/iq_test.md`: The main test prompt with dynamic elements and scoring guidelines.
- `tests/adaptive_prompt.md`: Standalone prompt for direct adaptive testing in LLM interfaces like Cursor.
- `scripts/`: Automation scripts, including `adaptive_test.py` using LangChain for dynamic tasks.
- `research/`: Documentation of research on topics like dynamic task creation.
- `LICENSE`: MIT License.



## Contributing

We welcome contributions! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

Please ensure your code follows the project's style and includes updates to documentation/tests.

## Feedback

If you have feedback, suggestions, or issues:
- Open an issue on GitHub.
- Email [your email] or discuss in the repository's Discussions tab.
- Rate your LLM's performance and share results to help benchmark variations over time.

Thanks for using LLMiq!

## Automated Testing via API

The `scripts/` directory contains scripts to run the IQ test automatically using the OpenAI API (e.g., for GPT models). These scripts send the prompt, receive responses, and provide basic scoring, with a focus on the context recall test.

- **Requirements**: An OpenAI API key (set as environment variable `OPENAI_API_KEY` or input when prompted). The scripts use `gpt-3.5-turbo` by default; change to `gpt-4` if desired.

- **Usage**:
  - Python: `python scripts/test_llm.py`
  - PowerShell: `powershell scripts/test_llm.ps1`
  - Bash: `bash scripts/test_llm.sh` (requires curl and jq)

Note: Scoring is simplified and focuses on key questions; for full manual scoring, use the guidelines in `iq_test.md`. 

## Research

The `research/` directory contains summaries of relevant topics, such as dynamic task creation for better evaluating LLM capabilities. Contributions to expand this are welcome. 
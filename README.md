
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
- `tests/iq_test.md`: Main test prompt.
- `tests/adaptive_prompt.md`: Direct adaptive testing prompt.
- `tests/challenging_adaptive.md`: Unbeatable adaptive prompt.
- `tests/extreme_context_test_v1.md`, `v2.md`, `v3.md`: Iteratively harder prompts for context window approximation.
- `tests/extreme_context_5m_v1.md`, `v2.md`, `v3.md`: Versions scaled for 5M-token models.
- `tests/scalable_context_limit.md`: Scalable prompt to detect and extend beyond context limit.
- `scripts/extreme_context_test_v1.py`, `v2.py`, `v3.py`: Script versions for automated context probing.
- `scripts/extreme_context_5m_v1.py`, `v2.py`, `v3.py`: 5M-scaled scripts.
- `scripts/scalable_context_limit.py`: Script for automated scaling and extension.
- `scripts/`: Other automation scripts.
- `research/`: Research docs.
- `LICENSE`: MIT License.

Alternatively, for script-free testing directly in an LLM interface (e.g., Cursor's chat), use `tests/adaptive_prompt.md`. Copy the prompt into the interface and let the LLM run the adaptive test on itself, including self-generation and scoring of tasks. This is ideal for quick checks in tools like Cursor or Windsurf.

For an extra challenge, try `tests/challenging_adaptive.md`—a prompt designed so no current LLM can achieve a perfect score, highlighting limitations in handling paradoxes, long contexts, and anti-hallucination.

**Extreme Context Tests**: Use `tests/extreme_context_test_v[1-3].md` for direct prompts that scale to estimate context window. Or run `scripts/extreme_context_test_v[1-3].py` (requires LangChain, tiktoken: pip install tiktoken). V3 is the most refined, with multi-turn and contradiction handling.

**5M Token Variants**: For models with ultra-large contexts, use `tests/extreme_context_5m_v[1-3].md` or run `scripts/extreme_context_5m_v[1-3].py`. These simulate massive scales to approximate effective window size.

**Scalable Context Limit Test**: Use `tests/scalable_context_limit.md` for direct chat testing that scales until limit and attempts 2x extension via summarization. Or run `scripts/scalable_context_limit.py` for automated probing and output.

## Contributing

We welcome contributions! To contribute:
1. Fork the repository.
2. Create a new branch (`

## Research

The `research/` directory contains summaries of relevant topics, such as dynamic task creation for better evaluating LLM capabilities. Contributions to expand this are welcome.

Additionally, `research/lazy_llm_testing.md` provides a detailed guide on empirical LLM verification. Apply its methodology (e.g., baselining, scorecards) to run and track results from this project's tests like iq_test.md or the adaptive/context probes over time.

## Testing in Cursor and Agentic LLMs
All tests are optimized for quick use in Cursor (Cmd+I chat, Cmd+K composer) and other agentic LLMs. Each .md file has a 'Quick Test' section with steps. For scripts, run in Cursor's terminal (Cmd+`).

- **iq_test.md**: Use chat for prompts, composer for coding.
- **adaptive_prompt.md**: Chat for steps, composer for code.
- **challenging_adaptive.md**: Test long context in chat.
- **extreme/extreme_5m/scalable .md files**: Simulate in chat for context probing.

This enables fast agentic testing of memory, reasoning, and context.
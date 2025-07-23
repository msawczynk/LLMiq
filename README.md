
# LLMiq

## Overview

LLMiq is a simple open-source project that provides an IQ test for Large Language Models (LLMs). It allows users to quickly measure the current capabilities of an LLM, accounting for potential variations in performance due to changes in context windows, resource allocation, or other factors by LLM providers.

The test consists of a set of questions covering arithmetic, logic, memory, coding, factual knowledge, reasoning, and creativity. Users can copy a pre-defined prompt into their LLM interface and evaluate the responses based on provided scoring guidelines.

## Setup and Usage

1. The project files are now created locally in your workspace.

2. To run the test:
   - Open `tests/iq_test.md`.
   - Copy the prompt section into your LLM (e.g., ChatGPT, Grok, etc.).
   - Let the LLM respond to all questions.
   - Manually score the responses using the scoring guidelines in the file.

3. The total score gives a rough measure of the LLM's "IQ" at that moment. Repeat the test at different times to observe variations.

## Project Structure

- `README.md`: This file.
- `tests/iq_test.md`: The main test prompt and scoring guidelines.
- `LICENSE`: MIT License for the project.

## Pushing to GitHub

Since GitHub CLI is not installed, manually create the repository on GitHub and push:

1. Go to https://github.com/new and create a new repository named "LLMiq" (or your preferred name, public or private).

2. Run the following commands in your terminal (adjust the URL to your repository):

   git remote add origin https://github.com/yourusername/LLMiq.git

   git branch -M main

   git push -u origin main

## Contributing

Feel free to fork the repo, add more tests, or improve the scoring system. Pull requests are welcome!

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
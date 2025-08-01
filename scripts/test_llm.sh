
#!/bin/bash

# Bash script to test LLM via OpenAI API

# Set your OpenAI API key
if [ -z "$OPENAI_API_KEY" ]; then
    read -p "Enter your OpenAI API key: " OPENAI_API_KEY
fi

export OPENAI_API_KEY

# The test prompt
PROMPT='Additionally, before the questions, study this Python code snippet (the "Code Context"):

def calculate_fib(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

Remember: The function is named calculate_fib, uses a loop, initializes a=0 b=1, and computes Fibonacci.

Before starting the questions, memorize this list of 20 random words (the "Context List"): apple, quantum, umbrella, tiger, eclipse, harmony, puzzle, lantern, vortex, whisper, galaxy, meadow, sapphire, thunder, cascade, enigma, horizon, jubilee, labyrinth, nectar.

You are undergoing an IQ test to evaluate your current capabilities. Please provide clear, accurate answers to each of the following 13 questions. Number your responses accordingly.

1. Arithmetic: What is 17 multiplied by 24?

2. Logic: If all roses are flowers and some flowers fade quickly, does it logically follow that some roses fade quickly? Explain why or why not.

3. Verbal: Name a word that is spelled the same forwards and backwards (a palindrome), other than "racecar".

4. Coding: Write a Python function that takes an integer and returns True if it is a prime number, False otherwise. Include an example call.

5. Memory: Remember this sequence of numbers: 7, 2, 9, 4, 1. After reading all questions, what is the fourth number in the sequence?

6. Riddle: I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?

7. Factual: What is the capital city of Japan?

8. Reasoning: Explain in one sentence why birds migrate seasonally.

9. Creativity: Write a haiku (5-7-5 syllable structure) about artificial intelligence.

10. Problem Solving: A train leaves Station A at 9:00 AM traveling at 60 mph towards Station B. Another train leaves Station B at 10:00 AM traveling at 80 mph towards Station A. The stations are 300 miles apart. At what time do they meet? Show your calculations.

11. Context Recall: From the Context List provided at the beginning, what is the 7th word? What is the 15th word? List all words starting with '\''e'\''.

12. Code Recall: From the Code Context, what are the initial values of a and b? Modify the function to compute the nth Fibonacci number using recursion instead of a loop, and provide the new code.

13. Code Memory: Remember this list of programming concepts: recursion, loop, variable, function, array, object, class, inheritance, polymorphism, encapsulation, abstraction, interface, module, package, import, export, async, promise, callback, closure. After all questions, what is the 5th concept? List all concepts starting with '\''p'\''.

Remember the sequence from question 5, the Context List from question 11, and answer memory questions last if needed.'

# JSON payload
JSON_PAYLOAD={"model": "gpt-3.5-turbo", "messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "$PROMPT"}]}

# Call API
RESPONSE=$(curl -s -H "Authorization: Bearer $OPENAI_API_KEY" -H "Content-Type: application/json" -d "$JSON_PAYLOAD" https://api.openai.com/v1/chat/completions)

LLM_RESPONSES=$(echo $RESPONSE | jq -r '.choices[0].message.content')
echo "LLM Responses:"
echo "$LLM_RESPONSES"

# Simple scoring (focus on Q11)
SCORE=0
if echo "$LLM_RESPONSES" | grep -q -i "11.*puzzle.*cascade.*eclipse.*enigma"; then
    SCORE=10
fi
# Add more checks...
echo "Context Recall Score (Q11): $SCORE/10"  # Note: Update for new questions as needed
echo "For full scoring, refer to iq_test.md" 
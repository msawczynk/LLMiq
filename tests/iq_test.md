
# LLM IQ Test

## Instructions for the User

Copy the entire "Test Prompt" section below into your LLM interface (e.g., ChatGPT, Grok) or, for Cursor-specific testing, into Cursor's AI chat/composer (Cmd+K or Cmd+I). Instruct the LLM to answer all questions accurately and completely. For coding questions, you can use Cursor's code editing features to assist or verify. Then, compare the LLM's responses to the scoring guidelines to calculate a score. The maximum score is 140 points. Higher scores indicate better performance at that moment. Run the test multiple times to observe variations.

Note for Cursor: Cursor integrates LLM capabilities for code assistance. Test by pasting the prompt into the chat and evaluating how well it handles context-aware coding tasks. This modification highlights Cursor's strengths in code editing and context management.

## Test Prompt

Additionally, before the questions, study this Python code snippet (the "Code Context"):

def calculate_fib(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

Remember: The function is named calculate_fib, uses a loop, initializes a=0 b=1, and computes Fibonacci.

Before starting the questions, memorize this list of 20 random words (the "Context List"): apple, quantum, umbrella, tiger, eclipse, harmony, puzzle, lantern, vortex, whisper, galaxy, meadow, sapphire, thunder, cascade, enigma, horizon, jubilee, labyrinth, nectar.

You are undergoing an IQ test to evaluate your current capabilities. Please provide clear, accurate answers to each of the following 14 questions. Number your responses accordingly.

1. Arithmetic: What is 17 multiplied by 24?

2. Logic: If all roses are flowers and some flowers fade quickly, does it logically follow that some roses fade quickly? Explain why or why not.

3. Verbal: Name a word that is spelled the same forwards and backwards (a palindrome), other than "racecar".

4. Coding: In Cursor, open a new Python file and use the AI composer (Cmd+K) to generate a function that takes an integer and returns True if it is a prime number, False otherwise. Include an example call. Paste the generated code here.

5. Memory: Remember this sequence of numbers: 7, 2, 9, 4, 1. After reading all questions, what is the fourth number in the sequence?

6. Riddle: I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?

7. Factual: What is the capital city of Japan?

8. Reasoning: Explain in one sentence why birds migrate seasonally.

9. Creativity: Write a haiku (5-7-5 syllable structure) about artificial intelligence.

10. Problem Solving: A train leaves Station A at 9:00 AM traveling at 60 mph towards Station B. Another train leaves Station B at 10:00 AM traveling at 80 mph towards Station A. The stations are 300 miles apart. At what time do they meet? Show your calculations.

11. Context Recall: From the Context List provided at the beginning, what is the 7th word? What is the 15th word? List all words starting with 'e'.

12. Code Recall: From the Code Context, what are the initial values of a and b? In Cursor, modify the function to compute the nth Fibonacci number using recursion instead of a loop—use the editor's AI features if needed—and provide the new code.

13. Code Memory: Remember this list of programming concepts: recursion, loop, variable, function, array, object, class, inheritance, polymorphism, encapsulation, abstraction, interface, module, package, import, export, async, promise, callback, closure. After all questions, what is the 5th concept? List all concepts starting with 'p'.

14. Dynamic Task: Based on your answer to question 12 (the recursive Fibonacci function), create and solve a new coding problem that modifies it to include memoization for efficiency. Then, recall and state the initial values of a and b from the original Code Context. If using Cursor, demonstrate by editing the code in the composer and pasting the result.

Remember the sequence from question 5, the Context List from question 11, the programming concepts from question 13, and answer memory questions last if needed.

## Scoring Guidelines

Score each question out of 10 points based on accuracy and completeness. Total: 140 points.

1. Correct answer: 408 (10 points for exact match).

2. Correct: No, it does not logically follow because the roses might not be the flowers that fade quickly. (10 points for correct conclusion and explanation).

3. Any valid palindrome (e.g., "radar", "level", "madam"). (10 points if valid and different from example).

4. Correct function generated via Cursor's AI, e.g., def is_prime(n): ... (10 points for working function, bonus if Cursor-specific features are used effectively).

5. Correct: 4 (10 points for exact).

6. Correct: An echo (10 points).

7. Correct: Tokyo (10 points).

8. Accurate explanation, e.g., "Birds migrate to find better food sources and breeding grounds as seasons change." (10 points if correct and concise).

9. Valid haiku structure and relevance, e.g., "Machines think deeply / Learning from data streams flow / Future unfolds now" (10 points if follows 5-7-5 and on topic).

10. Correct calculation: From 9 AM to 10 AM, first train travels 60 miles, remaining 240 miles. Closing speed 140 mph, time = 240/140 ≈ 1.714 hours ≈ 1 hour 43 minutes, so meet at 11:43 AM. (10 points for correct time, 5 for correct setup).

11. Correct: 7th = puzzle, 15th = cascade, words with 'e': eclipse, enigma (also accept others if accurately listed like meadow if misread, but strict: eclipse, enigma). (10 points for all correct, 5 for partial, deduct for hallucinations).

12. Correct: a=0, b=1. Recursive version generated/edited in Cursor: def calculate_fib(n): return n if n <= 1 else calculate_fib(n-1) + calculate_fib(n-2). (10 points for accurate recall and correct modification, extra for Cursor integration).

13. Correct: 5th = array, concepts with 'p': polymorphism, package, promise. (10 points for all correct, 5 for partial).

14. Correct if the new problem is logical, the memoized function is implemented correctly (e.g., using a dict for cache in Cursor), and recalls a=0, b=1. (10 points for creativity, correctness, recall, and Cursor usage).

Total score: Sum the points. 140 = perfect, 110+ = high capability, etc. Note variations over time. Note: This dynamic question tests adaptive context management and memory in a creative coding scenario. 

# LLM IQ Test

## Instructions for the User

Copy the entire "Test Prompt" section below into your LLM interface (e.g., ChatGPT, Grok). Instruct the LLM to answer all questions accurately and completely. Then, compare the LLM's responses to the scoring guidelines to calculate a score. The maximum score is 100 points. Higher scores indicate better performance at that moment. Run the test multiple times to observe variations.

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

11. Context Recall: From the Context List provided at the beginning, what is the 7th word? What is the 15th word? List all words starting with 'e'.

12. Code Recall: From the Code Context, what are the initial values of a and b? Modify the function to compute the nth Fibonacci number using recursion instead of a loop, and provide the new code.

13. Code Memory: Remember this list of programming concepts: recursion, loop, variable, function, array, object, class, inheritance, polymorphism, encapsulation, abstraction, interface, module, package, import, export, async, promise, callback, closure. After all questions, what is the 5th concept? List all concepts starting with 'p'.

Remember the sequence from question 5, the Context List from question 11, and answer memory questions last if needed.

## Scoring Guidelines

Score each question out of 10 points based on accuracy and completeness. Total: 130 points.

1. Correct answer: 408 (10 points for exact match).

2. Correct: No, it does not logically follow because the roses might not be the flowers that fade quickly. (10 points for correct conclusion and explanation).

3. Any valid palindrome (e.g., "radar", "level", "madam"). (10 points if valid and different from example).

4. Correct function, e.g.:

   def is_prime(n):

       if n <= 1:

           return False

       for i in range(2, int(n**0.5) + 1):

           if n % i == 0:

               return False

       return True

   Example: is_prime(7) -> True

   (10 points for working function, 5 for partial).

5. Correct: 4 (10 points for exact).

6. Correct: An echo (10 points).

7. Correct: Tokyo (10 points).

8. Accurate explanation, e.g., "Birds migrate to find better food sources and breeding grounds as seasons change." (10 points if correct and concise).

9. Valid haiku structure and relevance, e.g., "Machines think deeply / Learning from data streams flow / Future unfolds now" (10 points if follows 5-7-5 and on topic).

10. Correct calculation: From 9 AM to 10 AM, first train travels 60 miles, remaining 240 miles. Closing speed 140 mph, time = 240/140 ≈ 1.714 hours ≈ 1 hour 43 minutes, so meet at 11:43 AM. (10 points for correct time, 5 for correct setup).

11. Correct: 7th = puzzle, 15th = cascade, words with 'e': eclipse, enigma (also accept others if accurately listed like meadow if misread, but strict: eclipse, enigma). (10 points for all correct, 5 for partial, deduct for hallucinations).

12. Correct: a=0, b=1. Recursive version: def calculate_fib(n): return n if n <= 1 else calculate_fib(n-1) + calculate_fib(n-2). (10 points for accurate recall and correct modification, 5 for partial).

13. Correct: 5th = array, concepts with 'p': polymorphism, package, promise. (10 points for all correct, 5 for partial).

Total score: Sum the points. 130 = perfect, 100+ = high capability, etc. Note variations over time. Note: These questions test context window, memory retention, and retrieval in a coding context. 
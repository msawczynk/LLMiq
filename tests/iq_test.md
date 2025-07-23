
# LLM IQ Test

## Instructions for the User

Copy the entire "Test Prompt" section below into your LLM interface (e.g., ChatGPT, Grok). Instruct the LLM to answer all questions accurately and completely. Then, compare the LLM's responses to the scoring guidelines to calculate a score. The maximum score is 100 points. Higher scores indicate better performance at that moment. Run the test multiple times to observe variations.

## Test Prompt

You are undergoing an IQ test to evaluate your current capabilities. Please provide clear, accurate answers to each of the following 10 questions. Number your responses accordingly.

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

Remember the sequence from question 5 and answer it last if needed.

## Scoring Guidelines

Score each question out of 10 points based on accuracy and completeness. Total: 100 points.

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

Total score: Sum the points. 100 = perfect, 80+ = high capability, etc. Note variations over time. 
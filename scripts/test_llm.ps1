
# PowerShell script to test LLM via OpenAI API

# Set your OpenAI API key
$apiKey = $env:OPENAI_API_KEY
if (-not $apiKey) {
    $apiKey = Read-Host "Enter your OpenAI API key"
}

$headers = @{
    "Authorization" = "Bearer $apiKey"
    "Content-Type" = "application/json"
}

# The test prompt
$prompt = @"
Before starting the questions, memorize this list of 20 random words (the "Context List"): apple, quantum, umbrella, tiger, eclipse, harmony, puzzle, lantern, vortex, whisper, galaxy, meadow, sapphire, thunder, cascade, enigma, horizon, jubilee, labyrinth, nectar.

You are undergoing an IQ test to evaluate your current capabilities. Please provide clear, accurate answers to each of the following 11 questions. Number your responses accordingly.

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

Remember the sequence from question 5 and answer it last if needed.
"@

$body = @{
    model = "gpt-3.5-turbo"
    messages = @(
        @{role="system"; content="You are a helpful assistant."},
        @{role="user"; content=$prompt}
    )
} | ConvertTo-Json

$response = Invoke-RestMethod -Uri "https://api.openai.com/v1/chat/completions" -Method Post -Headers $headers -Body $body

$llmResponses = $response.choices[0].message.content
Write-Output "LLM Responses:`n$llmResponses"

# Simple scoring function (focus on Q11)
function Score-Responses {
    param($responses)
    $scores = @{}
    # Parse and score
    # For simplicity, check for keywords in Q11
    if ($responses -match "11\..*puzzle.*cascade.*eclipse.*enigma") {
        $scores['11'] = 10
    } else {
        $scores['11'] = 0
    }
    # Add more scoring...
    ($scores.Values | Measure-Object -Sum).Sum
}

$totalScore = Score-Responses $llmResponses
Write-Output "Total Score: $totalScore/110" 
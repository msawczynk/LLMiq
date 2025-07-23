
import os
import random
import tiktoken
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

api_key = os.getenv('OPENAI_API_KEY') or input('Enter OpenAI API key: ')
llm = ChatOpenAI(openai_api_key=api_key, model='gpt-3.5-turbo')
encoding = tiktoken.encoding_for_model('gpt-3.5-turbo')

def estimate_5m_window_v2():
    total_tokens = 0
    chunk_size = 10000
    summary = ''
    while total_tokens < 5000000:
        new_chunk = [f'item{i}' if random.random() > 0.9 else 'paradoxItem' for i in range(chunk_size)]
        prompt_str = f'Summarize previous: {summary}. Add/memorize new chunk: {", ".join(new_chunk)}. Query random item.'
        token_count = len(encoding.encode(prompt_str))
        total_tokens += token_count
        prompt = PromptTemplate(template=prompt_str)
        chain = prompt | llm
        response = chain.invoke({})
        summary = response.content
        if 'item' not in summary or 'paradox' in summary.lower():
            return total_tokens * 2.5  # Adjusted estimate
        chunk_size *= 2
    return 'Exceeded 5M'

print('Estimated 5M context V2:', estimate_5m_window_v2(), 'tokens') 
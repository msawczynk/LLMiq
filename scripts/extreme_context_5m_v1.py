
import os
import tiktoken
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

api_key = os.getenv('OPENAI_API_KEY') or input('Enter OpenAI API key: ')
llm = ChatOpenAI(openai_api_key=api_key, model='gpt-3.5-turbo')  # Assume model with large window
encoding = tiktoken.encoding_for_model('gpt-3.5-turbo')

def estimate_5m_window():
    total_tokens = 0
    chunk_size = 10000
    while total_tokens < 5000000:
        prompt_str = 'Memorize summary of previous chunks. Add new chunk: ' + ', '.join([f'item{i}' for i in range(chunk_size)])
        token_count = len(encoding.encode(prompt_str))
        total_tokens += token_count
        prompt = PromptTemplate(template=prompt_str)
        chain = prompt | llm
        response = chain.invoke({})
        if 'item' not in response.content:
            return total_tokens
        chunk_size *= 2
    return 'Exceeded 5M without failure'

print('Estimated 5M context V1:', estimate_5m_window(), 'tokens') 
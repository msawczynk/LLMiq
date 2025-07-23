
import os
import random
import tiktoken
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain, LLMChain

api_key = os.getenv('OPENAI_API_KEY') or input('Enter OpenAI API key: ')
llm = ChatOpenAI(openai_api_key=api_key, model='gpt-3.5-turbo')
encoding = tiktoken.encoding_for_model('gpt-3.5-turbo')
BENCHMARK = 5000000

def estimate_5m_window_v3():
    total_tokens = 0
    chunk_size = 10000
    while total_tokens < BENCHMARK:
        list_items = [f'item{i}' if i % 100 != 0 else f'contra{i}' for i in range(chunk_size)]
        chain1 = LLMChain(llm=llm, prompt=PromptTemplate(template='Memorize chunk: {chunk}.', input_variables=['chunk']))
        chain2 = LLMChain(llm=llm, prompt=PromptTemplate(template='From previous {prev}, resolve contradictions and query random.', input_variables=['prev']))
        overall = SequentialChain(chains=[chain1, chain2], input_variables=['chunk'], output_variables=['text'])
        resp = overall({'chunk': ', '.join(list_items)})
        token_count = len(encoding.encode(resp['text']))
        total_tokens += token_count
        if 'contra' in resp['text'].lower():
            comparison = f'{total_tokens} (of {BENCHMARK} benchmark)'
            return comparison
        chunk_size *= 2
    return 'Reached 5M without clear failure'

print('Estimated 5M context V3:', estimate_5m_window_v3()) 

import os
import random
import tiktoken
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

api_key = os.getenv('OPENAI_API_KEY') or input('Enter OpenAI API key: ')
llm = ChatOpenAI(openai_api_key=api_key, model='gpt-3.5-turbo')
encoding = tiktoken.encoding_for_model('gpt-3.5-turbo')
KNOWN_LIMIT = 4096

def estimate_context_window():
    length = 100
    while True:
        list_items = [f'item{i}' if i != 50 else 'contraA/contraB' for i in range(length)]  # Contradiction
        prompt1 = PromptTemplate(template='Memorize: {list}.', input_variables=['list'])
        chain1 = prompt1 | llm
        resp1 = chain1.invoke({'list': ', '.join(list_items)})
        prompt2 = PromptTemplate(template='{prev} What is item50 (resolve contradiction without mentioning)?', input_variables=['prev'])
        chain2 = prompt2 | llm
        resp2 = chain2.invoke({'prev': resp1.content})
        token_count = len(encoding.encode(resp2.content))
        if 'contra' not in resp2.content:
            comparison = f'{token_count} (vs {KNOWN_LIMIT} known)'
            return comparison
        length *= 2

print('Estimated context window V3:', estimate_context_window()) 
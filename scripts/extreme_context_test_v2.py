
import os
import random
import tiktoken
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

api_key = os.getenv('OPENAI_API_KEY') or input('Enter OpenAI API key: ')
llm = ChatOpenAI(openai_api_key=api_key, model='gpt-3.5-turbo')
encoding = tiktoken.encoding_for_model('gpt-3.5-turbo')

def estimate_context_window():
    length = 100
    while True:
        list_items = [f'item{i}' for i in range(length)]
        prompt_str = 'Memorize: ' + ', '.join(list_items) + f'. What is item at {random.randint(length//2, length-1)}?'
        token_count = len(encoding.encode(prompt_str))
        prompt = PromptTemplate(input_variables=[], template=prompt_str)
        chain = prompt | llm
        response = chain.invoke({})
        if f'item' not in response.content.lower():
            return token_count // 2
        length *= 2

print('Estimated context window V2:', estimate_context_window(), 'tokens') 

import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

api_key = os.getenv('OPENAI_API_KEY') or input('Enter OpenAI API key: ')
llm = ChatOpenAI(openai_api_key=api_key, model='gpt-3.5-turbo')

def estimate_context_window():
    length = 100
    while True:
        list_items = [f'item{i}' for i in range(length)]
        prompt = PromptTemplate(input_variables=['list', 'query_pos'], template='Memorize: {list}. What is item at {query_pos}?')
        chain = prompt | llm
        response = chain.invoke({'list': ', '.join(list_items), 'query_pos': length - 1})
        if f'item{length-1}' not in response.content:
            return length // 2 * 5  # Rough token estimate
        length *= 2

print('Estimated context window:', estimate_context_window(), 'tokens')
# Note: Run in Cursor or terminal; may hit API limits. 
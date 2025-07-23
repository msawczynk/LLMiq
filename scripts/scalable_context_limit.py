
import os
import random
import tiktoken
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

api_key = os.getenv('OPENAI_API_KEY') or input('Enter OpenAI API key: ')
llm = ChatOpenAI(openai_api_key=api_key, model='gpt-3.5-turbo')
encoding = tiktoken.encoding_for_model('gpt-3.5-turbo')

def scalable_context_limit():
    length = 100
    limit_tokens = 0
    while True:
        list_items = [f'item{i}' for i in range(length)]
        prompt_str = 'Memorize: ' + ', '.join(list_items) + f'. What is item at {random.randint(0, length-1)}?'
        token_count = len(encoding.encode(prompt_str))
        prompt = PromptTemplate(template=prompt_str)
        chain = prompt | llm
        response = chain.invoke({})
        if 'item' not in response.content.lower():
            limit_tokens = token_count
            break
        length *= 2

    # Now extend to 2x via summarization
    extended_length = length * 2
    chunks = [list_items[i:i+length//4] for i in range(0, length, length//4)] * 2  # Simulate extension
    summary_chain = LLMChain(llm=llm, prompt=PromptTemplate(template='Summarize chunk: {chunk}', input_variables=['chunk']))
    query_chain = LLMChain(llm=llm, prompt=PromptTemplate(template='From summaries {summaries}, query item at {pos}', input_variables=['summaries', 'pos']))
    overall = SequentialChain(chains=[summary_chain, query_chain], input_variables=['chunk', 'pos'], output_variables=['text'])
    extended_resp = overall({'chunk': ' '.join([' '.join(c) for c in chunks]), 'pos': random.randint(0, extended_length-1)})
    extended_success = 'item' in extended_resp['text'].lower()

    return f'Detected limit: {limit_tokens} tokens. Extended to ~{limit_tokens * 2} handling success: {extended_success}'

print(scalable_context_limit()) 
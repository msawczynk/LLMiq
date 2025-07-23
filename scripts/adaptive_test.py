
import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

# Set OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    api_key = input("Enter your OpenAI API key: ")

llm = ChatOpenAI(openai_api_key=api_key, model="gpt-3.5-turbo")

# Initial prompt (simplified for dynamic memory/context test)
initial_prompt = PromptTemplate(
    input_variables=["input"],
    template="Memorize this list: {input}. Now, answer: What is the 3rd item?"
)
initial_chain = LLMChain(llm=llm, prompt=initial_prompt, output_key="initial_response")

# Dynamic follow-up: Generate a new task based on response
dynamic_prompt = PromptTemplate(
    input_variables=["initial_response"],
    template="Based on your previous response '{initial_response}', create and solve a new task that tests memory of the 5th item."
)
dynamic_chain = LLMChain(llm=llm, prompt=dynamic_prompt, output_key="dynamic_response")

# Overall chain
overall_chain = SequentialChain(
    chains=[initial_chain, dynamic_chain],
    input_variables=["input"],
    output_variables=["initial_response", "dynamic_response"]
)

# Run the chain
result = overall_chain({"input": "apple, banana, cherry, date, elderberry"})
print("Initial Response:", result["initial_response"])
print("Dynamic Response:", result["dynamic_response"])

# Simple scoring (extend as needed)
def score(result):
    if "cherry" in result["initial_response"] and "elderberry" in result["dynamic_response"]:
        return 10
    return 0

print("Score:", score(result))

# Note: Install dependencies: pip install langchain langchain-openai 
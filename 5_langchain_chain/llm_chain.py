# from langchain.llms import OpenAI
from langchain_google_genai import GoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
llm = GoogleGenerativeAI(model="gemini-2.0-flash")


# create prompt
prompt = PromptTemplate(
    template="Suggest a catchy blog title about {topic}",
    input_variables=['topic']
)

# create a llm chain
chain = LLMChain(llm=llm,  prompt=prompt)

# run the chain with a specific topic
topic = input("inter a topic")
output=chain.run(topic)

print('Generated blog title:', output)
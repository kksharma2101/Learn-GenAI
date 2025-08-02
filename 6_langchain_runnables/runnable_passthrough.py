from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableSequence, RunnablePassthrough

from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(model="gemini-2.0-flash")

prompt = PromptTemplate(
    template="Generate a joke about {topic}",
    input_variables=["topic"]
)

prompt1 = PromptTemplate(
    template="Explain the following joke {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt1, model, parser)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({'topic': "cricket"})

print('this is the my joke --->',result['joke'])
print('this is the your explanation --->',result['explanation'])
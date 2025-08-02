from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableSequence
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(model="gemini-2.0-flash")

prompt = PromptTemplate(
    template="Generate a tweet about {topic}",
    input_variables=["topic"]
)

prompt1 = PromptTemplate(
    template="Generte a Linkedin post about of {topic}",
    input_variables=["topic"]
)
parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt, model, parser),
    'linkedin': RunnableSequence(prompt1, model, parser)
})

result = parallel_chain.invoke({'topic': 'AI'})

print(result['tweet'])
print(result['linkedin'])
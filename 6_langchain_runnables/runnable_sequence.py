from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(model="gemini-2.0-flash")

prompt = PromptTemplate(
    template= "write a joke on {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)

chain = RunnableSequence(prompt, model, parser, prompt1, model, parser)

print(chain.invoke({'topic': 'AI'}))
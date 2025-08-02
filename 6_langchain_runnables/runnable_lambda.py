from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableSequence, RunnablePassthrough, RunnableLambda

from dotenv import load_dotenv

load_dotenv()

def count_word(text):
    return len(text.split())

model = GoogleGenerativeAI(model="gemini-2.0-flash")

prompt = PromptTemplate(
    template="Generate a joke about {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)

parralel_chain = RunnableParallel({
    'Joke': RunnablePassthrough(),
    'Word': RunnableLambda(count_word)
})

final_chain = RunnableSequence(joke_gen_chain, parralel_chain)

result = final_chain.invoke({'topic': 'bollywood'})

print(result)
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-0528",
    task="text-generation"
)
    # "TinyLlama/TinyLlama-1.1B-Chat-v1.0",

model1 = ChatHuggingFace(llm = llm)
model2 = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt = PromptTemplate(
    template='Classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction': parser2.get_format_instructions()}
)

prompt2 = PromptTemplate(
    template='Write short an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write short an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

classifier_chain = prompt | model1 | parser2

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | model2 | parser),
    (lambda x:x.sentiment == 'negative', prompt3 | model2 | parser),
    RunnableLambda(lambda x: 'Could not find sentiment')
)

chain = classifier_chain | branch_chain

result = chain.invoke({'feedback': 'This is the great phonebook'})
# print(result)
print(chain.invoke({'feedback': 'This is the great phonebook'}))
# result = classify_chain.invoke({'feedback': 'This is wonderfull smartphone'}).sentiment

# print(result)
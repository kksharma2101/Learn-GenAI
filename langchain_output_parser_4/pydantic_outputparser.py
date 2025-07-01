# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="deepseek-ai/DeepSeek-R1-0528",
#     task="text-generation"
# )
    # "TinyLlama/TinyLlama-1.1B-Chat-v1.0",

# model = ChatHuggingFace(llm = llm)
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

class Person(BaseModel):
    
    name: str = Field(description="Name of the person")
    age: int = Field(gt=18, description="age of the person")
    city: str = Field(description="Name of the city the person belong to")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Generate the name, age and city of a fictional {place} person \n {format_intruction}',
    input_variables=['place'],
    partial_variables={'format_intruction': parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'place': 'india'})

print(result)
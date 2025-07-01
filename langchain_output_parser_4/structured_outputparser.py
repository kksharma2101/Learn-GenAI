# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="deepseek-ai/DeepSeek-R1-0528",
#     task="text-generation"
# )
    # "TinyLlama/TinyLlama-1.1B-Chat-v1.0",

# model = ChatHuggingFace(llm = llm)
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

schema = [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic')
    ]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give 3 fact about the {topic} \n {format_intruction}',
    input_variables=['topic'],
    partial_variables={'format_intruction': parser.get_format_instructions()}
)

# prompt = template.invoke({'topic': 'black hole'})

# result = model.invoke(prompt)

# final_result =parser.parse(result.content)
chain = template | model | parser
result = chain.invoke({'topic': 'narendra modi'})

print(result)

# Disadvantage of StructuredOutputParser: It is not capable to data valication
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# , HuggingFacePipeline
# if you want to load model data on your local machine so used HuggingFacePipeline
from dotenv import load_dotenv
import os
load_dotenv()

# Example of local machine model data
# llm = HuggingFacePipeline.from_model_id(
#     model_id="meta-llama/Meta-Llama-3-70B-Instruct",
#     task="text-generation",
#     pipeline_kwargs=dict(
#         tempreture=1.2,
#         max_new_tokens=200
#     )
# )
# model = ChatHuggingFace(llm)
# res = model.invoke("input")

# llm = HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0", # This model work on HuggingFace API
#     task="text-generation",
#     temperature=1.5
#     )

# Get the API key from environment
hf_token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

# Pass the token explicitly to HuggingFaceEndpoint
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-0528",
    task="text-generation",
    temperature=0.6,
    max_new_tokens=512,
    huggingfacehub_api_token=hf_token,
)

model = ChatHuggingFace(llm=llm)

res = model.invoke("Who is the cm of Uttar Pradesh")

print(res.content)
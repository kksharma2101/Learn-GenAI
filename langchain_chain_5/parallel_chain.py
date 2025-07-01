from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-0528",
    task="text-generation"
)
    # "TinyLlama/TinyLlama-1.1B-Chat-v1.0",

model1 = ChatHuggingFace(llm = llm)
model2 = ChatGoogleGenerativeAI(model="gemini-2.0-flash")


prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Generate 5 short question answers from the following text \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain = prompt3 | model2 | parser

chain = parallel_chain | merge_chain

text = """
Largest Contentful Paint (LCP) is an important, stable Core Web Vital metric for measuring perceived load speed because it marks the point in the page load timeline when the page's main content has likely loaded—a fast LCP helps reassure the user that the page is useful.

Historically, it's been a challenge for web developers to measure how quickly the main content of a web page loads and is visible to users. Older metrics like load or DOMContentLoaded don't work well because they don't necessarily correspond to what the user sees on their screen. And newer, user-centric performance metrics like First Contentful Paint (FCP) only capture the very beginning of the loading experience. If a page shows a splash screen or displays a loading indicator, this moment isn't very relevant to the user.

In the past, we've recommended performance metrics like First Meaningful Paint (FMP) and Speed Index (SI) (both available in Lighthouse) to help capture more of the loading experience after the initial paint, but these metrics are complex, hard to explain, and often wrong—meaning they still don't identify when the main content of the page has loaded.

Based on discussions in the W3C Web Performance Working Group and research done at Google, we've found that a more accurate way to measure when the main content of a page is loaded is to look at when the largest element is rendered.
"""

result = chain.invoke({'text': text})

print(result)

# chain.get_graph().print_ascii()
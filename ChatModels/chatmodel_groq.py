# from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0.7,
    # max_completion_tokens=10 # Restrict Tokens in output, like number is max so token generate max oposite as less number
)
# Temprature is a parameter that controls the randomness of a language model's output. It affects how creative or deterministic the response are.
# Lower Values: (0.0 - 0.3) = more deterministic and predictable
# Higher Values: (0.7 - 1.5) = more random, creative and diverse

# Use Case                                              Recommended Temprature
# Factual answer (Math, Code, facts)                    (0.0 - 0.3)
# Balanced Response (General, QA, Explanations)         (0.5 - 0.7)
# Creative, Writing, StoryTelling, Jokes                (0.9 - 1.2)
# Maximum Randomness (Wild Ides, BrainStorming)         (1.5+) Max Should be 2

res = llm.invoke("what is the capital of india")

print(res.content)
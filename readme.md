# What is the prompt?
- Prompts are the input instructions or queries given to a model to guide its output.
- Example: model.invoke("What is capital of india.)
- Note - Prompts has two type 1. Text base prompts, 2. Multimodel prompts

- Langchain has 3 types of messages like System msg, Human msg and AI msg. its help of crete chatbot

* Message placeholder

- A message placeholder in langchain is a special placeholder used inside a ChatPromptTemplate to dynamically insert chat history or a list of messages at runtime.

# Structured Output
- In langchain, structured output refers to the practice of having language models return responses in a well-defined data format (for example json), rather than free form text. this is makes the model output easier to parse and work with programmatically.

### most usecase of Structred Output:
- Data Extraction
- API Building
- Agents

# Output Parsers
- Output Parsers in Langchain help convert rew llm responses into structured formats like JSON, CSV, Pydantic models and more. They ensure consistency, validation and ease of use in applications.
- StrOutputParser: is the simplest output parser in langchain. It is used to parse the output of a Language Model(LLM) and return it as a plain string.
- JSONOutputParser
- StructuredOutputParser: This parser is helps structured Json data from LLM responses based on predefined field Schemas.
- PydanticOutputParser: This is a structured output parser in Langchain that uses Pydantic models to enforce schema validation when processing LLM responses.

# Runnables
- Runnables simplify the process of building, managing, and modifying complex workflows by providing a standardized way for different components to interact.
- Langchain has two types of runnables "Task Specific Runnables" and "Runnable Primitive".
- Task Specific Runnables: These are Core Langchain Components that have been converted into runnables so they can be used in pipslines. and is perform task specific operations like LLM Calls, Prompting, retrieval etc.
- Examples: 
    ChatOpenAI - Runs an LLM models.
    PromptTemplate - Formats Prompt Dynamically.
    Retriever - Retrieve relevent documents.

- Runnable Primitive: These are 'fundamental building blocks' for structuring execution logic in AI workflows. and They 'help orchestrate execution' by defining how different runnables interact (Sequentially, in parallel, conditionally etc.).
- Examples: 
    RunnablesSequence: Runs step in order ( | operator).
    RunnableParallel: Runs multiple steps simultaneously and etc.
    RunnableMap:
    RunnableBranch:
    RunnableLambda:
    RunnablePassThrough:
# What is the prompt?
- Prompts are the input instructions or queries given to a model to guide its output.
- Example: model.invoke("What is capital of india.)
- Note - Prompts has two type 1. Text base prompts, 2. Multimodel prompts

- Langchain has 3 types of messages like System msg, Human msg and AI msg. its help of crete chatbot

### Message placeholder
- A message placeholder in langchain is a special placeholder used inside a ChatPromptTemplate to dynamically insert chat history or a list of messages at runtime.

# Structured Output
- In langchain, structured output refers to the practice of having language models return responses in a well-defined data format (for example json), rather than free form text. this is makes the model output easier to parse and work with programmatically.

### most usecase of Structred Output:
- Data Extraction
- API Building
- Agents

# Typed Dictionary or Pydantic
- Pydantic is a data validation and data parsing library for python. It ensures that the data you work with is correct, structured and type-safe.

- TypedDict is a way to define a dictionary in python where you specify what keys and values should exist, It helps ensure that your dictionary follows a specific structure.

### Usecase
- It tells: Python what key are required and what types of values should have.
- It does not validate data at runtime (it just helps with type hints for better coding).
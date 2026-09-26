from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(
    model="llama3.2:3b",
)

prompt = ChatPromptTemplate(
    [
        ("system", "You are a teacher that mentors students. You must remember the student's name, goal, and preferred explanation style "),
        ("human", "Hello, i am {name}, I want to learn about  {topic}."),
        ("ai", "Hi {name}, sure, we can learn about {topic}, but what is your preferred explanation style?"),
        # ("human", "{input}")
    ]
)

parser = StrOutputParser()
chain = prompt | llm | parser

user_input=""

vars = {
    "name": "kacchan",
    "topic" : "making matcha",
    "input" : user_input
}

# result = chain.invoke(vars)

# print(f"Convo start: {result}")
# user_input = input("Reply to AI: ")
# prompt.append(message=("human", user_input))


# result2 = (prompt | llm | parser).invoke(vars)
# print(f"AI Response 2: {result2}")
# # second invoke will start over the


prompt2 = ChatPromptTemplate([
    ("system", "You are a teacher that mentors students. You must remember the student's name, goal, and preferred explanation style. Make sure start with greetings and asking them question so that you get enough context."),
])

human_input = ""
iteration = 1

# def invokeAI():



while True:

    chain = prompt2 | llm | parser

    result3 = chain.invoke(vars)

    print(f"AI: {result3}")
    print(f"[debug] iteration : {iteration}")
    # only if ai is asking question we ask for human input
    human_input = input("You :")

    if (input == ("quit" or "exit" or "X")) :
        break

    prompt2.append(("human", human_input))
    iteration+=1


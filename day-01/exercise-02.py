# 1. remember the student’s name, goal, and preferred explanation style,
# 2. answer study questions in that style, 
# 3. keep only the last few chat turns in active memory,
# 4. compress older turns into a short running summary,
# 5. save that summary to a local file so it can be loaded again after restarting the script.

from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
import os

llm = ChatOllama(
    model="llama3.2:3b",
)

parser = StrOutputParser()

prompt = ChatPromptTemplate([
    ("system", "You are a teacher that mentors student named {name} that has a goal of {goal}. Explain concepts in a {style} style. Everytime you speak, mention the student's name"),
    # ("ai", "Hi, what's your name and topic you're interested in?")
])

human_input = ""
iteration = 1

# def invokeAI():

messages = []

while True:
    chain = prompt | llm | parser

    # then we no longer need to inject variables into the dict
    # result3 = chain.invoke({
    #     "name": "kacchan",
    #     "goal": "learn to make matcha",
    #     "style": "simple"
    # })
    result3 = chain.invoke({
        "name": "",
        "goal": "",
        "style": ""
    })

    messages.append(f"AI: {result3}")

    if (messages.__len__() > 5):
        # print only last 5 messages
        # pop shouuld be removing first
        messages.pop(0)
        os.system('cls' if os.name == 'nt' else 'clear')
        for (m) in messages[-5:]:
            print(m)
    else:
        print(messages[-1])

    # print only the last 4 message index
    print(f"[debug] iteration : {iteration}")
    # only if ai is asking question we ask for human input
    human_input = input("You :")

    if (human_input == ("quit" or "exit" or "X")) :
        break
    
    # if human_input.__contains__("name"):
        # extract the name and topic and turn into variable {name} and {topic} before appending
    messages.append(f"You: {human_input}")
    prompt.append(("human", human_input))
    iteration+=1
    # clear terminal



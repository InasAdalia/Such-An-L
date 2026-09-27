# 1. remember the student’s name, goal, and preferred explanation style, ✅
# 2. answer study questions in that style, ✅
# 3. keep only the last few chat turns in active memory ✅
# 4. compress older turns into a short running summary,
# 5. save that summary to a local file so it can be loaded again after restarting the script.
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from utils import GREEN, RESET
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
history = []
human_input = ""
iteration = 1

while True:
    prompt = ChatPromptTemplate([
        ("system", "You are a teacher that mentors the user as a student. Begin by asking for the student's name, topic of interest, and preferred explanation style. Always mention their name in every conversation."),
        *history,
    ])
    chain = prompt | llm | parser

    result = chain.invoke({
        "name": "",
    })

    history.append(AIMessage(result))

    if (history.__len__() > 5): # print only last 5 messages
        
        os.system('cls' if os.name == 'nt' else 'clear') # clear terminal
        for (h) in history[-5:]:
            print(f"AI: {h.content}")
    else: # print last element
        print(f"AI: {history[-1].content}")

    # print only the last 4 message index
    print(f"[debug] iteration : {iteration}")

    human_input = input("You :")

    if (human_input == ("quit" or "exit" or "X")) :
        break
    
    history.append(HumanMessage(human_input))

    # [debug] to check history contents passed into prompt
    print(f"{GREEN}\n[debug]HISTORY: \n")
    for (index, h) in enumerate(history, start=1):
        print(f"{GREEN}\n{index}. {h.type}: {h.content} {RESET}\n")

    iteration+=1



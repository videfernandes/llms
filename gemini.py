from dotenv import load_dotenv
import os
from langchain_core.prompts import ChatPromptTemplate

from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env file
load_dotenv()

template = """Question: {question} 
Answer: Let's think step by step, in portuguese."""

# Access the environment variable
google_api_key = os.getenv("GOOGLE_API_KEY")

prompt = ChatPromptTemplate.from_template(template)

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

chain = prompt | llm


ai_msg = chain.invoke({"question": "What is LangChain?"})
print(ai_msg.content)

# messages = [
#     ("system", "Você é um assistente que traduz do portugues para o francês. Traduza o seguinte."),
#     ("human", "Olá mundo")
# ]
# ai_msg = llm.invoke(messages)
# print(ai_msg.content)
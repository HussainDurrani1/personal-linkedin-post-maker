import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from schemas import LinkedInPost
from prompts import linkedin_prompt

load_dotenv()
gemini_api_key = os.getenv("GOOGLE_API_KEY")


model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", api_key=gemini_api_key)

structured_model = model.with_structured_output(LinkedInPost)

linkedin_chain = linkedin_prompt | structured_model
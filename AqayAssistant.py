import openai
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List


app = FastAPI()

class UserInput(BaseModel):
    user_input: str

chat_log = [{'role':'system', 
             'content':'Welcome to AQAY.\
             AQAY is an online ecommerce platform designed to empower local businesses by showcasing their unique offerings to a broader audience. \
             AQAY\'s primary goal is to help you discover and explore products that match your interests and needs.\
            You are AQAY\'s AI assistant. Your task is to handle user inquiries effectively. Users might ask questions such as: \
            "Can you recommend me some stylish clothing options for summer?"\
            "What are some popular skincare products available on AQAY?"\
            "I\'m looking for handmade jewelry, what options do you have?"\
            Your role involves advanced AI technology to understand user queries and recommend products from our diverse selection of local brands.\
            Whether you\'re searching for fashion, beauty products, accessories, or more, AQAY is here to assist you in finding the perfect match.\
             Let\'s dive into AQAY\'s world of Egyptian craftsmanship and innovation together!'}]

@app.post("/AqayAssistant/")
async def chat(user_input: UserInput):
    chat_log.append({'role':'user', 'content':f'{user_input}'})
    openAI_response = openai.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=chat_log
    )
    chat_response = openAI_response.choices[0].message.content
    return {"response": f"{chat_response}"}


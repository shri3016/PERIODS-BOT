from textbase import bot, Message
from textbase.models import OpenAI
from typing import List

# Load your OpenAI API key
OpenAI.api_key = "YOUR_API_KEY"


SYSTEM_PROMPT = """You are chatting with an AI specialized in menstrual health. The AI will provide information and answers related to menstrual health topics. Feel free to ask questions or seek information about menstruation, menstrual cycles, period pain, and related subjects.
"""

@bot()
def on_message(message_history: List[Message], state: dict = None):

    # Generate GPT-3.5 Turbo response
    bot_response = OpenAI.generate(system_prompt=SYSTEM_PROMPT,
        message_history=message_history, # Assuming history is the list of user messages
        max_tokens=100,
        model="gpt-3.5-turbo",
    )
    
    response = {
        "data": {
            "messages": [
                {
                    "data_type": "STRING",
                    "value": bot_response,
                }
            ],
            "state": state
        },
        "errors": [
            {
                "message": ""
            }
        ]
    }

    return {
        "status_code": 200,
        "response": response
    }

import os
from anthropic import Anthropic
if __name__ == '__main__':

    XAI_API_KEY = os.getenv("XAI_API_KEY")
    client = Anthropic(
        api_key=XAI_API_KEY,
        base_url="https://api.xaicontrol.com",
    )
    message = client.messages.create(
        model="glm-4.6",
        max_tokens=128,
        system="You are AI.",
        messages=[
        {
            "role": "user",
            "content": "What is the meaning of life, the universe, and everything?",
        },
        ],
    )
    print(message.content)
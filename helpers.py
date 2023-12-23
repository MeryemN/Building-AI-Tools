#pydantic example
from openai import OpenAI
import os

# Load environment variables from the .env file

# Access the OpenAI API key

import instructor


#Replace With Your Open AI Key
open_ai_client = OpenAI(
     api_key="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",
)

instructor.patch(open_ai_client)

def structured_generator(openai_model,prompt,custom_moel):
    result : custom_moel = open_ai_client.chat.completions.create(
        model = openai_model, 
        response_model = custom_moel,
        messages= [{"role":"user","content" : f"{prompt}, output must be in json"}]
    )
    return result



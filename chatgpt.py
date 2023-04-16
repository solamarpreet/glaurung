import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_TOKEN")

response = openai.Completion.create(model="text-davinci-003", max_tokens=2048, prompt="can you generate python code for a simple discord bot")
print(response.choices[0].text.strip())
import openai
import config

openai.api_key = config.get_openai_token()

def get_chat_completion(message):
    return openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": message}
            ]
            )

import openai
import config

openai.api_key = config.get_openai_token()

def get_chat_completion(message):
    list_handler(message)
    completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=message_db[message.author]
            )
    message_db[message.author].append({"role": "assistant", "content": completion.choices[0].message.content})
    return completion.choices[0].message.content

def list_handler(message):
    if message_db.message.author:
        message_db[message.author].append({"role": "user", "content": message.content})
    else:
        message_db[message.author] = [{"role": "system", "content": "You are a helpful tutor that explains programming, devops concepts. You also generate code when asked, giving examples."}]

message_db = dict()
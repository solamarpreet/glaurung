import openai
import config
from textwrap import fill
import personas

openai.api_key = config.get_openai_token()
db = {}


def completion_handler(msg):
    if msg.content[:4].lower() == "glau":
        if msg.content[:10].lower() == "glau reset":
            db[msg.author.id] = [
            {"role": "system", "content": personas.persona_dict["code"]}
            ]
            return ("Noted !",)
        
        else:
            db[msg.author.id] = [
            {"role": "system", "content": msg.content[5:]}
            ]
            return get_chat_completion(msg)

    elif db.get(msg.author.id):
        db[msg.author.id].append({"role": "user", "content": msg.content})

    else:
        db[msg.author.id] = [
            {"role": "system", "content": personas.persona_dict["code"]},
            {"role": "user", "content": msg.content}
            ]
        
    return get_chat_completion(msg)


def get_chat_completion(msg):    
    completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=db[msg.author.id]
            )
    answer = completion.choices[0].message.content
    db[msg.author.id].append({"role": "assistant", "content": answer})
    if len(answer) > 2000:
    # Split the string into lines of at most 2000 characters each, preserving whole sentences
        answer_lines = fill(answer, width=2000, break_long_words=False).split("\n")
        return answer_lines
    else:
        return (answer,)

import openai
import config

openai.api_key = config.get_openai_token()
db = {}


def completion_handler(msg):
    print(msg.content)
    if msg.content.startswith("glau"):
        if msg.content.startswith("glau reset"):
            db[msg.author.id] = [
            {"role": "system", "content": "You are a helpful tutor that explains programming, devops concepts. You also generate code when asked, giving examples."}
            ]
            print(db)
            return "Noted !"
        else:
            db[msg.author.id] = [
            {"role": "system", "content": msg.content[5:]}
            ]
            return get_chat_completion(msg)

    elif db.get(msg.author.id):
        db[msg.author.id].append({"role": "user", "content": msg.content})

    else:
        db[msg.author.id] = [
            {"role": "system", "content": "You are a helpful tutor that explains programming, devops concepts. You also generate code when asked, giving examples."},
            {"role": "user", "content": msg.content}
            ]
        
    return get_chat_completion(msg)


def get_chat_completion(msg):    
    print(db)
    completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=db[msg.author.id]
            )
    db[msg.author.id].append({"role": "assistant", "content": completion.choices[0].message.content})
    return completion.choices[0].message.content

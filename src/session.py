import openai

f = open("./assets/API_KEY.txt", "r")
openai.api_base = 'https://api.pawan.krd/v1'
openai.api_key = f.read()
f.close()

f = open("./assets/PERSONALITY.txt", "r")
messages = [
    {"role":"system", "content":f.read()}
]
f.close()

def ask(question):
    messages.append({"role":"user", "content":question})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    chat_response = completion.choices[0].message.content
    print(chat_response)
    messages.append({"role":"assistant", "content":chat_response})


while True:
    question = str(input('>> '))
    if question == 'quit' or question == 'q':
        break
    else:
        ask(question)
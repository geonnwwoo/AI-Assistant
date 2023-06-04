import openai

f = open("./assets/API_KEY.txt", "r")

openai.api_base = 'https://api.pawan.krd/v1'
openai.api_key = f.read()

f.close()

def ask(question) :
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question}
        ]
    )

    print(completion.choices[0].message.content)


while True:
    question = str(input('>> '))
    if question == 'quit' or question == 'q':
        break
    else:
        ask(question)
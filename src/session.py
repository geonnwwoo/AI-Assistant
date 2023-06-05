import openai

f = open("./assets/API_KEY.txt", "r")
openai.api_base = 'https://api.pawan.krd/v1'
openai.api_key = f.read()
f.close()

def check_file_empty(file_path):
    try:
        with open(file_path, 'r') as file:
            if file.read().strip():
                return True
            else:
                return False
    except FileNotFoundError:
        return "File not found"
    except IOError:
        return "Error reading the file"
    
def file_contains_text(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if any(char.isprintable() for char in line):
                return True
    return False

def ask(question):
    messages.append({"role": "user", "content": question})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    chat_response = completion.choices[0].message.content
    print(chat_response)
    messages.append({"role": "assistant", "content": chat_response})

    with open('./assets/messages.txt', "w") as file:
        file.write(str(messages))


messages = []

if check_file_empty('./assets/messages.txt'):
    if file_contains_text('./assets/PERSONALITY.txt'):
        f = open("./assets/PERSONALITY.txt", "r")
        messages = [{"role": "system", "content": f.read()}]
        f.close()
    else:
        f = open("./assets/messages.txt", "r")
        messages = eval(f.read())
        f.close()
else:
    f = open("./assets/messages.txt", "r")
    messages = eval(f.read())
    f.close()

while True:
    question = str(input('>> '))
    if question == 'quit' or question == 'q':
        break
    else:
        ask(question)
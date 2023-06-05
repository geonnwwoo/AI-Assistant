# AI-Assistant

## Set-up

To make the ask.sh file available for use, use:
```
cd ./src/
chmod u+x ask.sh
```
By doing this, you give permission to ask.sh file.

You have to set an API Key from [here](https://github.com/PawanOsman/ChatGPT). You have to go to their Discord Server and get a private API Key. To use the API Key, use the command:
```
./ask.sh set-apikey [your API Key]
```

You can then give the Chatbot a personality by using the command:
```
./ask.sh set-personality [personality]
```
For example:
```
./ask.sh set-personality 'You are Abraham Lincoln'
```

## Usage

To ask a single question, use:
```
./ask [question]
```
For example:
```
./ask 'When was Thomas Jefferson born?'
```

To create a session where you can ask multiple questions, use:
```
./ask start
```
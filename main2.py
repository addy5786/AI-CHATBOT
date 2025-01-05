import nltk
from nltk.chat.util import Chat,reflections

pairs=[
    (r'Hello|Hi',['Hello,How are you']),
    (r'(.*)I am Fine',['Glad to know that,How can i help you']),
    (r'What do you call yourself?',['I am just a simple ChatBot']),
    (r'(.*)Your Name?', ['My name is AdilBot']),
    (r'(.*)Can you tell me a joke?', ["Sure! Here’s a classic one for you: Why don't scientists trust atoms? Because they make up everything!"]),
    (r'(.*)Tell me about your self(.*)?',['I am just a computer program']),

    (r'Thanks(.*)',['You are Welcome']),
    (r'(.*)bye|by(.*)',['It was great chatting with you,Please visit again'])
]


print("Welcome to the NTLK Chatbhot")

chatbot =Chat(pairs)
chatbot.converse()

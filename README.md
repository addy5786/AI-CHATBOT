# AI-CHATBOT

**Name**: ADIL SHAIKH

**Company**: CODETECH IT SOLUTIONS

**ID**: CT08DJS

**Domain**: Python Programming

**Duration**:12th December to 12th January

**Mentor**: Neela Santhosh Kumar

# OUTPUT OF THIS CODE

# PROJECT:AI-CHATBOT

![OUTPUT](https://github.com/user-attachments/assets/64234a9b-8063-49b0-92ee-09e08e8e654a)

This code implements a simple chatbot using the Natural Language Toolkit (NLTK) library in Python. 
Here’s an overview of each part of the code:

# 1. Importing Libraries:

The code imports the nltk library, which is a popular library for natural language processing in Python.
It specifically imports the Chat class and reflections from nltk.chat.util, which are used to create a simple rule-based chatbot.

# 2. Defining Conversation Patterns:

A list named pairs is defined, which contains tuples.Each tuple consists of:
A regular expression pattern (as a string) that the chatbot will look for in user input.
A list of possible responses that the chatbot can give when it matches the pattern.

# For example:

The pattern r'Hello|Hi' matches greetings, and the response is ['Hello, How are you'].
The pattern r'(.*)I am Fine' matches any input that includes "I am Fine" and responds with ['Glad to know that, How can I help you'].

# 3. Chatbot Initialization:

The code prints a welcome message to the user: "Welcome to the NTLK Chatbot".
An instance of the Chat class is created using the defined pairs. This instance will handle the conversation logic.

# 4. Starting the Conversation:

The converse() method of the Chat class is called, which starts the chatbot's interaction with the user.
The chatbot will continue to respond to user input until the user types a termination phrase (like "bye").

Overall, this code creates a simple rule-based chatbot that can respond to specific user inputs based on predefined patterns and responses.
It demonstrates basic natural language processing capabilities using regular expressions to match user queries and provide appropriate responses.
The chatbot can handle greetings, inquiries about itself, jokes, and farewells, making it a basic conversational agent.

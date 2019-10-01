# Truck-Chatbot
This repository build a small interactive system (Chat Bot) to identify trucks, their specification and number in particular fleet.
Customer is Fleet Owner or Fleet manager.
All conversations recorded for future analysis.

This chatbot is trained on Corpus of truck_data using
ChatterBot: https://github.com/gunthercox/ChatterBot and it can be improved by adding new conversations.


### Requirements
- python 3.5, 3.6
- chatterbot
- chatterbot-corpus
- csv
- nltk
- nameparser

```bash
pip install -r requirements.txt
```

### Usage

Chat start by running the chat script, chat is done in Terminal.:

```python
python chat.py
```

### Example of output

****** To finish the conversation, Please type Bye  *******

ChatBot: Hello, What is your name (First name and last name)?

User:John smith

JOHN SMITH, what do you do?

User:fleet owner

ChatBot: do you have a truck?

User:yes

ChatBot: (specification) what is the brand of your truck?

User:volvo

ChatBot: (specification) what is the Size of your truck, light, medium or heavy?

User:light

ChatBot: (specification) what is the class of your truck (eg. class 1-8)?

User:class2

ChatBot: what is the number of your truck?

User:PA-2345-00

ChatBot: Thanks for your information, Bye.

Trucks information: {'Specifications': ['volvo', 'light', 'class2'], 'Truck_Number': 'pa-2345-00'}
****All conversation was recorded in ./recorded_chat.csv****



All conversations are recorded in a csv file. In addition. truck's information are saved in a csv file.
Users are separated by a line in the csv files.


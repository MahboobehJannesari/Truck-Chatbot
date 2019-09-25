# Truck-Chatbot
This repository build a small interactive system (Chat Bot) to identify trucks, their specification and number in particular fleet.
Customer is Fleet Owner or Fleet manager.
All conversations recorded for future analysis.

This chatbot is trained on some lists of short conversation using
ChatterBot: https://github.com/gunthercox/ChatterBot and it can be improved by adding new conversations.


### Requirements
- python 3.5
- chatterbot 1.0.5
- chatterbot-corpus 1.2.0
- csv

```bash
pip install -r requirements.txt
```

### Usage

In first step, chatbot should be trained on "truck_data" by running the train script:

```python
python train.py
```

In second step, chat start by running the chat script, chat is done in Terminal.:

```python
python chat.py
```

### Example of output

******To finish the conversation, Please type Bye*******

ChatBot: Hello, What is your name?

User:Hi, Mr John 

ChatBot: What do you do?

User:I work as fleet manager

ChatBot: Do you have truck?

User:Yes,I have

ChatBot: What is the number of your truck?

ChatBot: The number is PA1234

User:The number is PA1234

ChatBot: what is specification of your truck?

User:mini, red

ChatBot: Red, mini track

User:bye

ChatBot: Bye

Trucks information: {'Truck_Number': 'The number is PA1234', 'Specifications': 'mini, red'}

****All conversation was recorded in ./recorded_chat.csv****



All conversations are recorded in a csv file. In addition. truck's information are saved in a csv file.
Users are separated by a line in the csv files.


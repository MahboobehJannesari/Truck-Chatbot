from chatterbot import ChatBot
from nameparser.parser import HumanName
import csv
import nltk
from chatterbot.trainers import ChatterBotCorpusTrainer


# detect name of human
def get_human_names(text):
    tokens = nltk.tokenize.word_tokenize(text)
    pos = nltk.pos_tag(tokens)
    sentt = nltk.ne_chunk(pos, binary = False)
    person_list = []
    person = []
    name = ""
    for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON'):
        for leaf in subtree.leaves():
            person.append(leaf[0])
        if len(person) > 1: #avoid grabbing lone surnames
            for part in person:
                name += part + ' '
            if name[:-1] not in person_list:
                person_list.append(name[:-1])
            name = ''
        person = []
    return (person_list)


def main():
    corpus_path = "./truck_data/"

    # a chatbot that do not learn duraing chat
    chatbot = ChatBot('Truck Bot',
                          preprocessors=["chatterbot.preprocessors.clean_whitespace",
                                         "chatterbot.preprocessors.convert_to_ascii"],
                          logic_adapters=[
                              {
                                  'import_path': 'chatterbot.logic.BestMatch',
                                  'default_response': 'Do you have a truck?',
                                  'maximum_similarity_threshold': 0.9
                              }
                          ], read_only=True)

    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train('chatterbot.corpus.english.greetings')

    trainer.train(corpus_path)


    # path of csv file to save all conversation
    recorded_chat_path = "./recorded_chat.csv"
    # path of csv file to save all information about trucks
    trucks_info_path = "./truck_info.csv"
    print("bye", "Bye".find("Bye"))

    print("****** To finish the conversation, Please type Bye  *******")

    # csv file for recording conversation, if it is not exist, it will created
    csv_file_chat = open(recorded_chat_path, "a")
    fieldnames = ["ChatBot", "User"]
    writer_chat = csv.DictWriter(csv_file_chat, fieldnames=fieldnames)
    # write header only once
    if csv_file_chat.tell()==0:
        writer_chat.writeheader()
    csv_file_chat.write("\n")


    # csv file for recording truck information, if it is not exist, it will created
    csv_file_truck = open(trucks_info_path, "a")
    fieldnames = ["Truck_Number", "Specifications"]
    writer_truck = csv.DictWriter(csv_file_truck, fieldnames=fieldnames)
    # write header only once
    if csv_file_truck.tell() == 0:
        writer_truck.writeheader()
    csv_file_truck.write("\n")


    ## bot start convesation
    print("ChatBot: Hello, What is your name (First name and last name)?")
    question = "Hello, What is your name?"
    reply = input("User:")
    writer_chat.writerow({"ChatBot": question, "User": reply})
    name = get_human_names("my name is " + reply.upper())

    if name:
        print("%s, what do you do?"%(name[0]))
    else:
        print("I think your name is not correct\n")

        print("what do you do?")

    question = "what do you do?"

    # a dictionary for saving the number and specification of trucks
    trucks_info = {}
    specification = []

    # continue conversation until user type bye or Bye
    while True:
        # user reply
        reply = input('User:')
        reply = reply.lower()

        # if user type bye or if usere does not any truck, conversation will be finished
        if reply.strip() == 'bye':
            print('ChatBot: Bye')
            writer_chat.writerow({"ChatBot":question, "User":"Bye"})
            break

        else:
            # record the number of truck and Specifications
            writer_chat.writerow({"ChatBot":question, "User":reply})

            if str(question).find("specification") > 0:
                specification.append(reply)
                trucks_info["Specifications"] = specification

            #last question
            elif str(question).find("number") > 0:
                trucks_info["Truck_Number"] = reply
                print("ChatBot: Thanks for your information, Bye.")
                writer_chat.writerow({"ChatBot": "Bye", "User": "Bye"})
                break

            # chatbot ask next question according user's reply, e.g. If user does not any truck, conversation will be fininshed.
            question = chatbot.get_response(reply)
            print('ChatBot:', question)
            if str(question).strip() == "bye.":
                writer_chat.writerow({"ChatBot": question, "User": "Bye"})
                break

    writer_truck.writerow(trucks_info)

    print("Trucks information:", trucks_info)
    print("****All conversation was recorded in %s****\n"%recorded_chat_path)


if __name__ == '__main__':
    main()
from chatterbot import ChatBot
import csv

# a chatbot that do not learn duraing chat
chatbot = ChatBot('Truck Bot', read_only=True)
# path of csv file to save all conversation
recorded_chat_path = "./recorded_chat.csv"
# path of csv file to save all information about trucks
trucks_info_path = "./truck_info.csv"

def main():
    print("******To finish the conversation, Please type Bye*******")

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
    print("ChatBot: Hello, What is your name?")
    question = "Hello, What is your name?"

    # a dictionary for saving the number and specification of trucks
    trucks_info = {}
    no_truck = False

    # continue conversation until user type bye or Bye
    while True:
        # user reply
        reply = input('User:')

        # if user type bye or if usere does not any truck, conversation will be finished
        if reply.strip() == 'Bye'.lower():
            print('ChatBot: Bye')
            writer_chat.writerow({"ChatBot":question, "User":"Bye"})
            break

        else:
            # record the number of truck and Specifications
            writer_chat.writerow({"ChatBot":question, "User":reply})
            if str(question).find("number") > 0:
                trucks_info["Truck_Number"] = reply

            elif str(question).find("specification") > 0:
                trucks_info["Specifications"] = reply
                writer_truck.writerow({"Truck_Number":trucks_info["Truck_Number"], "Specifications": reply})

            # chatbot ask next question according user's reply, e.g. If user does not any truck, conversation will be fininshed.
            question = chatbot.get_response(reply)
            print('ChatBot:', question)
            if str(question).strip() == "Bye":
                writer_chat.writerow({"ChatBot": question, "User": "Bye"})
                break

    print("Trucks information:", trucks_info)

    print("****All conversation was recorded in %s****\n"%recorded_chat_path)


if __name__ == '__main__':
    main()
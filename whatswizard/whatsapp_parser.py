import pandas as pd
import re

"""
This file header will provide a short description of whatsapp-parser.py

whatsapp_parser.py can be used to take an exported chat log (from WhatsApp) in this format:
[07/12/2022, 10:22:11 PM] Dhiren: Hello

The general format is [dd/mm/yyyy, hh:mm:ss AM/PM] sender: message.
Then, it extracts the timestamp, sender and message and puts them in a CSV.

Documentation by : Mandhiren Singh
"""
__author__ = "Mandhiren Singh"

def parse_actual_file(chatlog):
    """
    This function converts the raw .txt chatlog file to a DataFrame.

    :param chatlog: a .txt file obtained by exporting from WhatsApp (mobile app)
    :return: a DataFrame containing the timestamp, sender and message.
    """

    # Use the `open()` function to open the chat file
    with open(chatlog, "r", encoding='utf-8') as file:
        # Use the `readlines()` method to read the lines of the chat file
        lines = file.readlines()

    # Create a regular expression that matches the format of the chat file
    # The regular expression should look for a timestamp in the format `dd/mm/yyyy, hh:mm:ss AM/PM`,
    # followed by the sender's name and a colon, and finally the message itself
    pattern = re.compile(r"\[(\d{2}/\d{2}/\d{4}, \d{1,2}:\d{2}:\d{2} [AP]M)\] ([^:]+): (.*)")

    # Create an empty data frame
    data = pd.DataFrame()

    # Create a list then only make the data frame once
    data_list = []

    try:
        # Iterate over the lines of the chat file
        for line in lines:
            # Use the `re.match()` method to apply the regular expression to the line
            # and extract the relevant information
            match = pattern.match(line)

            # If the regular expression matches the line, add the extracted information
            # to the data frame
            if match:
                timestamp = match.group(1)
                sender = match.group(2)
                message = match.group(3)

                data_list.append([timestamp, sender, message])
    except:
        pass

    # Make the data frame
    data = pd.DataFrame(data_list, columns=['timestamp', 'sender', 'message'])


    # Print the data frame for reference
    print(data)

    # Convert data to CSV and store in directory
    extracted_file_name = str(chatlog).replace('.txt', '') + "_extracted.csv"
    data.to_csv(extracted_file_name)

    return data


def enhance_data(csv_file):
    """
    This function converts the strings to datetime objects and adds useful columns like weekday, month sent, date and
    hour.

    :param csv_file: file to work on (WhatsApp chatlog file)
    :return: enhanced DataFrame
    """


    data = pd.read_csv(csv_file)

    # Dropping unnecessary columns and coverting message type to string.
    data.drop('Unnamed: 0', inplace=True, axis=1)
    data['message'] = data['message'].astype('str')

    # Converting 'timestamp to datetime objects'
    data["timestamp"] = pd.to_datetime(data["timestamp"], format="%d/%m/%Y, %I:%M:%S %p")

    # new column weekday
    data['weekday'] = data['timestamp'].apply(lambda x: x.day_name())

    # new column month_sent
    data['month_sent'] = data['timestamp'].apply(lambda x: x.month_name())

    # column date
    data['date'] = [d.date() for d in data['timestamp']]

    # column hour
    data['hour'] = [d.time().hour for d in data['timestamp']]

    data.to_csv(str(csv_file).replace('_extracted.csv', '') + "_extracted.csv")

    return data


def run_parser(chatlog):
    """
    Runs the parser and returns the enhanced DataFrame.
    :param chatlog:
    :return:
    """
    parse_actual_file(chatlog)

    csv_name = str(chatlog).replace('.txt', '') + "_extracted.csv"

    data = enhance_data(csv_name)

    return data


if __name__ == "__main__":

    # Example usage of code
    # Parse the path of the text file through the function
    # df = parse_actual_file('it_chat.txt')

    # Make better csv
    # enhance_data('')


    pass


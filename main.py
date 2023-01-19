#!/usr/bin/env python3
"""
Script to select telegram chat history dump in json format
Dump consists of chat's information (name, members, etc).
chat["messages"] is usually the biggest value there.
It is a list of all messages sent (except the ones which were deleted)
Every message is a dictionary, too.
Example message:
{'date': '2029-06-33T05:33:11',
 'date_unixtime': '1455555555',
 'from': 'nickname',
 'from_id': 'user52107256321243124',
 'id': 12442586,
 'reply_to_message_id': 1000000,
 'text': 'hi',
 'text_entities': [{'text': 'hi',
                    'type': 'plain'}],
 'type': 'message'}
(all id's are broken there, all time mentioned is wrong dut to security reasons)
It's convenient to use `pprint` module while parsing the data
mb6ockatf, Fri 20 Jan 2023 12:27:28 AM MSK
"""

import json
from argparse import ArgumentParser
from pprint import pprint


def print_data(message: dict):
    pprint("date " + message["date"])
    try:
        pprint("from " + message["from"])
        pprint("from_id " + message["from_id"])
    except KeyError:
        pass
    pprint("text ")
    pprint(message["text"])
    print("*" * 10)


if __name__ == "__main__":
    prog = "tgHistoryObserver"
    desc = "Select data from Telegram chat history dump"
    parser = ArgumentParser(prog, desc)
    parser.add_argument("filename", type=str)
    parser.add_argument("-u", "--from-user", action="append", type=str)
    args = parser.parse_args()
    with open(args.filename, "r") as file:
        contents = file.read()
    stock = json.loads(contents)["messages"]
    for element in stock:
        try:
            if element["from_id"] in args.from_user:
                print_data(element)
        except KeyError:
            pprint(element)


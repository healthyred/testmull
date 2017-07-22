##This function's purpose is to match the EXT_ids of each card to the image URLS

import json
import sys


def matchingIDtourl(file, name):
    """
    function that takes in a json file of hearthstone cards and a name, and then
    outputs a dictionary with the format dbfId: name
    """
    with open(file, encoding = "utf-8") as fin:
        cardlist = json.loads(fin.read())
    cards = {}
    for card in cardlist:
        cards[card["id"]] = card["url"]
    json_file = json.dumps(cards)
    f = open(name, "w")
    f.write(json_file)
    f.close()

if __name__ == "__main__":
    file = sys.argv[1]
    name = sys.argv[2]
    matchingIDtourl(file,name)
    

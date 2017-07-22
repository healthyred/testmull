## Combines all the ID to name dictionaries into a final dictionary
import json

final = {}
with open("matchedlistone.json", "r") as fin1:
    a = json.load(fin1)
    final.update(a)
with open("matchedlisttwo.json", "r") as fin2:
    b = json.load(fin2)
    final.update(b)
with open("matchedlistthree.json", "r") as fin3:
    c = json.load(fin3)
    final.update(c)
with open("matchedlistfour.json", "r") as fin4:
    d = json.load(fin4)
    final.update(d)
    json_file = json.dumps(final)
    f = open("finalmatched.json","w")
    f.write(json_file)
    f.close

    

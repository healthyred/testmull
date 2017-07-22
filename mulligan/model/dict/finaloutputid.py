## Combines all the dbfID to ID dictionaries into a final dictionary
import json

final = {}
with open("matchedlistoneid.json", "r") as fin1:
    a = json.load(fin1)
    final.update(a)
with open("matchedlisttwoid.json", "r") as fin2:
    b = json.load(fin2)
    final.update(b)
with open("matchedlistthreeid.json", "r") as fin3:
    c = json.load(fin3)
    final.update(c)
with open("matchedlistfourid.json", "r") as fin4:
    d = json.load(fin4)
    final.update(d)
    json_file = json.dumps(final)
    f = open("finalmatchedid.json","w")
    f.write(json_file)
    f.close

    

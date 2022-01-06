import json
import os

#
p = "output/json"
index = {}
for filename in os.listdir(p):
    with open(os.path.join(p, filename), "r") as read_file:
        jmib = json.load(read_file)
        for i in jmib.items():
            data = i[1]
            if "class" in data and data["class"] == "moduleidentity":
                index[data["oid"]] = filename.replace(".json", "")
                break

with open("output/index.csv", "w") as f:
    for i in index.items():

        f.write(f"{i[0]},{i[1]}\n")

import json
import os

#
p = "output/json"
index = {}
for filename in os.listdir(p):
    mapped = False
    with open(os.path.join(p, filename), "r") as read_file:
        jmib = json.load(read_file)
        for i in jmib.items():
            data = i[1]
            if "class" in data:
                classname = data["class"]
                if classname in ["moduleidentity", "objectidentity"]:
                    # print(f"{classname} {data['oid']}")
                    if data and (
                        data["class"] == "moduleidentity"
                        or data["class"] == "objectidentity"
                    ):
                        mapped = True
                        index[data["oid"]] = filename.replace(".json", "")
        if not mapped and "-TC" not in filename:
            print(f"Unable to index {p}/{filename}")

with open("output/index.csv", "w") as f:
    for i in index.items():

        f.write(f"{i[1]},{i[0]}\n")

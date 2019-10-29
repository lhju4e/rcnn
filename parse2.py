import json
import xmltodict
import os
path = "./anno"
file_list = os.listdir(path)
file_list_json = [file for file in file_list if file.endswith(".json")]
file_list_json = [file for file in file_list_json if "_" in file]
print(file_list_json)

for file in file_list_json:
    with open("./anno/"+file) as f:
        lines = f.readlines()
        if file != file_list_json[-1]:
            lines = lines[:-2]
            lines += "  }\n}"

        newfile = file.split("_")[1]
        print(newfile)
        with open(newfile, "w") as fw:
            fw.writelines(lines)



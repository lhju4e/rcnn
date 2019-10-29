import json
import xmltodict
import os

path = "../"
file_list = os.listdir(path)
file_list_json = [file for file in file_list if file.endswith(".json")]
file_list_json = [file for file in file_list_json if "_" not in file]
print(file_list_json)

for file in file_list_json:
    with open(file) as f:
        #print(lines)
        jsonString = f.read()
        #f.writelines(lines)
# print('JSON input (json_to_xml.json):')
        #print(jsonString)
        try:
            xmlString = xmltodict.unparse(json.loads(jsonString), pretty=True)
            file_xml = file.split(".json")[0]
            file_xml += ".xml"
            with open(file_xml, 'w') as fw:
                fw.write(xmlString)
        except:
            print("*****can't convert : " + file)
# #xmlString = dicttoxml.dicttoxml(jsonString)
# #print('\nXML output(json_to_xml.xml):')
# #print(xmlString)
#
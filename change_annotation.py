import xml.etree.ElementTree as elemTree
import os

def change_label(filename):
    print(filename)
    doc = elemTree.parse(filename)
    root = doc.getroot()

    object = root.find('object') #label찾음
    if(object == None):
        print("cannot find <object>")
    else:
        label = object.find('name')
        if(label == None):
            print("cannot find <name>")
        else:
            if(int(label.text) < 50):
                label.text = str(int(label.text) + 50)#label에 50 더해줌
                doc.write(filename, encoding="utf-8", xml_declaration=False)

def protoparse(filename, search):
    f = open(filename)
    lines = f.readlines()
    cnt = 0
    for line in lines:
        cnt+=1
        if "\"" + search + "\"" in line:
            output = lines[cnt]
            output = output.replace("label: ", "")
            break;
    f.close()
    return int(output)


if __name__ == '__main__':
    import argparse

    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description='dir path')
    parser.add_argument("--dir",
                        help="'ex) python tml_to_txt.py --dir=test'")
    args = parser.parse_args()
    file_list = os.listdir(args.dir)
    file_xml = [file for file in file_list if file.endswith("xml")]
    for file in file_xml:
        change_label(args.dir+"/"+file)
        print(args.dir+"/"+file)

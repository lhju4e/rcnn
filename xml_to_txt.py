import xml.etree.ElementTree as elemTree
import os

def parse(filename):
    tree = elemTree.parse(filename)
    filename = tree.find('.filename')
    filename = filename.text.replace(".jpg", ".txt")
    resultdir = os.path.join(os.getcwd(), "result/")
    f = open(resultdir + filename,  mode='wt', encoding='utf-8')

    for objects in tree.findall('.object'):
        name = objects.find('name')

        try :
            name = int(name.text)
        except :
            name = protoparse("labelmap_recognizer.prototxt", name.text)

        # Sean : To change name '0' to str '10'
        if name == 0:
            name = 10
        box = objects.find('bndbox')
        xmin = box.find('xmin')
        ymin = box.find('ymin')
        xmax = box.find('xmax')
        ymax = box.find('ymax')


        f.write(str(name) + " ")
        f.write(xmin.text + " ")
        f.write(ymin.text + " ")
        f.write(xmax.text + " ")
        f.write(ymax.text +"\n")
    f.flush()
    f.close()

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
    os.mkdir("result")
    file_list = os.listdir(args.dir)
    file_xml = [file for file in file_list if file.endswith("xml")]
    for file in file_xml:
        parse(args.dir+"/"+file)


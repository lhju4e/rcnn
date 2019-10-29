import cv2
import os
f = open("/home/qisens/Desktop/juhee/10-28/car-damage-detector/dataset/all_val.json", "r+t")
fw = open("/home/qisens/Desktop/juhee/10-28/car-damage-detector/dataset/anno/tmp.json", "w")
print(os.getcwd())
while True:
    line = f.readline()

    if not line:
        break

#jpeg일때도 똑같이 처리해줘야하
    #jpg와 jpeg나눠서 처

    if "filename" in line:
        filename = line.split(":")[1].lstrip(" ")
        filename = filename.split("\"")[1]
        if "jpg" in filename:
            filename = filename.split(".jpg")[0]
            mode=1
        elif "jpeg" in filename:
            filename = filename.split(".jpeg")[0]
            mode=0
        elif "JPEG" in filename:
            filename = filename.split(".JPEG")[0]
            mode = 2
        elif "png" in filename:
            filename = filename.split(".png")[0]
            mode = 3
        print(filename)
        fw = open("./anno/_" + filename + ".json", "w")
        fw.write("{\n  \"annotation\" : {\n")
        fw.write(line)
        if mode == 1:
            fw.write("    \"path\" : \"" + os.getcwd() + "/val/" + filename + ".jpg\",\n")
        elif mode == 0:
            fw.write("    \"path\" : \"" + os.getcwd() + "/val/" + filename + ".jpeg\",\n")
        elif mode == 2:
            fw.write("    \"path\" : \"" + os.getcwd() + "/val/" + filename + ".JPEG\",\n")
        else:
            fw.write("    \"path\" : \"" + os.getcwd() + "/val/" + filename + ".png\",\n")
    elif "size" in line:
        line = line.split(":")[0]
        line += ": {\n"
        try:
            fw.write(line)
        except:
            print("*******\n ******error : ", filename)
        if mode == 1:
            im = cv2.imread("./val/" + filename + ".jpg")
        elif mode == 0:
            im = cv2.imread("./val/" + filename + ".jpeg")
        elif mode == 2:
            im = cv2.imread("./val/" + filename + ".JPEG")
        else:
            im = cv2.imread("./val/" + filename + ".png")
        fw.write("      \"width\" : " + str(im.shape[1]) + ",\n")
        fw.write("      \"height\" : " + str(im.shape[0])+",\n")
        fw.write("      \"depth\" : 3\n\t\t},\n")

    elif(line.find("polygon") != -1):
        line = line.replace("polygon", "rect")
    elif "shape_attributes" in line:
        line = line.replace("shape_attributes", "bndbox")
        fw.write(line)
    elif "regions" in line:
        line = line.replace("regions", "object")
        fw.write(line)
    elif "image_quality" in line:
        f.readline()
        f.readline()
        f.readline()
        f.readline()
        f.readline()
    elif "region_attributes" in line:
        line = f.readline()
        if "dent" in line:
            line = line.replace("\"dent\"", str(101))
            if "," in line:
                line = line.replace(",", "")
            fw.write(line)
            line = f.readline()
        if "scratch" in line:
            line = line.replace("\"scratch\"", str(102))
            if "," in line:
                line = line.replace(",", "")
            fw.write(line)
            line = f.readline()
    elif "all_points_x" in line :
        x_line = line.replace("all_points_x\": [", "xmin\": ")
        x_line = x_line.strip("\n")
        xli_line=[]
        while True:
            n_line = f.readline()
            if "]" in n_line:
                break
            n_line = n_line.replace(",", "")
            # print("nline : ", n_line)
            xli_line.append(int(n_line))

        x_line += str(min(xli_line))
        x_line += ",\n"
        fw.write(x_line)
#======== y
        line = f.readline()
        y_line = line.replace("all_points_y\": [", "ymin\": ")
        y_line = y_line.strip("\n")
        yli_line = []

        while True:
            n_line = f.readline()
            if "]" in n_line:
                break
            n_line = n_line.replace(",", "")
            yli_line.append(int(n_line))

        y_line += str(min(yli_line))
        y_line += ",\n"
        fw.write(y_line)
        fw.write("          \"xmax\" : " + str(max(xli_line)) + ",\n")
        fw.write("          \"ymax\" : " + str(max(yli_line)) + "\n")
        # fw.write("\"width\": " + str(max(xli_line) - min(xli_line)) + ",\n")
        # fw.write("\"height\": " + str(max(yli_line) - min(yli_line)) + "\n")

        #line = line.strip()
        #fw.write(line)
    else:
        fw.write(line)

f = open("/home/qisens/Desktop/juhee/10-28/car-damage-detector/dataset/val/all_val.json", "r+t")
fw = open("./make.json", "w")
while True:
    line = f.readline()

    if not line:
        break

    if(line.find("polygon") != -1):
        line = line.replace("polygon", "rect")
    if "all_points_x" in line :
        x_line = line.replace("all_points_x\": [", "x\": ")
        x_line = x_line.strip("\n")
        xli_line=[]
        while True:
            n_line = f.readline()
            if "]" in n_line:
                break
            n_line = n_line.replace(",", "")
            print("nline : ", n_line)
            xli_line.append(int(n_line))

        x_line += str(min(xli_line))
        x_line += ",\n"
        fw.write(x_line)
#======== y 
        line = f.readline()
        y_line = line.replace("all_points_y\": [", "y\": ")
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

        fw.write("\"width\": " + str(max(xli_line) - min(xli_line)) + ",\n")
        fw.write("\"height\": " + str(max(yli_line) - min(yli_line)) + "\n")

        #line = line.strip()
        #fw.write(line)
    else:
        print(line)
        fw.write(line)

f.close()
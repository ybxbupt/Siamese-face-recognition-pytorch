

#read txt method two
f = open("./label_train.txt", "r")
fw = open("./label_train_list.txt", "w")
label_list = []
index = 0
for line in f:
    line = line.strip('\n')
    line_subs = line.split("_")
    for i in range(0, len(line_subs)):
        sub = line_subs[i]
        if sub.isdigit():
            if sub in label_list:
                label_id = label_list.index(sub)
            else:
                label_id = len(label_list)
                label_list.append(sub)
            # index = int(line_subs[i])
            fw.write("%s,%d\n" % (line,label_id))
            break
    # name_list.append(line)
    print(line)

f.close()
fw.close()



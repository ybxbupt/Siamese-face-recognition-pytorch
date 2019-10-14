
import numpy as np
import random
from pathlib import Path
from collections import defaultdict
def create_label_dict(path):
    label_dict = defaultdict(list)
    names_list = Path(path).read_text().strip().split('\n')
    for f_name in names_list:
        f_s = f_name.split(',')
        label_dict[int(f_s[1])].append(f_s[0])
    return label_dict
def create_pairs_ddfa():
    label_dict = create_label_dict("./label_train_list.txt")
    fw = open("./testpair_list.txt", "w")
    for i in range(0,1000):
        label_1 = random.choice(range(len(label_dict)))
        img1_name = random.choice(label_dict[label_1])
        is_same = np.random.choice([0, 1], p=[0.5, 0.5])
        if is_same:
            pair_label = 1
            img2_name = random.choice(label_dict[label_1])
        else:
            pair_label = 0
            while True:
                label_2 = random.choice(range(len(label_dict)))
                if label_2 != label_1:
                    break
            img2_name = random.choice(label_dict[label_2])
        fw.write("%s,%s,%d\n" % (img1_name, img2_name,pair_label))
    fw.close()
if __name__ == "__main__":
    create_pairs_ddfa()


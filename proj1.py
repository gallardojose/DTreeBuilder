import random
import math

# Each tree node consists of:
#   1. a vector list => [([feature vector], class)..]
#   2. the selected attribute to split the vector list
#   3. left child
#   4. right child
class node:
    def __init__(self):
        self.vecs = list()
        self.attr_split = ""
        self.left = None
        self.right = None


# function to read data file
# parameter: data file name or path to data file
# return: list of featre vectors and its corresponding class pair => [([feature_vector], class)..]
def read_file(filename):
    fea_vecs = []
    file = open(filename, "r")
    for line in file:
        values = line.split(",")
        fea_vecs.append((values[:6], values[6].replace("\n", "")))
    return fea_vecs


feature_vecs = []
feature_vecs = read_file("550-p1-cset-krk-1.csv")

Training_Set = []
Holdout_Set= []
Validation_Set = []


def sets_generator():
    total_data = len(feature_vecs)
    data_indexes = list(range(total_data))

    total_training_set_data = int(total_data * (.60));
    remaining_data = total_data - total_training_set_data

    if remaining_data % 2 == 1:
        total_training_set_data += 1
        remaining_data - 1

    Training_indexes = random.sample(data_indexes, total_training_set_data)

    for element in Training_indexes:
        Training_Set.append(feature_vecs[element])
        data_indexes.remove(element)


    Holdout_indexes = random.sample(data_indexes, int(remaining_data/2))

    for element in Holdout_indexes:
        Holdout_Set.append(feature_vecs[element])
        data_indexes.remove(element);


    Validation_indexes = list(data_indexes);

    for element in Validation_indexes:
        Validation_Set.append(feature_vecs[element])
        data_indexes.remove(element)


def entropy(class_occurrence, total):
    node_entropy = 0
    for minwindepth in class_occurrence:
        class_probability = class_occurrence[minwindepth] / total
        node_entropy += -class_probability*math.log(class_probability,2)
    return node_entropy

co = {
    0: 2,
    1: 3,
    5: 3
}
t = 8
print(entropy(co,t))


# Formula to find information gain
def FindInfoGain(entropy_set,entropy_attr,probab):
    return entropy_set-sum([entropy_attr[i]*probab[i] for i in range(len(entropy_attr))])


# Select best attribut to split a node
# Take as input a tree node
# When finish, tree node's property is modified accordingly
def attribute_to_split(root):
    # Calculate root entropy
    class_occurrence = dict()
    for pair in root.vecs:
        if pair[1] in class_occurrence:
            class_occurrence[pair[1]] += 1
        else:
            class_occurrence[pair[1]] = 1
    total = len(root.vecs)
    root_ent = entropy(class_occurrence, total)
    print(root_ent)
    # ...

root = node()
root.vecs = [([""], "pos"),([""], "pos"),([""], "neg"),([""], "neg"),([""], "pos"),([""], "neg"),([""], "pos"),([""], "pos"),]
attribute_to_split(root)

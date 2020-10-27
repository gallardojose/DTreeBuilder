import random
import math

# Each tree node consists of:
#   1. a vector list => [([feature vector], class), ..]
#   2. the selected attribute to split the vector list
#   3. its children => {selected attribute value : node, ..}
class node:
    def __init__(self):
        self.vecs = list()
        self.attr_split = None
        self.children = dict()


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
attributes = ["White King file", " White King rank", "White Rook file", "White Rook rank", "Black King file", "Black King rank"]
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
def attribute_to_split(root, attrs):
    # Calculate root entropy
    class_occurrence = dict()
    for pair in root.vecs:
        if pair[1] in class_occurrence:
            class_occurrence[pair[1]] += 1
        else:
            class_occurrence[pair[1]] = 1
    total = len(root.vecs)
    root_ent = entropy(class_occurrence, total)
    print("root entropy:", root_ent)

    # Calculate average entropy for each attribute value
    info_gain = list()
    for i in range(len(root.vecs[0][0])):
        class_occurence = dict()
        total = dict()
        for pair in root.vecs:
            if pair[0][i] not in class_occurence:
                class_occurence[pair[0][i]] = dict()
                total[pair[0][i]] = 1
            else:
                total[pair[0][i]] += 1
            if pair[1] in class_occurence[pair[0][i]]:
                class_occurence[pair[0][i]][pair[1]] += 1
            else:
                class_occurence[pair[0][i]][pair[1]] = 1
        entropy_list = list()
        for attr_val in class_occurence:
            entropy_list.append((total[attr_val], entropy(class_occurence[attr_val], total[attr_val])))
        avg_ent = 0
        for ent in entropy_list:
            avg_ent += ent[0] / len(root.vecs) * ent[1]
        info_gain.append(avg_ent)
        print("Attribute " + attrs[i] + "'s average entropy:", avg_ent)

    # Calculate information gain for each attribute
    max_info = (0, 0)
    for i in range(len(info_gain)):
        info_gain[i] = root_ent - info_gain[i]
        if info_gain[i] > max_info[1]:
            max_info = (i, info_gain[i])
        print("Attribute " + attrs[i] + "'s information gain:", info_gain[i])
    print("Attribute " + attrs[max_info[0]] + " has the greatest information gain, so it is selected as the attribute to split")

    # Updatte root node properties
    root.attr_split = max_info[0]
    for pair in root.vecs:
        if pair[0][root.attr_split] not in root.children:
            root.children[pair[0][root.attr_split]] = node()
        root.children[pair[0][root.attr_split]].vecs.append(pair)

attributes = ["crust size", "shape", "filling size"]
root = node()
root.vecs = [(["big", "circle", "small"], "pos"),(["small", "circle", "small"], "pos"),(["big", "square", "small"], "neg"),(["big", "triangle", "small"], "neg"),(["big", "square", "big"], "pos"),(["small", "square", "small"], "neg"),(["small", "square", "big"], "pos"),(["big", "circle", "big"], "pos")]
print("\n\nTest Data:\n", root.vecs, "\n\nAttributes:\n", attributes, "\n")
attribute_to_split(root, attributes)
print("\nAfter splitting:")
for child in root.children:
    print("Attribute " + child + " has vector list:\n", root.children[child].vecs, "\n")
# function to read data file
# parameter: data file name or path to data file
# return: list of featre vectors and the corresponding list of classes
def read_file(filename):
    fea_vecs = []
    cls = []
    file = open(filename, "r")
    for line in file:
        values = line.split(",")
        fea_vecs.append(values[:6])
        cls.append(values[6].replace("\n", ""))
    return fea_vecs, cls
        

feature_vecs = []
classes = []
feature_vecs, classes = read_file("550-p1-cset-krk-1.csv")
print(feature_vecs)
print(classes)


# Hard coding Jonny Likes data
# [Shape, Crust Size, Crust Shade, Filling Size, Filling Shade]
feature_vecs = [["Circle", "Thick", "Gray", "Thick", "Dark"], #ex1
                ["Circle", "Thick", "White", "Thick", "Dark"], #ex2
                ["Triangle", "Thick", "White", "Thick", "Gray"], #ex3
                ["Circle", "Thin", "White", "Thin", "Dark"], #ex4
                ["Square", "Thick", "Dark", "Thin", "White"], #ex5
                ["Circle", "Thick", "White", "Thin", "Dark"], #ex6
                ["Circle", "Thick", "Gray", "Thick", "White"], #ex7
                ["Square", "Thick", "White", "Thick", "Gray"], #ex8
                ["Triangle", "Thin", "Gray", "Thin", "Dark"], #ex9
                ["Circle", "Thick", "Dark", "Thin", "White"], #ex10
                ["Square", "Thick", "White", "Thick", "Dark"], #ex11
                ["Triangle", "Thick", "White", "Thick", "Gray"]] #ex12
classes = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0] # 1==pos; 0==neg

print(feature_vecs)
print(classes)


import math

class_occurrence = {
    0: 2,
    1: 3,
    5: 3
}
total = 8


def entropy():
    node_entropy = 0
    for minwindepth in class_occurrence:
        class_probability = class_occurrence[minwindepth] / total
        node_entropy += -class_probability*math.log(class_probability)
    return node_entropy


print(entropy())

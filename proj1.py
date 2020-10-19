import random
import math

Training_Set = []
Holdout_Set= []
Validation_Set = []

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

class_occurrence = {
    0: 2,
    1: 3,
    5: 3
}
total = 8


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


def entropy():
    node_entropy = 0
    for minwindepth in class_occurrence:
        class_probability = class_occurrence[minwindepth] / total
        node_entropy += -class_probability*math.log(class_probability)
    return node_entropy


print(entropy())
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#########################################
# kNN: k Nearest Neighbors

# Input:      inX: vector to compare to existing dataset (1xN)
#             dataSet: size m data set of known vectors (NxM)
#             labels: data set labels (1xM vector)
#             k: number of neighbors to use for comparison

# Output:     the most popular class label
# Author: li yu
#########################################

from numpy import *
import operator
import os


# classify using kNN
def knn_classify(predict_input, data_set, labels, k):
    num_samples = data_set.shape[0]  # shape[0] stands for the num of row

    # step 1: calculate Euclidean distance
    # tile(A, reps): Construct an array by repeating A reps times
    # the following copy num_samples rows for dataSet
    diff = tile(predict_input, (num_samples, 1)) - data_set  # Subtract element-wise
    squared_diff = diff ** 2  # squared for the subtract
    squared_dist = sum(squared_diff, axis=1)  # sum is performed by row
    distance = squared_dist ** 0.5

    # step 2: sort the distance
    # argsort() returns the indices that would sort an array in a ascending order
    sorted_dist_indices = argsort(distance)

    class_count = {}  # define a dictionary (can be append element)
    for i in xrange(k):
        # step 3: choose the min k distance
        vote_label = labels[sorted_dist_indices[i]]

        # step 4: count the times labels occur
        # when the key voteLabel is not in dictionary class_count, get()
        #  will return 0
        class_count[vote_label] = class_count.get(vote_label, 0) + 1

    # step 5: the max voted class will return
    max_count = 0
    max_index = " "
    for key, value in class_count.items():
        if value > max_count:
            max_count = value
            max_index = key
    return max_index


# convert image matrix to vector
def img2vector(filename):
    rows = 32
    cols = 32
    img_vector = zeros((1, rows * cols))
    file_in = open(filename)
    for row in xrange(rows):
        line_str = file_in.readline()
        for col in xrange(cols):
            img_vector[0, row * 32 + col] = int(line_str[col])
    return img_vector


# load dataSet
def load_data_set(data_set_dir):
    # step 1: Getting training set
    print "---Getting training set..."
    # data_set_dir = '/Users/li/Downloads/digits/'   # 手写识别的训练集
    training_file_list = os.listdir(data_set_dir + 'trainingDigits')  # load the training data set
    num_train_samples = len(training_file_list)
    print "   Num of training data set: %d " % num_train_samples
    train_x = zeros((num_train_samples, 1024))
    train_y = []
    for i in xrange(num_train_samples):
        filename = training_file_list[i]
        if filename.endswith(".txt"):
            # get train_x
            train_x[i, :] = img2vector(data_set_dir + 'trainingDigits/%s' % filename)

            # get label from file name such as "1_18.txt"
            label = int(filename.split('_')[0])  # return 1
            train_y.append(label)

    # step 2: Getting testing set
    print "---Getting testing set..."
    testing_file_list = os.listdir(data_set_dir + 'testDigit')  # load the predict data set
    num_test_samples = len(testing_file_list)
    print "   Num of predict data set: %d " % num_test_samples
    test_x = zeros((num_test_samples, 1024))
    test_y = []
    for i in xrange(num_test_samples):
        filename = testing_file_list[i]
        if filename.endswith(".txt"):
            # get train_x
            test_x[i, :] = img2vector(data_set_dir + 'testDigit/%s' % filename)

            # get label from file name such as "1_18.txt"
            label = int(filename.split('_')[0])  # return 1
            test_y.append(label)

    return train_x, train_y, test_x, test_y


# match label with letter
def match(label):
    if label == 0:
        return "3"
    elif label == 1:
        return "4"
    elif label == 2:
        return "5"
    elif label == 3:
        return "6"
    elif label == 4:
        return "7"
    elif label == 5:
        return "8"
    elif label == 6:
        return "a"
    elif label == 7 or label == 27:
        return "a"
    elif label == 8 or label == 28:
        return "b"
    elif label == 9:
        return "c"
    elif label == 10 or label == 29:
        return "d"
    elif label == 11 or label == 30:
        return "e"
    elif label == 12 or label == 31:
        return "f"
    elif label == 13 or label == 33:
        return "h"
    elif label == 14 or label == 35:
        return "j"
    elif label == 15:
        return "k"
    elif label == 16:
        return "m"
    elif label == 17 or label == 37:
        return "n"
    elif label == 18:
        return "p"
    elif label == 19 or label == 38:
        return "q"
    elif label == 20 or label == 39:
        return "r"
    elif label == 21:
        return "s"
    elif label == 22:
        return "u"
    elif label == 23:
        return "v"
    elif label == 24:
        return "w"
    elif label == 25:
        return "x"
    elif label == 26 or label == 42:
        return "y"
    elif label == 32:
        return "g"
    elif label == 36:
        return "l"
    else:
        return "t"


# test captcha class
def captcha_test(data_set_dir):
    # #step 1: load data
    print "Step 1: load data..."
    # data_set_dir = '/Users/li/Desktop/Captcha/recognition/recogtest/'
    train_x, train_y, test_x, test_y = load_data_set(data_set_dir)

    # #step 2: training...
    print "Step 2: training..."
    pass

    # #step 3: testing
    print "Step 3: Testing..."
    num_test_samples = test_x.shape[0]
    print "        Num of predict data set: %d " % num_test_samples
    match_count = 0
    res = []
    for i in xrange(num_test_samples):
        predict = knn_classify(test_x[i], train_x, train_y, 3)
        res.append(predict)
        # print predict, test_y[i]  # print test data set and predict data set
        # print predict  # print predict data set
        if predict == test_y[i]:
            match_count += 1
    accuracy = float(match_count) / num_test_samples
    # #step 4: show the result
    print "Step 4: Show the result..."
    # print '        The classify accuracy is: %.2f%%' % (accuracy * 100)
    return res


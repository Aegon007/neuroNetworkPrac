#encoding=utf-8

import os
import sys
import argparse

import numpy as np
import pandas as pd


def sigmoid(x):
    # activation function is: f(x) = 1 / (1 + e^(-x))
    return 1 / (1 + np.exp(-x))

def mse_loss(y_true, y_pred):
    # need to be np array
    return ((y_true - y_pred) ** 2).mean()

class Neuron():
    def __init__(self, weights, bias=0):
        self.weights = weights
        self.bias = bias

    def feedforward(self, inputs):
        total = np.dot(self.weights, inputs) + self.bias
        return sigmoid(total)

def main(opts):
    print('welcome to main function!')

def parseOpts(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='')
    opts = parser.parse_args()
    return opts

if __name__ == "__main__":
    opts = parseOpts(sys.argv)
    main(opts)

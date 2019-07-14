#encoding=utf-8

import os
import sys
import argparse

import numpy as np
import pandas as pd


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

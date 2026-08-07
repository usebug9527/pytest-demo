import argparse
import sys

import pytest


def parse_arguments():
    parser = argparse.ArgumentParser()
    print(parser.parse_args())


if __name__ == '__main__':
    args = sys.argv
    parse_arguments()
    # print(args)
    # pytest.main(['-vs',r'..\test_case\test_demo.py'])
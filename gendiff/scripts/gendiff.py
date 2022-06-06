#!/usr/bin/python3
import argparse

from gendiff import generate_diff


def return_diff():
    args = parse_cli_arguments()
    print(generate_diff(args.first_file, args.second_file))


def parse_cli_arguments():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
    )
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    return_diff()

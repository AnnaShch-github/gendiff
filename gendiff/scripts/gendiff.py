#!/usr/bin/python3
from gendiff import generate_diff
from gendiff.parsing import parse_cli_arguments


def return_diff():
    # The main function of the package
    args = parse_cli_arguments()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    return_diff()

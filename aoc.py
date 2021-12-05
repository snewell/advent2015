import sys


def load(run_fn):
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as input:
            print(run_fn(input))
    else:
        print(run_fn(sys.stdin))

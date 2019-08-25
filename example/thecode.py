
import argparse
import os
import sys


def main(argv=None):
    print("main()")
    if argv is None:
        argv = sys.argv
    print("argv:", argv)
    
    prog = None
    if os.path.basename(sys.argv[0]) == "__main__.py":
        prog = f"{sys.executable} -m {__package__}"

    prs = argparse.ArgumentParser(prog=prog)
    prs.parse_args(argv[1:])
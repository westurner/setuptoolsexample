
import sys

from .thecode import main

def othermain():
    print("othermain")
    return main(sys.argv)

if __name__ == "__main__":
    othermain()

### publish new version of this library to PyPI

from shutil import copyfile
import fileinput
import sys
import os
import argparse

parser = argparse.ArgumentParser(description="Publish the Targomo python library to PyPi")
parser.add_argument("--version", required=True, type=str, help="The version number", nargs="?")
args = parser.parse_args()

copyfile("./setup.py.default", "./setup.py")

for line in fileinput.input("./setup.py", inplace=True):
    line = line.replace("$VERSION", args.version)
    sys.stdout.write(line),

os.system("python3 setup.py sdist")
os.system("twine upload --repository pypitest dist/*")
os.system("twine upload --repository pypi dist/*")

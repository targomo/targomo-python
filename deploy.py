### publish new version of this library to PyPI

import git
from shutil import copyfile
import fileinput
import sys
import os

yesOrNo = input('Have you commited all changes? Yes (Y) or no (n)?')

if "Y" == yesOrNo:
    copyfile("./setup.py.default", "./setup.py")

    repo    = git.Repo(".")
    lasttag = sorted(repo.tags, key=lambda t: t.commit.committed_date)[-1]
    nexttag = "0." + str(int(str(lasttag).replace("0.", "")) + 1)

    for line in fileinput.input("./setup.py", inplace=True):
        line = line.replace("$VERSION", str(nexttag))
        sys.stdout.write(line),

    new_tag = repo.create_tag(str(nexttag), message='Automatic deployment of new version "{0}"'.format(nexttag))
    repo.remotes.origin.push(new_tag)

    os.system("python3 setup.py sdist")
    os.system("twine upload --repository pypitest dist/*")
    os.system("twine upload --repository pypi dist/*")

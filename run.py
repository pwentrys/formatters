from scripts import pepper, tabber
import sys


if __name__ == '__main__':
    # Project path.
    path = sys.path[0]

    # Runs
    tabber.run(path)
    pepper.run(path)

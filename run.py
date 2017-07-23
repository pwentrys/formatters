from scripts import Scripts
import sys
from pathlib import Path


if __name__ == '__main__':
    # Project path.
    path = sys.path[0]
    Scripts.run(str(Path(path).parent))

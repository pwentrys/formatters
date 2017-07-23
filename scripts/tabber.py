from config.blacklist import allowed
import tabnanny
from pathlib import Path


class Tabber:
    @staticmethod
    def run(string: str):
        """
        Run tabnanny if path exists.
        :param string:
        :return:
        """
        if allowed(string):
            path = Path(string)
            if path.exists():
                tabnanny.check(path)

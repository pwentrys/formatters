from .pep8 import Pep8 as pepper
from .tabber import Tabber as tabber


class Scripts:
    @staticmethod
    def run(string: str):
        """
        Format path
        :param string:
        :return:
        """
        pepper.run(string)
        tabber.run(string)

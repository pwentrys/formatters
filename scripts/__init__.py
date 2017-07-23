from .pep8 import Pep8 as pepper


class Scripts:
    @staticmethod
    def run(string: str):
        """
        Format path
        :param string:
        :return:
        """
        return pepper.gather_paths(string, [])

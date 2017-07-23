from autopep8 import fix_code
from os.path import splitext
from pathlib import Path


class Pep8:
    ENCODING = 'utf-8'
    OPTIONS = {
        'pep8_passes': 10,
        'experimental': True,
        'aggressive': 8
    }

    @staticmethod
    def _on_file(path):
        """
        Run pep8 on file.
        :param path:
        :return:
        """
        raw = path.read_text(encoding=Pep8.ENCODING)
        formatted = fix_code(
            raw,
            options=Pep8.OPTIONS,
            encoding=Pep8.ENCODING
        )
        if raw != formatted:
            path.write_text(
                formatted,
                encoding=Pep8.ENCODING
            )

    @staticmethod
    def _on_dir(path):
        """
        Iter each path in dir.
        :param path:
        :return:
        """
        for file in path.iterdir():
            Pep8.run(str(file))

    @staticmethod
    def run(string: str):
        """
        Runs autopep8 on path.
        :param string:
        :return:
        """
        path = Path(string)
        if path.is_file():
            if splitext(string)[1] == '.csv':
                Pep8._on_file(path)
        elif path.is_dir():
            Pep8._on_dir(path)
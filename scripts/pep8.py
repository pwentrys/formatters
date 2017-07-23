from config.blacklist import allowed
from autopep8 import fix_code
from os.path import basename, splitext
from pathlib import Path
import asyncio


class Pep8:
    ENCODING = 'utf-8'
    OPTIONS = {
        'pep8_passes': 10,
        'experimental': True,
        'aggressive': 8
    }

    @staticmethod
    async def _on_file_async(path):
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
        await asyncio.sleep(0.0000000000000000001)

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
        if allowed(basename(path)):
            for file in path.iterdir():
                Pep8.run(str(file))

    @staticmethod
    def _on_dir_for_async(path, paths):
        """
        Iter each path in dir.
        :param path:
        :return:
        """
        if allowed(basename(path)):
            for file in path.iterdir():
                paths = Pep8.gather_paths(str(file), paths)
        return paths

    @staticmethod
    def gather_paths(string: str, paths: list) -> list:
        """
        Gather paths for async loop run.
        :param paths:
        :param string:
        :return:
        """
        if allowed(string):
            path = Path(string)
            if path.is_file() and splitext(string)[1] == '.py':
                paths.append(path)
                # Pep8._on_file(path)
            elif path.is_dir():
                paths = Pep8._on_dir_for_async(path, paths)
        return paths

    @staticmethod
    def run(string: str):
        """
        Runs autopep8 on path.
        :param string:
        :return:
        """
        if allowed(string):
            path = Path(string)
            if path.is_file() and splitext(string)[1] == '.py':
                Pep8._on_file(path)
            elif path.is_dir():
                Pep8._on_dir(path)

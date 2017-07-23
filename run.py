import time
import asyncio

from scripts import Scripts
from scripts.pep8 import Pep8
import sys
from pathlib import Path


def get_loop():
    if sys.platform == "win32":
        loop = asyncio.ProactorEventLoop()
        asyncio.set_event_loop(loop)
        return loop
    else:
        return asyncio.get_event_loop()

if __name__ == '__main__':
    # Project path.
    path = sys.path[0]
    start_time = time.time()
    paths = Scripts.run(str(Path(path).parent))
    gathering_time = time.time()

    loop = get_loop()
    loop.run_until_complete(asyncio.gather(*[Pep8._on_file_async(file) for file in paths]))
    loop.close()
    end_time = time.time()
    print(f'Total Files: {len(paths)}\n'
          f'Start: {start_time}\n'
          f'End: {end_time}\n'
          f'Gathering: {gathering_time - start_time}\n'
          f'Processing: {end_time - gathering_time}\n'
          f'Duration: {end_time - start_time}'
          )

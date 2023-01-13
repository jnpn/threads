"""CLI interface for threads project.

Be creative! do whatever you want!

- Install click or typer and create a CLI app
- Use builtin argparse
- Start a web application
- Import things from your .base module
"""
import time

from .ascii import rerender
from .threads import Monitor, Dummy


def main():  # pragma: no cover
    """
    The main function executes on commands:
    `python -m threads` and `$ threads `.

    This is your program's entry point.

    You can change this function to do whatever you want.
    Examples:
        * Run a test suite
        * Run a server
        * Do some other stuff
        * Run a command line application (Click, Typer, ArgParse)
        * List all available tasks
        * Run an application (Flask, FastAPI, Django, etc.)
    """
    ts = [Dummy() for _ in range(4)]
    m = Monitor(ts)
    m.start()
    for t in ts:
        t.start()

    time.sleep(5)
    m.toggle()

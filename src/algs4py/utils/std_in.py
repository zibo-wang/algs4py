"""StdIn

StdIn is a utility class that provides methods for reading from standard input.
We simulate the Java like StdIn using a queue.

"""

import sys
from queue import Queue
from typing import Any, Iterator, List, Optional, TextIO

import numpy as np

from algs4py.utils.std_out import StdOut


class StdIn:
    """Overview"""

    def __init__(self) -> None:

        # Assume UTF-8 encoding for std input.
        self.CHARSET_NAME: str = "UTF-8"
        # Assume language = English, country = AU for consistency with System.out.
        self.LOCALE: str = "en_AU"

        self._input: TextIO = sys.stdin

        self.tokens: Queue[str] = Queue()

        self.__stdin2queue()

    def __stdin2queue(self) -> None:
        """Read from stdin and put into queue."""
        for line in self._input:
            for token in line:
                self.tokens.put(token)

    def is_empty(self) -> bool:
        """Is the queue empty?

            Use this method to check if next to read_string(), read_double() etc.
            will succeed.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self.tokens.empty()

    def has_next_line(self) -> bool:
        """Does the input have more lines?

            Use this method to check if read_line() will succeed.

        Returns:
            bool: True if the input has more lines, False otherwise.
        """
        return not self.is_empty()
    def has_next_char(self) -> bool:
        """Does the input have more characters?

            Use this method to check if read_char() will succeed.

        Returns:
            bool: True if the input has more characters, False otherwise.
        """
        return not self.is_empty()

    def read_line(self) -> Optional[str]:
        """Reads the next line of text from standard input and returns it as a string.

        Returns:
            Optional[str]: The next line of text from standard input as a string.
        """
        if self.tokens.empty():
            return None
        else:
            return self.tokens.get()

    def print_queue(self) -> None:
        """Print the queue."""
        l: List[str] = []
        while not self.tokens.empty():
            l.append(self.tokens.get())
        print(l)
        self.__stdin2queue()


if __name__ == "__main__":
    StdOut().print("Type a string: ")
    StdIn().print_queue()

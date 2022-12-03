"""Overview

"""

import sys
from typing import TextIO


class StdIn:
    """Overview"""

    def __init__(self):

        # Assume UTF-8 encoding for std input.
        self.CHARSET_NAME: str = "UTF-8"
        # Assume language = English, country = AU for consistency with System.out.
        self.LOCALE: str = "en_AU"

        self.input: TextIO = sys.stdin

        self.cursor: int = 0

    def is_empty(self) -> bool:
        """Check if the std in is empty.

        Returns:
            bool: True if the standard input is empty, False otherwise.
        """
        return not sys.stdin.readable()

    def has_next_line(self) -> bool:
        """Check if the std in has next line.

        Returns:
            bool: True if the standard input has next line, False otherwise.
        """

        try:
            self.input.seek(self.cursor)
            self.input.readline()
            self.cursor = self.input.tell()
            return True
        except:
            return False

    def has_next_char(self) -> bool:
        """Check if the std in has next char.

        Returns:
            bool: True if the standard input has next char, False otherwise.
        """
        try:
            self.input.seek(self.cursor)
            self.input.read(1)
            self.cursor = self.input.tell()
            return True
        except:
            return False

    def read_line(self) -> str:
        """Read a line from the std in.

        Returns:
            str: A line from the standard input.
        """
        return self.input.readline()

    def read_char(self) -> str:
        """Read a char from the std in.

        Returns:
            str: A char from the standard input.
        """
        return self.input.read(1)

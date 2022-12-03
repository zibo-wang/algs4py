"""Overview

The StdOut class provides methods for printing strings and numbers to standard 
output.

"""

import locale
import sys
from typing import Any, Optional, TextIO

language, encoding = locale.getdefaultlocale()


class StdOut:
    """Overview"""

    def __init__(self) -> None:
        """Overview"""

        # Assume UTF-8 encoding for std output.
        self.CHARSET_NAME: str = "UTF-8"
        # Assume language = English, country = AU for consistency with System.out.
        self.LOCALE: str = "en_AU"

        self.output: TextIO = sys.stdout

    def println(self, x: Optional[Any] = None) -> None:
        """Print the terminates the current line by printing the line-separator string.

        Args:
            x (Optional[Any], optional): The object to print. Defaults to None.

        """
        if x is None:
            print(file=self.output)
        else:
            print(x, file=self.output)
        self.output.flush()

    def print(self, x: Optional[Any] = None) -> None:
        """Print the object to the standard output stream.

        Args:
            x (Optional[Any], optional): The object to print. Defaults to None.

        """
        if x is None:
            self.output.flush()
        else:
            print(x, end="", file=self.output)
            self.output.flush()

    def printf(
        self, fmt: str, *args: Any, new_locale: Optional[str] = None
    ) -> None:
        """Print the formatted string to the standard output stream.

        Args:
            fmt (str): The format string.
            *args (Any): The arguments.
            locale (Optional[str], optional): The locale. Defaults to None.

        """
        if locale is None:
            self.output.write(fmt % args)
        else:
            locale.setlocale(locale.LC_ALL, new_locale)
            self.output.write(fmt % args)
            locale.setlocale(locale.LC_ALL, self.LOCALE)
        self.output.flush()


if __name__ == "__main__":
    StdOut().println("Test")
    StdOut().println(17)
    StdOut().print()
    StdOut().print(True)
    StdOut().println()
    StdOut().printf("%.6f\n", 1.0 / 7.0)

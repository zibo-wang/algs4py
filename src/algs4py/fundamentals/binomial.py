"""Binomial

https://algs4.cs.princeton.edu/11model/Binomial.java.html

"""

import sys
from typing import Any

import numpy as np
import numpy.typing as npt


class Binomial:
    def __init__(self) -> None:
        pass

    def binomial1(self, n: int, k: int, p: float) -> float:
        """Binomial coefficient.

        Args:
            n: Number of trials.
            k: Number of successes.
            p: Probability of success.

        Returns:
            float: Binomial coefficient.

        """
        if n == 0 and k == 0:
            return 1.0
        if n < 0 or k < 0:
            return 0.0
        return (1.0 - p) * self.binomial1(n - 1, k, p) + p * self.binomial1(
            n - 1, k - 1, p
        )

    def binomial2(self, n: int, k: int, p: float) -> Any:
        """Binomial coefficient.

        Args:
            n: Number of trials.
            k: Number of successes.
            p: Probability of success.

        Returns:
            Any: Binomial coefficient. (Might be float or int.)
                Type hint for this one is due to pow function.

        """
        # TODO: add type hint
        b: npt.NDArray[np.float64] = np.zeros((n + 1, k + 1))

        for i in range(n + 1):
            b[i][0] = pow(1.0 - p, i)
        b[0][0] = 1.0

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                b[i][j] = (1.0 - p) * b[i - 1][j] + p * b[i - 1][j - 1]
        return b[n][k]


if __name__ == "__main__":
    n = int(sys.argv[1])
    k = int(sys.argv[2])
    p = float(sys.argv[3])
    b = Binomial()
    print(b.binomial1(n, k, p))
    print(b.binomial2(n, k, p))

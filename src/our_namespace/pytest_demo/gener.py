class NumGenerator:
    """Генерує послідовність елементів заданої довжини та з заданою сумою."""

    def __init__(self, count: int = 1, sum: float = 1):
        self.count = count
        self.sum = float(sum)

    def __iter__(self):
        n = self.count
        step = self.sum / n if n > 0 else 0
        a = step
        while (n := n - 1) >= 0:
            yield a


class RandGenerator(NumGenerator):
    """Генерує послідовність випадкових елементів заданої довжини та з заданою сумою."""

    _rng = None

    @property
    def rng(self):
        if self._rng is None:
            import numpy
            self._rng = numpy.random.default_rng()
        return self._rng

    """Генерує послідовність випадкових елементів заданої довжини та з заданою сумою."""

    def __init__(self, count: int = 1, sum: float = 1):
        super().__init__(count, sum)

    def __iter__(self):
        n = self.count
        a = 0
        s = self.sum
        while (n := n - 1) >= 0:
            p = 1 - (self.rng.random() if n > 0 else 0)
            a = s * p
            yield a
            s -= a

import abc
from abc import ABC, abstractmethod
from config import TARGET_DIS, LABEL_UP, LABEL_DOWN, NONE


class Strategy(ABC):
    @abstractmethod
    def __init__(self, ds, std_close):
        self.target = self.get_target(ds)
        self.std_close = std_close

    def get_target(self, ds):
        return ds[:, 0]

    @abstractmethod
    def add_labels(self, start, end):
        pass


class ThreeClassPrediction(Strategy):
    def __init__(self, ds, std_close):
        super().__init__(ds, std_close)

    def up(self, i):
        return self.target[i + TARGET_DIS] > (self.target[i] + self.std_close)

    def none(self, i):
        return (self.target[i + TARGET_DIS] <= (self.target[i] + self.std_close)) and \
               (self.target[i + TARGET_DIS] >= (self.target[i] - self.std_close))

    def down(self, i):
        return self.target[i + TARGET_DIS] < (self.target[i] - self.std_close)

    def add_labels(self, start, end):
        labels = []
        for i in range(start, end):
            if self.up(i):
                labels.append(LABEL_UP)
            elif self.none(i):
                labels.append(NONE)
            elif self.down(i):
                labels.append(LABEL_DOWN)
        return labels

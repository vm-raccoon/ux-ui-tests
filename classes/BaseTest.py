from abc import abstractmethod


class BaseTest:

    @abstractmethod
    def run(self):
        pass

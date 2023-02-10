from abc import abstractmethod


class BaseTest:

    active = True

    @abstractmethod
    def run(self):
        pass

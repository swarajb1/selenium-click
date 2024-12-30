from random import random
from time import sleep

from core.config import settings


def one_click():
    print("One click!")

    raise NotImplementedError("This function 'one click' is not implemented yet.")

    for _ in range(1000):
        click_function()

        sleep(settings.SINGLE_CLICK_TIME_SECONDS * (1 + random()))

    return True


def click_function():
    print("Click function!")

    return True

from datetime import datetime
from random import random
from time import sleep

import pyautogui
from core.config import settings
from utils.logger import log_click


def click_auto():
    print("One click!")

    for i in range(1, 10001):
        sleep(settings.SINGLE_CLICK_TIME_SECONDS * (1 + random()))

        click_function(i)

    return True


def click_function(num):
    x, y = pyautogui.position()

    pyautogui.click(x, y)  # Perform a mouse click

    log_click(num, datetime.now())

    return True

from core.config import settings
from enums import PurposeEnum
from utils.logger import logging
from work.click_auto import click_auto
from work.one_click import one_click


def main():
    # input("Press Enter to start...")

    for i in settings:
        logging.info(i)
        print("\n")

    if settings.PURPOSE == PurposeEnum.SINGLE_CLICK:
        one_click()

    elif settings.PURPOSE == PurposeEnum.SINGLE_CLICK_2:
        click_auto()


if __name__ == "__main__":
    main()

import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)


def log_click(num, time_interval):
    logging.info(f"clicked number {num} : clicked at {time_interval}")


def log_start(purpose):
    logging.info(f"started {purpose}")

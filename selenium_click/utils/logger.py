import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)


def log_click(num, time_interval):
    logging.info(f"clicked number {num} \t: clicked at {time_interval}")

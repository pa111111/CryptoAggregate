from Service import FlipsideService, PriceServiceManager
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('application.log', mode='a')])


def main():
    PriceServiceManager.update_all_prices()


main()

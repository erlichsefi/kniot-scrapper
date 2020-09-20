import logging
from kniot_scrapper import ScrapperRunner


#logging.basicConfig(filename='running.log',level=logging.DEBUG)

class Main:

    def start(self):
        runner = ScrapperRunner()
        runner.run()

if __name__ == '__main__':
    Main().start()

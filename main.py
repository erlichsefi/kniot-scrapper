from kniot_scrapper import ScrapperRunner


class Main:

    def start(self):
        runner = ScrapperRunner()
        runner.run()

if __name__ == '__main__':
    while True: # Because we want to be always up to date
        Main().start()

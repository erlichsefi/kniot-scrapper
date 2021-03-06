
class Logger:

    @staticmethod
    def start_scrapper(chain):
        print("Scrapping " + chain)

    @staticmethod
    def file_parse(chain, file_name):
        print("Parsing " + chain + "::" + file_name)

    @staticmethod
    def file_retry(chain, file_name):
        print("Retrying " + chain + "::" + file_name)

    
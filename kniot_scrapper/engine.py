import os


class Engine:

    chain = ''
    storage_path = ''

    def __init__(self):
        self.storage_path = os.path.join(os.environ['XML_STORE_PATH'], self.chain)
        
    def scrape(self):
        self.make_storage_path_dir()

    def make_storage_path_dir(self) -> None:
        if os.path.exists(self.storage_path):
            return
        os.mkdir(self.storage_path)

        
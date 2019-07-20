import asyncio
import ntpath
import os
from ftplib import FTP_TLS
from kniot_scrapper.utils import Gzip
from kniot_scrapper.utils import Logger

class Cerberus:

    chain = ''
    ftp_host = 'url.retail.publishedprices.co.il'
    ftp_path = '/'
    ftp_username = ''
    ftp_password = ''
    storage_path = ''

    target_file_extension = '.xml'

    ftp = False

    def scrape(self):

        self.storage_path = 'dumps/' + self.chain + '/'
        os.mkdir(self.storage_path)

        self.ftp = FTP_TLS(self.ftp_host, self.ftp_username, self.ftp_password)
        self.ftp.cwd(self.ftp_path)

        file_names = self.ftp.nlst()

        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.persist_files(file_names))

        self.ftp.quit()

    async def persist_files(self, file_names):

        loop = asyncio.get_event_loop()
        futures = []
        for file_name in file_names:
            futures.append(loop.run_in_executor(
                None, 
                self.persist_file, 
                file_name
            )) 

        for response in await asyncio.gather(*futures):
            pass


    def persist_file(self, file_name):

        Logger.file_parse(self.chain, file_name)

        temporary_gz_file_path = os.path.join(self.storage_path, file_name)

        self.fetch_temporary_gz_file(file_name, temporary_gz_file_path)
       
        extension = os.path.splitext(file_name)[1]

        if extension != '.gz':
            return

        file_save_path = self.storage_path + ntpath.basename(temporary_gz_file_path)
        file_name = os.path.splitext(file_save_path)[0]

        Gzip.extract_xml_file_from_gz_file(self.target_file_extension, file_save_path, file_name)

        os.remove(temporary_gz_file_path)

    def fetch_temporary_gz_file(self, file_name, temporary_gz_file_path):

        file = open(temporary_gz_file_path, 'wb')

        ftp = FTP_TLS(self.ftp_host, self.ftp_username, self.ftp_password)
        ftp.cwd(self.ftp_path)
        ftp.retrbinary('RETR ' + file_name, file.write)
        
        ftp.quit()

        file.close()



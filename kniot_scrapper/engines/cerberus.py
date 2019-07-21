import asyncio
import ntpath
import os
from ftplib import FTP_TLS
from kniot_scrapper import Engine
from kniot_scrapper.utils import Gzip
from kniot_scrapper.utils import Logger

class Cerberus(Engine):

    ftp_host = 'url.retail.publishedprices.co.il'
    ftp_path = '/'
    ftp_username = ''
    ftp_password = ''

    target_file_extension = '.xml'

    ftp = False

    def scrape(self):
        super(Cerberus, self).scrape()
        
        loop = asyncio.get_event_loop()
        files = self.get_files()
        loop.run_until_complete(self.persist_files(files))

    def get_files(self):
        self.ftp = FTP_TLS(self.ftp_host, self.ftp_username, self.ftp_password)
        self.ftp.cwd(self.ftp_path)
        files = self.ftp.nlst()
        self.ftp.quit()
        return files

    async def persist_files(self, file_names):
        loop = asyncio.get_event_loop()
        EXECUTOR = concurrent.futures.ThreadPoolExecutor(max_workers=8)

        futures = []
        for file_name in file_names:
            futures.append(loop.run_in_executor(
                EXECUTOR, 
                self.persist_file, 
                file_name
            )) 

        for response in await asyncio.gather(*futures):
            pass

    def persist_file(self, file_name):
        extension = os.path.splitext(file_name)[1]
        if extension != '.gz':
            return

        Logger.file_parse(self.chain, file_name)

        temporary_gz_file_path = os.path.join(self.storage_path, file_name)
        self.fetch_temporary_gz_file(temporary_gz_file_path)
        Gzip.extract_xml_file_from_gz_file(temporary_gz_file_path)

        os.remove(temporary_gz_file_path)

    def fetch_temporary_gz_file(self, temporary_gz_file_path):
        file = open(temporary_gz_file_path, 'wb')
        file_name = ntpath.basename(temporary_gz_file_path)

        try:
            ftp = FTP_TLS(self.ftp_host, self.ftp_username, self.ftp_password)
            ftp.cwd(self.ftp_path)
            ftp.retrbinary('RETR ' + file_name, file.write)
            ftp.quit()
        except:
            Logger.file_parse(self.chain, file_name)
            self.fetch_temporary_gz_file(temporary_gz_file_path)

        file.close()
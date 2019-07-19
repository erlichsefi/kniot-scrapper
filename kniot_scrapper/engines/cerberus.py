from ftplib import FTP_TLS
from kniot_scrapper.utils import Gzip
import ntpath
import os


class Cerberus:

    ftp_host = 'url.retail.publishedprices.co.il'
    ftp_username = ''
    ftp_password = ''
    storage_path = ''

    target_file_extension = '.xml'

    def scrape(self):

        ftp = FTP_TLS(self.ftp_host, self.ftp_username, self.ftp_password)

        file_names = ftp.nlst()

        for filename in file_names:
            self.persist_file(ftp, filename)

        ftp.quit()

    def persist_file(self, ftp, filename):

        temporary_gz_file_path = os.path.join(self.storage_path, filename)

        self.fetch_temporary_gz_file(ftp, filename, temporary_gz_file_path)
       
        extension = os.path.splitext(filename)[1]

        if extension != '.gz':
            return

        file_save_path = self.storage_path + ntpath.basename(temporary_gz_file_path)
        filename = os.path.splitext(file_save_path)[0]

        Gzip.extract_xml_file_from_gz_file(self.target_file_extension, file_save_path, filename)

        os.remove(temporary_gz_file_path)

    def fetch_temporary_gz_file(self, ftp, filename, temporary_gz_file_path):

        file = open(temporary_gz_file_path, 'wb')

        ftp.retrbinary('RETR ' + filename, file.write)

        file.close()



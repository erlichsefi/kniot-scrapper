from ftplib import FTP_TLS
from kniot_scrapper.utils import Gzip
from kniot_scrapper.utils import S3
import ntpath
import os
from tqdm import tqdm


class Cerberus:

    ftp_host = 'url.retail.publishedprices.co.il'
    ftp_username = ''
    ftp_password = ''
    storage_path = ''

    progressbar = False

    target_file_extension = '.xml'

    def scrape(self):

        ftp = FTP_TLS(self.ftp_host, self.ftp_username, self.ftp_password)

        file_names = ftp.nlst()

        self.progressbar = tqdm(total=len(file_names))

        for filename in file_names:
            self.persist_file(ftp, filename)

        ftp.quit()

    def persist_file(self, ftp, filename):

        self.progressbar.update(1)

        local_filename = os.path.join(self.storage_path, filename)

        file = open(local_filename, 'wb')

        ftp.retrbinary('RETR ' + filename, file.write)

        file.close()

        extension = os.path.splitext(filename)[1]

        if extension != '.gz':
            return

        file_save_path = self.storage_path + ntpath.basename(local_filename)

        filename = os.path.splitext(file_save_path)[0]

        Gzip.extract_xml_file_from_gz_file(self.target_file_extension, file_save_path, filename)

        S3.upload(filename + self.target_file_extension, filename + self.target_file_extension)

        os.remove(filename + self.target_file_extension)

        os.remove(local_filename)

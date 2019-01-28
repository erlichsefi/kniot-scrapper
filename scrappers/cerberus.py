from ftplib import FTP_TLS
import os
from tqdm import tqdm
import ntpath
import gzip


class Cerberus:

    ftp_host = 'url.retail.publishedprices.co.il'
    ftp_username = ''
    ftp_password = ''
    storage_path = './'

    progressbar = False

    target_file_extension = '.xml'

    def scrape(self):
        ftp = FTP_TLS(self.ftp_host, self.ftp_username, self.ftp_password)

        filenames = ftp.nlst()

        self.progressbar = tqdm(total=len(filenames))

        for filename in filenames:
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

        self.extract_xml_file_from_gz_file(file_save_path, filename)

        os.remove(local_filename)

    def extract_xml_file_from_gz_file(self, file_save_path, filename):
        with gzip.open(file_save_path, 'rb') as infile:
            with open(filename + self.target_file_extension, 'wb') as outfile:
                for line in infile:
                    outfile.write(line)
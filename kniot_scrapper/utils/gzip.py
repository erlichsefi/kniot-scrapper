import gzip
import shutil
import os

class Gzip:

    @staticmethod
    def extract_xml_file_from_gz_file(file_save_path):
        try:
            with gzip.open(file_save_path, 'rb') as infile:
                with open(os.path.splitext(file_save_path)[0] + '.xml', 'wb') as outfile:
                    shutil.copyfileobj(infile, outfile)
        except:
            print('Error decoding file:' + file_save_path)
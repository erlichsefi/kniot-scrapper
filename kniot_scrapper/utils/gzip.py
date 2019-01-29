import gzip


class Gzip:

    @staticmethod
    def extract_xml_file_from_gz_file(target_file_extension, file_save_path, filename):
        try:
            with gzip.open(file_save_path, 'rb') as infile:
                with open(filename + target_file_extension, 'wb') as outfile:
                    for line in infile:
                        outfile.write(line)
        except:
            print('Error decoding file:' + filename)
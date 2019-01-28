from scrappers import cerberus


class FreshMarket(cerberus.Cerberus):

    ftp_username = 'freshmarket'

    storage_path = './files/freshmarket/'

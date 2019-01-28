from scrappers import cerberus


class StopMarket(cerberus.Cerberus):

    ftp_username = 'Stop_Market'

    storage_path = './files/stop_market/'

from sec_edgar_downloader import Downloader
class Scraper:
    def __init__(self):
        self.downloader = Downloader()
    def get10Ks(self, ticker):
        self.downloader.get("10-K", ticker, download_details=True)
    def get10kyear(self, ticker, year):
        self.downloader.get('10-K', ticker, after = str(year)+"-01-01",
        before = str(year)+"-12-31", download_details=True)
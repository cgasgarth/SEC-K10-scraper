class Stock:
    def __init__(self, link, myid, permno, CUSIP, date_0_trd, Offer_Date, ipo_year,
    ipo_ticker, ipo_name):
        self.link = link
        self.myid = myid
        self.permno = permno
        self.CUSIP = CUSIP
        self.date_0_trd = date_0_trd
        self.Offer_Date = Offer_Date
        self.ipo_year = ipo_year
        self.ipo_ticker = ipo_ticker
        self.ipo_name = ipo_name
        self.f10k5 = ipo_year + 5
        self.f10k10 = ipo_year + 10

    def return_link(self):
        return self.link
    def return_myid(self):
        return self.myid
    def return_permno(self):
        return self.permno
    def return_CUSIP(self):
        return self.CUSIP
    def return_date_0_trd(self):
        return self.date_0_trd
    def return_Offer_Date(self):
        return self.Offer_Date
    def return_ipo_year(self):
        return self.ipo_year
    def return_ipo_ticker(self):
        return self.ipo_ticker
    def return_ipo_name(self):
        return self.ipo_name
    def return_f10k5(self):
        return self.f10k5
    def return_f10k10(self):
        return self.f10k10
    def return_RS(self):
        return self.RS
    def return_NOTES(self):
        return self.NOTES

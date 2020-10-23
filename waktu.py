from datetime import date

def create_date(tahun, bulan):
    d = date(int(tahun), int(bulan), 1)
    result = d.strftime("%y%b-%Y-%B-%x")
    return result
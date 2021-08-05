import pyqrcode
from pyqrcode import QRCode

str = "https://covid-tracker-618cf.web.app/"

url = pyqrcode.create(str)

url.svg('Covidtracker.svg',scale=5)
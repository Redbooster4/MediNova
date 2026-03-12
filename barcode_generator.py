from io import BytesIO
import barcode
from barcode import EAN13
from barcode.writer import SVGWriter

rv = BytesIO()
ean = EAN13("100000902922", writer=SVGWriter())
ean.write(rv)
ean.save("barcode")
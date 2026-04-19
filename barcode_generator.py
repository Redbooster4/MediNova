# from io import BytesIO
# import barcode
# from barcode import EAN13
# from barcode.writer import SVGWriter

# rv = BytesIO()
# ean = EAN13("100000902922", writer=SVGWriter())
# ean.write(rv)
# ean.save("barcode")

import qrcode
import json

# List of medicines (you can scale this)
medicines = [
    {
        "supplier_id": 1,
        "medicine_name": "Amoxicillin 250mg",
        "barcode": "8901234567891",
        "category": "Antibiotic",
        "expiry_date": "2027-03-15",
        "manufacturer": "Cipla",
        "mrp": 120.0,
        "stock_qty": 150
    },
    {
        "supplier_id": 1,
        "medicine_name": "Ibuprofen 400mg",
        "barcode": "8901234567892",
        "category": "Pain Relief",
        "expiry_date": "2026-09-10",
        "manufacturer": "Dr Reddy's",
        "mrp": 60.0,
        "stock_qty": 300
    },
    {
        "supplier_id": 1,
        "medicine_name": "Cetirizine 10mg",
        "barcode": "8901234567893",
        "category": "Antihistamine",
        "expiry_date": "2027-01-20",
        "manufacturer": "Zydus",
        "mrp": 35.0,
        "stock_qty": 180
    }
]

# Generate QR codes
for med in medicines:
    data = json.dumps(med)

    qr = qrcode.make(data)
    for i in range(0,3):
        filename = f"medicine_{i}.png"
        qr.save(filename)
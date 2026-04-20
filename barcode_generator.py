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
    },
    {
        "supplier_id": 2,
        "medicine_name": "Paracetamol 500mg",
        "barcode": "8901234567894",
        "category": "Pain Relief",
        "expiry_date": "2026-12-01",
        "manufacturer": "Sun Pharma",
        "mrp": 50.0,
        "stock_qty": 500
    },
    {
        "supplier_id": 2,
        "medicine_name": "Azithromycin 500mg",
        "barcode": "8901234567895",
        "category": "Antibiotic",
        "expiry_date": "2026-08-15",
        "manufacturer": "Cipla",
        "mrp": 200.0,
        "stock_qty": 90
    },
    {
        "supplier_id": 3,
        "medicine_name": "Metformin 500mg",
        "barcode": "8901234567896",
        "category": "Diabetes",
        "expiry_date": "2027-06-10",
        "manufacturer": "Torrent",
        "mrp": 80.0,
        "stock_qty": 250
    },
    {
        "supplier_id": 5,
        "medicine_name": "Atorvastatin 10mg",
        "barcode": "8901234567897",
        "category": "Cholesterol",
        "expiry_date": "2027-04-25",
        "manufacturer": "Zydus",
        "mrp": 150.0,
        "stock_qty": 130
    },
    {
        "supplier_id": 2,
        "medicine_name": "Pantoprazole 40mg",
        "barcode": "8901234567898",
        "category": "Acidity",
        "expiry_date": "2026-11-30",
        "manufacturer": "Dr Reddy's",
        "mrp": 90.0,
        "stock_qty": 220
    },
    {
        "supplier_id": 4,
        "medicine_name": "Levocetirizine 5mg",
        "barcode": "8901234567899",
        "category": "Antihistamine",
        "expiry_date": "2027-02-18",
        "manufacturer": "Sun Pharma",
        "mrp": 45.0,
        "stock_qty": 160
    },
    {
        "supplier_id": 4,
        "medicine_name": "Dolo 650",
        "barcode": "8901234567800",
        "category": "Pain Relief",
        "expiry_date": "2026-10-05",
        "manufacturer": "Micro Labs",
        "mrp": 30.0,
        "stock_qty": 600
    }
]

for i, med in enumerate(medicines):
    data = json.dumps(med)

    qr = qrcode.make(data)

    filename = f"medicine_{i}.png"
    qr.save(filename)
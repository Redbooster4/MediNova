import smtplib
from gui.db import fetch_supplier, fetch_medicine

provieders=fetch_supplier()
#print(provieders)
medicine=fetch_medicine()

for i in range(len(provieders)):
    receiver_email = provieders[i][3]
    print(receiver_email)
    address="Kandivali, Mumbai-400067, Maharashtra"
    medicine="Strepcils"

    text = f"""Subject: MEDICINE OUT OF STOCK\n\n
        Dear Sir/Madam,
        Your {medicine} at Appollo Medical Store present in {address}
        has been low of stock. We would appreciate it if you could arrange a resupply.

        Thank you for your Support,\n
        Regards,
        Neev Panchal
        Appolo Medical Store
    """

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("neeewww4@gmail.com", "gjes owgu dtmu rwtl")
    server.sendmail("neeewww4@gmail.com", receiver_email, text)
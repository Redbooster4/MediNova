import smtplib
from . import *
from db import *

def send_email():
    data = low_qty_providers()
    print(data)
    #[('Paracetamol 500mg', 'Neev Panchal', '7977424440', 'neev.p4@gmail.com'),
    # ('Strepcils 500 mg', '', '',  '', '')]

    for i in range(len(data)):
        receiver_email = data[i][3]
        print("Sending...",receiver_email)
        address="Kandivali, Mumbai-400067, Maharashtra"
        medicine = data[i][0]

        text = f"""Subject: MEDICINE OUT OF STOCK\n\n
            Dear Sir/Madam,
            Your {medicine} at Appollo Medical Store present in {address}
            has been low of stock(below 15). We would appreciate it if you could arrange a resupply.\n
            This month's invoice sales generated are attached on the pdf present below.

            Thank you for your Support,\n
            Regards,
            Neev Panchal
            Appolo Medical Store
        """
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("neeewww4@gmail.com", "gjes owgu dtmu rwtl")
        server.sendmail("neeewww4@gmail.com", receiver_email, text)

        Messagebox.show_info("Email Sent Successfully !!", title="SUCESS")
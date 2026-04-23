import smtplib
from . import *
from db import *
from email.message import EmailMessage

def send_email():
    data = to_mail_providers()
    #print(data)
    #[('Paracetamol 500mg', 10, 'neev.p4@gmail.com'),
    # ('Strepcils 500 mg', 10, 'email@gmail.com')]

    for i in range(len(data)):
        receiver_email = data[i][2]
        print("Sending...",receiver_email)
        branch="Kandivali, Mumbai-400067, Maharashtra"
        medicine = data[i][0]

        msg = EmailMessage()
        msg['Subject'] = "Medicine Out Of Stock"
        msg['From'] = "neeewww4@gmail.com"
        msg['To'] = receiver_email

        #Medicine Name
        #Quantity
        #Status
        rows=""
        for row in data:
            rows += f"<td>{row[0]}</td>"
            rows += f"<td>{row[1]}</td>"
            if row[1]<=10:
                reason = "Low Stock"
            else:
                reason = "Expired"
            print(reason)
            rows += f"<td>{reason}</td>"
        #print(rows) # <td>Paracetamol 500mg</td><td>10</td><td>Expired</td>
        msg.set_content(f'''
            <!DOCTYPE html>
            <html>
            <body>
                <table>
                    <tr>
                    <td align="center">
                        <table width="600">
                            <tr>
                                <td style="background:#162c15; padding:20px 32px;">
                                    <h1 style="margin:0; color:#ffffff; font-size:20px;">
                                        Apollo Medical Store
                                    </h1>
                                    <p style="color: hsl(0, 0%, 74%);font-size:13px;">Kandivali, Mumbai - 400067</p>
                                </td>
                            </tr>
                            <tr>
                                <td style="background:#fff3e0; padding:14px 32px; border-left:4px solid #ff9800;">
                                    <p style="margin:0; color:#e65100; font-size:14px; font-weight:bold;">
                                        Medicine Restock Required !!
                                    </p>
                                    <p style="margin:4px 0 0; color:#bf360c; font-size:12px;">
                                        The following medicines have been expired/low of stock
                                    </p>
                                </td>
                            </tr>
                            <p>
                                Dear Sir/Madam,<br>
                                Your Paracetamol 500mg at Appollo Medical Store present in Kandivali, Mumbai-400067, Maharashtra
                                has been low of stock(below 10). We would appreciate it if you could arrange a resupply.

                                <br><br>Thank you for your Support,<br><br>

                                Regards,<br>
                                Neev Panchal<br>
                                Appolo Medical Store<br>
                            </p>
                            <tr>
                                <td style="padding:24px 32px;">
                                    <table width="100%" style="border-collapse:collapse;">
                                        <thead>
                                            <tr style="background:#1a1a2e;">
                                                <th style="padding:10px 14px; color:#FFFFFF ;text-align:left; font-size:12px;">
                                                    Medicine Name</th>
                                                <th style="padding:10px 14px; color:#FFFFFF ;text-align:left; font-size:12px;">
                                                    Current Quantity</th>
                                                <th style="padding:10px 14px; color:#FFFFFF ;text-align:left; font-size:12px;">
                                                    Status</th>
                                            </tr>
                                        </thead>
                                        <tbody> <!-- data=[('Paracetamol 500mg', 'Neev Panchal', '7977424440', 'neev.p4@gmail.com'),()]-->
                                            <tr>
                                                {rows}
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </table>
                    </td>
                    </tr>
                </table>
                <p> 
            </body>
            </html>''', subtype="html")
        server = smtplib.SMTP_SSL("smtp.gmail.com")
        server.login("neeewww4@gmail.com", "gjes owgu dtmu rwtl")
        server.send_message(msg)
        server.quit()
        #SMTP_SSL →  ENCRYPT → connect → login → send

        Messagebox.show_info("Email Sent Successfully !!", title="SUCESS")
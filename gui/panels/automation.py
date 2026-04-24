from email.message import EmailMessage
import smtplib
from db import *

def group_by_email(records, key_index):
    grouped={}
    for row in records:
        email=row[key_index]
        if email not in grouped:
            grouped[email] = []
        grouped[email].append(row)
    return grouped

def build_rows(items, is_expiry=False):
    rows=""
    for row in items:
        rows+="<tr>"
        rows+=f"<td>{row[0]}</td>"
        if is_expiry:
            rows += f"<td>{row[1]}</td>"
            rows += "<td>Expiring Soon</td>"
        else:
            rows += f"<td>{row[1]}</td>"
            rows += "<td>Low Stock</td>"
        rows += "</tr>"
    print(rows)
    return rows

def send_email():
    low_qty, expiry=to_mail_providers()
    low_grouped=group_by_email(low_qty, 2)
    exp_grouped=group_by_email(expiry, 2)
    sender="neeewww4@gmail.com"
    branch="Kandivali, Mumbai-400067, Maharashtra"
    try:
        server=smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender,"gjes owgu dtmu rwtl")
        for email, items in low_grouped.items():
            msg=EmailMessage()
            msg['Subject']="Low Stock Alert"
            msg['From']=sender
            msg['To']=email
            rows=build_rows(items)
            msg.set_content(f"""
            <html>
            <body>
                <table>
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
                                The following medicines are below Minimum Stock Threshold
                            </p>
                        </td>
                    </tr>
                <h2>Low Stock Alert - Apollo Medical Store</h2>
                <p>{branch}</p>
                <table border="1" cellpadding="8">
                    <tr>
                        <th>Medicine</th>
                        <th>Quantity</th>
                        <th>Status</th>
                    </tr>
                    {rows}
                </table>
                </table
            </body>
            </html>
            """, subtype="html")
            server.send_message(msg)

        for email, items in exp_grouped.items():
            msg=EmailMessage()
            msg['Subject']="Expiry Alert"
            msg['From']=sender
            msg['To']=email
            rows=build_rows(items, is_expiry=True)
            msg.set_content(f"""
            <html>
            <body>
                <table>
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
                                The following medicines are below EXPIRED
                            </p>
                        </td>
                    </tr>
                <h2>Expiry Alert - Apollo Medical Store</h2>
                <p>{branch}</p>

                <table border="1" cellpadding="8">
                    <tr>
                        <th>Medicine</th>
                        <th>Expiry Date</th>
                        <th>Status</th>
                    </tr>
                    {rows}
                </table>
                </table
            </body>
            </html>
            """, subtype="html")
            server.send_message(msg)
        server.quit()
        Messagebox.show_info("Email Sent Successfully!", title="SUCCESS")
    except Exception as e:
        print("Email error:", e)
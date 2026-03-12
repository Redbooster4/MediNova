#imports for the SCANNER PART
import cv2 as cv 
import numpy as np
from pyzbar.pyzbar import decode
#imports for the GUI embedding PART
import tkinter as tk
from PIL import Image, ImageTk

camera = cv.VideoCapture(0)

def launch_scanner(master, on_result):
    window = tk.Toplevel(master)
    window.title("Barcode Scanning Window")
    window.geometry("660x520")

    barcode_present = False
    running = {"active": True}
    
    label=tk.Label(window)
    label.pack(pady=12)
    def update_frame():
        if not running["active"]:
            return

        ret, frame = camera.read()
        frame=cv.flip(frame, 1)
        if not ret:
            print("not captured")
            window.after(10, update_frame)
            return
        barcodes = decode(frame)

        for code in barcodes:
            points = code.polygon
            if points:
                barcode_present=True
                pts = np.array([(p.x, p.y) for p in points], np.int32)
                pts = pts.reshape((-1,1,2))
                cv.polylines(frame, [pts], True, (0,255,0), 5)
            
        frame=cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        img= ImageTk.PhotoImage(Image.fromarray(frame))
        label.config(image=img)
        label.image = img #prevent garbage

        window.after(10, update_frame)

        if barcodes:
            data=barcodes[0].data.decode("utf-8")
            label.configure(text=f"BARCODE DETECTED: {data}")
            print(data)
            running["active"]=False
            #window.after(600, got_barcode(data))
            return

        # cv.imshow('Scanner', frame)
        # key = cv.waitKey(1)
        # if key == ord('q'):
        #     print("Exiting Frame.")
        #     break

    def on_close():
        running["active"] = False
        camera.release()
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_close)
    update_frame()


#py -m pip install -r requirement.txt
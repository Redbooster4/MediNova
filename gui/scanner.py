#imports for the SCANNER PART
import cv2 as cv 
import numpy as np
from pyzbar.pyzbar import decode
#imports for the GUI embedding PART
from tkinter import *
from PIL import Image, ImageTk
from db import *
import json

def launch_scanner(master):
    camera = cv.VideoCapture(0)
    window = Toplevel(master)
    window.title("Barcode Scanning Window")
    window.geometry("660x550")
    running = {"active": True}

    webcam=Label(window)#video frames->Label
    webcam.pack(pady=12)
    result=Label(window) #barcode txt->Bottom Line
    result.pack()
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
                pts = np.array([(p.x, p.y) for p in points], np.int32)
                pts = pts.reshape((-1,1,2))
                cv.polylines(frame, [pts], True, (0,255,0), 5)
            
        frame=cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        img= ImageTk.PhotoImage(Image.fromarray(frame))
        webcam.config(image=img)
        webcam.image = img #prevent garbage
        window.after(10, update_frame)
        if barcodes:
            data=barcodes[0].data.decode("utf-8")
            result.configure(text=f"BARCODE DETECTED: {data}")
            #print(data)
            running["active"]=False
            camera.release()
            #print(type(data)) #JSON STRING
            med_dict = json.loads(data)
            window.after(1000, lambda:add_medicine(med_dict))
            on_close()
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

    #window.protocol("WM_DELETE_WINDOW", on_close)
    update_frame()
#py -m pip install -r requirement.txt
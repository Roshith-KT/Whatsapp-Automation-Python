import keyboard as k
import pyautogui
import time
import pandas as pd
import webbrowser as web
from urllib.parse import quote


def send_whatsapp_message(contact_file_excel,message_file_txt,x_cord=530,y_cord=629):
    counter = 0
    df=pd.read_excel(contact_file_excel,dtype={"Contact":str})
    name=df['Name'].values
    contact=df['Contact'].values

    with open(message_file_txt) as f:
        message_file_data=f.read()

    zipped=zip(name,contact)

    for (a,b) in zipped:
        msg=message_file_data.format(a)

        web.open(f"https://web.whatsapp.com/send?phone={b}&text={quote(msg)}")
        time.sleep(60)
        pyautogui.click(x_cord,y_cord)
        time.sleep(2)
        pyautogui.click(1326, 696)
        #k.press_and_release('enter')
        time.sleep(2)
        k.press_and_release('ctrl+w')
        time.sleep(1)
        counter+=1
        print(counter,"-Messages sent")
    print("Done")


contact_path=r"./contact.xlsx"
message_path=r"./message.txt"

send_whatsapp_message(contact_path,message_path)
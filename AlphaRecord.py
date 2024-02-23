import datetime
from datetime import datetime as dt
from tkinter import *
import time
import webbrowser
import pyautogui as pag
from PIL import ImageGrab
import threading
import os

def th():
    th = threading.Thread(target=R_R_B)
    th.daemon = True
    th.start()

def R_R_B():
    # 1. 링크 주소 들어가 있는지 확인 2. 예약시간 확인 3. 예약되었습니다. 4. 예약시간 대기 후 record
    url = (link.get("1.0", END))
    reservation_hour = int((reservation_time_hour.get("1.0", END)))
    reservation_minutes = int((reservation_time_minutes.get("1.0", END)))
    reservation_time = reservation_hour * 60 + reservation_minutes
    # now_time = d.datetime.now().hour * 60 + d.datetime.now().minute
    # left_time = reservation_time - now_time
    while True:
        now_time = dt.now().hour * 60 + dt.now().minute
        # if now_time <= reservation_time - 5:
        #     print("예약시간 {0}분 남았습니다.".format(reservation_time - now_time))
        #     time.sleep(60 * left_time * 0.65)
        if reservation_time - now_time == 5:
            print("예약시간 5분 남았습니다.")
        elif now_time >= reservation_time:    
                webbrowser.open(str(url))
                zoom_pos = (997, 587)
                time.sleep(30)
                pag.click(zoom_pos)
                pag.hotkey("alt", "r")
                button_pos = (1147, 573)
                button_rgb = (14, 114 , 237)
                screen = ImageGrab.grab()
                rgb = screen.getpixel(button_pos)
                pag.keyDown("esc")
                while True:
                    time.sleep(4)
                    pag.hotkey("alt", "r")
                    screen = ImageGrab.grab()
                    rgb = screen.getpixel(button_pos)
                    if rgb == button_rgb:
                        time.sleep(0.7)
                    else:
                        os._exit(0)
                    pag.keyDown("esc")
                
        time.sleep(10)
        

root = Tk()
root.title("ZOOM 자동 녹화")
root.geometry("340x400") # 가로 * 세로 + x좌표 + y좌표
root.resizable(False, False)

link = Text(root, width=30, height=1)
link.pack()
link.insert(END, "링크를 입력해주세요.")

reservation_time_hour = Text(root, width=30, height=1)
reservation_time_hour.pack()
reservation_time_hour.insert(END, "시")

reservation_time_minutes = Text(root, width=30, height=1)
reservation_time_minutes.pack()
reservation_time_minutes.insert(END, "분")

record_reservation_button = Button(root, text="예약 시작", command = th)
record_reservation_button.pack()


root.mainloop()
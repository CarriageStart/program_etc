import pygetwindow as gw
import pywinauto
import time

def bring_window_to_front(window_title):
    # 윈도우 타이틀을 이용해 윈도우 핸들 가져오기
    windows = gw.getWindowsWithTitle(window_title)
    if not windows:
        print(f"'{window_title}' 창을 찾을 수 없습니다.")
        return

    window = windows[0]
    
    # 윈도우를 맨 앞으로 가져오기
    if not window.isActive:
        app = pywinauto.Application().connect(handle=window._hWnd)
        app.top_window().set_focus()
        window.activate()
        print(f"'{window_title}' 창을 맨 앞으로 고정했습니다.")
    else:
        print(f"'{window_title}' 창이 이미 활성화되어 있습니다.")

# 예제 사용
bring_window_to_front("Chrome")  # 'Chrome'이라는 타이틀을 가진 창을 맨 앞으로 고정


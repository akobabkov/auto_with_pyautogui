"""
1. Идем по списку вниз
2. Открываем форму нажатием enter
3. Ставим мышь в определенную координату экрана
4. Кликаем левой кнопкой
5. Закрываем форму комбинацией ctrl+enter
"""
import pyautogui as pg
import time as t

i = 1
while i <= 100:
    t.sleep(5)
    pg.hotkey('down')
    pg.press('enter')
    t.sleep(7)
    pg.moveTo(1145, 696)
    pg.click(button='left')
    t.sleep(2)
    pg.hotkey('ctrlright','enter')
    i = i + 1
    
    


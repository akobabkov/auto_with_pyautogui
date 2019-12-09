"""
1. Идем по списку вниз
2. Открываем форму нажатием enter
3. Ставим мышь в определенную координату экрана
4. Кликаем левой кнопкой
5. Ставим мышь в определенную координату экрана
6. Кликаем левой кнопкой
7. Ставим мышь в определенную координату экрана
8. Кликаем левой кнопкой
"""
import pyautogui as pg
import time as t

i = 1
while i <= 100:
    t.sleep(7)
    pg.hotkey('down')
    pg.press('enter')
    t.sleep(7)
    pg.moveTo(1145, 696)
    pg.click(button='left')
    t.sleep(3)
    pg.moveTo(1275, 725)
    pg.click(button='left')
    t.sleep(3)
    pg.moveTo(1333, 1010)
    pg.click(button='left')
    i = i + 1
    
    


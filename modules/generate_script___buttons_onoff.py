# Ce script permet de générer buttons_onoff.py

import os
import pathlib

here = os.path.dirname(pathlib.Path(__file__))
space = "    "
enter = "\n"

file = open(f"{here}{os.sep}buttons_onoff.py", "w", encoding='utf-8')

file.write("from modules import globals" + enter)
file.write("from modules import buttons" + enter)
file.write (enter)

for fn in range(1, 101, 1):  # function number
    file.write(f"def onoff{fn}(all_tabs):" + enter)
    file.write(space + f"\"\"\"La fonction permet d’activer/désactiver l’image n°{fn}.\"\"\"" + enter)
    file.write(space + f"if globals.enabled[{fn}]:" + enter)
    file.write(space + space + f"globals.enabled[{fn}] = 0" + enter)
    file.write(space + space + f"buttons.turnToGrayImages(all_tabs, {fn})" + enter)
    file.write(space + f"else:" + enter)
    file.write(space + space + f"globals.enabled[{fn}] = 1" + enter)
    file.write(space + space + f"buttons.turnToRGBImages(all_tabs, {fn})" + enter)
    file.write(space + f"return 0" + enter)
    file.write(enter)
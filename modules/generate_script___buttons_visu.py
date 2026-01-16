# Ce script permet de générer buttons_visu.py

import os
import pathlib

here = os.path.dirname(pathlib.Path(__file__))
space = "    "
enter = "\n"

file = open(f"{here}{os.sep}buttons_visu.py", "w", encoding='utf-8')

file.write("import os " + enter)
file.write("from core.common import *" + enter)
file.write("from modules import globals" + enter)
file.write(enter)

for fn in range(1, 101, 1):  # function number
    file.write(f"def visu{fn}(all_tabs):" + enter)
    file.write(space + f"\"\"\"Affiche la fenêtre de visualisation de l’image n°{fn} après édition.\"\"\"" + enter)
    file.write(space + f"if globals.edited[{fn}]:" + enter)
    file.write(space + space + "all_tabs.dialog = VISU()" + enter)
    file.write(space + space + f"all_tabs.dialog.display(all_tabs.out + os.sep + '{fn}_out.jpg')" + enter)
    file.write(space + "else:" + enter)
    file.write(space + space +  "all_tabs.dialog = MESSAGE()" + enter)
    file.write(space + space +  "all_tabs.dialog.message_erreur2()" + enter)
    file.write(enter)
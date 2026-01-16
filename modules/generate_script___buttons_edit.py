# Ce script permet de générer buttons_edit.py

import os
import pathlib

here = os.path.dirname(pathlib.Path(__file__))
space = "    "
enter = "\n"

file = open(f"{here}{os.sep}buttons_edit.py", "w", encoding='utf-8')

file.write("from core.common import *" + enter)
file.write("import logging" + enter)
file.write("from modules import globals" + enter)
file.write (enter)

for fn in range(1, 101, 1):  # function number
    file.write(f"def edit{fn}(all_tabs):" + enter)
    file.write(space + f"\"\"\"Affiche la fenêtre d’édition de l’image n°{fn}.\"\"\"" + enter)
    file.write(space + f"if globals.loaded[{fn}]:" + enter)
    file.write(space + space + f"all_tabs.dialog = EDIT(all_tabs, {fn})" + enter)
    file.write(space + space + f"all_tabs.dialog.display('{fn}_in.jpg', all_tabs)" + enter)
    file.write(space + space + f"logging.info(\"Edition de l'image {fn}\")" + enter)
    file.write(space + space + "logging.info('----------------------')" + enter)
    file.write(space + "else:" + enter)
    file.write(space + space + f"all_tabs.dialog = MESSAGE()" + enter)
    file.write(space + space + f"all_tabs.dialog.message_erreur1()" + enter)
    file.write(enter)
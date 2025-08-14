import os
import pathlib

here = os.path.dirname(pathlib.Path(__file__))
space = "    "
enter = "\n"

file = open(f"{here}{os.sep}buttons_edit.py", "w")

file.write("from core.common import *" + enter)
file.write("import logging" + enter)
file.write("from modules import globals" + enter)
file.write (enter)

for fn in range(1, 101, 1):  # function number
    file.write(f"def editFile{fn}(TABs):" + enter)
    file.write(space + f"if globals.loaded[{fn}]:" + enter)
    file.write(space + space + f"TABs.dialog = EDIT(TABs, {fn})" + enter)
    file.write(space + space + f"TABs.dialog.display('{fn}_in.jpg', TABs)" + enter)
    file.write(space + space + f"logging.info(\"Edition de l'image {fn}\")" + enter)
    file.write(space + space + "logging.info('----------------------')" + enter)
    file.write(space + "else:" + enter)
    file.write(space + space + f"TABs.dialog = MESSAGE()" + enter)
    file.write(space + space + f"TABs.dialog.message_erreur1()" + enter)
    file.write(enter)
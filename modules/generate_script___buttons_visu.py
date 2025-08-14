import os
import pathlib

here = os.path.dirname(pathlib.Path(__file__))
space = "    "
enter = "\n"

file = open(f"{here}{os.sep}buttons_visu.py", "w")

file.write("import os " + enter)
file.write("from core.common import *" + enter)
file.write("from modules import globals" + enter)
file.write(enter)

for fn in range(1, 101, 1):  # function number
    file.write(f"def visu{fn}(TABs):" + enter)
    file.write(space + f"if globals.edited[{fn}]:" + enter)
    file.write(space + space + "TABs.dialog = VISU()" + enter)
    file.write(space + space + f"TABs.dialog.display(TABs.out + os.sep + '{fn}_out.jpg')" + enter)
    file.write(space + "else:" + enter)
    file.write(space + space +  "TABs.dialog = MESSAGE()" + enter)
    file.write(space + space +  "TABs.dialog.message_erreur2()" + enter)
    file.write(enter)
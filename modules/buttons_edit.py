from kore.common import *
import logging
# from modules.ci_and_ds_tools import POINT

def editFile1(TAB):
    TAB.num = 1
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "1_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°1")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile2(TAB):
    TAB.num = 2
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "2_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°2")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()
    
def editFile3(TAB):
    TAB.num = 3
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "3_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°3")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()
    
def editFile4(TAB):
    TAB.num = 4
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "4_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°4")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()
    
def editFile5(TAB):
    TAB.num = 5
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "5_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°5")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()
    
def editFile6(TAB):
    TAB.num = 6
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "6_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°6")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()
    
def editFile7(TAB):
    TAB.num = 7
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "7_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°7")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()
    
def editFile8(TAB):
    TAB.num = 8
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "8_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°8")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()
    
def editFile9(TAB):
    TAB.num = 9
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "9_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°9")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()
    
def editFile10(TAB):
    TAB.num = 10
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "10_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°10")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile11(TAB):
    TAB.num = 11
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "11_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°11")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()
    
def editFile12(TAB):
    TAB.num = 12
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "12_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°12")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()
    
def editFile13(TAB):
    TAB.num = 13
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "13_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°13")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()
    
def editFile14(TAB):
    TAB.num = 14
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "14_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°14")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile15(TAB):
    TAB.num = 15
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "15_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°15")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()
    
def editFile16(TAB):
    TAB.num = 16
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "16_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°16")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile17(TAB):
    TAB.num = 17
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "17_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°17")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()
    
def editFile18(TAB):
    TAB.num = 18
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "18_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°18")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()
    
def editFile19(TAB):
    TAB.num = 19
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "19_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°19")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile20(TAB):
    TAB.num = 20
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "20_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°20")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()
    
def editFile21(TAB):
    TAB.num = 21
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "21_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°21")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()
    
def editFile22(TAB):
    TAB.num = 22
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "22_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°22")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile23(TAB):
    TAB.num = 23
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "23_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°23")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile24(TAB):
    TAB.num = 24
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "24_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°24")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()
    
def editFile25(TAB):
    TAB.num = 25
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "25_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°25")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile26(TAB):
    TAB.num = 26
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "26_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°26")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile27(TAB):
    TAB.num = 27
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "27_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°27")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()
    
def editFile28(TAB):
    TAB.num = 28
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "28_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°28")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()
    
def editFile29(TAB):
    TAB.num = 29
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "29_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°29")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()
    
def editFile30(TAB):
    TAB.num = 30
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "30_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°30")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()
    
def editFile31(TAB):
    TAB.num = 31
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "31_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°31")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()
    
def editFile32(TAB):
    TAB.num = 32
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "32_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°32")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()
    
def editFile33(TAB):
    TAB.num = 33
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "33_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°33")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()
    
def editFile34(TAB):
    TAB.num = 34
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "34_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°34")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()
    

def editFile35(TAB):
    TAB.num = 35
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "35_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°35")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile36(TAB):
    TAB.num = 36
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "36_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°36")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile37(TAB):
    TAB.num = 37
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "37_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°37")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile38(TAB):
    TAB.num = 38
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "38_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°38")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()
    
def editFile39(TAB):
    TAB.num = 39
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "39_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°39")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile40(TAB):
    TAB.num = 40
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "40_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°40")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile41(TAB):
    TAB.num = 41
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "41_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°41")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile42(TAB):
    TAB.num = 42
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "42_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°42")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1() 

def editFile43(TAB):
    TAB.num = 43
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "43_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°43")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()
    
def editFile44(TAB):
    TAB.num = 44
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "44_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°44")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile45(TAB):
    TAB.num = 45
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "45_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°45")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile46(TAB):
    TAB.num = 46
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "46_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°46")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()
    
def editFile47(TAB):
    TAB.num = 47
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "47_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°47")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()
    
def editFile48(TAB):
    TAB.num = 48
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "48_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°48")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile49(TAB):
    TAB.num = 49
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "49_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°49")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()
    
def editFile50(TAB):
    TAB.num = 50
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "50_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°50")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile51(TAB):
    TAB.num = 51
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "51_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°51")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile52(TAB):
    TAB.num = 52
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "52_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°52")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile53(TAB):
    TAB.num = 53
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "53_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°53")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()
    
def editFile54(TAB):
    TAB.num = 54
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "54_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°54")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile55(TAB):
    TAB.num = 55
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "55_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°55")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile56(TAB):
    TAB.num = 56
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "56_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°56")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()
    
def editFile57(TAB):
    TAB.num = 57
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "57_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°57")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()
    
def editFile58(TAB):
    TAB.num = 58
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "58_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°58")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()
    
def editFile59(TAB):
    TAB.num = 59
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "59_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°59")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile60(TAB):
    TAB.num = 60
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "60_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°60")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile61(TAB):
    TAB.num = 61
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "61_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°61")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile62(TAB):
    TAB.num = 62
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "62_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°62")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile63(TAB):
    TAB.num = 63
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "63_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°63")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile64(TAB):
    TAB.num = 64
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "64_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°64")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile65(TAB):
    TAB.num = 65
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "65_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°65")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile66(TAB):
    TAB.num = 66
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "66_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°66")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile67(TAB):
    TAB.num = 67
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "67_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°67")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile68(TAB):
    TAB.num = 68
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "68_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°68")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile69(TAB):
    TAB.num = 69
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "69_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°69")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile70(TAB):
    TAB.num = 70
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "70_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°70")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile71(TAB):
    TAB.num = 71
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "71_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°71")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile72(TAB):
    TAB.num = 72
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "72_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°72")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile73(TAB):
    TAB.num = 73
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "73_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°73")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile74(TAB):
    TAB.num = 74
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "74_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°74")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile75(TAB):
    TAB.num = 75
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "75_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°75")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile76(TAB):
    TAB.num = 76
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "76_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°76")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile77(TAB):
    TAB.num = 77
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "77_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°77")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile78(TAB):
    TAB.num = 78
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "78_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°78")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile79(TAB):
    TAB.num = 79
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "79_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°79")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile80(TAB):
    TAB.num = 80
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "80_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°80")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile81(TAB):
    TAB.num = 81
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "81_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°81")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile82(TAB):
    TAB.num = 82
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "82_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°82")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile83(TAB):
    TAB.num = 83
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "83_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°83")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile84(TAB):
    TAB.num = 84
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "84_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°84")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile85(TAB):
    TAB.num = 85
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "85_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°85")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile86(TAB):
    TAB.num = 86
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "86_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°86")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile87(TAB):
    TAB.num = 87
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "87_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°87")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile88(TAB):
    TAB.num = 88
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "88_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°88")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile89(TAB):
    TAB.num = 89
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "89_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°89")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()

def editFile90(TAB):
    TAB.num = 90
    file_exists = 0
    name = ""
    for file in os.listdir(TAB.in_):
        if "90_in" in file:
            file_exists = True
            name = file
    if file_exists:
        TAB.dialog = EDIT(TAB, num=TAB.num)
        TAB.dialog.display(name)
        logging.info("Edition de l'image n°90")
        logging.info("----------------------")
    else:
        TAB.dialog = MESSAGE()
        TAB.dialog.message_erreur1()
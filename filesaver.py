import os
import shutil

x = int(input())

os.mkdir("C:/Users/314Cl/Google ドライブ/Prog1/Prog1_" + str(x))
dir = "C:/Users/314Cl/Google ドライブ/Prog1/Prog1_" + str(x)
files1 = os.listdir("C:/Users/314Cl/Google ドライブ/Prog1")

for file in files1:
    if "1_" + str(x) in file:
        if "hw" in file:
            shutil.copy("C:/Users/314Cl/Google ドライブ/Prog1/" + file + "/Debug/" + file + ".exe",   "C:/Users/314Cl/Google ドライブ/Prog1/Prog1_" + str(x))
            shutil.copy("C:/Users/314Cl/Google ドライブ/Prog1/" + file + "/" + file + "/" + file + ".c",   "C:/Users/314Cl/Google ドライブ/Prog1/Prog1_" + str(x))

    if "1_" + str(x+1) in file:
        if "pre" in file:
            shutil.copy("C:/Users/314Cl/Google ドライブ/Prog1/" + file + "/Debug/" + file + ".exe",   "C:/Users/314Cl/Google ドライブ/Prog1/Prog1_" + str(x))
            shutil.copy("C:/Users/314Cl/Google ドライブ/Prog1/" + file + "/" + file + "/" + file + ".c",   "C:/Users/314Cl/Google ドライブ/Prog1/Prog1_" + str(x))
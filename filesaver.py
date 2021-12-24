import os
import shutil
import tkinter
from tkinter import filedialog

print("Progのフォルダがある場所を選択してください")
dire = "C://download"
fld = filedialog.askdirectory(initialdir = dire)

print("第何回か入力してください（数字のみ）")
n = input()

dir = fld + "_" + n

files1 = os.listdir(fld)

os.mkdir(fld + "/Prog1_" + n)

for file in files1:
    if "1_" + n in file:
        if "hw" in file:
            shutil.copy("{}/{}/Debug/{}.exe".format(fld, file, file), "{}/prog1_{}".format(fld, n))
            shutil.copy("{}/{}/{}/{}.c".format(fld, file, file, file), "{}/Prog1_{}".format(fld, n))

    if "1_" + str(int(n) + 1) in file:
        if "pre" in file:
            shutil.copy("{}/{}/Debug/{}.exe".format(fld, file, file), "{}/prog1_{}".format(fld, n))
            shutil.copy("{}/{}/{}/{}.c".format(fld, file, file, file), "{}/Prog1_{}".format(fld, n))

print("只今圧縮中のため、少々お待ちください。")
shutil.make_archive('1_{}'.format(n), 'zip', root_dir=fld)
    
print("完了しました。選択したディレクトリをご確認ください。")

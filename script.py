import os, shutil

path = r"C:/Users\JoshuaDavids\Desktop"

file__name = os.listdir(path)

folder__names = ['Test', 'Test One', 'Test Two']

for loop in range(0,3):
    if not os.path.exists(path + folder__names[loop]):
        # print(path + folder__names[loop])
        os.makedirs(path + folder__names[loop])

for file in file__name:
    if ".csv" in file and not os.path.exists(path + "Test/" + file):
        shutil.move(path + file, path + "Test/" + file)
    if ".png" in file and not os.path.exists(path + "Test One/" + file):
        shutil.move(path + file, path + "Test One/" + file)
    if ".txt" in file and not os.path.exists(path + "Test Two/" + file):
        shutil.move(path + file, path + "Test Two/" + file)
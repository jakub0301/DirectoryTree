import os
from colorama import init
from termcolor import colored

path = os.getcwd()

main_folder = path.split("/")[len(path.split("/")) - 1]

#lista = os.listdir(path)

#isFile = os.path.isfile(path + "/" + lista[0])
#isDirectory = os.path.isdir(path + "/" + lista[0])
#print(lista)
#print(isFile)
#print(isDirectory)


def check_file(path, call):
    folders_and_files = os.listdir(path)
    for element in folders_and_files:
        if os.path.isfile(path + "/" + element):
            print(colored("- " * call + " " + element, 'blue'))
        else:
            print(colored("- " * call + " " + element, 'green'))
            check_file(path + "/" + element, call + 1)


print(colored(" " * 10 + main_folder + "\n", 'red'))
check_file(path, 1)




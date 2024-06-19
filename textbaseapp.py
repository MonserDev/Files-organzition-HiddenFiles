import fileorz
import hi_folder
import os
import subprocess
path = r"file_list.csv"
path_array = hi_folder.csv_reader(path)


def restart_explorer(): # restart explorer.exe
    try:
        # Kill the explorer process
        subprocess.run(["taskkill", "/f", "/im", "explorer.exe"], check=True)

        # Start the explorer process again
        subprocess.Popen(["explorer.exe"])

        print("Explorer restarted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


def main_interface():
    print("================================================================")
    print("\t Welcome to Application")
    key = input("\t Enter the key: ")
    print("================================================================")
    if key == "l111": #legacy
        subprocess.run("HideOnOff\OFF.bat")
        hi_folder.muti_hider_array(path_array,"-")
        

    elif key == "l0": #legacy
        subprocess.run("HideOnOff\ON.bat")
        hi_folder.muti_hider_array(path_array, "+")


    elif key == "2":
        file = hi_folder.csv_reader(path)
        i = 0
        for e in file:
            print(f"[{i}] {e[0]}")
            i+=1
        option = int(input("Section :"))
        os.startfile(file[option][0])


    elif key == "3":
        file = hi_folder.csv_reader(path)
        i = 0
        for e in file:
            print(f"[{i}] {e[0]}")
            i += 1
        option = int(input("Section :"))
        fileorz.packfile(file[option][0])

    elif key =="0": #currently
        subprocess.run("HideOnOff\ON.bat")
        hi_folder.muti_sortedhider(path_array, "+")
        restart_explorer()

    elif key =="111": #currently
        subprocess.run("HideOnOff\OFF.bat")
        restart_explorer()

    return key

if main_interface() == "-1":
    hi_folder.muti_hider(path,"-")



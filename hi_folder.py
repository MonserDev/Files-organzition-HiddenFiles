import os
import subprocess
import csv

def hider(path,commad):
    listfile = os.listdir(path)

    for file in listfile:
        if file == "fhder.lnk":
            continue
        if commad == "+":
            subprocess.run(["attrib", "+h", os.path.join(path,file)], shell=True, check=True)
        elif commad == "-":
            subprocess.run(["attrib", "-h", os.path.join(path, file)], shell=True, check=True)


def muti_hider(csvpath,commad):

    filelist = csv_reader(csvpath)

    for file in filelist:
        hider(file[0],commad) #[0] mean first column in that row.
    print("Successful")

def muti_hider_array(array,commad):
    for element in array:
        hider(element[0], commad)
    print("Successful")

def csv_reader(csvpath):

    list = []

    with open(csvpath, mode='r', newline='') as file:
        # Create a CSV reader
        csv_reader = csv.reader(file)
        next(csv_reader)
        # Iterate over each row in the CSV file

        for row in csv_reader:
            list.append(row)

    return list

def sorted_hider(path,command):
    import os, stat, subprocess

    # Specify the directory
    directory_path = path

    def has_hidden_attribute(filepath):
        return bool(os.stat(filepath).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)

    # Get a list of files in the directory
    files = os.listdir(directory_path)

    # # Filter out directories, we are only interested in files
    # files = [f for f in files if os.path.isfile(os.path.join(directory_path, f))]

    # Sort files by modification date
    sorted_files = sorted(files, key=lambda x: os.path.getmtime(os.path.join(directory_path, x)), reverse=True)

    # Print sorted files with their modification dates
    for file in sorted_files:
        if (command == "+"):
            if has_hidden_attribute(os.path.join(directory_path, file)) == False:
                subprocess.run(["attrib", "+h", os.path.join(directory_path, file)], shell=True, check=True)
        else:
            if has_hidden_attribute(os.path.join(directory_path, file)) == True:
                subprocess.run(["attrib", "-h", os.path.join(directory_path, file)], shell=True, check=True)

    print(path + "  **end**")
def muti_sortedhider(array,command):
    for element in array:
        sorted_hider(element[0], command)
    print("Successful")
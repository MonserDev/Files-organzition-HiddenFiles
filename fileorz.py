import os
import shutil
import hi_folder
format = {
    'png' : '!PNG_img',
    'PNG' : '!PNG_img',
    'jpg' : '!JPG_img',
    'pdf' : '!PDF_file',
    'psd' : '!Photo_shop',
    'other' : '!Other',
    'mp4' : '!MP4_vid',
    'mp3' : '!MP4_sound',
    'mov' : '!MP4_vid',
    'jfif' : '!JPG_img',
    'MOV' : '!MP4_vid',
    'GIF' : '!GIF_img',
    'jpeg' : '!JPG_img',
    'exe' : '!EXE_file',
    'zip' : '!Zip_file',
    'rar' : '!Zip_file',


}
path = r'C:\Users\Monser\Downloads'
dir = format["jpg"]

def packfile(path):
    file = os.listdir(path)
    for e in file:
        if "." in e and not "fhder.bat" in e:
            old_path = f'{path}\{e}'
            try:
                new_path = f'{path}\{format[e.split(".")[len(e.split("."))-1]]}'
            except:
                new_path = f'{path}\{format["other"]}'

            if os.path.exists(new_path) == False:
                os.mkdir(new_path)
            try:
                shutil.move(old_path,new_path)
            except Exception as e:
                try:
                    newname  = old_path+"(_1_)"
                    os.rename(old_path,newname)
                    shutil.move(newname, new_path)
                except Exception as r:
                    print(r)

def unpack_dir(path):
    file = os.listdir(f'{path}')
    new = str(path).split("\\")

    for e in file:
        old_path = path
        if dir != "Other":
            new_path = f'{path}\{format[e.split(".")[1]]}'
        else:
            new_path = f'{path}\{format["other"]}'
        shutil.move(f'{new_path}\{e}', old_path)
        #os.remove(new_path)

def onetimes_pack(path):
    file = os.listdir(path)
    for e in file:
         try:
             packfile(f"{path}\{e}")
         except IOError as r:
            print(r)
            return r

def hidden(path):
    file = os.listdir(path)

    for e in file:
        sw = False
        if e == "fhder.bat":
            continue

        for r in format:
            if e == format[r]:
                sw = True
        if sw:
            full_path = os.path.join(path, e)
            os.system(fr"attrib +h {full_path}")

def hidden_all(path):
    file = os.listdir(path)

    for e in file:
        if e == "fhder.bat":
            continue
        full_path = os.path.join(path,e)
        os.system(fr"attrib +h {full_path}")

def show(path):
    file = os.listdir(path)
    for e in file:
        full_path = os.path.join(path, e)
        os.system(fr"attrib -h {full_path}")






if __name__ == '__main__':
    pass








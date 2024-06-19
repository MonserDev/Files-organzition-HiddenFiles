import tkinter as tk

class App:

    def __init__(self,size,title):

        self.__size = size
        self.title = title


    def init_tk(self,size,title):

        root = tk.Tk()

        root.geometry(size)
        root.title(title)

        root.mainloop()

    def get_size(self):
        return self.__size

if __name__ == '__main__':
    pass


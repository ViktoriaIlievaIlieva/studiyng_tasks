# Използвай tkinter отвори прозорец за избиране на файл(file dialogue).
# След като е избран файл - принтирай го на конзолата. Бонус - ако файла е ограничен за избиране само с: .txt екстеншън

from tkinter import filedialog, Tk
from tkinter.messagebox import showinfo

# Hides the default window that tkinter creates
root = Tk()
root.withdraw()

filetypes = ('text files', '*.txt')
filename = filedialog.askopenfilename(filetypes=[filetypes])

file = open(filename, "r")
file_content = file.read()
file.close()
print(file_content)

showinfo(
        title='Selected File',
        message=filename
    )


# Done май


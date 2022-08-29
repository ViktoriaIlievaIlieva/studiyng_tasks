# ⦁	Старата библиотека
# Прибирайки се вкъщи, тя вижда старата библиотека на баба си и си спомня за любимата си книга.
# Помогнете на Ани, като напишете програма, в която тя въвежда търсената от нея книга (текст).
# Докато Ани не намери любимата си книга или не провери всички книги в библиотеката, програмата
# трябва да чете всеки път на нов ред името на всяка следваща книга (текст), която тя проверява. Книгите в библиотеката
# са свършили щом получите текст "No More Books".
# ⦁	Ако не открие търсената книгата да се отпечата на два реда:
# ⦁	"The book you search is not here!"
# ⦁	"You checked {брой} books."
# ⦁	Ако открие книгата си се отпечатва един ред:
# ⦁	"You checked {брой} books and found it."

favorite_book: str = input()


numbers_books: int = 0


book: str = input()
while book != "No More Books" and book != favorite_book:
    numbers_books += 1
    book: str = input()

if book == "No More Books":
    print("The book you search is not here!")
    print(f"You checked {numbers_books} books.")

elif book == favorite_book:
    print(f"You checked {numbers_books} books and found it.")

# DONE

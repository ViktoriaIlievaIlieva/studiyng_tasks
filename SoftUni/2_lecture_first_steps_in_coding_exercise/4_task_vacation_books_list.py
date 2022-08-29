# Задължителна литература
# За лятната ваканция в списъка със задължителна литература на Жоро има определен брой книги.
# Понеже Жоро предпочита да играе с приятели навън, вашата задача е да му помогнете да изчисли колко часа на ден трябва
# да отделя, за да прочете необходимата литература.
# Вход - От конзолата се четат 3 реда:
# Брой страници в текущата книга – цяло число в интервала [1…1000]
# Страници, които прочита за 1 час – цяло число в интервала [1…1000]
# Броят на дните, за които трябва да прочете книгата – цяло число в интервала [1…1000]
# Изход - Да се отпечата на конзолата броят часове, които Жоро трябва да отделя за четене всеки ден.
#212 страници / 20 страници за час = 10 часа общо


num_pages_from_current_book = int(input())
num_pages_for_1_hour = int(input())
num_days_for_book = int(input())

result = (num_pages_from_current_book // num_pages_for_1_hour) // num_days_for_book
print (result)

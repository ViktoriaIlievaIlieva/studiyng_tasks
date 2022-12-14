# Озеленяване на дворове - Божидара разполага с няколко къщи на Черноморието и желае да озелени дворовете на някои
# от тях, като по този начин създаде уютна обстановка и комфорт на гостите си. За целта е наела фирма.
# Напишете програма, която изчислява необходимате сума, които Божидара ще трябва да заплати на фирмата
# изпълнител на проекта. Цената на един кв. м. е 7.61 лв със ДДС. Понеже нейният двор е доста голям, фирмата изпълнител
# предлага 18% отстъпка от крайната цена.
# Вход
# От конзолата се прочита само един ред:
# Кв. метри, които ще бъдат озеленени – реално число в интервала [0.00 … 10000.00]
# Изход
# На конзолата се отпечатват два реда:
# "The final price is: {крайна цена на услугата} lv."
# "The discount is: {отстъпка} lv."

square_meters = float (input())
price_for_square_meters = 7.61

whole_price = square_meters * price_for_square_meters
discount = whole_price / 100 * 18
final_price = whole_price - discount

print (f"The final price is: {final_price} lv.")
print (f"The discount is: {discount} lv.")

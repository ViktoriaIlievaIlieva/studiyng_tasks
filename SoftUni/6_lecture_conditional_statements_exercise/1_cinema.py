# ⦁	Кино
# В една кинозала столовете са наредени в правоъгълна форма в r реда и c колони. Има три вида прожекции с билети на
# различни цени:
# ⦁	Premiere - премиерна прожекция, на цена 12.00 лева;
# ⦁	Normal - стандартна прожекция, на цена 7.50 лева;
# ⦁	Discount - прожекция за деца, ученици и студенти на намалена цена от 5.00 лева.
# Напишете програма, която чете тип прожекция (текст), брой редове и брой колони в залата (цели числа), въведени от
# потребителя, и изчислява общите приходи от билети при пълна зала. Резултатът да се отпечата във формат 2 знака след
# десетичната точка.

projection: str = input()
r: int = int(input())
c: int = int(input())

seats: int = r * c

if projection == "Premiere":
    seats *= 12
elif projection == "Normal":
    seats *= 7.50
elif projection == "Discount":
    seats *= 5

print(f"{seats:.2f}")

# DONE

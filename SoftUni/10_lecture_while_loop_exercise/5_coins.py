# ⦁	Монети
# Производителите на вендинг машини искали да направят машините си да връщат възможно най-малко монети ресто.
# Напишете програма, която приема сума - рестото, което трябва да се върне и изчислява с колко най-малко монети може
# да стане това.

change: float = float(input())

two_lv: int = 200
one_lv: int = 100
fifty_st: int = 50
twenty_st: int = 20
ten_st: int = 10
five_st: int = 5
two_st: int = 2
one_st: int = 1
coins: int = 0

change *= 100

while change > 0:
    if change >= two_lv:
        change -= two_lv
        coins += 1

    elif change >= one_lv:
        change -= one_lv
        coins += 1

    elif change >= fifty_st:
        change -= fifty_st
        coins += 1

    elif change >= twenty_st:
        change -= twenty_st
        coins += 1

    elif change >= ten_st:
        change -= ten_st
        coins += 1

    elif change >= five_st:
        change -= five_st
        coins += 1

    elif change >= two_st:
        change -= two_st
        coins += 1

    elif change >= one_st:
        change -= one_st
        coins += 1

print(coins)

# -------------------------


change: float = float(input())

two_lv: int = 200
one_lv: int = 100
fifty_st: int = 50
twenty_st: int = 20
ten_st: int = 10
five_st: int = 5
two_st: int = 2
one_st: int = 1
coins: int = 0

change *= 100

if change >= two_lv:
    count = change // two_lv
    change -= count * two_lv
    coins += count

if change >= one_lv:
    count = change // one_lv
    change -= count * one_lv
    coins += count

if change >= fifty_st:
    count = change // fifty_st
    change -= count * fifty_st
    coins += count

if change >= twenty_st:
    count = change // twenty_st
    change -= count * twenty_st
    coins += count

if change >= ten_st:
    count = change // ten_st
    change -= count * ten_st
    coins += count

if change >= five_st:
    count = change // five_st
    change -= count * five_st
    coins += count

if change >= two_st:
    count = change // two_st
    change -= count * two_st
    coins += count

if change >= one_st:
    count = change // one_st
    change -= count * one_st
    coins += count

print(f"{coins:.0f}")



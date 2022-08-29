# ⦁	Търговски комисионни
# Фирма дава следните комисионни на търговците си според града, в който работят и обема на продажбите:

# Град	0 ≤ s ≤ 500     	500 < s ≤ 1 000	    1 000 < s ≤ 10 000	    s > 10 000
# Sofia	    5%	                7%	                8%	                    12%
# Varna	    4.5%	            7.5%	            10%	                    13%
# Plovdiv	5.5%	            8%	                12%	                    14.5%

# Напишете конзолна програма, която чете име на град (текст) и обем на продажби (реално число), въведени от потребителя,
# и изчислява и извежда размера на търговската комисионна според горната таблица. Резултатът да се изведе форматиран до
# 2 цифри след десетичната точка. При невалиден град или обем на продажбите (отрицателно число) да се отпечата "error".

city: str = input()
sales: float = float(input())
earnings: float = 0

if city == "Sofia":
    if 0 <= sales <= 500:
        earnings = sales * 0.05
    elif 500 <= sales <= 1000:
        earnings = sales * 0.07
    elif 1000 <= sales <= 10000:
        earnings = sales * 0.08
    elif sales > 10000:
        earnings = sales * 0.12

elif city == "Varna":
    if 0 <= sales <= 500:
        earnings = sales * 0.045
    elif 500 <= sales <= 1000:
        earnings = sales * 0.075
    elif 1000 <= sales <= 10000:
        earnings = sales * 0.1
    elif sales > 10000:
        earnings = sales * 0.13

elif city == "Plovdiv":
    if 0 <= sales <= 500:
        earnings = sales * 0.055
    elif 500 <= sales <= 1000:
        earnings = sales * 0.08
    elif 1000 <= sales <= 10000:
        earnings = sales * 0.12
    elif sales > 10000:
        earnings = sales * 0.145

if (city != "Sofia" and city != "Varna" and city != "Plovdiv") or sales < 0:
    print("error")
else:
    print(f"{earnings:.2f}")

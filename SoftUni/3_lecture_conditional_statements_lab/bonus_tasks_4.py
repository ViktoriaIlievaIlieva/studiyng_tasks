# Цена за транспорт
# Студент трябва да пропътува n километра. Той има избор измежду три вида транспорт:
# Такси. Начална такса: 0.70 лв. Дневна тарифа: 0.79 лв. / км. Нощна тарифа: 0.90 лв. / км.
# Автобус. Дневна / нощна тарифа: 0.09 лв. / км. Може да се използва за разстояния минимум 20 км.
# Влак. Дневна / нощна тарифа: 0.06 лв. / км. Може да се използва за разстояния минимум 100 км.
# Напишете програма, която въвежда броя километри n и период от деня (ден или нощ) и изчислява цената на най-евтиния транспорт.
# Вход
# От конзолата се четат два реда:
# Първият ред съдържа числото n – брой километри – цяло число в интервала [1…5000]
# Вторият ред съдържа дума “day” или “night” – пътуване през деня или през нощта
# Изход
# Да се отпечата на конзолата най-ниската цена за посочения брой километри, форматирана до втория знак след десетичния разделител.

taxi_initial_tax: float = 0.70
taxi_day_tariff_for_km: float = 0.79
taxi_night_tariff_for_km: float = 0.90

bus_tariff_for_km: float = 0.09

train_tariff_for_km: float = 0.06

n_kilometers: int = int(input())
part_of_day: str = input()

taxi_price = taxi_initial_tax + (taxi_day_tariff_for_km if part_of_day == "day" else taxi_night_tariff_for_km) * n_kilometers
taxi_price_day = taxi_initial_tax + taxi_day_tariff_for_km*n_kilometers
taxi_price_night = taxi_initial_tax + taxi_night_tariff_for_km * n_kilometers

bus_price = bus_tariff_for_km * n_kilometers

train_price = train_tariff_for_km * n_kilometers

if part_of_day == "day":
    if n_kilometers < 20:
        print(f"{taxi_price_day:.2f}")

    elif 20 <= n_kilometers < 100:
        if bus_price < taxi_price_day:
            print(f"{bus_price:.2f}")
        else:
            print(f"{taxi_price_day:.2f}")

    elif n_kilometers >= 100:
        if taxi_price_day < bus_price and taxi_price_day < train_price:
            print(f"{taxi_price_day:.2f}")
        elif bus_price < taxi_price_day and bus_price < train_price:
            print(f"{bus_price:.2f}")
        elif train_price < bus_price and train_price < taxi_price_day:
            print(f"{train_price:.2f}")

elif part_of_day == "night":
    if n_kilometers < 20:
        print(f"{taxi_price_night:.2f}")

    elif 20 <= n_kilometers < 100:
        if bus_price < taxi_price_night:
            print(f"{bus_price:.2f}")
        else:
            print(f"{taxi_price_night:.2f}")

    elif n_kilometers >= 100:
        if taxi_price_night < bus_price and taxi_price_night < train_price:
            print(f"{taxi_price_night:.2f}")
        elif bus_price < taxi_price_night and bus_price < train_price:
            print(f"{bus_price:.2f}")
        elif train_price < bus_price and train_price < taxi_price_night:
            print(f"{train_price:.2f}")

# --------------------------------------------------------------------------------

taxi_initial_tax: float = 0.70
taxi_day_tariff_for_km: float = 0.79
taxi_night_tariff_for_km: float = 0.90

bus_tariff_for_km: float = 0.09

train_tariff_for_km: float = 0.06

n_kilometers: int = int(input())
part_of_day: str = input()

taxi_tariff = taxi_day_tariff_for_km if part_of_day == "day" else taxi_night_tariff_for_km
taxi_price = taxi_initial_tax + taxi_tariff * n_kilometers


bus_price = bus_tariff_for_km * n_kilometers

train_price = train_tariff_for_km * n_kilometers


if n_kilometers < 20:
    print(f"{taxi_price:.2f}")

elif 20 <= n_kilometers < 100:
    if bus_price < taxi_price:
        print(f"{bus_price:.2f}")
    else:
        print(f"{taxi_price:.2f}")

elif n_kilometers >= 100:
    if taxi_price < bus_price and taxi_price < train_price:
        print(f"{taxi_price:.2f}")
    elif bus_price < taxi_price and bus_price < train_price:
        print(f"{bus_price:.2f}")
    elif train_price < bus_price and train_price < taxi_price:
        print(f"{train_price:.2f}")



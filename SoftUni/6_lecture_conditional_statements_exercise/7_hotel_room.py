# ⦁	Хотелска стая
# Хотел предлага 2 вида стаи: студио и апартамент. Напишете програма, която изчислява цената за целия престой за студио
# и апартамент. Цените зависят от месеца на престоя:

# Май и октомври	            Юни и септември	                    Юли и август
# Студио - 50 лв./нощувка	    Студио - 75.20 лв./нощувка	        Студио - 76 лв./нощувка
# Апартамент - 65 лв./нощувка	Апартамент - 68.70 лв./нощувка	    Апартамент - 77 лв./нощувка


# Предлагат се и следните отстъпки:
# ⦁	За студио, при повече от 7 нощувки през май и октомври : 5% намаление.
# ⦁	За студио, при повече от 14 нощувки през май и октомври : 30% намаление.
# ⦁	За студио, при повече от 14 нощувки през юни и септември: 20% намаление.
# ⦁	За апартамент, при повече от 14 нощувки, без значение от месеца : 10% намаление.


month: str = input()
nights: int = int(input())
price_studio: float = 0
price_apartment: float = 0


if month == "May" or month == "October":
    studio = 50
    apartment = 65

    price_studio: float = studio * nights
    price_apartment: float = apartment * nights

    if 7 < nights < 14:
        price_studio -= price_studio * 0.05
    elif nights > 14:
        price_studio -= price_studio * 0.30
        price_apartment -= price_apartment * 0.10

elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70

    price_studio: float = studio * nights
    price_apartment: float = apartment * nights

    if nights > 14:
        price_studio -= price_studio * 0.20
        price_apartment -= price_apartment * 0.10

elif month == "July" or month == "August":
    studio = 76
    apartment = 77

    price_studio: float = studio * nights
    price_apartment: float = apartment * nights

    if nights > 14:
        price_apartment -= price_apartment * 0.10

print(f"Apartment: {price_apartment:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")

# DONE

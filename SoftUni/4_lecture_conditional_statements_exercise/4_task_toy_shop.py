# ⦁	Магазин за детски играчки
# Петя има магазин за детски играчки. Тя получава голяма поръчка, която трябва да изпълни. С парите, които ще
# спечели иска да отиде на екскурзия.
# Цени на играчките:
# ⦁	Пъзел - 2.60 лв.
# ⦁	Говореща кукла - 3 лв.
# ⦁	Плюшено мече - 4.10 лв.
# ⦁	Миньон - 8.20 лв.
# ⦁	Камионче - 2 лв.
#
# Вход
# От конзолата се четат 6 реда:
# ⦁	Цена на екскурзията - реално число в интервала [1.00 … 10000.00]
# ⦁	Брой пъзели - цяло число в интервала [0… 1000]
# ⦁	Брой говорещи кукли - цяло число в интервала [0 … 1000]
# ⦁	Брой плюшени мечета - цяло число в интервала [0 … 1000]
# ⦁	Брой миньони - цяло число в интервала [0 … 1000]
# ⦁	Брой камиончета - цяло число в интервала [0 … 1000]
# Изход
# На конзолата се отпечатва:
# ⦁	Ако парите са достатъчни се отпечатва:
# ⦁	"Yes! {оставащите пари} lv left."
# ⦁	Ако парите НЕ са достатъчни се отпечатва:
# ⦁	"Not enough money! {недостигащите пари} lv needed."
#
# Резултатът трябва да се форматира до втория знак след десетичната запетая.

# Ако поръчаните играчки са 50 или повече магазинът прави отстъпка 25% от общата цена. От спечелените пари Петя трябва
# да даде 10% за наема на магазина. Да се пресметне дали парите ще ѝ стигнат да отиде на екскурзия.

puzzel: float = 2.60
talk_doll: int = 3
teddy_bear: float = 4.10
minion: float = 8.20
truck: int = 2

trip_price: float = float(input())
num_puzzels: int = int(input())
num_talk_dolls: int = int(input())
num_bears: int = int(input())
num_minions: int = int(input())
num_trucks: int = int(input())

number_toys: float = num_puzzels + num_talk_dolls + num_bears + num_minions + num_trucks
earnings: float = num_puzzels * puzzel + num_talk_dolls * talk_doll + num_bears * teddy_bear + num_minions * minion \
          + num_trucks * truck

if number_toys >= 50:
    earnings -= (earnings / 100) * 25

final_earnings: float = earnings - (earnings / 100) * 10

dif: float = abs(final_earnings - trip_price)

if final_earnings >= trip_price:
    print(f"Yes! {dif:.2f} lv left.")

else:
    print(f"Not enough money! {dif:.2f} lv needed.")

# DONE

# ⦁	Торта
# Поканени сте на 30-ти рожден ден, на който рожденикът черпи с огромна торта.
# Той обаче не знае колко парчета могат да си вземат гостите от нея.
# Вашата задача е да напишете програма, която изчислява броя на парчетата, които гостите са взели преди тя да свърши.
# Ще получите размерите на тортата (широчина и дължина – цели числа и след това на всеки ред, до получаване на
# командата "STOP" или докато не свърши тортата, броят на парчетата, които гостите вземат от нея.
# Всяко парче торта е с размер 1х1 см.
# Да се отпечата на конзолата един от следните редове:
# ⦁	"{брой парчета} pieces are left." - ако стигнете до STOP и не са свършили парчетата торта;
# ⦁	"No more cake left! You need {брой недостигащи парчета} pieces more."


cake_height: int = int(input())
cake_width: int = int(input())

cake_size: int = cake_width * cake_height
num_pieces: float = cake_size
num_eaten_pieces: int = 0

num_parts: str = input()
while num_parts != "STOP":
    num_eaten_pieces += int(num_parts)
    if num_eaten_pieces < num_pieces:
        num_parts: str = input()
    else:
        break

diff: float = abs(num_pieces - num_eaten_pieces)

if num_eaten_pieces >= num_pieces:
    print(f"No more cake left! You need {diff} pieces more.")
elif num_parts == "STOP":
    print(f"{diff} pieces are left.")

# DONE

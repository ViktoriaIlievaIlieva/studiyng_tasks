# Тръби в басейн
# Басейн с обем V има две тръби от които се пълни. Всяка тръба има определен дебит (литрите вода минаващи през една
# тръба за един час). Работникът пуска тръбите едновременно и излиза за N часа. Напишете програма, която изкарва
# състоянието на басейна, в момента, когато работникът се върне.
# Вход
# От конзолата се четат четири реда:
# Първият ред съдържа числото V – Обем на басейна в литри – цяло число в интервала [1…10000].
# Вторият ред съдържа числото P1 – дебит на първата тръба за час – цяло число в интервала [1…5000].
# Третият ред съдържа числото P2 – дебит на втората тръба за час– цяло число в интервала [1…5000].
# Четвъртият ред съдържа числото H – часовете които работникът отсъства – реално число в интервала [1.0…24.00]
# Изход
# Да се отпечата на конзолата едно от двете възможни състояния:
# До колко се е запълнил басейна и коя тръба с колко процента е допринесла.
# "The pool is {запълненост на басейна в проценти}% full. Pipe 1: {процент вода от първата тръба}%. Pipe 2: {процент
# вода от втората тръба}%."
# Aко басейнът се е препълнил – с колко литра е прелял за даденото време.
# "For {часовете, които тръбите са пълнили вода} hours the pool overflows with {литрите вода в повече} liters."

v: int = int(input())
pipe_1_liters_per_h: int = int(input())
pipe_2_liters_per_h: int = int(input())
hours: float = float(input())

water_from_pipe_1: float = pipe_1_liters_per_h * hours
water_from_pipe_2: float = pipe_2_liters_per_h * hours

all_the_water = (pipe_2_liters_per_h + pipe_1_liters_per_h) * hours

pool_percent: float = (all_the_water / v) * 100

pipe_1_percent: float = (water_from_pipe_1 / all_the_water) * 100
pipe_2_percent: float = (water_from_pipe_2 / all_the_water) * 100

overflow: float = all_the_water - v

if all_the_water <= v:
    print(f"The pool is {pool_percent}% full. Pipe 1: {pipe_1_percent}%. Pipe 2: {pipe_2_percent}%.")

else:
    print(f"For {hours} hours the pool overflows with {overflow} liters.")

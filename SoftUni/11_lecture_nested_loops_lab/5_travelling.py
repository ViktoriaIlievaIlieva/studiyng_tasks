# ⦁	Пътуване
# Ани обича да пътува и иска тази година да посети няколко различни дестинации.
# Като си избере дестинация, ще прецени колко пари ще й трябват, за да отиде до там, и ще започне да спестява.
# Когато е спестила достатъчно, ще може да пътува.
# От конзолата всеки път ще се четат първо дестинацията и минималния бюджет (десетично число), който ще е нужен
# за пътуването.
# След това ще се четат няколко суми (десетични числа), които Ани спестява като работи и когато успее да събере
# достатъчно за пътуването, ще заминава, като на конзолата трябва да се изпише: "Going to {дестинацията}!"
# Когато е посетила всички дестинации, които иска, вместо дестинация ще въведе "End" и програмата ще приключи.

destination: str = input()
while destination != "End":
    budget: float = float(input())
    saved_money: float = 0
    while saved_money < budget:
        suma: float = float(input())
        saved_money += suma
    print(f"Going to {destination}!")
    destination: str = input()

# DONE

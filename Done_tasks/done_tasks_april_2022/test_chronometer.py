from thefuzz import fuzz

viki_loves_ico: bool = True
while viki_loves_ico:
    feelings: str = input("Insert feelings and wishes: ")
    if fuzz.ratio(feelings, "dead") >= 50:
        print("Together in the after world!")
        viki_loves_ico = False
    else:
        for _ in range(1, 20):
            print("Love forever!")


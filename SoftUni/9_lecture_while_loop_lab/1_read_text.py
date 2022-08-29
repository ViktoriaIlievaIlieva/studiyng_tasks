# ⦁	Четене на думи
# Напишете програма, която чете текст от конзолата(стринг) и го принтира, докато не получи командата "Stop".

go: bool = True
while go:
    word: str = input()
    if word != "Stop":
        print(word)
    else:
        go = False

# 2nd option ------------------------

word: str = input()
while word != "Stop":
    print(word)
    word: str = input()

# DONE

# Напишете програма, която чете градуси по скалата на Целзий (°C) и ги преобразува до градуси по скалата на Фаренхайт (°F).
# Потърсете в Интернет подходяща формула, с която да извършите изчисленията.
# Форматирате изхода до втория знак след десетичната запетая.
# The Formula for the conversion is degrees Celsius times 9 divided by 5 plus 32.


celsius = float (input ())
fahrenheit = celsius * 9 / 5 + 32

print (format (fahrenheit, ".2f"))

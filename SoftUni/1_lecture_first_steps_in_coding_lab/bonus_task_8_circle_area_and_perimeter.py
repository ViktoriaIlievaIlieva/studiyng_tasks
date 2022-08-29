# ⦁	Периметър и лице на кръг
# Напишете програма, която чете от конзолата число r и пресмята и отпечатва лицето и периметъра на кръг / окръжност
# с радиус r, като форматирате изхода в следния вид: "<calculated area>"
# "<calculated parameter>". Форматирайте изходните данни до втория знак след десетичната запетая.

import math

r = float (input ())

perimeter = (2 * math.pi * r)
area = math.pi * r * r


print (format (area, ".2f" ))
print (format (perimeter, ".2f"))


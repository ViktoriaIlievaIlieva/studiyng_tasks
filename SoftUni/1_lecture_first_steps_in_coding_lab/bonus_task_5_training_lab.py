# Учебна зала има правоъгълен размер w на h метра, без колони във вътрешността си. Залата е разделена на две части – лява и дясна,
# с коридор приблизително по средата. В лявата и в дясната част има редици с бюра. В задната част на залата има голяма входна врата.
# В предната част на залата има катедра с подиум за преподавателя. Едно работно място заема 70 на 120 cm
# (маса с размер 70 на 40 cm + място за стол ипреминаване с размер 70 на 80 cm). Коридорът е широк поне 100 cm.
# Изчислено е, че заради входната врата (която е с отвор 160 cm) се губи точно 1 работно място, а заради катедрата
# (която е с размер 160 на 120 cm) се губят точно 2 работни места. Напишете програма, която въвежда размери на
# учебната зала и изчислява броя работни места в нея при описаното

h = float(input())
w = float(input())

width_space  = (w * 100) - 100
height_space = h * 100

amount_desks_width = width_space // 70
amount_desks_height = height_space // 120

total_seats = (amount_desks_height * amount_desks_width) - 3

format_seats = int(total_seats)

print(format_seats)

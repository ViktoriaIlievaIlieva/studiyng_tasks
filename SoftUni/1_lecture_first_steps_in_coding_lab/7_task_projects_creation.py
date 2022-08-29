#⦁	Изготвяне на проекти
# Напишете програма, която изчислява колко часа ще са необходими на един архитект, за да изготви проектите на няколко
# строителни обекта. Изготвянето на един проект отнема три часа.
# Вход - От конзолата се четат 2 реда:
# Името на архитекта - текст
# Брой на проектите, които трябва да изготви - цяло число в интервала [0 … 100]
# Изход - На конзолата се отпечатва:
# #"The architect {името на архитекта} will need {необходими часове} hours to complete {брой на проектите} project/s."

name_of_architect = input()
number_of_projects = int(input ())
hours_to_finish = number_of_projects * 3

print (f"The architect {name_of_architect} will need {hours_to_finish} hours to complete {number_of_projects} project/s.")

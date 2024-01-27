print("\n==================")
print("-Розрахунок дітей в класі відсотками-")
print("==================")
girls = input ("Введіть кількість дівчат в класі")
boys = input  ("Введіть кількість хлопців в класі")
current_children = int(girls) + int(boys)
number_girls = int(girls) * 100 / int(current_children)
number_boys = int(boys) * 100 / int(current_children)
print(f" Дівчат: {number_girls}% Хлопців: {number_boys}% ")


print('Кінець програми', end="\n\n")
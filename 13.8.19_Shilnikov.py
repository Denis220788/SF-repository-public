t = int(input("Введите количество билетов: "))
tot_coast = 0
list_pos = [int(input("Укажите возраст посетителя ")) for i in range(1, t+1)]
for m in range (t):
    if list_pos[m] > 25:
        tot_coast += 1390
    elif 18 <= list_pos[m] <= 25:
        tot_coast += 990
if t >= 3:
    tot_coast = tot_coast * 0.9
print("Сумма к оплате: ", tot_coast, "руб.")
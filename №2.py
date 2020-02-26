second_user = int(input("Введите число , которое хотите конвертировать: "))
second = int(second_user % 60)
minute = int((second_user % 3600) / 60)
hour = int(second_user / 3600)
print("{} ч {} м {} с" .format(hour, minute, second))



while True:
    name, age, weight = input().split()
    if name == '#' and age == weight == "0":
        break
    elif int(age) > 17 or int(weight) >= 80:
        print(name, "Senior")
    else:
        print(name, "Junior")
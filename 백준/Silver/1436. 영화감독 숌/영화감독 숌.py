def get_movie_num(n):
    if n == 1:
        return "666"
    left_num = 0
    right_num = 0
    for _ in range(n - 1):
        if str(left_num)[-1] in ["5", "6"]:
            if str(left_num)[-1] == "5":
                left_num += 1
                if left_num >= 10 and str(left_num)[-2] == "6":
                    if left_num >= 100 and str(left_num)[-3] == "6":
                        movie_num = str(left_num)[:-3] + "666" + str(right_num).zfill(3)
                    else:
                        movie_num = str(left_num)[:-2] + "666" + str(right_num).zfill(2)
                else:
                    movie_num = str(left_num)[:-1] + "666" + str(right_num)
            else:
                if (str(left_num).zfill(3)[-2] != "6" and right_num == 9) \
                    or (str(left_num).zfill(3)[-2] == "6" and str(left_num).zfill(3)[-3] != "6" and right_num == 99) \
                    or str(left_num).zfill(3)[-3:] == "666" and right_num == 999:
                    right_num = 0
                    left_num += 1
                    movie_num = str(left_num) + "666"
                else:
                    if (left_num >= 100 and str(left_num)[-3:] == "666"):
                        right_num += 1
                        movie_num = str(left_num)[:-3] + "666" + str(right_num).zfill(3)
                    elif (left_num >= 10 and str(left_num)[-2] == "6"):
                        right_num += 1
                        movie_num = str(left_num)[:-2] + "666" + str(right_num).zfill(2)
                    else:
                        right_num += 1
                        movie_num = str(left_num)[:-1] + "666" + str(right_num)
        else:
            left_num += 1
            movie_num = str(left_num) + "666"
    return movie_num

n = int(input())
print(get_movie_num(n))
width_computer, heigth_computer, width_sticker, heigth_sticker = map(int, input().split())
if width_computer >= width_sticker + 2 \
    and heigth_computer >= heigth_sticker + 2:
    print(1)
else:
    print(0)
wavelength = int(input())
if wavelength >= 380 and wavelength < 425:
    print("Violet")
elif wavelength >= 425 and wavelength < 450:
    print('Indigo')
elif wavelength >= 450 and wavelength < 495:
    print('Blue')
elif wavelength >= 495 and wavelength < 570:
    print('Green')
elif wavelength >= 570 and wavelength < 590:
    print('Yellow')
elif wavelength >= 590 and wavelength < 620:
    print('Orange')
elif wavelength >= 620 and wavelength <= 780:
    print('Red')
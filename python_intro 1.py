print ('podaj głośność:')
volume = int(input())
if volume < 20:
    print("Prawie nic nie slychac.")
elif 20 <= volume < 40:
    print("O, muzyka leci w tle.")
elif 40 <= volume < 60:
    print("Idealnie, moge uslyszec wszystkie detale")
elif 60 <= volume < 80:
    print("Dobre na imprezy")
elif 80 <= volume < 100:
    print("Troszeczke za glosno!")
else:
    print("Ojoj! Moje uszy! :(")

from enemy import Enemy, Troll, Vampyre, VampyreKing

dracula = VampyreKing("Dracula")
print(dracula)
dracula.take_damage(12)
print(dracula)


ugly_troll = Troll("Yash")
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Bernard")
print("Another troll - {}".format(another_troll))
another_troll.take_damage(18)
print(another_troll)

brother = Troll("Adhokshaj")
print(brother)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

vamp = Vampyre("Vlad")
print(vamp)
vamp.take_damage(5)
print(vamp)

print("-" * 40)
another_troll.take_damage(30)
print(another_troll)


vamp._lives = 0
vamp._hit_points = 1
print(vamp)

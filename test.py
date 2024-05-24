from PIL import Image
zoo = ["Pig", "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Sheep", "Monkey", "Rooster", "Dog"]


icons = []
for animal in zoo:
    icons.append(Image.open("img/" + animal + ".png"))

print(len(zoo))

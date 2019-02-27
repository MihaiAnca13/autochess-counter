import pytesseract
import cv2
import csv

y = 350
h = 100
x = 350
w = 1350


class Hero:
    def __init__(self, n, s, c, g):
        self.name = n.replace(' ', '')
        self.species = []
        self.classes = []
        self.count = 0
        for i in s.split('/'):
            self.species.append(i)
        for i in c.split('/'):
            self.classes.append(i)
        self.cost = int(g)


heroes = []
with open('data.csv') as f:
    csv_data = csv.reader(f)
    for r in csv_data:
        heroes.append(Hero(r[0], r[1], r[2], r[3]))

hero_names = [her.name for her in heroes]

img = cv2.imread('test3.jpg')
img = img[y:y + h, x:x + w]

img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

cv2.imwrite('temp.jpg', img)

boxes = pytesseract.image_to_boxes(img)

word = ''
for b in boxes.splitlines():
    if b[0].isalpha():
        word += b[0]
    if word in hero_names:
        for hero in heroes:
            if hero.name == word:
                hero.count += 1
                break
        word = ''

for hero in heroes:
    if hero.count > 0:
        print(hero.name+' '+' '.join(hero.species)+' '+' '.join(hero.classes))
# cv2.imshow('output',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

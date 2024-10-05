# a.  try ו-except -  דרך לטיפול בשגיאות, בחריגים
# b.  כדאי לתפוס את השגיאות בפייתון מכיוון שזה מונע מהתוכנית לקרוס ובעצם ככה ניתן להציל את התוכנית מלהתפוצץ

# c.
# start

x: int = None
try:
    x = int(input('enter a number:'))
    if 88 / 0:
        print('error')
except:
    print('the number cannot divide by zero')
print('try again')

# stop

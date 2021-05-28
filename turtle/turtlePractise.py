from turtle import Turtle, Screen

'''Drawing a square'''
cursor = Turtle()
my_screen = Screen()
cursor.speed(1)
cursor.pos()
cursor.pen(fillcolor="red",pensize=10,pencolor="black")
for i in range(4):
    cursor.fd(100)
    cursor.rt(90)
    

#undoing square
for _ in range(8):
    cursor.undo()

cursor.shapesize(2,3,1)
#drawing circle
cursor.circle(90)
cursor.undo()
 
cursor.shapesize(3,4,2)
'''heroes is the package that contains all superheroes name in the module by using heroes.gen()'''

# my_screen.clear() 
for i in range(4):
    for _ in range(10):
        if cursor.isdown():
            cursor.up()
        else:
            cursor.down()
        cursor.fd(40)
        
    for _ in range(20):
        cursor.undo()
    cursor.rt(90)
    

my_screen.exitonclick()

#dashed line





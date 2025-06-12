import turtle

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("white")

# Create turtle
smiley = turtle.Turtle()
smiley.speed(5)

# Draw face
smiley.penup()
smiley.goto(0, -150)
smiley.pendown()
smiley.circle(150)

# Draw left eye
smiley.penup()
smiley.goto(-70, 50)
smiley.pendown()
smiley.circle(20)

# Draw right eye
smiley.penup()
smiley.goto(70, 50)
smiley.pendown()
smiley.circle(20)

# Draw smile
smiley.penup()
smiley.goto(-70, -30)
smiley.pendown()
smiley.setheading(-60)
smiley.circle(80, 120)

# Hide turtle
smiley.hideturtle()

# Keep the window open
wn.mainloop()

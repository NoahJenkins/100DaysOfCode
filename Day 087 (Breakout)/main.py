import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Breakout")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Create the paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Create the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

# Create bricks
bricks = []
brick_colors = ["red", "orange", "yellow", "green", "blue"]

for y in range(5):
    for x in range(-7, 8):
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(brick_colors[y // 1])
        brick.shapesize(stretch_wid=1, stretch_len=2)
        brick.penup()
        brick.goto(100 * x, 180 - 25 * y)
        bricks.append(brick)

# Function to move the paddle left
def move_left():
    x = paddle.xcor()
    x -= 20  # Adjust the movement speed here
    if x < -380:  # Adjust the left boundary if needed
        x = -380
    paddle.setx(x)

# Function to move the paddle right
def move_right():
    x = paddle.xcor()
    x += 20  # Adjust the movement speed here
    if x > 380:  # Adjust the right boundary if needed
        x = 380
    paddle.setx(x)

# Keyboard bindings
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Main game loop
while True:
    screen.update()

    # Remove the line that moves the paddle automatically
    # paddle.setx(paddle.xcor() + 0.2)

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for collision with the paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -240:
        ball.dy *= -1

    # Check for collision with the walls
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.dx *= -1
    if ball.ycor() > 290:
        ball.dy *= -1

    # Check for collision with the bricks
    for brick in bricks:
        if ball.distance(brick) < 20:
            ball.dy *= -1
            bricks.remove(brick)
            brick.hideturtle()

    # Check for game over
    if ball.ycor() < -290:
        # Reset the ball position
        ball.goto(0, 0)
        ball.dy *= -1

    # Check for game win
    if len(bricks) == 0:
        # Display win message
        win_message = turtle.Turtle()
        win_message.color("white")
        win_message.penup()
        win_message.goto(0, 0)
        win_message.write("You Win!", align="center", font=("Courier", 24, "normal"))

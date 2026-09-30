
import turtle
import random


# 1. CREATE GAME WINDOW

screen = turtle.Screen()
screen.title("Flappy Bird - Python Project")
screen.bgcolor("skyblue")
screen.setup(width=800, height=600)
screen.tracer(0)

# 2. CREATE THE BIRD 


bird = turtle.Turtle()
bird.shape("circle")
bird.color("yellow")
bird.penup()
bird.goto(-200, 0)

bird.dy = 0


# 3. CREATE THE PIPES

pipe_top = turtle.Turtle()
pipe_top.shape("square")
pipe_top.color("green")
pipe_top.shapesize(stretch_wid=10, stretch_len=2)
pipe_top.penup()

pipe_bottom = turtle.Turtle()
pipe_bottom.shape("square")
pipe_bottom.color("green")
pipe_bottom.shapesize(stretch_wid=10, stretch_len=2)
pipe_bottom.penup()

pipe_x = 350
gap_y = random.randint(-50, 150)

pipe_top.goto(pipe_x, gap_y + 250)
pipe_bottom.goto(pipe_x, gap_y - 250)



# 4. SCORE

score = 0

score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.color("black")
score_writer.penup()
score_writer.goto(0, 240)

score_writer.write(
    "Score: 0",
    align="center",
    font=("Arial", 24, "bold")
)


# 5. GAME OVER TEXT

game_over = turtle.Turtle()
game_over.hideturtle()
game_over.color("red")
game_over.penup()
game_over.goto(0, 0)


# 6. BIRD JUMP FUNCTION

def jump():
    bird.dy = 8


# Press SPACE to make the bird jump
screen.listen()
screen.onkeypress(jump, "space")


# 7. RESET PIPE

def reset_pipe():

    global pipe_x
    global gap_y

    pipe_x = 350
    gap_y = random.randint(-80, 120)

    pipe_top.goto(pipe_x, gap_y + 250)
    pipe_bottom.goto(pipe_x, gap_y - 250)


# 8. COLLISION FUNCTION

def collision():

    # Collision with top pipe
    if bird.distance(pipe_top) < 60:
        return True

    # Collision with bottom pipe
    if bird.distance(pipe_bottom) < 60:
        return True

    # Collision with ground
    if bird.ycor() < -280:
        return True

    # Collision with ceiling
    if bird.ycor() > 280:
        return True

    return False


# 9. GAME VARIABLES

game_running = True
pipe_passed = False


# 10. This keeps the game running until the bird hits something

while game_running:

    # Bird gravity

    bird.dy -= 0.5

    bird.sety(bird.ycor() + bird.dy)


    # Move pipes

    pipe_x -= 3

    pipe_top.setx(pipe_x)
    pipe_bottom.setx(pipe_x)


    # Check if pipe passed

    if pipe_x < -250 and not pipe_passed:

        score += 1
        pipe_passed = True

        score_writer.clear()

        score_writer.write( 
        "Score: " + str(score),
            align="center",
            font=("Arial", 24, "bold"))
    
    # Create new pipe
    

    if pipe_x < -450:

        reset_pipe()
        pipe_passed = False


    # Check collision
    
    if collision():

        game_running = False

        game_over.write(
            "GAME OVER",
            align="center",
            font=("Arial", 40, "bold")
        )


    # Update screen
    screen.update()

    # Small delay
    turtle.time.sleep(0.02)


# 11. KEEP SCREEN FREEZE

screen.mainloop()

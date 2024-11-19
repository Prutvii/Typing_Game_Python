from random import choice, randrange
from string import ascii_lowercase
from turtle import *
from freegames import vector

targets = []
letters = []
score = 0
level = 1
speed = 100  # Initial speed of letters (in milliseconds)
drop_rate = 20  # Probability of a new letter being added
awards = [50, 100, 200]  # Award milestones

# Define boundaries for letter animation
DIVIDER_Y = 150  # Y-coordinate for the bottom edge of the score-level division
BOTTOM_LIMIT = -200  # Bottom limit of the screen

def inside(point):
    """Return True if point is inside the animation area."""
    return -200 < point.x < 200 and BOTTOM_LIMIT < point.y < DIVIDER_Y

def draw():
    """Draw letters and display score and level."""
    clear()
    # Draw the division background
    penup()
    goto(-200, DIVIDER_Y)
    pendown()
    color('black')
    begin_fill()
    goto(200, DIVIDER_Y)
    goto(200, 200)
    goto(-200, 200)
    goto(-200, DIVIDER_Y)
    end_fill()

    # Display score and level in the division
    penup()
    goto(-190, 170)
    color('white')
    write(f"Score: {score}", align='left', font=('Arial', 16, 'bold'))
    goto(100, 170)
    write(f"Level: {level}", align='left', font=('Arial', 16, 'bold'))

    # Draw letters below the division
    for target, letter in zip(targets, letters):
        goto(target.x, target.y)
        color('black')  # Ensure font color for letters is black
        write(letter, align='center', font=('Consolas', 20, 'bold'))

    update()

def move():
    """Move letters and adjust speed based on level."""
    global drop_rate
    if randrange(drop_rate) == 0:
        x = randrange(-150, 150)
        target = vector(x, DIVIDER_Y - 20)
        targets.append(target)
        letter = choice(ascii_lowercase)
        letters.append(letter)

    for target in targets:
        target.y -= 1

    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, speed)

def press(key):
    """Handle key presses, update score and level, and give awards."""
    global score, level, speed, drop_rate

    if key in letters:
        score += 1
        pos = letters.index(key)
        del targets[pos]
        del letters[pos]
    else:
        score -= 1

    # Check for level-up every 10 points
    if score > 0 and score % 10 == 0:
        level += 1
        speed = max(30, speed - 20)  # Decrease speed by 20 ms (faster letters)
        print(f"Level Up! You are now at Level {level}!")

    # Awards for specific scores
    if score in awards:
        print(f"Congratulations! You've earned the title: '{get_award_title(score)}!'")
        speed = max(30, speed - 20)  # Extra speed boost for achieving an award
        drop_rate = max(10, drop_rate - 5)  # Increase the likelihood of new letters

    draw()  # Update display

def get_award_title(score):
    """Return the award title based on the score."""
    if score == 50:
        return "Fast Typist"
    elif score == 100:
        return "Typing Master"
    elif score == 200:
        return "Typing Legend"
    return ""

# Set up the game screen
setup(420, 420, 370, 0)
bgcolor('lightyellow')  # Set background color
hideturtle()
up()
tracer(False)
listen()

# Bind each key to its respective function
for letter in ascii_lowercase:
    onkey(lambda l=letter: press(l), letter)

move()
done()
 
'''By PRUTVIRAJ#'''
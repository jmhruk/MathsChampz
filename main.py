import pygame
import random

running = True
score = 0
#colour related
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
orange = (255,128,0)
green = (0, 255, 0)

operation = ""

guessed = False

pygame.init()
window_width = 1280
window_height = 720
window = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("MathsChampions")
clock = pygame.time.Clock()

game_active = False
game_end = False

def generate_question():
    global operation
    num1 = random.randint(1,20)
    num2 = random.randint(1,20)
    
    #evaluate question
    return f"{num1} {operation} {num2}", eval(f"{num1}{"+"}{num2}")

def input():
    input = ""
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return input
            else:
                input += event.unicode

def write_text(s : str, n : int, c : tuple, b : tuple, x : int, y : int):
    global window, window_width, window_height, green, blue
    font = pygame.font.Font('freesansbold.ttf', n)
    text = font.render(s, True, c, b)
    textRect = text.get_rect()
    textRect.center = (x,y)
    window.blit(text, textRect)

#main game logic
while running == True:
    while game_active == False:
        window.fill(blue)
        #font = pygame.font.Font('freesansbold.ttf', 25)
        #text = font.render("1 == Addition, 2 == Subtraction, 3 == Multiplication, 4 == Division", True, green, blue)
        #textRect = text.get_rect()
        #textRect.center = (window_width / 2, window_height / 2)
        #window.blit(text, textRect)
        
        write_text("MathsChampz", 50, blue, green, (window_width / 2), (window_height / 2)  - 120)
        write_text("Made by @JMHRUK", 25, green, blue, (window_width / 2), (window_height / 2)  - 60)
        write_text("1 == Addition, 2 == Subtraction, 3 == Multiplication, 4 == Division", 25, green, blue, window_width / 2, window_height / 2)
        
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            score = 0
            game_active = True
            if event.key == pygame.K_1:
                operation = "+"
            elif event.key == pygame.K_2:
                operation = "-"
            elif event.key == pygame.K_3:
                operation = "*"
            elif event.key == pygame.K_4:
                operation = "/"
            else:
                print("Please enter a valid key!")
        
        pygame.display.update()

        
    while game_active == True:
        window.fill(green)
        #start round
        #print("GAME STARTED")
        font = pygame.font.Font('freesansbold.ttf', 50)
        text = font.render("Press Space to start:", True, orange, blue)
        textRect = text.get_rect()
        textRect.center = (window_width / 2, (window_height / 2))
        window.blit(text, textRect)
        
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            #start
            
            game_active = False
            round_active = True

        else:
            pass
        
        pygame.display.update()
    
    start_ticks=pygame.time.get_ticks()
    while round_active == True:
        seconds=(pygame.time.get_ticks()-start_ticks)/1000
        if seconds > 30:
            game_end = True
            break
            
        question, answer = generate_question()
        user_input = ""
        guessed = False
        
        window.fill(green)
        
        font = pygame.font.Font('freesansbold.ttf', 50)
        text = font.render(str(question), True, orange, blue)
        textRect = text.get_rect()
        textRect.center = (window_width / 2, (window_height / 2) - 100)
        window.blit(text, textRect)
        
        font = pygame.font.Font('freesansbold.ttf', 20)
        score_text = font.render("Score: " + str(score), True, orange, blue)
        textRect = text.get_rect()
        textRect.center = ((window_width / 2), (window_height / 2) + 100)
        window.blit(score_text, textRect)
        pygame.display.update()
        
        while guessed == False:
            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                    
                elif event.key == pygame.K_RETURN:
                    #print(user_input)
                    if user_input.strip() == "":
                        score -= 1
                        guessed = True
                    elif int(user_input) == int(answer):
                        score += 1
                        guessed = True
                        
                    else:
                        window.fill(green)
                        print(user_input)
                        font = pygame.font.Font('freesansbold.ttf', 50)
                        text = font.render("INCORRECT", True, orange, blue)
                        textRect = text.get_rect()
                        textRect.center = (window_width / 2, (window_height / 2) - 100)
                        window.blit(text, textRect)
                        
                        pygame.display.update()
                        
                        acknowledged = False
                        while acknowledged == False:
                            event = pygame.event.wait()
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                                acknowledged = True
                            else:
                                pass
                            
                        score -= 1
                        guessed = True
                        
                else:
                    user_input += event.unicode 
                
                write_text(user_input, 20, white, orange, (window_width / 2), (window_height / 2))
                pygame.display.update()

    while game_end == True:
        print("game over")
        window.fill(green)
        write_text("Game Over!", 50, orange, green, window_width / 2, (window_height / 2) - 120)
        write_text("Score: " + str(score), 50, orange, green, window_width / 2, (window_height / 2) - 60)
        write_text("Press Space to continue...", 50, orange, green, window_width / 2, (window_height / 2))
        
        pygame.display.update()
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key ==  pygame.K_SPACE:
                game_end = False
                game_active = False
                break
        else:
            continue
        

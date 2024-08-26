import pygame
import random

running = True

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

#main game logic
while running == True:
    while game_active == False:
        window.fill(blue)
        font = pygame.font.Font('freesansbold.ttf', 25)
        text = font.render("1 == Addition, 2 == Subtraction, 3 == Multiplication, 4 == Division", True, green, blue)
        textRect = text.get_rect()
        textRect.center = (window_width / 2, window_height / 2)
        window.blit(text, textRect)
        
        
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                operation = "+"
                game_active = True
            elif event.key == pygame.K_2:
                operation = "-"
                game_active = True
            elif event.key == pygame.K_3:
                operation = "*"
                game_active = True
            elif event.key == pygame.K_4:
                operation = "/"
                game_active = True
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
    
    while round_active == True:
        
        question, answer = generate_question()
        user_input = ""
        guessed = False
        
        window.fill(green)
        
        font = pygame.font.Font('freesansbold.ttf', 50)
        text = font.render(str(question), True, orange, blue)
        textRect = text.get_rect()
        textRect.center = (window_width / 2, (window_height / 2) - 100)
        window.blit(text, textRect)
        pygame.display.update()
        while guessed == False:
            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print(user_input)
                    if int(user_input) == int(answer):
                        guessed = True
                        
                else:
                    user_input += event.unicode
            
            pygame.display.update()

        
        
        
        
        


            

    
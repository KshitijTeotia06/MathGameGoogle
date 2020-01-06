import pygame
number = 0
pygame.init()
groups = 0
gDone = False
validChars = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
shiftChars = '~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
ar = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
font = pygame.font.Font('freesansbold.ttf', 32)
class TextBox(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.text = ""
    self.font = pygame.font.Font(None, 50)
    self.image = self.font.render("Type Group Count", False, [0, 0, 0])
    self.rect = self.image.get_rect()

  def add_chr(self, char):
    global shiftDown
    if char in validChars and not shiftDown:
        self.text += char
    elif char in validChars and shiftDown:
        self.text += shiftChars[validChars.index(char)]
    self.update()

  def update(self):
    old_rect_pos = self.rect.center
    self.image = self.font.render(self.text, False, [0, 0, 0])
    self.rect = self.image.get_rect()
    self.rect.center = old_rect_pos


screen = pygame.display.set_mode([800, 600])
textBox = TextBox()
shiftDown = False
textBox.rect.center = [320, 240]
x = font.render('Find the value of x:', True, black, white)
xRect = x.get_rect()
xRect.center = (160, 100)
answerLabel = font.render('Answer:', True, black, white)
answerLabelRect = answerLabel.get_rect()
answerLabelRect.center = (100, 400)

problems = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png']
choices = ['A: x=4  B: x=-5 C: x=3 D:x=10', 'A:x=4 B:x=-5 C:x=-10 D:x=-25', 'A:x=5 B:x=6 C:x=7 D:x=10',
           'A:x=5 B:x=3 C:x=4 D:x=10', 'A:5 B:-2 C:3 D:3', 'A:5 B:1 C:0 D:-4', 'A:4 B:0 C:-10 D:14',
           'A:-6 B:-7 C:-8 C:-9', 'A:-2 B:-5 C:10 D:123', 'A:1 B:12 C:7 D:12']
answer = [4, -5, 6, 5, 5, 5, 4, -6, -5, 1]

running = True
while running:
    screen.fill([255, 255, 255])
    textRect = textBox.image.get_rect()
    textRect.center = (400, 500)
    screen.blit(answerLabel, answerLabelRect)
    screen.blit(textBox.image, textRect)
    screen.blit(x, xRect)
    im = pygame.image.load(problems[number])
    screen.blit(im, (300, 100))
    choices = font.render(choices[number], True, black, white)
    choicesRect = choices.get_rect()
    choicesRect.center = (100, 500)
    pygame.display.flip()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYUP:
            if e.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
                shiftDown = False
        if e.type == pygame.KEYDOWN:
            textBox.add_chr(pygame.key.name(e.key))
            if e.key == pygame.K_SPACE:
                textBox.text += " "
                textBox.update()
            if e.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
                shiftDown = True
            if e.key == pygame.K_BACKSPACE:
                textBox.text = textBox.text[:-1]
                textBox.update()
            if e.key == pygame.K_RETURN:
                if len(textBox.text) > 0:
                    print(textBox.text)
                    if(groups):
                        groups = int(textBox.text)
                        gDone = True
pygame.quit()


import pygame, random

class Messi(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image= pygame.image.load("sprites/messi.png")
		self.rect= self.image.get_rect()
		self.velX= 0
		
	def update(self):
		self.rect.y= 650
		self.rect.x += self.velX
		
class Bola(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image= pygame.image.load("sprites/bola.png")
		self.rect= self.image.get_rect()
		self.rect.x= 150
		self.rect.y= 500
		self.velX= -3
		self.velY= -3
		
	def update(self):
		self.rect.x += self.velX
		self.rect.y += self.velY
		
		if self.rect.x >= 450 or self.rect.x <= 0:
			self.velX *= -1
		
		if self.rect.y <= 0 or self.rect.y >= 750:
			self.velY *= -1
			
class Moneda(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image= pygame.image.load("sprites/moneda.png")
		self.rect= self.image.get_rect()
		
pygame.init()
size= (450,750)
screen= pygame.display.set_mode(size)
pygame.display.set_caption('Messi Money Brick')
clock= pygame.time.Clock()

#Imagenes
	#INICIO
messiInicio= pygame.image.load("sprites/messi2.png")
rect_messi= messiInicio.get_rect()
rect_messi.x= 150
rect_messi.y= 300

	#Audios
monedaS= pygame.mixer.Sound('sounds/coin.ogg.oga')
fondo= pygame.mixer.Sound('sounds/fondo.ogg')
salto= pygame.mixer.Sound('sounds/jump.oga')
winStage= pygame.mixer.Sound('sounds/completo.oga')

	#Win
win= pygame.image.load("sprites/completado.png")
rect_win= win.get_rect()
rect_win.x= 150
rect_win.y= 300

winSC= [10]
#Lista de Sprites
sprite_list= pygame.sprite.Group()
messi_list= pygame.sprite.Group()
monedas= pygame.sprite.Group()

messi= Messi()
bola= Bola()

for i in range(0,300,25):
	gold= Moneda()
	gold.rect.x= 100 +i
	gold.rect.y = 150
	monedas.add(gold)
	sprite_list.add(gold)
	
for i in range(0,300,25):
	gold= Moneda()
	gold.rect.x= 100 +i
	gold.rect.y = 175
	monedas.add(gold)
	sprite_list.add(gold)
	
for i in range(0,300,25):
	gold= Moneda()
	gold.rect.x= 100 +i
	gold.rect.y = 200
	monedas.add(gold)
	sprite_list.add(gold)
	
for i in range(0,300,25):
	gold= Moneda()
	gold.rect.x= 100 +i
	gold.rect.y = 225
	monedas.add(gold)
	sprite_list.add(gold)
	
for i in range(0,300,25):
	gold= Moneda()
	gold.rect.x= 100 +i
	gold.rect.y = 250
	monedas.add(gold)
	sprite_list.add(gold)
	
sprite_list.add(messi, bola)
messi_list.add(messi)

#Bievenida
letra= pygame.font.SysFont("Monospace", 30)
texto= letra.render("Presiona espacio jugar", True, (200,200,200), (0,0,255))
posicionTexto= (50,500)

letra2= pygame.font.SysFont("Monospace", 30)
texto2= letra2.render("Has Ganado!!", True, (0,0,0), (0,255,0))
posicionTexto2= (120,500)

letra3= pygame.font.SysFont("Monospace", 30)
texto3= letra3.render("Has Perdido XD", True, (200,200,200), (20,25,30))
posicionTexto3= (120,500)

#Ventanas
juego= False
principal= True
win_screen= False
lose= False

while principal:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			principal= False
	fondo.play()
	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_SPACE]:
		juego= True
		principal= False
		
	screen.fill((0,0,255))
	
	screen.blit(messiInicio,rect_messi)
	screen.blit(texto, posicionTexto)
	
	pygame.display.flip()
	clock.tick(60)
	

while juego:
	fondo.stop()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done= False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a or event.key == pygame.K_LEFT:
				messi.velX = -3
			if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
				messi.velX = 3

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_a or event.key == pygame.K_LEFT:
				messi.velX = 0
			if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
				messi.velX = 0

	
	
	cabesazo= pygame.sprite.spritecollide(bola, messi_list, False)	
	#fondo.play()				
	choque= pygame.sprite.spritecollide(bola, monedas, True)
	
	if choque:
		monedaS.play()
	
	if cabesazo:
		salto.play()
		
	if choque or cabesazo:
		bola.velY *= -1
		
		
	for i in choque:
		monedas.remove(i)
	
		
		
	
		
	screen.fill((255,255,255))
	sprite_list.draw(screen)
	sprite_list.update()
	
	if len(monedas) ==  0:
		#fondo.stop()
		win_screen= True
		juego = False
		
	if bola.rect.y >700:
		lose= True
		juego = False
		
	pygame.display.flip()
	clock.tick(60)
	
while win_screen:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			win_screen= False
	for i in winSC:
		winStage.play()
	if len(winSC) > 0:
		winSC.pop()
	screen.fill((0,255,0))
	screen.blit(win, rect_win)
	screen.blit(texto2, posicionTexto2)
	
	pygame.display.flip()
	clock.tick(60)
	
while lose:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			lose= False
	screen.fill((20,25,30))
	screen.blit(texto3, posicionTexto3)
	
	pygame.display.flip()
	clock.tick(60)
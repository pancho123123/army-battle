import pygame, random

WIDTH = 1280
HEIGHT = 726

BLACK = (0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = (0, 255, 0)
RED = ( 255, 0, 0)
BLUE = (0,0,255)
PLOMO = (122,122,122)
BROWN = (50,20,30)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("C")
clock = pygame.time.Clock()

def draw_text1(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, WHITE)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_text2(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, BLACK)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_text3(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, PLOMO)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_hp_bar1(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, GREEN, fill)
	pygame.draw.rect(surface, BLACK, border, 2)

def draw_hp_bar(surface, x, y, percentage):
	BAR_LENGHT = 50
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, GREEN, fill)
	pygame.draw.rect(surface, BLACK, border, 2)

def draw_hp_bar2(surface, x, y, percentage):
	BAR_LENGHT = 900
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, BROWN, fill)
	pygame.draw.rect(surface, BROWN, border, 2)

def draw_hp_bar3(surface, x, y, percentage):
	BAR_LENGHT = 80
	BAR_HEIGHT = 7
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, RED, fill)
	pygame.draw.rect(surface, BLACK, border, 2)

def draw_hp_bar4(surface, x, y, percentage):
	BAR_LENGHT = 30
	BAR_HEIGHT = 7
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, RED, fill)
	pygame.draw.rect(surface, BLACK, border, 2)

def draw_mana_bar(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, BLUE, fill)
	pygame.draw.rect(surface, BLACK, border, 2)
	
class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/sniper.png").convert(),(50,65))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.speed_x = 0
		self.hp = 500
		self.mana = 100
		self.armor = 2
		self.rect.centerx = WIDTH//2
		self.rect.centery = HEIGHT//2
		self.bullet_int = 0
		self.direction = 0
		self.weapon_a = 300
		self.weapon_b = 100

	def update(self):
		if self.weapon_a < 0:
			self.weapon_a = 0
		if self.weapon_a > 300:
			self.weapon_a = 300
		if self.weapon_b < 0:
			self.weapon_b = 0
		if self.weapon_b > 100:
			self.weapon_b = 100
		self.hp += 1/40
					
		if self.hp > 500:
			self.hp = 500
		if self.hp <= 0:
			self.hp = 0
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_a]:
			self.speed_x = -7
			self.direction = 3
		if keystate[pygame.K_d]:
			self.speed_x = 7
			self.direction = 1
		self.rect.x += self.speed_x
		if keystate[pygame.K_w]:
			self.speed_y = -7
			self.direction = 0
		if keystate[pygame.K_s]:
			self.speed_y = 7
			self.direction = 2
		self.rect.y += self.speed_y
		
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.top < 0:
			self.rect.top = 0
		if self.rect.bottom > 700:
			self.rect.bottom = 700

	def shoot(self):
		if self.bullet_int == 0:
			if self.weapon_a > 0:
				bullet0 = Bullet0(self.rect.centerx, self.rect.centery, self.direction)
				all_sprites.add(bullet0)
				bullets.add(bullet0)
				self.weapon_a -= 1
		elif self.bullet_int == 1:
			if self.weapon_b > 0:
				bullet1 = Bullet1(self.rect.centerx, self.rect.centery, self.direction)
				all_sprites.add(bullet1)
				bullets2.add(bullet1)
				self.weapon_b -= 1

class Bullet0(pygame.sprite.Sprite):
	def __init__(self, x, y, direct):
		super().__init__()
		self.image = pygame.image.load("img/bullet.png").convert()
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centery = y
		self.rect.centerx = x
		self.speed = 10
		self.direction = direct

	def update(self):
		if self.direction == 0:
			self.rect.y -= self.speed
		elif self.direction == 1:
			self.rect.x += self.speed
		elif self.direction == 2:
			self.rect.y += self.speed
		else:
			self.rect.x -= self.speed
		if self.rect.right < 0 or self.rect.left > 1280 or self.rect.bottom < 0 or self.rect.top > 720:
			self.kill()

class Bullet1(pygame.sprite.Sprite):
	def __init__(self, x, y, direct):
		super().__init__()
		self.image = pygame.image.load("img/bullet2.png").convert()
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centery = y
		self.rect.centerx = x
		self.speed = 10
		self.direction = direct

	def update(self):
		if self.direction == 0:
			self.rect.y -= self.speed
		elif self.direction == 1:
			self.rect.x += self.speed
		elif self.direction == 2:
			self.rect.y += self.speed
		else:
			self.rect.x -= self.speed
		if self.rect.right < 0 or self.rect.left > 1280 or self.rect.bottom < 0 or self.rect.top > 720:
			self.kill()

def distance(a,b):
	#pitagoras distancia entre a y b
	dx = b.rect.centerx - a.rect.centerx
	dy = b.rect.centery - a.rect.centery
	return (dx**2 + dy**2)**(1/2)

def direction(a,b):
	#vector unitario desde a a b
	dx = b.rect.centerx - a.rect.centerx
	dy = b.rect.centery - a.rect.centery
	radio = (dx**2 + dy**2)**(1/2)
	if radio != 0:
		x, y = (dx/radio, dy/radio)
	else:
		x, y = (0, 0)
	return x, y

class CreepMelee(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/creep_melee1.png").convert(),(25,50))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = random.choice([-100,1300])
		self.rect.y = random.choice([100,200,300,400,500])
		self.speed = 2
		self.hp = 400
		self.int = 0
	
	def update(self):
		target = player	
		x,y = direction(self, target)
		self.rect.centerx += self.speed*x
		self.rect.centery += self.speed*y
		
		if self.hp > 400:
			self.hp = 400
		if self.hp <= 0:
			self.kill()

class CreepRange(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/creep_ranged1.png").convert(),(25,50))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = random.choice([-100,1300])
		self.rect.y = random.choice([100,200,300,400,500])
		self.hp = 300
		self.speed = 2
		self.int = 1
		
	def update(self):
		target = player	
		x,y = direction(self, target)
		self.rect.centerx += self.speed*x
		self.rect.centery += self.speed*y
		if self.hp <= 0:
			self.kill()

class Barrel(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/barril.png").convert(),(25,50))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = random.choice([300,400, 500, 600, 700, 800, 900,1000])
		self.rect.y = random.choice([100,200,300,400,500])
		self.hp = 100
		
	def update(self):
		if self.hp <= 0:
			number = random.randint(1,3)
			numbers = random.randint(0,1)
			if number == 2:
				if numbers == 0:
					suply = SuplyA(self.rect.centerx, self.rect.centery)
				else:
					suply = SuplyB(self.rect.centerx, self.rect.centery)
				all_sprites.add(suply)
				supply_list.add(suply)
			elif number == 3:
				heart = Heart(self.rect.centerx, self.rect.centery)
				all_sprites.add(heart)
				heart_list.add(heart)
			self.kill()

class SuplyA(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/supA.png").convert(),(25,50))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.int = 0
		
	def update(self):
		pass

class SuplyB(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/supB.png").convert(),(25,50))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.int = 1
		
	def update(self):
		pass

class Heart(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/heart.png").convert(),(25,25))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.centery = y
		
	def update(self):
		pass

class Weapon(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/supA.png").convert(),(60,40))
		#self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH//2
		self.rect.centery = 60

	def update(self):
		if player.bullet_int == 0:
			self.image = pygame.transform.scale(pygame.image.load("img/supA.png").convert(),(25,50))
		else:
			self.image = pygame.transform.scale(pygame.image.load("img/supB.png").convert(),(25,50))

class WeaponA(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/supA.png").convert(),(20,20))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH - 250
		self.rect.centery = 25

class WeaponB(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/supB.png").convert(),(20,20))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH - 250
		self.rect.centery = 50

def show_go_screen():
	
	screen.fill(BLACK)
	draw_text1(screen, "Blast letal", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Destruye los enemigos", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)
	#draw_text(screen, "Created by: Francisco Carvajal", 10,  60, 500)
	
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

def show_game_over_screen():
	screen.fill(BLACK)
	draw_text1(screen, "Game Over", 60, WIDTH  // 2, HEIGHT * 1/4)
	draw_text1(screen, "score: "+str(score), 30, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 4/5)
	
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

#background = pygame.transform.scale(pygame.image.load("img/fond.png").convert(),(1300,700))

all_sprites = pygame.sprite.Group()
player_list = pygame.sprite.Group()
bullets = pygame.sprite.Group()
bullets2 = pygame.sprite.Group()
creeps = pygame.sprite.Group()
heart_list = pygame.sprite.Group()
supply_list = pygame.sprite.Group()
barrel_list = pygame.sprite.Group()
counter1 = True
counter2 = True
counter3 = True
number1 = random.randint(3000,4000)
number2 = random.randint(8000,15000)
number3 =  random.randint(8000,15000)

game_over = False
running = True

show_go_screen()
player = Player()
all_sprites.add(player)
player_list.add(player)
score = 0
weapon = Weapon()
wep1 = WeaponA()
wep2 = WeaponB()
all_sprites.add(weapon, wep1, wep2)
start_time = pygame.time.get_ticks()
while running:
	if game_over:
		show_game_over_screen()
		game_over = False
		player = Player()
		all_sprites.add(player)
		player_list.add(player)
		score = 0
		start_time = pygame.time.get_ticks()
		weapon = Weapon()
		wep1 = WeaponA()
		wep2 = WeaponB()
		all_sprites.add(weapon, wep1, wep2)
		
	clock.tick(60)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			sys.exit()
		
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_f:
				if player.hp > 0:
					player.shoot()
				else:
					pass
			if event.key == pygame.K_r:
				if player.bullet_int == 0:
					player.bullet_int = 1
				elif player.bullet_int == 1:
					player.bullet_int = 0
	
	current_time = pygame.time.get_ticks()
	elapsed_time = current_time -start_time

	if elapsed_time >= number1:
		if counter1:
			number1 = random.randint(8000,15000)
			counter1 = False
			creep_m = CreepMelee() 
			barrel = Barrel()
			barrel_list.add(barrel)
			all_sprites.add(creep_m, barrel)
			creeps.add(creep_m)
			counter2 = True
			start_time = pygame.time.get_ticks()

	if elapsed_time >= number2:
		if counter2:
			number2 = random.randint(8000,15000)
			counter2 = False
			creep_r = CreepRange() 
			barrel = Barrel()
			barrel_list.add(barrel)
			all_sprites.add(creep_r, barrel)
			creeps.add(creep_r)
			counter3 = True
			start_time = pygame.time.get_ticks()

	if elapsed_time >= number3:
		if counter3:
			number3 = random.randint(8000,15000)
			counter3 = False
			creep_m = CreepMelee() 
			barrel = Barrel()
			barrel_list.add(barrel)
			all_sprites.add(creep_m, barrel)
			creeps.add(creep_m)
			counter1 = True
			start_time = pygame.time.get_ticks()

	if player.hp <= 0:
		game_over = True
		
		
	# Checar colisiones - boss - bullets
	for bullet in bullets:
		for creep in creeps:
			if pygame.sprite.collide_rect(creep, bullet):
				if creep.int == 0:
					creep.hp -= 40
					bullet.kill()
				else:
					creep.hp -= 10
					bullet.kill()

	# Checar colisiones - bullets - creeps
	for bullet in bullets2:
		for creep in creeps:
			if pygame.sprite.collide_rect(creep, bullet):
				if creep.int == 0:
					creep.hp -= 10
					bullet.kill()
				else:
					creep.hp -= 40
					bullet.kill()

	# Checar colisiones - boss - bullets
	for bullet in bullets:
		for barril in barrel_list:
			if pygame.sprite.collide_rect(barril, bullet):
				barril.hp -= 20
				bullet.kill()
				score += random.randint(10,40)
		

	# Checar colisiones - bullets - creeps
	for bullet in bullets2:
		for barril in barrel_list:
			if pygame.sprite.collide_rect(barril, bullet):
				barril.hp -= 20
				bullet.kill()
				score += random.randint(10,40)
		
	# Checar colisiones - players - creeps
	
	for creep in creeps:
		if pygame.sprite.collide_rect(player, creep):
			player.hp -= 30
			if creep.rect.x > player.rect.x:
				player.rect.x -= 70
			else:
				player.rect.x += 70

	# Checar colisiones - boss - players
	for heart in heart_list:
		for player in player_list:
			if pygame.sprite.collide_rect(heart, player):
				player.hp += random.randint(7,15)
				heart.kill()
				score += random.randint(10,30)
	
	# Checar colisiones - boss - players
	for suply in supply_list:
		if pygame.sprite.collide_rect(suply, player):
			if suply.int == 0:
				player.weapon_a += random.randint(25,50)
				suply.kill()
				score += random.randint(10,30)
			else:
				player.weapon_b += random.randint(25,50)
				suply.kill()
				score += random.randint(10,30)
	
	
	all_sprites.update()
				
	"""
	# dtención del juego en t = () en mlseg	
	now = pygame.time.get_ticks()
	if now > 16000:
		game_over = True"""
	
	screen.fill(BLACK)

	all_sprites.draw(screen)

	#Marcador
	draw_text1(screen, str(score), 25, WIDTH // 2, 10)

	draw_text1(screen, str(player.weapon_a), 25, WIDTH - 200, 10)
	draw_text1(screen, str(player.weapon_b), 25, WIDTH - 200, 30)

	# Escudo.
	draw_text2(screen, "P1", 20, 210, 6)

	draw_hp_bar1(screen, 220, 5, player.hp/5)
	draw_text2(screen, str(int(player.hp)) + "/500", 10, 270, 6)


	for creep in creeps:
		try:
			if creep.hp > 0:
				draw_hp_bar4(screen, creep.rect.x, creep.rect.y, creep.hp/5.5)
		except(NameError):
			pass

	#reloj
	draw_text1(screen, str(pygame.time.get_ticks()//1000), 30, 600, 50)

	pygame.display.flip()
pygame.quit()
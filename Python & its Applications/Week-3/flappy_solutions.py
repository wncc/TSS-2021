import pygame, sys, random 

pygame.init()
screen = pygame.display.set_mode((576,1024))
clock = pygame.time.Clock()
game_font = pygame.font.SysFont(None,40)


gravity = 0.25
bird_movement = 0
game_active = True
score = 0
floor_x_pos = 0

#Load the necessary images

bg_surface = pygame.image.load('flappy_assets/background.png')
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('flappy_assets/floor.png')
floor_surface = pygame.transform.scale2x(floor_surface)

bird_surface = pygame.transform.scale2x(pygame.image.load('flappy_assets/bluebird.png'))
bird_rect = bird_surface.get_rect(center = (100,512))

pipe_surface = pygame.image.load('flappy_assets/pipe.png')
pipe_surface = pygame.transform.scale2x(pipe_surface)

game_over_surface = pygame.transform.scale2x(pygame.image.load('flappy_assets/message.png'))
game_over_rect = game_over_surface.get_rect(center = (288,512))


pipe_list = []

# We have created this custom event which will be automatically trigerred according to the time set
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200)
pipe_height = [400,600,800]





ddef create_pipe():
	"""
	Create and return rects for 2 pipes using pip_surface(one at top and other at bottom) You can use functions from random 
	to change the height of the pipes.(but keeping the size of opening constant) 
	"""
	random_pipe_pos = random.choice(pipe_height)
	bottom_pipe = pipe_surface.get_rect(midtop = (700,random_pipe_pos))
	top_pipe = pipe_surface.get_rect(midbottom = (700,random_pipe_pos - 300))
	return bottom_pipe,top_pipe



def move_pipes(pipes):
	"""
	Move the pipes back in order to give the feeling that the bird is moving forward.
	"""
	for pipe in pipes:
		pipe.centerx -= 5
	return pipes


def draw_pipes(pipes):
	"""
	Draw the pipes on the screen using the rects and pipe_surface. Use blit(). You will have to judge whether its a top pipe or 
	a bottom pipe and appropriately use the image. You can use pygame.transform.flip() to flip an image.
	"""
	for pipe in pipes:
		if pipe.bottom >= 1024:
			screen.blit(pipe_surface,pipe)
		else:
			flip_pipe = pygame.transform.flip(pipe_surface,False,True)
			screen.blit(flip_pipe,pipe)

def remove_pipes(pipes):
	"""
	As the pipes reach the left side of the screen remove them. 
	"""
	for pipe in pipes:
		if pipe.centerx == -600:
			pipes.remove(pipe)
	return pipes


def draw_floor():
	"""Draw the floor surfaces on the screen. Hint: Use 2 floor surfaces to ensure proper motion of the floor"""
	screen.blit(floor_surface,(floor_x_pos,900))
	screen.blit(floor_surface,(floor_x_pos + 576,900))


def check_collision(pipes):
	"""
	check whether the bird might have collided with any of the pipes you can use
	colliderect(). Or the bird might have hit the floor or crossed the top.
	"""
	for pipe in pipes:
		if bird_rect.colliderect(pipe):
			return False

	if bird_rect.top <= -100 or bird_rect.bottom >= 900:
		return False

	return True


def score_display(game_state):
	"""
	display the score on the screen. Note depending on what the game state is 
	score will have to be displayed at different places.
	"""
	if game_state == 'main_game':
		score_surface = game_font.render(str(int(score)),True,(255,255,255))
		score_rect = score_surface.get_rect(center = (288,100))
		screen.blit(score_surface,score_rect)
	if game_state == 'game_over':
		score_surface = game_font.render(f'Score: {int(score)}' ,True,(255,255,255))
		score_rect = score_surface.get_rect(center = (288,100))
		screen.blit(score_surface,score_rect)


def check_for_events():
	"""
	Will contain main for loop listening for events. It should have code to respond to 
	quitting, pressing the spacebar(if game is active it causes the jump, use bird_movement attribute and if not
	it should turn the game active and start it). It should also listen for the SPAWNPIPE event 
	"""
	global game_active
	global score
	global bird_movement
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE and game_active:
				bird_movement = 0
				bird_movement -= 12
				
			if event.key == pygame.K_SPACE and game_active == False:
				game_active = True
				pipe_list.clear()
				bird_rect.center = (100,512)
				bird_movement = 0
				score = 0

		if event.type == SPAWNPIPE:
			pipe_list.extend(create_pipe())


def update_bird(pipe_list):
	"""
	Update the postion of the bird, update the bird_movement variable for gravity, 
	check for collisions with the pipes
	"""
	global game_active
	global bird_movement
	bird_movement += gravity
	bird_rect.centery += bird_movement
	screen.blit(bird_surface,bird_rect)
	game_active = check_collision(pipe_list)


def update_pipes(pipe_list):
	"""
	Using the above defined functions, move, remove and draw the pipes
	"""
	pipe_list = move_pipes(pipe_list)
	pipe_list = remove_pipes(pipe_list)
	draw_pipes(pipe_list)


def update_score():
	"""
	Update the score if the bird has passed through the opening
	"""
	global score
	for pipe in pipe_list:
		if bird_rect.centerx == pipe.centerx:
			score+=1
			return


while True:
	check_for_events()
	screen.blit(bg_surface,(0,0))

	if game_active:
		update_bird(pipe_list)
		update_pipes(pipe_list)

		update_score()
		score_display('main_game')
		
	else:
		screen.blit(game_over_surface,game_over_rect)
		score_display('game_over')


	# Change the position of the floor and draw it. Make sure if it reaches the left end reset it
	floor_x_pos -= 1
	draw_floor()
	if floor_x_pos <= -576:
		floor_x_pos = 0

	pygame.display.flip()

	# set the speed of the game
	clock.tick(120)

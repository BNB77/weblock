'''Запускать из рабочей директории!'''
import pygame
import time
from storage import *


pygame.init()

usr_name = ''
score = 0
right_answers_loop_1 = 'count+1'
right_answers_loop_2 = '10,0,-1', '100-1'   

W, H, FPS = 800, 600, 30
col_in = (0, 200, 200)
col_out = (255, 241, 55)

app = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

back_img = pygame.image.load(r'assets\menu.png')
back_img_theme = pygame.image.load(r'assets\bg.png')

ifelse_img_s = pygame.image.load(r'assets\ifelse_s.jpg')
ifelse_img = pygame.image.load(r'assets\ifelse.jpg')
list_img_s = pygame.image.load(r'assets\list_s.jpg')
list_img = pygame.image.load(r'assets\list.jpg')
func_img_s = pygame.image.load(r'assets\func_s.jpg')
func_img = pygame.image.load(r'assets\func.jpg')
loop_img_s = pygame.image.load(r'assets\loop_s.jpg')
loop_img = pygame.image.load(r'assets\loop.jpg')
rocket_0_img = pygame.image.load(r'assets\rocket0.png')
rocket_1_img = pygame.image.load(r'assets\rocket7.png')
rocket_2_img = pygame.image.load(r'assets\rocket6.png')

s1_m, s2_m, s3_m, s4_m, s5_m = [pygame.image.load(r'assets\star' + str(i) + '_s_w.png') for i in range(1, 6)] 
s1, s2, s3, s4, s5 = [pygame.image.load(r'assets\star' + str(i) + '.png') for i in range(1, 6)] 


pygame.mixer.music.set_volume(0.1)


def is_clicked_with_sound(need_delay=True):
	clicked = pygame.mouse.get_pressed()
	if clicked[0] == 1: 
		pygame.mixer.music.load(r'assets\click.mp3')
		pygame.mixer.music.play()
		if need_delay:
			pygame.time.delay(500)
	return clicked


def button_txt(x, y, w, h, mes, action=None, f_size=30, x_sh=25, y_sh=25):
	mouse = pygame.mouse.get_pos()
	clicked = is_clicked_with_sound()

	if x < mouse[0] < x + w and y < mouse[1] < y + h:
		pygame.draw.rect(app, col_in, (x, y, w, h))
		if clicked[0] == 1:
			if action is not None:
				action()
				quit()
	else:
		pygame.draw.rect(app, col_out, (x, y, w, h))
	
	print_text(mes, x + x_sh, y + y_sh, font_size=f_size) 


def button_img(x_c, y_c, w_btn, h_btn, img, img_b, action=None):
	mouse = pygame.mouse.get_pos()
	clicked = is_clicked_with_sound(need_delay=False)

	w = 50
	h = 50
	w_b = 100
	h_b = 100
	
	x = x_c - w // 2
	y = y_c - h // 2
	x_b = x_c - w_b // 2
	y_b = y_c - h_b // 2

	if x < mouse[0] < x + w_btn and y < mouse[1] < y + h_btn:
		app.blit(img_b, (x_b, y_b))
		if clicked[0] == 1:
			if action is not None:
				action()
				quit()
	else:
		app.blit(img, (x, y))
	

def print_text(mes, x, y, font_col=(0, 0, 0), font_type=None, font_size=30):
	font = pygame.font.Font(font_type, font_size)
	text_surface = font.render(mes, True, font_col)
	app.blit(text_surface, (x, y))


def draw_stars(is_animation=False):
	if is_animation is False:
		app.blit(s1_m, (0, 35))
		app.blit(s2_m, (70, 25))
		app.blit(s3_m, (160, 15))
		app.blit(s4_m, (260, 10))
		app.blit(s5_m, (380, 0))
	else:
		app.blit(s1, (0, 35))
		pygame.display.update()
		pygame.time.delay(500)
		app.blit(s2, (70, 25))
		pygame.display.update()
		pygame.time.delay(500)
		app.blit(s3, (160, 15))
		pygame.display.update()
		pygame.time.delay(500)
		app.blit(s4, (260, 10))
		pygame.display.update()
		pygame.time.delay(500)
		app.blit(s5, (380, 0))
		pygame.display.update()
		pygame.time.delay(500)


def loop():
	global score

	answer_loop_1	= ''
	is_end = False
	count_ans = 0
	is_anim = False
	wrong_ans = False

	while True:
		if is_end:
			score += 4 - count_ans
			loop_2()
			quit()
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			if event.type == pygame.KEYDOWN:
				pygame.mixer.music.load(r'assets\type.mp3')
				pygame.mixer.music.play()

				if event.key == pygame.K_RETURN:
					count_ans += 1
					if ''.join(answer_loop_1.split()) == right_answers_loop_1:
						is_anim = True
						is_end = True
					else:
						wrong_ans = True
				elif event.key == pygame.K_BACKSPACE:
					answer_loop_1 = answer_loop_1[:-1]
				else:
					if len(answer_loop_1) < 10:
						answer_loop_1 += event.unicode
		

		keys = pygame.key.get_pressed()
		if keys[pygame.K_ESCAPE]:
			pause()

		app.blit(back_img_theme, (0, 0))

		x = 300
		y = 300
		height_line = 40
		with_tab = 30
		pygame.draw.rect(app, col_out, (x - 10, y - 10, 220, height_line * 4 + 20))
		pygame.draw.rect(app, (0, 0, 0), (x - 10, y - 10, 220, height_line * 4 + 20), 2)
		print_text('count = 1', x, y, font_size=30)
		print_text('while count < 6:', x, y + height_line * 1, font_size=30)
		print_text('print(count)', x + with_tab, y + height_line * 2, font_size=30)
		print_text('count = _________', x + with_tab, y + height_line * 3, font_size=30)
		button_txt(x + 25, y + height_line * 5.5, 150, 50, answer_loop_1, x_sh=20, y_sh=20)
		
		x = 100
		y = 180
		height_line = 30

		print_text('В ряд стоят 5 звёздочек. Их нужно посчитать, ', x, y, font_size=30)
		print_text('но вот незадача: из программы, которая должна была ', x, y + height_line, font_size=30)
		print_text('это сделать потерялась часть строчки. Помоги ', x, y + height_line * 2, font_size=30)
		print_text('её восстановить.', x, y + height_line * 3, font_size=30)

		if wrong_ans:
			if count_ans < 3:
				print_text("Неверно!", 330, 480, font_size=40, font_col=(200, 0, 0))
				pygame.display.update()
				pygame.time.delay(1000)
				answer_loop_1 = ''
			else:
				print_text("Попытки закончились (", 260, 480, font_size=40, font_col=(200, 0, 0))
				pygame.display.update()
				pygame.time.delay(1000)
				is_end = True
			wrong_ans = False
		
		draw_stars(is_anim)

		pygame.display.update()
		clock.tick(FPS)


def loop_2():
	global score

	answer_loop_2 = ''
	is_end = False
	count_ans = 0
	is_anim = False
	wrong_ans = False

	x_r = 100
	y_r = 450
	sign = 50
	speed = 10
	value = 400

	while True:
		if is_end:
			score += 4 - count_ans
			end_app()
			quit()
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			if event.type == pygame.KEYDOWN:
				pygame.mixer.music.load(r'assets\type.mp3')
				pygame.mixer.music.play()

				if event.key == pygame.K_RETURN:
					count_ans += 1
					if ''.join(answer_loop_2.split()) in right_answers_loop_2 or\
						''.join(answer_loop_2.split(',')) in right_answers_loop_2:
						is_anim = True
					else:
						wrong_ans = True
				elif event.key == pygame.K_BACKSPACE:
					answer_loop_2 = answer_loop_2[:-1]
				else:
					if len(answer_loop_2) < 10:
						answer_loop_2 += event.unicode
		

		keys = pygame.key.get_pressed()
		if keys[pygame.K_ESCAPE]:
			pause()

		app.blit(back_img_theme, (0, 0))

		x = W // 2 - 100
		y = H // 2
		height_line = 40
		with_tab = 30
		pygame.draw.rect(app, (250, 250, 0), (x - 20, y - 20, 270, height_line * 4 + 20))
		pygame.draw.rect(app, (0, 0, 0), (x - 20, y - 20, 270, height_line * 4 + 20), 2)
		print_text('for i in range(__, __, __):', x, y + height_line * 0, font_size=30)
		print_text('print(i)', x + with_tab, y + height_line * 1, font_size=30)
		print_text("print('Пуск!')", x, y + height_line * 2, font_size=30)
		button_txt(x + 25, y + height_line * 5.5, 150, 50, answer_loop_2, x_sh=20, y_sh=20)


		print_text('До запуска ракеты остается 10 секунд. Но из ', W // 4 - 40, H // 2 - 120, font_size=30)
		print_text('программы, которая должна была вести отсчет до нуля, ', W // 4 - 40, H // 2 - 90, font_size=30)
		print_text('потерялась часть условия. Помоги его восстановить. ', W // 4 - 40, H // 2 - 60, font_size=30)
		
		app.blit(rocket_1_img, (x_r, y_r))

		if is_anim:
			y_r -= speed // 10
			x_r += sign // 10
			sign *= -1
			if sign > 0:
				sign -= 1
				speed += 1
			if y_r > value:
   				app.blit(rocket_0_img,(x_r, y_r)) 
			else:
   				app.blit(rocket_2_img,(x_r, y_r))
			if y_r == -90:
				is_end = True
			
		
		if wrong_ans:
			if count_ans < 3:
				print_text("Неверно!", 330, 480, font_size=40, font_col=(200, 0, 0))
				pygame.display.update()
				pygame.time.delay(1000)
				answer_loop_2 = ''
			else:
				print_text("Попытки закончились (", 260, 480, font_size=40, font_col=(200, 0, 0))
				pygame.display.update()
				pygame.time.delay(1000)
				is_end = True
			wrong_ans = False

		pygame.display.update()
		clock.tick(FPS)


def chose_theme():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()

		keys = pygame.key.get_pressed()
		if keys[pygame.K_ESCAPE]:
			pause()

		app.blit(back_img, (0, 0))

		button_img(100, 200, 200, 100, loop_img_s, loop_img, action=loop)
		button_img(550, 200, 200, 100, ifelse_img_s, ifelse_img)
		button_img(100, 400, 200, 100, list_img_s, list_img)
		button_img(550, 400, 200, 100, func_img_s, func_img)
		
		pygame.display.update()
		clock.tick(FPS)


def pause():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()

		keys = pygame.key.get_pressed()

		if keys[pygame.K_n]:
			return

		app.blit(back_img, (0, 0))
		print_text('PAUSE', W // 2, H // 2, font_size=50)
		print_text('Press n to continue', W // 2, H // 2 + 100, font_size=50)
		
		pygame.display.update()
		clock.tick(FPS)


def check_name_existance():
	list_names = [user[0] for user in data.select_all()]
	if usr_name in list_names:
		print_text("Такое имя уже занято!", 280, 500, font_size=30, font_col=(200, 0, 0))
		pygame.display.update()
		pygame.time.delay(3000)
		return True
	else:
		return False
		

def usr_name_input():
	global usr_name

	usr_name = ''
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			if event.type == pygame.KEYDOWN:
				pygame.mixer.music.load(r'assets\type.mp3')
				pygame.mixer.music.play()

				if event.key == pygame.K_RETURN:
					if usr_name:
						if check_name_existance():
							usr_name = ''
						else:
							chose_theme()
				elif event.key == pygame.K_BACKSPACE:
					usr_name = usr_name[:-1]
				else:
					if len(usr_name) < 10:
						usr_name += event.unicode

		app.blit(back_img, (0, 0))

		print_text('Пожалуйста, введи ник (меньше 10 символов)', W // 5 + 20, 200, font_size=30)
		print_text('Затем нажми на  \'enter\'', W // 3 + 15, 250, font_size=30)

		button_txt(320, 300, 150, 70, usr_name, x_sh=20, y_sh=30)
		button_txt(335, 400, 110, 70, 'Quit', x_sh=30, y_sh=30, action=exit)

		pygame.display.update()
		clock.tick(FPS // 2)
	

def menu():
	global score, usr_name
	
	score = 0
	usr_name = ''

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()

		app.blit(back_img, (0, 0))

		button_txt(335, 200, 110, 70, 'Старт', x_sh=25, y_sh=27, action=usr_name_input)
		button_txt(335, 300, 110, 70, 'Выход', x_sh=20, y_sh=27, action=exit)

		pygame.display.update()
		clock.tick(FPS)


def show_list():
	global data

	list_data	= sorted(data.select_all(), key=lambda x: -x[1])[:5]
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()

		app.blit(back_img, (0, 0))

		for i in range(len(list_data)):
			button_txt(W // 7 + W // 25 + 100, H // 3 + i * H // 10 - 50,\
				W // 5, H // 9, list_data[i][0], x_sh=30, y_sh=20)
			button_txt(W // 7 + W // 25 + 250, H // 3 + i * H // 10 - 50,\
				W // 5, H // 9, str(list_data[i][1]), x_sh=70, y_sh=20)
		
		button_txt(340, 470, 110, 50, 'Меню', x_sh = 25, y_sh = 20, action=menu)
		button_txt(340, 530, 110, 50, 'Выход', x_sh = 20, y_sh = 15, action=exit)

		pygame.display.update()
		clock.tick(FPS // 2)


def end_app():
	data.insert_into(usr_name, score)
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		
		app.blit(back_img, (0, 0))
		if score > 5:
			print_text('Молодец!', W // 2 - 50, 170, font_size=30)
		elif score > 3:
			print_text('Нeплохо.',  W // 2 - 50, 170, font_size=30)
		else:
			print_text('Знаю, ты можешь лучше!',  W // 2 - 130, 170, font_size=30)
		x = 310
		y = H // 2 - 20
		print_text(usr_name, x + 130 - len(usr_name) * 15, y - 40, font_size=30)
		print_text('Ты набрал', x, y, font_size=30)
		print_text(str(score), x + 115, y, font_size=30)
		if score >= 5:
			print_text('баллов', x + 140, y, font_size=30)
		elif score >= 2:
			print_text('балла',  x + 140, y, font_size=30)
		else:
			print_text('балл',  x + 140, y, font_size=30)

		button_txt(340, 350, 110, 70, 'Топ', x_sh = 35, y_sh = 30, action=show_list)
		button_txt(340, 450, 110, 70, 'Выход', x_sh = 20, y_sh = 30, action=exit)

		pygame.display.update()
		clock.tick(FPS)


data = Storage()
menu()

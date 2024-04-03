import pygame  # импортируем pygame

clock = pygame.time.Clock()

bat_list = []

pygame.init()  # инициализируем pygame
screen = pygame.display.set_mode((1260, 768))  # вводим размер игрового поля (ширина \ высота)
pygame.display.set_caption('Break your Space')  # вводим название проги
icon = pygame.image.load(
    'gg/icons8-steelseries-gg-64.png').convert_alpha()  # создаём переменную с логотипом, предварительно загрузив его
pygame.display.set_icon(icon)  # вводим логотип в прогу

# square = pygame.Surface((50, 170)) #создаём плоскость на которой обозначаем размеры нашего квадрата (ширина \ высота)
# square.fill((94, 0, 125)) #обращаямся к нашей фигуре, и задаём ей нужный нам цвет
Bg = pygame.image.load('GG/XXXX.png').convert()

walk_right = [
    pygame.image.load('player/qqqqqqq/qwer6 (2).png').convert_alpha(),
    pygame.image.load('player/qqqqqqq/qwer7.png').convert_alpha(),
    pygame.image.load('player/qqqqqqq/qwer8.png').convert_alpha(),
    pygame.image.load('player/qqqqqqq/qwer9.png').convert_alpha(),
    pygame.image.load('player/qqqqqqq/qwer.10.png').convert_alpha(),
    pygame.image.load('player/qqqqqqq/qwer.10.png').convert_alpha(),
    pygame.image.load('player/qqqqqqq/qwer.12.png').convert_alpha(),
    pygame.image.load('player/qqqqqqq/qwer13 (2).png').convert_alpha(),
    pygame.image.load('player/qqqqqqq/qwer14.png').convert_alpha(),
    pygame.image.load('player/qqqqqqq/qwer15 (2).png').convert_alpha(),
    pygame.image.load('player/qqqqqqq/qwer16.png').convert_alpha(),
    pygame.image.load('player/qqqqqqq/qwer18 (2).png').convert_alpha(),
    pygame.image.load('player/qqqqqqq/qwer19.png').convert_alpha(),
    pygame.image.load('player/qqqqqqq/qwer20.png').convert_alpha(),
    pygame.image.load('player/qqqqqqq/qwer21.png').convert_alpha(),
    pygame.image.load('player/qqqqqqq/qwer22.png').convert_alpha(),
    pygame.image.load('player/qqqqqqq/qwer23 (2).png').convert_alpha(),
    pygame.image.load('player/qqqqqqq/qwer24.png').convert_alpha(),
    pygame.image.load('player/qqqqqqq/qwer25.png').convert_alpha(),
    pygame.image.load('player/qqqqqqq/qwer26.png').convert_alpha(),
    pygame.image.load('player/qqqqqqq/qwer27.png').convert_alpha(),
    pygame.image.load('player/qqqqqqq/qwer28.png').convert_alpha(),
    pygame.image.load('player/qqqqqqq/qwer29 (2).png').convert_alpha(),
    pygame.image.load('player/qqqqqqq/qwer30.png').convert_alpha(),
    pygame.image.load('player/qqqqqqq/qwer31.png').convert_alpha(),
    pygame.image.load('player/qqqqqqq/qwer32.png').convert_alpha(),
    pygame.image.load('player/qqqqqqq/qwer33.png').convert_alpha(),
]
walk_left = [
    pygame.image.load('zxc/xxxxxxxx/zxc1.png').convert_alpha(),
    pygame.image.load('zxc/xxxxxxxx/zxc2.png').convert_alpha(),
    pygame.image.load('zxc/xxxxxxxx/zxc4.png').convert_alpha(),
    pygame.image.load('zxc/xxxxxxxx/zxc5.png').convert_alpha(),
    pygame.image.load('zxc/xxxxxxxx/zxc6.png').convert_alpha(),
    pygame.image.load('zxc/xxxxxxxx/zxc7.png').convert_alpha(),
    pygame.image.load('zxc/xxxxxxxx/zxc8 (2).png').convert_alpha(),
    pygame.image.load('zxc/xxxxxxxx/zxc9.png').convert_alpha(),
    pygame.image.load('zxc/xxxxxxxx/zxc10.png').convert_alpha(),
    pygame.image.load('zxc/xxxxxxxx/zxc11.png').convert_alpha(),
    pygame.image.load('zxc/xxxxxxxx/zxc12 (2).png').convert_alpha(),
    pygame.image.load('zxc/xxxxxxxx/zxc13 (2).png').convert_alpha(),
    pygame.image.load('zxc/xxxxxxxx/zxc14.png').convert_alpha(),
    pygame.image.load('zxc/xxxxxxxx/zxc15.png').convert_alpha(),
    pygame.image.load('zxc/xxxxxxxx/zxc16.png').convert_alpha(),
    pygame.image.load('zxc/xxxxxxxx/zxc17 (2).png').convert_alpha(),
    pygame.image.load('zxc/xxxxxxxx/zxc18.png').convert_alpha(),
    pygame.image.load('zxc/xxxxxxxx/zxc19.png').convert_alpha(),
    pygame.image.load('zxc/xxxxxxxx/zxc20.png').convert_alpha(),
    pygame.image.load('zxc/xxxxxxxx/zxc1.png').convert_alpha(),
    pygame.image.load('zxc/xxxxxxxx/zxc21.png').convert_alpha(),
    pygame.image.load('zxc/xxxxxxxx/zxc22 (2).png').convert_alpha(),
    pygame.image.load('zxc/xxxxxxxx/zxc23.png').convert_alpha(),
    pygame.image.load('zxc/xxxxxxxx/zxc24.png').convert_alpha(),
    pygame.image.load('zxc/xxxxxxxx/zxc25 (2).png').convert_alpha(),
    pygame.image.load('zxc/xxxxxxxx/zxc26.png').convert_alpha(),
    pygame.image.load('zxc/xxxxxxxx/zxc27.png').convert_alpha(),
    pygame.image.load('zxc/xxxxxxxx/zxc28.png').convert_alpha(),
]
bat = pygame.image.load('gg/bat (1).png').convert_alpha()
bat_x = 1265
n = pygame.image.load('gg/imgonline-com-ua-Resize-U2gkqIt2ie7SznCz.jpg').convert()
gameplay = True
player_anim_count = 0
player_a = 100
a = 0
running = True
player_walk = 12.5
player_y = 589
bullets_zxc = 0
is_jump = False
jump_count = 9
bg_sound = pygame.mixer.Sound('Music/Clear Like Water(248+251) [1080p+medium]--online-audio-convert.com.mp3')
bg_sound.play()
bullet = pygame.image.load('gg/цыч.png').convert_alpha()
bullets = []
bat_timer = pygame.USEREVENT + 1
pygame.time.set_timer(bat_timer, 4000)
bullets_left = 9
label = pygame.font.Font('fff/ofont.ru_Maki Sans.ttf', 90)
zxc_label = pygame.font.Font('fff/213.ttf', 45)
lose_label = label.render('GG', False, (0, 119, 181))
rest_label = zxc_label.render('Try again ?', False, (237, 41, 57))
rest_rect = rest_label.get_rect(topleft=(3, 245))
while running:  # пока running == True
    screen.blit(Bg, (a, 0))
    screen.blit(Bg, (a + 1260, 0))
    if gameplay:

        keys = pygame.key.get_pressed()  # если ключ = ключ нажат

        player_rect = walk_left[0].get_rect(topleft=(player_a, player_y))

        if bullets:
            for i, el in enumerate(bullets):
                screen.blit(bullet, (el.x, el.y))
                el.x += 9.5

                if el.x > 1260:
                    bullets.pop(i)

            if bat_list:
                for (index, bat_el) in enumerate(bat_list):
                    if el.colliderect(bat_el):
                        bat_list.pop(index)
                        bullets.pop(i)

        if bat_list:
            for i in bat_list:
                screen.blit(bat, i)
                i.x -= 12.5

                if player_rect.colliderect(i):
                    gameplay = False
        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
        else:
            if jump_count >= -9:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 2
                else:
                    player_y += (jump_count ** 2) / 2
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 9

        if keys[pygame.K_LEFT]:
            screen.blit(walk_left[player_anim_count], (player_a, player_y))
        else:
            screen.blit(walk_right[player_anim_count], (player_a, player_y))

        if keys[pygame.K_LEFT] and player_a > 30:
            player_a -= player_walk
        elif keys[pygame.K_RIGHT] and player_a < 1100:
            player_a += player_walk

        if player_anim_count == (len(walk_right) - 1):
            player_anim_count = 0
        else:
            player_anim_count += 1

        a -= 5
        if a == -1260:
            a = 0

        bat_x -= 10
    else:
        print(bullets_left, bullets_zxc)
        screen.blit(n, (0, 0))
        screen.blit(lose_label, (5, 12))
        screen.blit(rest_label, rest_rect)
        bg_sound.stop()
        mouse = pygame.mouse.get_pos()
        if bullets_left < 9:
            bullets_left += bullets_zxc
        if rest_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_a = 100
            bat_list.clear()
            bg_sound.play()
            bullets.clear()
    pygame.display.update()  # обновляем дисплей во время цикла
    for event in pygame.event.get():  # который поможет нам получить список всех возможных событий

        if event.type == bat_timer:
            bat_list.append(bat.get_rect(topleft=(1255, 680)))

        if event.type == pygame.QUIT:  # если тип события это выход из прилложения
            running = False  # то прога прерывается
            pygame.quit()  # и вылетает
        elif event.type == pygame.KEYDOWN:  # если тип события это нажатие клавиши
            if event.key == pygame.K_w:  # клавиши 'w' то
                screen.fill((112, 23, 12))  # цвет меняется на тот, что мы указали в скобках (его RGB значение)
        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_f and bullets_left > 0:
            bullets.append(bullet.get_rect(topleft=(player_a + 60, player_y + 95)))
            bullets_left -= 1
            bullets_zxc += 1
    clock.tick(11)
#это мой первый проект который я делал сам; не судите строго ведб тогда я практически ничего не знал о стандартах написания кода таких как Pep8 :)
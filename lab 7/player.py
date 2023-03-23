import pygame

music = [r"C:\pp2\all labs\lab 7\files_for_7lab\songs_for_player\BTD.mp3", r"C:\pp2\all labs\lab 7\files_for_7lab\songs_for_player\ST.mp3", r"C:\pp2\all labs\lab 7\files_for_7lab\songs_for_player\IWBY.mp3", r"C:\pp2\all labs\lab 7\files_for_7lab\songs_for_player\FF.mp3", r"C:\pp2\all labs\lab 7\files_for_7lab\songs_for_player\WILY.mp3"]

def next_music():
    global music
    music = music[1:] +[music[0]]
    pygame.mixer.music.load(music[0])
    pygame.mixer.music.play()

def previous_music():
    global music
    music = [music[-1]] + music[:-1]
    pygame.mixer.music.load(music[0])
    pygame.mixer.music.play()

pygame.init()
done = False
play = True
screen = pygame.display.set_mode((500, 312))
clock = pygame.time.Clock()
background = pygame.image.load(r"C:\pp2\all labs\lab 7\files_for_7lab\images_for_player\ST.jpg")
center_of_background = background.get_rect(center=(250, 156))
screen.blit(background, center_of_background)
pygame.display.update()

SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)
next_music()



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
            play = not play
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT]: next_music()
    if pressed[pygame.K_LEFT]: previous_music()

    if not play:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
    pygame.display.flip()
    clock.tick(60)
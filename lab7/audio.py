import pygame
import os

# Initialize Pygame
pygame.init()

# Set screen dimensions (not used for this example)
screen_width = 400
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Player")

# Initialize Pygame mixer for audio playback
pygame.mixer.init()
# Load image
image_path = "C:/Users/Asus/Desktop/mysongs/alienpic.jpg"  # Path to your image file
image = pygame.image.load(image_path)



# Set up the music directory
music_directory = "C:/Users/Asus/Desktop/mysongs"

music_files = ['alien.mp3', 'close.mp3', 'volcano.mp3', 'wish You Back.mp3', 'streetlight.mp3', 'levanter.mp3']


music_images = {
    'alien.mp3': 'alienpic.jpg',
    'close.mp3': 'closepic.jpg',
    'volcano.mp3': 'volcanopic.jpg',
    'wish You Back.mp3': 'wishpic.jpg',
    'streetlight.mp3': 'streetlightpic.jpg',
    'levanter.mp3': 'levanterpic.jpg'
}

# Current index of the playing music
current_track_index = 0

# Load the first image
current_image = pygame.image.load(os.path.join(music_directory, music_images[music_files[current_track_index]]))
current_image = pygame.transform.scale(current_image, (screen_width, screen_height))

# Play the first track
pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track_index]))
pygame.mixer.music.play()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Play/Pause
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:  # Next track
                current_track_index = (current_track_index + 1) % len(music_files)
                current_image = pygame.image.load(os.path.join(music_directory, music_images[music_files[current_track_index]]))
                current_image = pygame.transform.scale(current_image, (screen_width, screen_height))
                pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track_index]))
                pygame.mixer.music.play()

            elif event.key == pygame.K_LEFT:  # Previous track
                current_track_index = (current_track_index - 1) % len(music_files)
                current_image = pygame.image.load(os.path.join(music_directory, music_images[music_files[current_track_index]]))
                current_image = pygame.transform.scale(current_image, (screen_width, screen_height))
                pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track_index]))
                pygame.mixer.music.play()

    # Fill the screen with the current image
    screen.blit(current_image, (0, 0))
    pygame.display.flip()
# Quit Pygame 
pygame.quit()



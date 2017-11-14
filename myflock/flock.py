import sys, random
import pyglet
from bird import Bird

# from game import load, resources

# assumes bird sprite is in current directory
screen_width = 1200  
screen_height = 1000

def birds(num_birds, batch=None):
    """Generate bird objects with random positions and velocities,"""
    Bird.set_screen(screen_width, screen_height)
    birds = []
    for i in range(num_birds):

        bird_x = random.randint(0, screen_width)
        bird_y = random.randint(0, screen_height)
        new_bird = Bird(img=bird_image, x=bird_x, y=bird_y, batch=batch)
        new_bird.rotation = random.randint(0, 360)
        new_bird.speed = random.random() * 40
        birds.append(new_bird)
    return birds

bird_image = pyglet.resource.image("birdSprite.png")
bird_image.anchor_x = bird_image.width / 2
bird_image.anchor_y = bird_image.height / 2    
    
# Set up a window
game_window = pyglet.window.Window(screen_width, screen_height)
main_batch = pyglet.graphics.Batch()

# Make three birds so we have something to shoot at 
birds = birds(12, main_batch)
game_objects = birds

@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()

def update(dt):
    for obj in game_objects:  obj.update(dt)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        screen_width = int(sys.argv[0])
        screen_heigth = int(sys.argv[1])
    # Tell pyglet to do its thing
    print(birds)
    pyglet.clock.schedule_interval(update, 1 / 30.0)
    pyglet.app.run()
    
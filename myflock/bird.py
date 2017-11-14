import pyglet
from math import cos, sin, radians

class Bird(pyglet.sprite.Sprite):
    """A sprite with physical properties such as velocity"""
    @classmethod
    
    def set_screen(cls, w, h):
        cls.screen_width = w
        cls.screen_height = h
    
    def __init__(self, *args, **kwargs):
        ''' Bird(sreen=(<width>,<height>)) required '''
        super(Bird, self).__init__(*args, **kwargs)
        self.speed = 0.0

    def update(self, dt):
        """This method should be called every frame."""
        r_degree = radians(self.rotation)
        speed_x = self.speed * cos(r_degree)
        speed_y = -self.speed * sin(r_degree)
        self.x += speed_x * dt   # update x,y
        self.y += speed_y * dt
        # print(f'moved to {self.x},{self.y}')
        self.check_bounds()  # wrap if needed

    def check_bounds(self):
        """Use the classic Asteroids screen wrapping behavior"""
        # off screen when object center half way off
        min_x = -self.image.width / 2 
        min_y = -self.image.height / 2
        max_x = Bird.screen_width + self.image.width / 2
        max_y = Bird.screen_height + self.image.height / 2
        if self.x < min_x: self.x = max_x
        if self.y < min_y: self.y = max_y
        if self.x > max_x: self.x = min_x
        if self.y > max_y: self.y = min_y
        
    def __repr__(self):
        return f"Bird(location=({self.x:},{self.y}) speed={self.speed:.1f})"
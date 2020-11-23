from laserbeam import LaserBeam
from asteroid import Asteroid
from spaceship import Spaceship


class GameController:
    """
    Maintains the state of the game
    and manages interactions of game elements.
    """

    def __init__(self, SPACE, fadeout):
        """Initialize the game controller"""
        self.SPACE = SPACE
        self.fadeout = fadeout

        self.spaceship_hit = False
        self.asteroid_destroyed = False
        self.asteroids = [Asteroid(self.SPACE)]
        self.laser_beams = []
        self.spaceship = Spaceship(self.SPACE)

    def update(self):
        """Updates game state on every frame"""
        self.do_intersections()

        for asteroid in self.asteroids:
            if asteroid.intact:
                asteroid.display()
            else:
                self.asteroids.remove(asteroid)
        if not self.asteroids:
            self.asteroid_destroyed = True

        # Laser beam handler

        for l in (self.laser_beams):
            if l.start_frame >= frameCount - 100 and l.intact:
                l.display()
            else:
                self.laser_beams.remove(l)


        self.spaceship.display()

        # Carries out necessary actions if game over
        if self.spaceship_hit:
            if self.fadeout <= 0:
                fill(1)
                textSize(30)
                text("YOU HIT AN ASTEROID",
                     self.SPACE['w']/2 - 165, self.SPACE['h']/2)
            else:
                self.fadeout -= 1

        if self.asteroid_destroyed:
            fill(1)
            textSize(30)
            text("YOU DESTROYED THE ASTEROIDS!!!",
                 self.SPACE['w']/2 - 250, self.SPACE['h']/2)

    def fire_laser(self, x, y, rot):
        """Add a laser beam to the game"""
        x_vel = sin(radians(rot))
        y_vel = -cos(radians(rot))
        self.laser_beams.append(
            LaserBeam(self.SPACE, x, y, x_vel, y_vel, frameCount)
            )

    def handle_keypress(self, key, keycode=None):
        if (key == ' '):
            if self.spaceship.intact:
                self.spaceship.control(' ', self)
        if (keycode):
            if self.spaceship.intact:
                self.spaceship.control(keycode)

    def handle_keyup(self):
        if self.spaceship.intact:
            self.spaceship.control('keyup')

    def do_intersections(self):
        # Check each asteroid for intersection
        for i in range(len(self.asteroids)):
            for j in range(len(self.laser_beams)):
                if (
                        abs(self.asteroids[i].x - self.laser_beams[j].x)
                        < max(self.asteroids[i].radius, self.laser_beams[j].radius)
                        and
                        abs(self.asteroids[i].y - self.laser_beams[j].y)
                        < max(self.asteroids[i].radius, self.laser_beams[j].radius)
                   ):
                    self.blow_up_asteroid(i, j)

        # If the space ship still hasn't been blown up
        if self.spaceship.intact:
            # Check each asteroid for intersection
            for i in range(len(self.asteroids)):
                if (
                      abs(self.spaceship.x - self.asteroids[i].x)
                      < max(self.asteroids[i].radius, self.spaceship.radius)
                      and
                      abs(self.spaceship.y - self.asteroids[i].y)
                      < max(self.asteroids[i].radius, self.spaceship.radius)
                  ):
                    # We've intersected an asteroid
                    self.spaceship.blow_up(self.fadeout)
                    self.spaceship_hit = True

    def blow_up_asteroid(self, i, j):
        # Asteroid blow-up

        self.asteroids[i].intact = False
        self.laser_beams[j].intact = False
        # Add new astroids.
        x = self.asteroids[i].x
        y = self.asteroids[i].y
        x_vel = self.laser_beams[j].x_vel
        y_vel = self.laser_beams[j].y_vel
        if self.asteroids[i].asize == 'Large':
            self.asteroids.append(Asteroid(self.SPACE, 'Med', x, y, x_vel=y_vel / 5, y_vel=-x_vel / 5))
            self.asteroids.append(Asteroid(self.SPACE, 'Med', x, y, x_vel=-y_vel/5, y_vel=x_vel/5))
        if self.asteroids[i].asize == 'Med':
            self.asteroids.append(Asteroid(self.SPACE, 'Small', x, y, x_vel=y_vel / 5, y_vel=-x_vel / 5))
            self.asteroids.append(Asteroid(self.SPACE, 'Small', x, y, x_vel=-y_vel/5, y_vel=x_vel/5))
            self.asteroids.append(Asteroid(self.SPACE, 'Small', x, y, x_vel=x_vel/5, y_vel=y_vel/5))

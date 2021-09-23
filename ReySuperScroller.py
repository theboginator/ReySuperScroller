"""
This super scroller game lets the player manipulate Rey the fox as he shoots his pellet gun at absolutely nothing.
He can move up or down as he runs along the map.

The base code is built off the code provided in-class.

The moving background code was built from an example found here:
https://stackoverflow.com/questions/55167496/infinite-scrolling-background-in-python


"""
import arcade
import pathlib
from enum import auto, Enum

SCREEN_WIDTH = 1821
SCREEN_HEIGHT = 1024
BG_WIDTH = 1821
SCROLLRATE = 3


class MoveEnum(Enum):
    NONE = auto()
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()


class MinimalSprite(arcade.Sprite):
    def __init__(self, ship_path: str, speed: int, game_window):
        super().__init__(ship_path)
        self.speed = speed
        self.game = game_window

    def move(self, direction: MoveEnum):
        # as a class exercise, lets fix this so it doesn't go off the window
        if direction == MoveEnum.UP:
            self.center_y += self.speed
        elif direction == MoveEnum.DOWN:
            self.center_y -= self.speed
        elif direction == MoveEnum.LEFT:
            self.center_x -= self.speed
        elif direction == MoveEnum.RIGHT:
            self.center_x += self.speed
        else:  # should be MoveEnum.NONE
            pass


class MimimalArcade(arcade.Window):

    def __init__(self, image_name: str, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.image_path = pathlib.Path.cwd() / 'assets' / image_name
        self.bga_path = pathlib.Path.cwd() / 'assets' / 'BGA.png'
        self.bgb_path = pathlib.Path.cwd() / 'assets' / 'BGB.png'
        self.pict = None
        self.direction = MoveEnum.NONE
        self.pictlist = None
        self.background_sprite_2 = arcade.Sprite(self.bgb_path)
        self.background_sprite = arcade.Sprite(self.bga_path)
        self.background_list = arcade.SpriteList()

    def setup(self):
        # SETUP THE PLAYER SPRITE:
        self.pict = MinimalSprite(str(self.image_path), speed=3, game_window=self)
        self.pict.center_x = 500
        self.pict.center_y = 500
        self.pictlist = arcade.SpriteList()
        self.pictlist.append(self.pict)

        # SETUP THE BACKGROUND IMAGES:

        self.background_sprite.center_x = BG_WIDTH // 2
        self.background_sprite.center_y = SCREEN_HEIGHT // 2
        self.background_sprite.change_x = -SCROLLRATE

        self.background_list.append(self.background_sprite)

        # SECOND BACKGROUND IMAGE

        self.background_sprite_2.center_x = SCREEN_WIDTH + BG_WIDTH // 2
        self.background_sprite_2.center_y = SCREEN_HEIGHT // 2
        self.background_sprite_2.change_x = -SCROLLRATE

        self.background_list.append(self.background_sprite_2)


    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        # Code to draw the screen goes here
        self.background_list.draw()
        self.pictlist.draw()

    def update(self, delta_time: float):
        # to get really smooth movement we would use the delta time to
        # adjust the movement, but for this simple version I'll forgo that.
        self.pict.move(self.direction)
        if self.background_sprite.right < 0:
            self.background_sprite.center_x = self.background_sprite_2.center_x + BG_WIDTH

        if self.background_sprite_2.right < 0:
            self.background_sprite_2.center_x = self.background_sprite.center_x + BG_WIDTH

        self.background_list.update()



    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.UP or key == arcade.key.W:
            self.direction = MoveEnum.UP
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.direction = MoveEnum.DOWN
        """
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.direction = MoveEnum.LEFT
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.direction = MoveEnum.RIGHT
        """
    def on_key_release(self, key: int, modifiers: int):
        """called by arcade for keyup events"""
        if (key == arcade.key.UP or key == arcade.key.W) and \
                self.direction == MoveEnum.UP:
            self.direction = MoveEnum.NONE
        if (key == arcade.key.DOWN or key == arcade.key.S) and \
                self.direction == MoveEnum.DOWN:
            self.direction = MoveEnum.NONE
        if (key == arcade.key.LEFT or key == arcade.key.A) and \
                self.direction == MoveEnum.LEFT:
            self.direction = MoveEnum.NONE
        if (key == arcade.key.RIGHT or key == arcade.key.D) and \
                self.direction == MoveEnum.RIGHT:
            self.direction = MoveEnum.NONE


def main():
    """ Main method """
    window = MimimalArcade("armed_rey.png", SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()


if __name__ == '__main__':
    main()

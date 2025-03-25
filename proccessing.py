import pygame
import objs


def find_id(id_):
    nums = []
    for char in id_:
        if char.isdigit():
            nums.append(char)

    id_ = ""
    for num in nums:
        id_ += num
    id_ = int(id_)

    return id_


class Main:
    def __init__(self, parent):
        pygame.init()
        self.parent = parent

    def ev(self, text):
        text = text.lower()
        if 'move' in text:
            self.move(text)
        if 'resize' in text:
            self.resize(text)
        if 'new' in text:
            self.new(text)
        if 'color' in text or 'colour' in text:
            self.color(text)

    def move(self, text):
        text = text.split()
        id_ = find_id(text[0])
        Horizontal = ("left", "right", "Right", "Left", "write")
        Vertical = ("up", "down", "Down", "Up")

        x, y = 0, 0

        for i in range(len(text)):
            part = text[i]

            par = part.split(",")
            part = par[0] + par[1] if len(par) > 1 else part

            if part in Horizontal:
                x = int(text[i + 1])
                if part == "left":
                    x = x * -1
            if part in Vertical:
                y = int(text[i + 1])
                if part == "up":
                    y = y * -1

        print("id" + str(id_))
        print("x" + str(x))
        print("y" + str(y))

        try:
            self.parent.objs[id_].rect.x += int(x)
            self.parent.objs[id_].rect.y += int(y)
        except (ValueError, IndexError):
            pass

    def resize(self, text):
        text = text.split()
        id_ = find_id(text[0])

        width, height = self.parent.objs[id_].rect.width, self.parent.objs[id_].rect.height

        for i in range(len(text)):
            part = text[i]
            if part == "width" or part == "with":
                width = int(text[i + 1])
            if part == "height" or part == "kite":
                height = int(text[i + 1])

        print("id" + str(id_))
        print("width" + str(width))
        print("height" + str(height))

        try:
            self.parent.objs[id_].rect.width = width
            self.parent.objs[id_].rect.height = height
            self.parent.objs[id_].rect.x -= int(width) / 2
            self.parent.objs[id_].rect.y -= int(height) / 2
            self.parent.objs[id_].surface = pygame.Surface((width, height))
        except (ValueError, IndexError):
            pass

    def new(self, text):
        self.parent.objs.append(objs.Obj(self.parent.visuals, 100, 100, 50, 50))
        if text == "square":
            pass

    def color(self, text):
        text = text.split()
        id_ = find_id(text[0])

        r, g, b = 255, 255, 255  # Default color

        for i in range(len(text)):
            part = text[i]
            if part == "red":
                try:
                    r = int(text[i + 1])
                except (ValueError, IndexError):
                    r = 0
            if part == "green":
                try:
                    g = int(text[i + 1])
                except (ValueError, IndexError):
                    g = 0
            if part == "blue":
                try:
                    b = int(text[i + 1])
                except (ValueError, IndexError):
                    b = 0

        print("id" + str(id_))
        print("color" + str((r, g, b)))

        try:
            self.parent.objs[id_].color = (r, g, b)
        except (ValueError, IndexError):
            pass

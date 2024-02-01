import pyray as pr
from raylib import colors


class Button: #класс кнопки
    def __init__(self, x_center, y_center, width, height, text, color_bg, color_text, color_nk, font_size=30):
        self.x = x_center
        self.y = y_center
        self.w = width
        self.h = height
        self.t = text
        self.c1 = color_bg
        self.c2 = color_text
        self.c3 = color_nk
        self.f = font_size

    def draw(self):
        pr.draw_rectangle_rounded(
            pr.Rectangle(self.x - self.w // 2, self.y - self.h // 2, self.w, self.h), #рисуем кнопку
            0.4, 100, self.c1)


        pr.draw_text(self.t, self.x - pr.measure_text(self.t, self.f) // 2, self.y - self.f // 2, self.f, self.c3) #текст с его постоянным цветом

        pr.draw_rectangle_rounded_lines(
            pr.Rectangle(self.x - self.w // 2, self.y - self.h // 2, self.w, self.h), 0.4, 100, 4, self.c3) #постоянная обводка кнопки

        if self.is_hover():
            pr.draw_rectangle_rounded_lines(pr.Rectangle(self.x - self.w // 2, self.y - self.h // 2, self.w, self.h), 0.4, 100, 4, self.c2) #обводка кнопки при наведении
            pr.draw_text(self.t, self.x - pr.measure_text(self.t, self.f) // 2, self.y - self.f // 2, self.f, self.c2) #текст при наведении

    def is_hover(self):
        if pr.check_collision_point_rec(pr.get_mouse_position(), pr.Rectangle(self.x - self.w // 2, self.y - self.h // 2, self.w, self.h)):
            return True
        return False

    def is_clicked(self):
        if (pr.check_collision_point_rec(pr.get_mouse_position(), pr.Rectangle(self.x - self.w // 2, self.y - self.h // 2, self.w, self.h)) and pr.is_mouse_button_pressed(0)):
            return True
        return False



class Calculator:
    def __init__(self):
        """ Initializing UI objects """
        print("init")

    def draw(self):
        """ Drawing UI objects """
        print("draw")

    def proccess(self):
        """ Buttons logic """
        print("proccess")

class Application:
    def __init__(self):
        pr.init_window(1200, 1020, "RoCalc")
        pr.set_target_fps(30)
        self.scenes = {
            'calculator': Calculator(),
        }
        self.current_scene = 'calculator'

    def run(self):
        while not pr.window_should_close():
            pr.begin_drawing()
            self.scenes[self.current_scene].draw()
            pr.end_drawing()
            self.scenes[self.current_scene].proccess()
            if (self.current_scene != self.scenes[self.current_scene].scene):
                self.current_scene = self.scenes[self.current_scene].scene
                self.scenes['calculator'].scene = 'calculator'
        pr.close_window()


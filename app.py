import pyray as pr
from raylib import colors


class Button: #класс кнопки
    def __init__(self, x_center, y_center, width, height, text, color_bg, color_text, color_nk, font_size=70):
        self.x = x_center
        self.y = y_center
        self.w = width
        self.h = height
        self.t = text
        self.c1 = color_bg
        self.c2 = color_text
        self.c3 = color_nk
        self.f = font_size
        self.font = pr.load_font("fonts/CascadiaMono-Bold.otf")

    def draw(self):
        pr.draw_rectangle_rounded(
            pr.Rectangle(self.x - self.w // 2, self.y - self.h // 2, self.w, self.h), #рисуем кнопку
            0.4, 100, self.c1)

        text_pos = self.x - pr.measure_text(self.t, self.f) // 2, self.y - self.f // 2
        pr.draw_text_ex(self.font, self.t, text_pos, self.f, 1, self.c3) #текст с его постоянным цветом

        pr.draw_rectangle_rounded_lines(
            pr.Rectangle(self.x - self.w // 2, self.y - self.h // 2, self.w, self.h), 0.4, 100, 4, self.c3) #постоянная обводка кнопки

        if self.is_hover():
            pr.draw_rectangle_rounded_lines(pr.Rectangle(self.x - self.w // 2, self.y - self.h // 2, self.w, self.h), 0.4, 100, 4, self.c2) #обводка кнопки при наведении
            pr.draw_text_ex(self.font, self.t, text_pos, self.f, 1, self.c2) #текст при наведении

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
        self.seven = Button(60, 200, 100, 100, "7", colors.BLACK, colors.WHITE, colors.GRAY)
        self.eight = Button(180, 200, 100, 100, "8", colors.BLACK, colors.WHITE, colors.GRAY)
        self.nine = Button(300, 200, 100, 100, "9", colors.BLACK, colors.WHITE, colors.GRAY)

        self.four = Button(60, 320, 100, 100, "4", colors.BLACK, colors.WHITE, colors.GRAY)
        self.five = Button(180, 320, 100, 100, "5", colors.BLACK, colors.WHITE, colors.GRAY)
        self.six = Button(300, 320, 100, 100, "6", colors.BLACK, colors.WHITE, colors.GRAY)

        self.three = Button(60, 440, 100, 100, "3", colors.BLACK, colors.WHITE, colors.GRAY)
        self.two = Button(180, 440, 100, 100, "2", colors.BLACK, colors.WHITE, colors.GRAY)
        self.one = Button(300, 440, 100, 100, " 1  ", colors.BLACK, colors.WHITE, colors.GRAY)
        self.zero = Button(60, 560, 100, 100, "0", colors.BLACK, colors.WHITE, colors.GRAY)

        self.divide = Button(420, 200, 100, 100, " / ", colors.BLACK, colors.WHITE, colors.GRAY)
        self.minus = Button(420, 320, 100, 100, "-", colors.BLACK, colors.WHITE, colors.GRAY)
        self.multiply = Button(420, 440, 100, 100, "*", colors.BLACK, colors.WHITE, colors.GRAY)
        self.plus = Button(420, 560, 100, 100, "+", colors.BLACK, colors.WHITE, colors.GRAY)
        self.equal = Button(300, 560, 100, 100, "=", colors.BLACK, colors.WHITE, colors.GRAY)
        self.dot = Button(180, 560, 100, 100, ". ", colors.BLACK, colors.WHITE, colors.GRAY)

    def draw(self):
        """ Drawing UI objects """
        pr.clear_background(colors.LIGHTGRAY)
        outx = 240
        outy = 75
        outh = 110
        outw = 450
        pr.draw_rectangle_rounded_lines(
            pr.Rectangle(outx - outw // 2, outy - outh // 2, outw, outh),
            0.1, 100, 5, colors.GRAY)
        pr.draw_rectangle_rounded(
            pr.Rectangle(outx - outw // 2, outy - outh // 2, outw, outh),
            0.1, 100, colors.WHITE)

        self.seven.draw()
        self.eight.draw()
        self.nine.draw()

        self.four.draw()
        self.five.draw()
        self.six.draw()

        self.three.draw()
        self.two.draw()
        self.one.draw()
        self.zero.draw()

        self.plus.draw()
        self.minus.draw()
        self.multiply.draw()
        self.divide.draw()
        self.equal.draw()
        self.dot.draw()

        output = "test"
        pr.draw_text_ex(pr.load_font("fonts/CascadiaMono-Bold.otf"), output, (250, 25), 100, 1, colors.BLACK, "right")

    def proccess(self):
        # if self.seven.is_clicked:
        #     output += "7"
        # if self.eight.is_clicked:
        #     output += "8"
        # if self.nine.is_clicked:
        #     output += "9"
        #
        # if self.four.is_clicked:
        #     output += "4"
        self.five.draw()
        self.six.draw()

        self.three.draw()
        self.two.draw()
        self.one.draw()
        self.zero.draw()

        self.plus.draw()
        self.minus.draw()
        self.multiply.draw()
        self.divide.draw()
        self.equal.draw()
        self.dot.draw()

class Application:
    def __init__(self):
        pr.init_window(480, 620, "RoCalc")
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
        pr.close_window()


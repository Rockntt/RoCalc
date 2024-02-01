import pyray as pr
from raylib import colors

def calculate(expression):
    try:
        result = round(eval(expression), 4)  # Используем встроенную функцию eval для вычисления выражения
        return result
    except Exception as e:
        return "Error"

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
        self.font = pr.load_font("fonts/CascadiaMono-Bold.otf")

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

        self.output = ""
        self.outx = 240
        self.outy = 75
        self.outh = 110
        self.outw = 450
        self.out_str_x = 450

    def draw(self):
        """ Drawing UI objects """
        pr.clear_background(colors.LIGHTGRAY)

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

        pr.draw_rectangle_rounded(
            pr.Rectangle(self.outx - self.outw // 2, self.outy - self.outh // 2, self.outw, self.outh),
            0.1, 100, colors.WHITE)

        pr.draw_text_ex(self.font, self.output, (self.out_str_x, 25), 100, 1, colors.BLACK)

        pr.draw_rectangle_rounded(
            pr.Rectangle((self.outx - self.outw // 2) - 450, self.outy - self.outh // 2, self.outw, self.outh),
            0.1, 100, colors.LIGHTGRAY)

        pr.draw_rectangle_rounded_lines(
            pr.Rectangle(self.outx - self.outw // 2, self.outy - self.outh // 2, self.outw, self.outh),
            0.1, 100, 5, colors.GRAY)


    def proccess(self):
        n = 51
        if pr.is_key_pressed(259):
            self.output = ""
            self.out_str_x = 450
        if self.seven.is_clicked():
            self.output += "7"
            self.out_str_x -= n
        if self.eight.is_clicked():
            self.output += "8"
            self.out_str_x -= n
        if self.nine.is_clicked():
            self.output += "9"
            self.out_str_x -= n

        if self.four.is_clicked():
            self.output += "4"
            self.out_str_x -= n
        if self.five.is_clicked():
            self.output += "5"
            self.out_str_x -= n
        if self.six.is_clicked():
            self.output += "6"
            self.out_str_x -= n

        if self.three.is_clicked():
            self.output += "3"
            self.out_str_x -= n
        if self.two.is_clicked():
            self.output += "2"
            self.out_str_x -= n
        if self.one.is_clicked():
            self.output += "1"
            self.out_str_x -= n
        if self.zero.is_clicked():
            self.output += "0"
            self.out_str_x -= n

        if self.plus.is_clicked():
            self.output += "+"
            self.out_str_x -= n
        if self.minus.is_clicked():
            self.output += "-"
            self.out_str_x -= n
        if self.multiply.is_clicked():
            self.output += "*"
            self.out_str_x -= n
        if self.divide.is_clicked():
            self.output += "/"
            self.out_str_x -= n
        if self.equal.is_clicked():
            self.output = str(calculate(self.output))
            self.out_str_x = 450
            self.out_str_x -= len(self.output) * 51
        if self.dot.is_clicked():
            self.output += "."
            self.out_str_x -= n

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


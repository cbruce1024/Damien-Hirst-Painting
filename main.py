# import colorgram
#
# rgb_colors = []
#
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(236, 219, 86), (125, 177, 150), (162, 85, 45), (200, 150, 119), (26, 116, 162), (102, 179, 207), (51, 17, 6), (196, 149, 155), (138, 164, 30), (169, 12, 22), (63, 117, 66), (229, 175, 167), (219, 89, 60), (140, 62, 70), (222, 175, 184), (12, 96, 34), (28, 171, 208), (163, 20, 16), (14, 73, 33), (98, 87, 10), (3, 43, 102), (76, 169, 143), (6, 47, 143), (162, 206, 187), (50, 11, 14), (229, 215, 10)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()






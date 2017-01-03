#!/usr/bin/env python3

black = (0, 0, None)
brown = (1, 1, 1.0)
red = (2, 2, 2)
orange = (3, 3, None)
yellow = (4, 4, None)
green = (5, 5, 0.5)
blue = (6, 6, 0.25)
violet = (7, 7, 0.1)
grey = (8, 8, None)
white = (9, 9, None)
gold = (None, -1, 5.0)
silver = (None, -2, 10.0)
_none = (None, None, 20.0)


def calc_colors(ohm, tolerance):
    raise NotImplementedError()
    numbers = [int(num) for num in ohm if num in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]]

    colors = []
    tolerance_color = None

    # validate itself
    if (ohm, tolerance) == translate_colors(colors, tolerance=tolerance_color):
        return colors, tolerance_color
    else:
        raise Exception("Impossible resistor")


def _get_matching_color(color):
    color = str(color).lower()
    if color in ['black', 'bl']:
        return black
    elif color in ['brown', 'br']:
        return brown
    elif color in ['red', 'r']:
        return red
    elif color in ['orange', 'o']:
        return orange
    elif color in ['yellow', 'y']:
        return yellow
    elif color in ['green', 'gn']:
        return green
    elif color in ['blue', 'b']:
        return blue
    elif color in ['violet', 'v']:
        return violet
    elif color in ['grey', 'gy']:
        return grey
    elif color in ['white', 'w']:
        return white
    elif color in ['gold', 'gd']:
        return gold
    elif color in ['silver', 's']:
        return silver
    else:
        return _none


def translate_colors(*color_args, tolerance=None):
    if len(color_args) > 4:
        raise Exception("Resistors can not have more than 3 digits and 1 multiplier")
    colors = [_get_matching_color(color) for color in color_args]
    numbers = [color[0] for color in colors[:-1]]
    multi = (colors[-1])[1]
    tolerance = _get_matching_color(tolerance)[2]

    num_code = ''.join([str(color) for color in numbers])
    ohm = float(num_code)
    if multi == 0:
        pass
    elif multi != 0:
        ohm *= (10 ** multi)

    return ohm, tolerance


def print_translated_colors(ohm, tolerance):
    print("%s, +/-%s%%" % (ohm, tolerance))


if __name__ == '__main__':
    print_translated_colors(*translate_colors("Green", "Red", "Gold", tolerance="Silver"))
    print("CORRECT IS: 5.2, +/- 10%")
    print_translated_colors(*translate_colors("White", "Violet", "Black"))
    print("CORRECT IS: 97, +/- 20%")
    print_translated_colors(*translate_colors("Brown", "Green", "Grey", "Silver", tolerance="Red"))
    print("CORRECT IS: 1.58, +/- 2%")

    # print("\n\n##################################\n\n")
    #
    # print(calc_colors(5.2, 10))
    # print("CORRECT IS: Green, Red, Gold | Silver")
    # print(calc_colors(97, 20))
    # print("CORRECT IS: White, Violet, Black | None")
    # print(calc_colors(1.58, 2))
    # print("CORRECT IS: Brown, Green, Silver | Red")

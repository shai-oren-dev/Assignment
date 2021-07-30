from colorama import init, Fore, Style


class ColorHandler:

    @staticmethod
    def convert_true():
        init(convert=True)

    @staticmethod
    def print_highlighted_text(color, text):
        '''
        print highlighted text by required color string
        :param color: color to highlight text
        :param text: text to highlight
        :return:None,
        '''
        ColorHandler.convert_true()
        if str(color).lower() == "black":
            color = Fore.BLACK
        elif str(color).lower() == "red":
            color = Fore.RED
        elif str(color).lower() == "green":
            color = Fore.GREEN
        elif str(color).lower() == "yellow":
            color = Fore.YELLOW
        elif str(color).lower() == "blue":
            color = Fore.BLUE
        elif str(color).lower() == "magenta":
            color = Fore.MAGENTA
        elif str(color).lower() == "cyan":
            color = Fore.CYAN
        else:
            color = Style.RESET_ALL
        print(color + str(text) + Style.RESET_ALL)


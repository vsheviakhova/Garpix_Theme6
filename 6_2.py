class ListWorker:
    def __init__(self, *args):
        args_numbers = []
        args_strings = []
        args_else = []
        for arg in args:
            if type(arg) == int:
                args_numbers.append(arg)
            elif type(arg) == str:
                args_strings.append(arg)
            else:
                args_else.append(arg)
        self.args_numbers = args_numbers
        self.args_strings = args_strings
        self.args_else = args_else

    def get_numbers(self):
        return self.args_numbers

    def get_strings(self):
        return self.args_strings

    def get_else(self):
        return self.args_else

# тестирую класс
#a = ListWorker(12, 35, 67, 'dkfjdkjf', 'dkfjkdjfkdjfj', 'ieurmv', [23, 'kdfkjdf'], {3:54, 'dfk':45})
#print(a.get_numbers())
#print(a.get_strings())
#print(a.get_else())

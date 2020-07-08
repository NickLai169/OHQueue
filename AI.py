breakers = [" ", ",", "@"]

class BasicInput:

    def __init__(self, piece):
        self.my_piece = piece

    def make_fragments(self, string):
        while string:
            temp_string = ''
            while not string[0] in breakers:
                print('make')
                temp_string += string[0]
                string = string[1:]
            exec_str = temp_string + ' = BasicInput("{0}")'.format(temp_string)
            print(exec_str)
            exec(exec_str)




a = """
def bob():
"""
a += "\n    print('johnstone')"

exec(a)
bob()

# hel = BasicInput('my piece')


# hel.make_fragments(hel.my_piece)

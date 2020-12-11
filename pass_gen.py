import random

class pass_gen:

    @staticmethod
    #n = number of elements
    def generate_pass(n):
        password = ""
        for i in range(0,n):
            rand_char = chr(random.randint(33, 127))
            password += rand_char
        
        return password



    
import random
import string

class Utility:

    def __init__(self, driver):
        super().__init__(driver)

    def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))



import string
import random


TINY_URL = "tinyurl.com/"
choices = string.ascii_letters + string.digits
random_choice = "".join(random.choice(choices) for _ in range(10))
short_url = TINY_URL + random_choice

print(short_url)

choice = short_url.replace(TINY_URL, "")
print(choice)
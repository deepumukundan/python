s = 'hElLo WORLD'
print(s.lower())  # Output: hello world
print(s.upper())  # Output: HELLO WORLD
print(s.title())  # Output: Hello World
print(s.capitalize())  # Output: Hello world
print(s.swapcase())  # Output: HELLO world
print(s.casefold())  # Output: hello world
print(s.islower())  # Output: False
print(s.isupper())  # Output: False
print(s.istitle())  # Output: False
print(s.isalpha())  # Output: False (contains space)
print(s.isalnum())  # Output: False (contains space)
print(s.isdigit())  # Output: False (contains letters)
print(s.isnumeric())  # Output: False (contains letters)
print(s.isascii())  # Output: True (all characters are ASCII)
print(s.isprintable())  # Output: True (all characters are printable)
print(s.startswith('hello'))  # Output: True
print(s.endswith('WORLD'))  # Output: True
print(s.find('WORLD'))  # Output: 6 (index of 'WORLD')
print(s.index('WORLD'))  # Output: 6 (index of 'WORLD')
print(s.count('l'))  # Output: 2 (count of 'l')
print(s.replace('WORLD', 'Python'))  # Output: hello Python
print(s.split())  # Output: ['hello', 'WORLD']
print(s.join(['Python', 'is', 'great']))  # Output: Pythonhello WORLD
print(s.strip())  # Output: hello WORLD (no leading/trailing whitespace)
print(s.lstrip())  # Output: hello WORLD (no leading whitespace)
print(s.rstrip())  # Output: hello WORLD (no trailing whitespace)
print(s.partition(' '))  # Output: ('hello', ' ', 'WORLD')
print(s.rpartition(' '))  # Output: ('hello ', ' ', 'WORLD')
print(s.splitlines())  # Output: ['hello WORLD'] (no newlines)
print(s.zfill(15))  # Output: 00000hello WORLD (pads with zeros)
print(s.center(20))  # Output: '   hello WORLD    ' (centers the string)
print(s.ljust(20))  # Output: 'hello WORLD        ' # Left-justifies the string
print(s.rjust(20))  # Output: '        hello WORLD' # Right-justifies the string
print(s.expandtabs(4))  # Output: 'hello WORLD' (no tabs to expand)
print(s.removeprefix('hello '))  # Output: WORLD (removes prefix)
print(s.removesuffix('WORLD'))  # Output: hello (removes suffix)
# print(s.translate(str.maketrans('', '', 'l'))  # Output: heo WOR (removes 'l')
print(s.encode('utf-8'))  # Output: b'hello WORLD' (encodes to bytes)
# print(s.decode('utf-8'))  # Output: hello WORLD (decodes bytes to string)
print(s.format())  # Output: hello WORLD (no placeholders to format)
print(s.format_map({'greeting': 'hello', 'subject': 'WORLD'}))  # Output: hello WORLD (no placeholders to format)
# print(s.fstring())  # Output: hello WORLD (no f-string syntax in Python 3.6+)
# print(s.remove('WORLD'))  # Raises ValueError: substring not found
print(s.split(' '))  # Output: ['hello', 'WORLD'] (splits by space)
print(s.rsplit(' '))  # Output: ['hello', 'WORLD'] (splits by space from the right)
print(s.partition(' '))  # Output: ('hello', ' ', 'WORLD')
print(s.rpartition(' '))  # Output: ('hello ', ' ', 'WORLD')
print(s.format('hello', 'WORLD'))  # Raises TypeError: not enough arguments for format string
# print(s.format_map({'greeting': 'hello', 'subject': 'WORLD'})  # Output: hello WORLD (no placeholders to format)
# print(s.fstring())  # Raises AttributeError: 'str' object has no attribute 'fstring'
# print(s.remove('WORLD'))  # Raises ValueError: substring not found
print(s.split(' '))  # Output: ['hello', 'WORLD'] (splits by space)
print(s.rsplit(' '))  # Output: ['hello', 'WORLD'] (splits by space from the right)
print(s.partition(' '))  # Output: ('hello', ' ', 'WORLD')
print(s.rpartition(' '))  # Output: ('hello ', ' ', 'WORLD')
print(s.format('hello', 'WORLD'))  # Raises TypeError: not enough arguments for format string
print(s.format_map({'greeting': 'hello', 'subject': 'WORLD'}))  # Output: hello WORLD (no placeholders to format)
# print(s.fstring())  # Raises AttributeError: 'str' object has no attribute 'fstring'
# print(s.remove('WORLD'))  # Raises ValueError: substring not found
print(s.split(' '))  # Output: ['hello', 'WORLD'] (splits by space)
print(s.rsplit(' '))  # Output: ['hello', 'WORLD'] (splits by space from the right)
print(s.partition(' '))  # Output: ('hello', ' ', 'WORLD')
print(s.rpartition(' '))  # Output: ('hello ', ' ', 'WORLD')
print(s.format('hello', 'WORLD'))  # Raises TypeError: not enough arguments for format string
print(s.format_map({'greeting': 'hello', 'subject': 'WORLD'}))  # Output: hello WORLD (no placeholders to format)
# print(s.fstring())  # Raises AttributeError: 'str' object has no attribute 'fstring'
# print(s.remove('WORLD'))  # Raises ValueError: substring not found
print(s.split(' '))  # Output: ['hello', 'WORLD'] (splits by space)
print(s.rsplit(' '))  # Output: ['hello', 'WORLD'] (splits by space from the right)
print(s.partition(' '))  # Output: ('hello', ' ', 'WORLD')
print(s.rpartition(' '))  # Output: ('hello ', ' ', 'WORLD')
# print(s.format('hello', 'WORLD'))  # Raises TypeError: not enough arguments for format string
print(s.format_map({'greeting': 'hello', 'subject': 'WORLD'}))  # Output: hello WORLD (no placeholders to format)
# print(s.fstring())  # Raises AttributeError: 'str' object has no attribute 'fstring'
# print(s.remove('WORLD'))  # Raises ValueError: substring not found
print(s.split(' '))  # Output: ['hello', 'WORLD'] (splits by space)
print(s.rsplit(' '))  # Output: ['hello', 'WORLD'] (splits by space from the right)
print(s.partition(' '))  # Output: ('hello', ' ', 'WORLD')
print(s.rpartition(' '))  # Output: ('hello ', ' ', 'WORLD')
# print(s.format('hello', 'WORLD'))  # Raises TypeError: not enough arguments for format string
print(s.format_map({'greeting': 'hello', 'subject': 'WORLD'}))  # Output: hello WORLD (no placeholders to format)
# print(s.fstring())  # Raises AttributeError: 'str' object has no attribute 'fstring'    
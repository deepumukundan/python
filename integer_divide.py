num = 123456789
while num > 0:
    rem = num % 10  
    num = num // 10
    print(f"rem: {rem}")  
    print(f"num: {num}")
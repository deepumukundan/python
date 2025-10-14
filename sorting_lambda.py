
a = {
    "z": [0,0,1,1],
    "y": [0,1,1,0],
    "x": [1,1,0,0],
    "w": [1,0,1,0],    
    }
b = sorted(a.keys(), reverse=True, key=lambda x: (a[x], x))

print("".join(b))

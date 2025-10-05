def grouper_naive(inputs, n):
    num_groups = len(inputs) // n
    return [tuple(inputs[i*n:(i+1)*n]) for i in range(num_groups)]


for _ in grouper_naive(range(100000000), 10):
    pass
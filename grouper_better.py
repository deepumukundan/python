def grouper_better(inputs, n):
    iters = [iter(inputs)] * n
    return zip(*iters)

for _ in grouper_better(range(100000000), 10):
    pass
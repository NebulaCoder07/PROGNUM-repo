sequence = [1,2]                                # gives the first two elements of the sequence
for i in range(3,101):                          # the sequence goes from the 3rd to the 100th element
    sequence.append(sequence[-1]+sequence[-2])  # calculates the next element by the definition of Fib seq
print(sequence[99])

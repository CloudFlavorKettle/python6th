def generate_alophabet(start_latter, end_latter):
    start = ord(start_latter)
    end = ord(end_latter)
    while start <= end:
        yield chr(start)
        start += 1

runner = generate_alophabet('A', 'F')

for letter in runner:
    print(letter)
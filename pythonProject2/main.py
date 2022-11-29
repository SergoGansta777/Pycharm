test = "Hello hahha it's me Mario"

for c in test:
    if c == ' ': continue
    for i in range(10):
        print(' ' * i + c)
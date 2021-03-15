def reverse_text(text):
    current_index = len(text)-1
    while True:
        if current_index < 0:
            break
        yield text[current_index]
        current_index -= 1


for char in reverse_text("step"):
    print(char, end='')

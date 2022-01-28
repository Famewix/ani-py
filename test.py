def take_input(text, min, max, i_type=int):
    while True:
        try:
            result = i_type(input(text))
            if result < min:
                print("Value too small.")
            elif result > max:
                print("Value too big.")
            else:
                break
        except ValueError:
            print("Invalid Input")

take_input("Input", min=0, max=10)
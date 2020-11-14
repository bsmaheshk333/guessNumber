# decorators allow us to add the functionality without having to change the underlying code
# decorator takes underlying guess() as a parameter as s func


def decorator(func):
    # nested function
    def HandleError():
        try:
            number = int(input("[+] Guess the number: "))
            if number == '':
                raise ValueError

        except ValueError:
            print("input cannot be string.")
        else:
            return func()

    return HandleError


@decorator
def guess():
    guess_range = [i for i in range(1)]
    guess_limit, number = 0, int(input(" [+] Guess the number: "))

    while guess_limit < 2 and number not in guess_range:
        guess_limit += 1
        print("[-] Wrong guess!\t attempts left {}".format(3 - guess_limit))

        # ask the user to guess again since the chances are 3 times
        number = int(input("[+] Guess the number: "))

    print("correct") if number in guess_range else print("Error ~ Too many Failed Attempts.")


guess()


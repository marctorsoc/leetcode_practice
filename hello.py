def main():
    import random

    # List of numbers
    numbers = [525, 576, 677, 11, 13, 15, 165, 179, 1, 200]
    numbers += [215, 26, 2, 347, 34, 35, 3, 492, 49, 53, 560]
    numbers += [70, 733, 77, 784, 729, 14, 2466, 2684, 367, 1189]

    # Select 5 random numbers
    random_numbers = random.sample(numbers, 5)

    print("Hello from leetcode-practice!")
    print(random_numbers)


if __name__ == "__main__":
    main()

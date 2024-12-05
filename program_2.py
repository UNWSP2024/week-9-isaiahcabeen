import random

def write_random_numbers_to_file(file_name, num_count):
    with open(file_name, 'w') as file:
        for _ in range(num_count):
            random_number = random.randint(1, 500)
            file.write(f"{random_number}\n")
    print(f"Successfully wrote {num_count} random numbers to {file_name}")

def main():
    while True:
        try:
            num_count = int(input("How many random numbers you want to generate (up to 1000): "))
            if 1 <= num_count <= 1000:
                break
            else:
                print("Please enter a number between 1 and 1000.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    file_name = "random_numbers.txt"

    write_random_numbers_to_file(file_name, num_count)

if __name__ == "__main__":
    main()

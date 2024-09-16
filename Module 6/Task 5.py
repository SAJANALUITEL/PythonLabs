def remove_odds(numbers):

    return [num for num in numbers if num % 2 == 0]

def main():

    original_list = [3, 5, 7, 8, 10, 13, 16, 19, 22]
    even_list = remove_odds(original_list)

    print(f"Original list: {original_list}")
    print(f"List with odd numbers removed: {even_list}")

if __name__ == "__main__":
    main()
    

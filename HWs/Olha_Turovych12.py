def first_f() -> str:
    """
    This function opens existing file for reading and returns its content
    """
    with open("file1.txt", "r") as f:
        content = f.read()
        return content


def converted_content(content: str) -> str:
    """
    This function takes the content of the first file and transfors numbers column to string of numbers
    """
    numbers = content.split()
    numbers_str = " ".join(numbers)
    return numbers_str


def second_f(numbers_str: str):
    """
    This function writes the transformed content of the first file to the second
    """
    with open("file2.txt", "w") as f:
        f.write(numbers_str)


def main():
    content = first_f()
    numbers_str = converted_content(content)
    result = second_f(numbers_str)
    print("Check the file!")


if __name__ == "__main__":
    main()

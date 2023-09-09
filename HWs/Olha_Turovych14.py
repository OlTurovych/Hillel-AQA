from typing import List, Union, Dict


def get_user_input() -> List[Union[str, list, tuple, int, float]]:
    """
    This function obtains user's input
    This function converts user's input into the list type'

    param: any
    output: list
    """
    user_input = input("Enter a list of items: ")
    user_input_list = user_input.split(" ")
    return user_input_list


def convert_to_dict(user_input_list: List) -> Dict:
    """
    This function takes a user's list and converts it into the dictionary using iteration by list index

    param: list
    output: dict
    """
    converted_dict = {}
    for i in range(0, len(user_input_list), 2):
        key = user_input_list[i]
        value = user_input_list[i + 1]
        converted_dict[key] = value
    return converted_dict


def display_result(converted_dict):
    """
    This function displays the converted from user's input dictionary
    """
    print(converted_dict)


def main():
    user_input_list = get_user_input()
    converted_dict = convert_to_dict(user_input_list)
    display_result(converted_dict)


if __name__ == "__main__":
    main()

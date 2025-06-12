def letter_count(input_string):
    count_dict = {}
    for char in input_string:
        if char.isalpha():
            char = char.lower()
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1
    return count_dict

# Example usage
input_string = "Hello World"
print(letter_count(input_string))

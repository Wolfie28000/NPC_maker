import re


def main():
    answer = input("Input a number: ")
    answer = convert_text_to_int(answer)
    print(answer)


def convert_text_to_int(user_input):
    number_dict = {
        "ones": {
            "zero": 0,
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9
        },
        "tens": {
            "ten": 10,
            "twenty": 20,
            "thirty": 30,
            "forty": 40,
            "fifty": 50,
            "sixty": 60,
            "seventy": 70,
            "eighty": 80,
            "ninety": 90,
        },
        "others": {
            "eleven": 11,
            "twelve": 12,
            "thirteen": 13,
            "fourteen": 14,
            "fifteen": 15,
            "sixteen": 16,
            "seventeen": 17,
            "eighteen": 18,
            "nineteen": 19,
            "hundred": 100
        }
    }

    try:
        return int(user_input)

    except ValueError:

        all_keys = list(number_dict["ones"].keys()) + \
            list(number_dict["tens"].keys()) + list(number_dict["others"].keys())
        pattern = re.compile(r'|'.join(sorted(all_keys, key=len, reverse=True)) + r'|\d+')

        user_input = pattern.findall(user_input.lower().strip())

        num_val = 0
        prior_num = None

        for i in user_input:
            if i.isdigit():
                prior_num = int(i)
                num_val += prior_num
            elif i in number_dict["ones"]:
                prior_num = number_dict["ones"][i]
                num_val += prior_num
            elif i in number_dict["tens"]:
                prior_num = number_dict["tens"][i]
                num_val += prior_num
            elif i in number_dict["others"] and not i == "hundred":
                prior_num = number_dict["others"][i]
                num_val = prior_num
            elif i == "hundred":
                if prior_num is not None:
                    num_val += (prior_num * 100) - prior_num
                prior_num = None
            elif i:
                continue

        return num_val if num_val != 0 else None


if __name__ == "__main__":
    main()

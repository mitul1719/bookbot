def count_words(file_contents):
    print(f"{len(file_contents.split())} words found in the document")


def char_freq(file_contents):
    lowercase_file_content = file_contents.lower()
    count_dict = {}
    for j in range(97, 123):
        count = 0
        for i in lowercase_file_content:
            if i == chr(j):
                count += 1
        count_dict[chr(j)] = count
    for key, value in count_dict.items():
        print(f"The {key} character was found {value} times")


with open("./books/frankenstein.txt") as f:
    file_contents = f.read()
    print("--- Begin report of books/frankenstein.txt ---")
    count_words(file_contents)
    char_freq(file_contents)
    print("--- End report  ---")

    # print(file_contents)

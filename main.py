from stats import get_num_words
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    file_contents = get_book_text(path_to_file)
    num_words = get_num_words(file_contents)
    character_count = get_char_count(file_contents)

    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {path_to_file}...')
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print(gen_char_rep(character_count),end='')
    print('============= END ===============')

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def get_char_count(text):
    result = {}
    for char in text:
        if not char.isalpha():
            continue
        char_low = char.lower()
        if char_low in result:
            result[char_low] += 1
        else:
            result[char_low] = 1
    return result

def gen_char_rep(char_count):
    result = ''
    char_count_dictlist = [{'char': x, 'num': char_count[x]} for x  in char_count]
    char_count_dictlist.sort(reverse=True, key=lambda x: x['num'])
    for char_count_dict in char_count_dictlist:
        result += f"{char_count_dict['char']}: {char_count_dict['num']}\n"
    return result

main()
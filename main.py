def main(path_to_file):
    file_contents = get_book_text(path_to_file)
    num_words = get_num_words(file_contents)
    character_count = get_char_count(file_contents)
    
    print(f'--- Begin report of {path_to_file} ---')
    print(f"{num_words} words found in the document")
    print()
    print(gen_char_rep(character_count))
    print('--- End report ---')
    

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def get_num_words(text):
    return len(text.split())

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
        result += f"The '{char_count_dict['char']}' character was found {char_count_dict['num']} times\n"
    return result

main("books/frankenstein.txt")
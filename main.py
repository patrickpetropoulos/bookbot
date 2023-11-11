with open('books/frankenstein.txt') as f:
    file_contents = f.read().lower()
    dict = {}
    for r in file_contents:
        if r in dict:
            dict[r] = dict[r]+1
        else:
            dict[r] = 1
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f'{len(file_contents.split())} words in the document')
    print()
    for e in sorted(dict.items(),  key=lambda x: x[1], reverse=True):
        if e[0].isalpha():
            print(f'The \'{e[0]}\' character was found {e[1]} times')

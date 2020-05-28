def can_make_word(word, blocks):
    letters = [c for c in word]
    def block_has_letter(block):
        letter1, letter2 = block
        return (letter1 in letters) or (letter2 in letters)
    useful_blocks = [b for b in filter(block_has_letter, blocks)]
    def selected_blocks(letters, blocks, tried_blocks, started_with_blocks):
        if len(letters) == 0:
            return True
        elif len(blocks) == 0:
            if len(tried_blocks) == 0:
                return False
            elif set(tried_blocks) == set(started_with_blocks):
                return False
            else:
                return selected_blocks(letters, tried_blocks, [], tried_blocks)
        else:
            block = blocks[0]
            remaining_blocks = blocks[1:]
            first_letter = letters[0]
            remaining_letters = letters[1:]
            if first_letter in block:
                return selected_blocks(remaining_letters, remaining_blocks, tried_blocks, started_with_blocks) or \
                       selected_blocks(letters, remaining_blocks, tried_blocks + [block], started_with_blocks)
            else:
                return selected_blocks(letters, remaining_blocks, tried_blocks + [block], started_with_blocks)
    return selected_blocks(letters, useful_blocks, [], useful_blocks)


def main():
    blocks = [
        ("B", "O"),
        ("X", "K"),
        ("D", "Q"),
        ("C", "P"),
        ("N", "A"),
        ("G", "T"),
        ("R", "E"),
        ("T", "G"),
        ("Q", "D"),
        ("F", "S"),
        ("J", "W"),
        ("H", "U"),
        ("V", "I"),
        ("A", "N"),
        ("O", "B"),
        ("E", "R"),
        ("F", "S"),
        ("L", "Y"),
        ("P", "C"),
        ("Z", "M"),
    ]
    words = [("A",       True),
             ("BARK",    True),
             ("BOOK",    False),
             ("TREAT",   True),
             ("COMMON",  False),
             ("SQUAD",   True),
             ("CONFUSE", True)
             ]
    for (word, expected_possible) in words:
        is_possible = can_make_word(word, blocks)
        print(f"Can make {word}: {is_possible}:", is_possible == expected_possible)


if __name__ == "__main__":
    main()

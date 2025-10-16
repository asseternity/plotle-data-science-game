import random
import json

consonants = 'bcdfghjklmnpqrstvwxyz'
vowels = 'aeiouy'
with open('username_decorations.json') as f:
    data = json.load(f)

def generate_username():
    # randoms
    number_of_letters = random.randint(3, 6)
    start_with_consonant = random.randint(0, 1)

    # data
    chosen_letters_list = []
    consonants_list = list(consonants)
    vowels_list = list(vowels)
    previous_letter_consonant = True

    for i in range(number_of_letters):
        if i == 0:
            if start_with_consonant == 1:
                letter_index = random.randint(0, len(consonants_list) - 1)
                chosen_letters_list.append(consonants[letter_index])
                previous_letter_consonant = True
            else:
                letter_index = random.randint(0, len(vowels_list) - 1)
                chosen_letters_list.append(vowels[letter_index])
                previous_letter_consonant = False
        else:
            if previous_letter_consonant:
                letter_index = random.randint(0, len(vowels_list) - 1)
                chosen_letters_list.append(vowels[letter_index])
                previous_letter_consonant = False
            else:
                letter_index = random.randint(0, len(consonants_list) - 1)
                chosen_letters_list.append(consonants[letter_index])
                previous_letter_consonant = True

    gibberish = ''.join(chosen_letters_list)
    final_username = gibberish

    chance = random.randint(1, 10)
    if chance > 8:
        # add suffix
        final_username = gibberish + data['suffixes'][random.randint(0, len(data['suffixes']) - 1)]
    elif chance < 2:
        # add prefix
        final_username = data['prefixes'][random.randint(0, len(data['prefixes']) - 1)] + gibberish 

    return final_username
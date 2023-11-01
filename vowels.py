def count_vowels_and_consonants(statement):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    vowel_count = 0
    consonant_count = 0

    for char in statement:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
    
    return vowel_count, consonant_count


input_statement = "Saveetha School of Engineering Sample"


vowels, consonants = count_vowels_and_consonants(input_statement)


if vowels > consonants:
    print(f"Number of vowels = {vowels} (Maximum)")
    print(f"Number of consonants = {consonants}")
elif consonants > vowels:
    print(f"Number of vowels = {vowels}")
    print(f"Number of consonants = {consonants} (Maximum)")
else:
    print(f"Number of vowels = {vowels}")
   

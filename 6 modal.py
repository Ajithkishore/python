def count_matching_characters(string1, string2):
    match_count = 0
    for char1, char2 in zip(string1, string2):
        if char1 == char2:
            match_count += 1

    return match_count
string1 = "what"
string2 = "watch"
matching_count = count_matching_characters(string1, string2)
print("Number of matching characters:", matching_count)
 




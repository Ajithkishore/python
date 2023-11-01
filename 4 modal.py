def count_special_characters(statement):
    special_characters = "!@#$%^&*()_-+=<>?/,.|{}[]~`"

    count = 0
    for char in statement:
        if char in special_characters:
            count += 1
    return count
statement = "Modi Birthday @ September 17 #&$% is the wishes code for him"
special_character_count = count_special_characters(statement)
print("Number of special characters:", special_character_count)







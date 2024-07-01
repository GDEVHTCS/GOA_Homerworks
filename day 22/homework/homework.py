def sort_by_length(strings):
   
    return sorted(strings, key=len)

strings = ["giorgi", "manqana", "pc", "qatami"]
sorted_strings = sort_by_length(strings)
print(sorted_strings)


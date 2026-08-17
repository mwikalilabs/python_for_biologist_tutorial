seq = ["ATGC", "GGCTA", "TTAAC"]
"""
print(type(seq))
print(seq[2])
print(len(seq))
print(len(seq[2]))#to get the length of the string present in the list
print(seq[0])
"""

"""
#for loop
#to iterate through the list and print each element
for s in seq:
    print(s)
"""

"""
genes = ["BRCA1", "TP53", "EGFR"]
for g in genes:
    print(g)
"""

"""
fruit = ["apple", "banana", "cherry"]
for f in fruit:
    print(f)
    """

dna_sequence = ["ATGC", "CGTAA", "TTGCA"]

print(type(dna_sequence))
print(dna_sequence)

print(len(dna_sequence))
print(len(dna_sequence[0]))#to get the length of the string present in the list at the first index
print(dna_sequence[1])#to get the second element of the list

print(dna_sequence[1][0])#to get the first character of the second element of the list
print(dna_sequence[0][-1])#to get the last character of the first element of the list

for d in dna_sequence: #to iterate through the list and print each element
    print(d)


"""
in this lesson i learned:
    - Lists in Python
    - Accessing elements in a list
    - Iterating through a list
    - Modifying elements in a list

"""
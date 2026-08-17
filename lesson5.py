# String indexing and slicing
dna = "ATGGTAT"
print(dna[-1])
print(len(dna))
print(len(dna)+1)
print(len(dna)-1)
print(dna[len(dna)-1]) #last nucleotide


#Qn 1
#type of the variable
seq = "ATGCTAGGCTA"
print(seq)
print(type(seq))


#Qn 2
#length of the string --using len() function
seq = "ATGCGTACGTTAGC"
print(len(seq))


#Qn 3
#indexing of the string
seq = "ATGCGTAC"
print(seq[0])#first nucleotide
print(seq[2])#third nucleotide
print(seq[len(seq)-1])#last nucleotide


#Qn 4
#working with two strings 
dna_1 = "ATGCGT"
dna_2 = "ATGCGTAGG"
print(dna_1 , dna_2)
print(dna_2[4])
print(dna_1[len(dna_1)-1])
print(dna_1[len(dna_1)-6])
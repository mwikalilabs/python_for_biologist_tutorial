"""
seqIO is a module in Biopython that provides functions for reading and 
writing sequence data in various formats, such as FASTA, GenBank, and others. It allows you to 
parse sequence files, access sequence records, and perform operations on them.
"""
"""
seqIO.read() is a function that reads a single sequence record from a file in a specified format.
It reads the file, parses the sequence data, and returns a SeqRecord object representing the sequence record.
The SeqRecord object contains information about the sequence, such as its identifier, description, and the
actual sequence itself.
"""


"""
from Bio import SeqIO  
cox1 = SeqIO.parse("cox1.fasta", "fasta") 
for record in cox1:
    print(record.id)
    print(record.description)
    print(len(record))
    #print(record.seq)
"""

from Bio import SeqIO
insulin = SeqIO.read("insulin.fasta", "fasta")
print(insulin.id)
print(insulin.description)
print(insulin.name)
print(len(insulin))
# print(insulin.seq)
from Bio.Seq import Seq#to import the Seq class from the Bio.Seq module in Biopython. The Seq class is used to represent biological sequences, such as DNA, RNA, or protein sequences.
from Bio.SeqRecord import SeqRecord#to import the SeqRecord class from the Bio.SeqRecord module in Biopython. The SeqRecord class is used to represent a sequence record, which includes a sequence along with associated metadata such as an identifier, name, and description.

"""
#Example 1
dna = Seq("ATGCGT")

record = SeqRecord(
    dna,
    id = "Gene1",
    name = "Example Gene",
    description = "Sample DNA seq for Practice"
)


print(record.id)
print(record.name)
print(record.description)
print(record.seq)
"""

"""
#Example 2
protein_seq = Seq("MKTLLV")
protein_record = SeqRecord(
    protein_seq,
    # id = 
    "Prot01",
    # name = 
    "Test Protein", 
    # description = 
    "Sample Protein seq example"
    )

print(protein_record.id)
print(protein_record.name)
print(protein_record.description)
"""

"""
#Qn 1 : create a DNA seq ... and print the sequence
#from Bio.Seq import Seq
dna = Seq("ATGCGT")
print(dna)
print(type(dna))
"""


"""
#Qn 2 : create a DNA seq and print the complement and transcribe the DNA sequence to RNA
#from Bio.Seq import Seq
dna = Seq("ATGC")
# print(dna)
print(dna.complement())
print(dna.transcribe())
#or
# rna = dna.transcribe()
# print(rna)
"""

"""
#Qn 4: create a SeqRecord object with a DNA sequence, an identifier, and a description. Then, print the attributes of the SeqRecord object.
seq = Seq("ATGCAA")
seq_record = SeqRecord(
    seq,
    id = "Gene1",
    description = "Sample gene sequence"
)
print(seq_record.description)
print(seq_record.id)
print(seq_record.name)
print(seq_record.seq)
"""


#Qn 5
"""
gene = Seq[("ATGC","TTAA")]
gene_record = SeqRecord(
    gene,
    id = ["GeneA", "GeneB"]

)
for id in gene_record:
    print(id)
"""


"""
#correct answer for Qn 5:create two SeqRecord objects with different DNA sequences and identifiers. Then, store them in a list and iterate through the list to print the identifiers of each SeqRecord object.
r1 = SeqRecord (
    Seq("ATGC"), 
    id= "GeneA"
    )
r2 = SeqRecord(
    Seq("TTAA"), 
    id = "GeneB"
    )

records = [r1, r2]

for rec in records:
    print(rec.id)
"""


"""
in this lesson, I learned:
create a SeqRecord object
read the attributes of a SeqRecord object which starts with id, name, description, and seq
worked with for loop to iterate through a list of SeqRecord objects

"""
"""
read - for one fasta file
parse - for multiple fasta 
"""

from Bio import SeqIO

"""
#fasta
for record in SeqIO.parse("cox1.fasta", "fasta"):
    print(record.id)
    print(record.description)
    print(len(record))
    print("-"*30)
"""

   
#genbank
cox1 = SeqIO.read("cox1.gb", "genbank")
print(cox1.id)
print(cox1.description)
print(cox1.name)
print(cox1.annotations)#extra info.
print(len(cox1.features)) #how many features inside the file
for f in cox1.features:#loop the features
    print(f)
    print("-"*50)
    print(f.type , f.location)#type of features present

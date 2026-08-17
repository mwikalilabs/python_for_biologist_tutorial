# from Bio import SeqIO

# record = SeqIO.read("insulin_protein.fasta", "fasta")

# print(record.id)
# print(record.description)
# print(len(record.seq))
# print("*" * 30)
# print(record.seq)


#Qn1
from Bio import SeqIO

proteins = SeqIO.parse("proteins.fasta", "fasta")
for p in proteins:
    print(p.id , p.description)
    # print(p.description)
    print(len(p))
    print(p.seq)
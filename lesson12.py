from Bio.Blast import NCBIWWW
from Bio import SeqIO
record = SeqIO.read("insulin_protein.fasta", "fasta")
result = NCBIWWW.qblast(
    program = "blastp",
    database = "nr",
    sequence = "MALWMRLLPLLALLALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFYTPKTRREAEDLQVGQVELGGGPGAGSLQPLALEGSLQKRGIVEQCCTSICSLYQLENYCN"
    #sequence = record.seq
)


#with --key word to open a file, then open
#"w"--write mode
with open("blast_result.xml", "w") as b:
    b.write(result.read())
print("done!!!")


#NCBIXML

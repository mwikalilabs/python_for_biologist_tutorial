#import Bio 
from Bio.Seq import Seq#imp
#print(Bio.__version__)

dna = Seq("ATGCGT")

"""
print(type(dna))
print(dna)
print(dna.complement())
print(dna.transcribe())
"""

"""
#transcribe the DNA sequence to RNA
rna = dna.transcribe()
print(rna)

print(rna.translate())

#translate the RNA sequence to protein
print(rna.translate())
"""

"""
#translation eg
protein = dna.translate()
print(protein)
"""

"""
in this lesson, I learned:

import seq
seq version identification--what version of biopython is installed
create a DNA sequence
transcribe the DNA sequence to RNA
translate the RNA sequence to protein
complement the DNA sequence
"""
amino_acids = {
        "Methionine" : ["AUG"],
        "Phenylalanine": ["UUU", "UUC"],
        "Leucine": ["UUA", "UUG"],
        "Serine": ["UCU", "UCC", "UCA", "UCG"],
        "Tyrosine": ["UAU", "UAC"],
        "Cysteine": ["UGU", "UGC"],
        "Tryptophan": ["UGG"],
        "STOP": ["UAA", "UAG", "UGA"]
    }

def proteins(strand):
    codons = [strand[i:i+3] for i in range(0, len(strand), 3)]
    protien = []
    for codon in codons:
        for amino_acid, nucleotide_sequence in amino_acids.items():
            if codon in nucleotide_sequence:
                amino = amino_acid
                if amino == "STOP":
                    return(protien)
                else:
                    protien.append(amino)
    return(protien)
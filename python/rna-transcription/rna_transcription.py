def to_rna(dna_strand):
    def nucleotides(base):
        return {
            "G": "C",
            "C": "G",
            "T": "A",
            "A": "U"
        }.get(base)
    return ''.join( [nucleotides(base) for base in dna_strand ] )
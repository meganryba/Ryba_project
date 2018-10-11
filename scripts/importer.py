import dendropy

amphib = dendropy.DnaCharacterMatrix.get(
    path="../data/plethodon.phy",
)

amphib.write_to_path("../data/plethodon.fa", schema="fasta")
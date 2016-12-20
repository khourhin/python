from pyensembl import EnsemblRelease

# You should first install the corresponding files from ensembl with:
# pyensembl install --release 77 --species homo_sapiens

data = EnsemblRelease(77, species="homo_sapiens")
gene_names = data.gene_names_at_locus(contig=6, position=29945884)
exon_ids  = data.exon_ids_of_gene_name(gene_names[0])


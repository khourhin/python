from pyensembl import EnsemblRelease

# You should first install the corresponding files from ensembl with:
# pyensembl install --release 77 --species homo_sapiens

data = EnsemblRelease(species="homo_sapiens")
gene_names = data.gene_names_at_locus(contig=6, position=29945884)
exon_ids  = data.exon_ids_of_gene_name(gene_names[0])

print(gene_names)
print(exon_ids)

# How many genes in total
gene_ids = data.gene_ids()
print(len(gene_ids))
# Only protein coding genes
genes = [data.gene_by_id(gene_id) for gene_id in gene_ids]
coding_genes = [gene for gene in genes if gene.biotype == 'protein_coding']
print(len(coding_genes))

from pybiomart import Dataset

# Initiate a ensembl dataset
dataset = Dataset(name='hsapiens_gene_ensembl', host='www.ensembl.org')

# Get list of all attributes
attrs = dataset.list_attributes()

# Fetch a particular attribute by regex
attrs[attrs.name.str.contains('unip')]

# Extract a table with the required fields
table = dataset.query(attributes=['ensembl_gene_id', 'external_gene_name', 'unigene'])

# Subset this table
a = table[table['UniGene ID'].isin(['Hs.631534','Hs.745449'])]


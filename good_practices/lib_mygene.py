import mygene

################################################################################
# MORE INFO AT http://mygene-py.readthedocs.io/en/latest/#
################################################################################

# List of fields at
# http://docs.mygene.info/en/latest/doc/data.html?highlight=fields

mg = mygene.MyGeneInfo()

# Print out the list of all available fields
# for k in mg.get_fields():
#     print(k)

# Search through the fields 
# print(mg.get_fields('kegg'))

# Get a gene by gene id (apparently lots of different types are
# supported)
# A t guttata gene
print(mg.getgene('ENSTGUG00000018470'))

# Getting several genes
#mg.getgenes

# Looking for a refseq id
print(mg.query('NM_001199862'))

# More specific way
print(mg.query('NM_001199862', scopes='refseq', species='human'))

# For several (good for ID mapping)
#mg.querymany()

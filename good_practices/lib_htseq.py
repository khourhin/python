import HTSeq
import itertools
import numpy
from matplotlib import pyplot

################################################################################
## FASTQ
################################################################################

# Import FASTQ
fastq_file = HTSeq.FastqReader("demo_data/htseq/yeast_RNASeq_excerpt_sequence.txt", "solexa")

# Iterate through reads
for read in itertools.islice(fastq_file, 10):
    print(read)

# Performing average quality per position through all reads
qualsum = numpy.zeros(len(read), numpy.int)
nreads = 0
for read in fastq_file:
    qualsum += read.qual
    nreads += 1

mean_pos_quality = qualsum / float(nreads)

pyplot.plot(mean_pos_quality)
#pyplot.show()

################################################################################
## SAM / BAM
################################################################################

align_file = HTSeq.SAM_Reader("demo_data/htseq/yeast_RNASeq_excerpt.sam")

# Iterate though reads
nreads = 0
for aln in itertools.islice(align_file, 10):
    print(aln.aligned)
    if aln.iv:
        print(aln.iv)
        print(aln.iv.chrom)
        print(aln.iv.start)         
        print(aln.iv.end)
        print(aln.iv.strand)
    else:
        print("No genomic interval for read %s (i.e read not aligned)" % (aln.read.name))
    

# For bams
# bam_reader = HTSeq.BAM_Reader( "SRR001432_head_sorted.bam" )
# Fetch a particular region
# for a in bam_reader.fetch( region = "1:249000000-249200000" ):
#     print "Writing Alignment", a, "to file", bam_writer.filename
#     bam_writer.write( a )

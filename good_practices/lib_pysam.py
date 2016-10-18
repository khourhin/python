import pysam

# Get a fasta file
with pysam.FastxFile(fasta) as fa:
    for seq in fa:
        print(seq.name)
        print(seq.sequence)

# Get a fastq file
with pysam.FastxFile(fastq) as fq:
    for read in fq:
        print(read.name)
        print(read.sequence)

# Get a bam file
samfile = pysam.AlignmentFile("demo_bams/read_100_pass1_Aligned.sortedByCoord.out.bam")


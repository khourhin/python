from pybedtools import BedTool
import argparse


def get_splice_saf(star_splice_junctions, gtf):
    """
    Get a saf file of the splicing junctions. This file format can be
    used with featureCount for splicing junction quantification.
    """

    sj = BedTool(star_splice_junctions)
    gtf = BedTool(gtf)

    for i in sj.intersect(gtf, wb=True):
        gene_id = i[17].split(';')[0].split(' ')[1].strip('"')
        print('{0}\t{1}\t{2}\t{3}\t{4}'.format(gene_id, i[0], i[1], i[2], i[15]))


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('star_splice_junctions', )
    parser.add_argument('gtf', )
    args = parser.parse_args()

    get_splice_saf(args.star_splice_junctions, args.gtf)


    # Example usage
    # cd /home/ekornobis/Programming/snakeMake_recipes
    # python ../python/good_practices/lib_pybedtools.py star_out/SRR019721_tiny_SJ.out.tab ~/data/genomes/c_elegans/Caenorhabditis_elegans.WBcel235.86.gtf > sj.bed

import click

### WARNING !!!!
### Click function are not normal function, they cannot return object for example !!

@click.command()
@click.option('--repeats', '-r', default=1, help='Number of repetitions')
@click.argument('message')
def hello(message, repeats):
    for i in range(repeats):
        click.echo(click.style(message, fg='green'))


# Apparently cool way to call click
@click.command()
@click.option('--bamdir', default=None, type=click.Path(exists=True), required=True, help='Path to the bam directory.')
@click.option('--fqdir', default=None, type=click.Path(exists=True), required=True, help='Path to the fastqs directory.')
@click.option('--strand', default=0, type=int, required=True, help='Strandedness: 0:not stranded; 1:stranded; 2: reverse stranded.')
@click.option('--paired', default=False, type=bool, required=True, help='Paired end: either True or False.')
@click.option('--json_out', default='snakemake.json', type=str, help='Path to the json output.')
@click.option('--fixed_exons', is_flag=True, help="Set a fixed size for the exons")
def main(**kwargs):
    """A simple parser to get NGS library information
    """
    print(kwargs)
#    job = init_job(**kwargs)


        
if __name__ == '__main__':
    # Check automatic help generated:
    # python lib_click.py --help
    #hello()
    main()

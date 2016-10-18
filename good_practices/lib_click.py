import click


@click.command()
@click.option('--repeats', '-r', default=1, help='Number of repetitions')
@click.argument('message')
def hello(message, repeats):
    for i in range(repeats):
        click.echo(message)

if __name__ == '__main__':
    # Check automatic help generated:
    # python lib_click.py --help
    hello()

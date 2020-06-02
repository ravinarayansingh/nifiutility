"""Console script for nifiutility."""
import sys
import click

from nifiutility.lib.processor_group import ProcessGroup


@click.group()
def cli():
    pass


@cli.command()
@click.argument('host')
@click.argument('port')
@click.argument('id')
def clear_queue(host, port, id):
    """Console script for nifiutility."""
    pg = ProcessGroup(host, port, id)
    click.echo(pg.clear_queues())
    return 0


if __name__ == "__main__":
    cli.add_command(clear_queue)
    sys.exit(cli())  # pragma: no cover

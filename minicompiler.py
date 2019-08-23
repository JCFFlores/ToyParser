from lexer import tokenize, InvalidTokenException
import click

@click.group()
def cli():
    pass


@cli.command()
@click.argument('input_string')
def scanner(input_string: str) -> None:
    try:
        for token in tokenize(input_string):
            print(token)
    except InvalidTokenException as e:
        print(e)


if __name__ == '__main__':
    cli()

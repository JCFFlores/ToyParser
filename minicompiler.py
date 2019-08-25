from lexer import tokenize, InvalidTokenException
from parser import TokenList, parse, IncorrectTokenException, ExcedingTokensException, NoMoreTokensException
from collections import deque
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


@cli.command()
@click.argument('input_string')
def parser(input_string: str) -> None:
    try:
        token_list: TokenList = deque(tokenize(input_string))
        parse(token_list)
        print(f'{input_string} is a correct and valid expression')
    except InvalidTokenException as e:
        print(e)
    except IncorrectTokenException as e:
        print(e)
    except ExcedingTokensException:
        print(f'{input_string} is too long to be a valid expression')
    except NoMoreTokensException:
        print(f'{input_string} is to short to be a valid expression')


if __name__ == '__main__':
    cli()

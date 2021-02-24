#!/usr/bin/env python

import click

@click.option('-o',
              '--opt',
              required=False, 
              help='Provide additional data if required')
@click.argument('argu',
                required=True)
@click.command()
def mycli(argu, opt):
    """Env is all set!!!!"""
    print("Provided argument is {} and Option is  {}".format(argu, opt))

if __name__ == '__main__':
    mycli()

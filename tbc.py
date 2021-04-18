#!/usr/bin/env python3

import toml
import click
import subprocess


def load_config():
	with open('.tbc.toml') as f:
		return toml.loads(f.read())

def execute(config, command):
	if command != "":
		# requested
		execution_key = command
	else:
		# first
		execution_key = next(iter(config))
	
	exe = config[execution_key]['exe']
	executable_string = str(exe)

	if 'args' in config[execution_key]:
		args = config[execution_key]['args']
		args = [args] if isinstance(args, str) else args
		executable_string += ' '
		executable_string += ' '.join(args)

	subprocess.call(executable_string, shell=True)

@click.command()
@click.option('--list-commands', is_flag=True, help="List available commands")
@click.argument('command', default="")
def main(command, list_commands):
	"""Tools By Config reads .tbc.toml and executes commands with arguments defined in there.

	Example .tbc.toml:

	\b
	[echo]
		exe = "echo"
		args = ["Hello", "World"]

	Example launch: `tbc.py echo` or just `tbc.py`"""
	config = load_config()
	if list_commands:
		print('Available options are {cmds}.'.format(cmds=', '.join(list(config.keys()))))
		exit()
	if command != "" and command not in config:
		print(f'{command} can not be found in .tbc.toml')
		print('Available options are {cmds}.'.format(cmds=', '.join(list(config.keys()))))
	else:
		execute(config, command)

if __name__ == '__main__':
	main()
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from configparser import ConfigParser 
from os import system
DATA = 'data.ini'
EDITOR = 'vim'
PATH = './data/'

"""
This software is distributed under a GPL2 License.
@Author: Samuel López Saura
@Web Page: blog.curiosoinformatico.com 
@Twitter: @Mago_Geminis

#Just for fun

Any question, direct message on twitter.

"""
def comments(name):
	with open('data/{0}/setup.sh'.format(name), 'wt') as fich:
		fich.write('#!/bin/bash\n')
		fich.write('#This file is the instalation script\n')
		fich.write('#You should write the things you need to do\n')
		fich.write('#to install the module.\n\n\n')

def continue_():
	input ('~~~~~~~~~~~~~~~~~~~~~~~\nPress Enter to continue')
	main()

def read():
	config = ConfigParser()
	config.read(DATA)
	return config

def main():
	system('clear')
	option = str(input('1)List Modules\n2)Install Module\n3)Add Module\n4)Edit Module Script\n5)Exit\n~~  '))
	if option == '5':
		quit()
	else:
		config = read()
		if option == '1':
			for section in config.sections():
				print ('~    ' + section)
			
			
		elif option == '2':
			name = str(input('Name of the module: '))
			try:
				print ('Description: ' + config[name]['description'])
				print ('Path: ' + config[name]['path'])
				print ('Extra info: ' + config[name]['extra info'])
				opt = str(input('Do you wish to continue? [Y|n]'))
				if opt != 'n':
					system('bash ' + PATH + name + '/setup.sh')
			except:
				print ('>> Wrong module name <<')
		
		elif option == '3':
			name = str(input('Name of the module: '))
			description = str(input('Description: '))
			system('mkdir '+ PATH + name )
			comments(name)
			system(EDITOR + ' ' + PATH + name + '/setup.sh')
			config [name] = {}
			config[name]['description'] = description
			config[name]['install'] = PATH + name + '/setup.sh'
			config[name]['path'] = PATH + name
			config[name]['extra info'] = str(input('Extra info: '))
			with open(DATA, 'wt') as fich:
				config.write(fich)

		elif option == '4':
			name = str(input('Name of the module: '))
			open(PATH + name + '/setup.sh').close()
			system(EDITOR + ' ' + PATH + name + '/setup.sh')


		else:
			print ('>>   Wrong option   <<')
		
		continue_()

if __name__ == '__main__':
	main()

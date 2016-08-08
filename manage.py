import sys, os
from shutil import copytree

def create_weblog():
    id = raw_input('Weblog ID: ')
    name = raw_input('Weblog Name: ')
    welcome = raw_input('Welcome Text: ')
    email = raw_input('Email: ')
    tele = raw_input('Telegram ID: ')
    copytree(os.path.dirname(__file__)+'/base_template', 'templates')
    os.mkdir('posts')
    os.mkdir('result')

def main(args):
    if len(args) == 2 and args[0] == 'create' and args[1] == 'weblog':
        create_weblog()
    else:
        print 'Invalid arguments'
if __name__ == '__main__':
    main(sys.argv[1:])

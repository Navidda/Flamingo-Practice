import sys, os
from shutil import copytree

def init_index(data): # TODO
    pass

def init_about(data): # TODO
    pass

def create_weblog():
    id = raw_input('Weblog ID: ')
    name = raw_input('Weblog Name: ')
    welcome = raw_input('Welcome Text: ')
    email = raw_input('Email: ')
    tele = raw_input('Telegram ID: ')
    data = {'id': id, 'name': name, 'welcome': welcome, 'email': email, 'tele': tele}
    os.mkdir('posts')
    os.mkdir('result')
    copytree(os.path.dirname(__file__)+'/base_template', 'templates')
    init_index(data)
    init_about(data)

def main(args):
    if len(args) == 2 and args[0] == 'create' and args[1] == 'weblog':
        create_weblog()
    else:
        print 'Invalid arguments'
if __name__ == '__main__':
    main(sys.argv[1:])

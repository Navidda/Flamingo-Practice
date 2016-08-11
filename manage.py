import sys, os
import xml.etree.ElementTree as ET
from shutil import copytree

def edit_html(data, address):
    tree = ET.parse(address)
    root = tree.getroot()
    for weblog_name in root.iter('weblog-name'):
        weblog_name.text = data['name']
    for welcome in root.iter('welcome'):
        welcome.text = data['welcome']
    for email in root.iter('email'):
        email.text = data['email']
    for tele in root.iter('telegram'):
        tele.text = data['tele']
    tree.write(address)

def create_weblog():
    id = raw_input('Weblog ID: ')
    name = raw_input('Weblog Name: ')
    welcome = raw_input('Welcome Text: ')
    email = raw_input('Email: ')
    tele = raw_input('Telegram ID: ')
    data = {'id': id, 'name': name, 'welcome': welcome, 'email': email, 'tele': tele}
    copytree(os.path.dirname(__file__)+'/base_template', id+'/templates')
    os.chdir(id)
    os.mkdir('posts')
    os.mkdir('result')
    edit_html(data, 'templates/index.html')
    edit_html(data, 'templates/about.html')

def main(args):
    if len(args) == 2 and args[0] == 'create' and args[1] == 'weblog':
        create_weblog()
    else:
        print 'Invalid arguments'
if __name__ == '__main__':
    main(sys.argv[1:])

import sys, os, json, time
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

    print "Enter Welcome text! finish with a line equal to '_finish'"
    text = ""
    while true:
        line = raw_input()
        if line == '_finish':
            break
        text += line + '\n';

    email = raw_input('Email: ')
    tele = raw_input('Telegram ID: ')
    data = {'id': id, 'name': name, 'welcome': welcome, 'email': email, 'tele': tele}
    copytree(os.path.dirname(__file__)+'/base_template', 'templates')
    os.mkdir('posts')
    os.mkdir('result')
    edit_html(data, 'templates/index.html')
    edit_html(data, 'templates/about.html')

def create_post():
    id = raw_input('Post ID: ')
    title = raw_input('Title: ')

    print "Enter your post! finish with a line equal to '_finish'"
    text = ""
    while True:
        line = raw_input()
        if line == '_finish':
            break
        text += line + '\n';

    timestring = time.asctime( time.localtime(time.time()) )
    data = json.dumps([title, text, timestring])
    fo = open('posts/'+id+'.json', 'w')
    fo.write(data)
    fo.close()

def main(args):
    if len(args) == 2 and args[0] == 'create' and args[1] == 'weblog':
        create_weblog()
    elif len(args) == 2 and args[0] == 'create' and args[1] == 'post':
        create_post()
    else:
        print 'Invalid arguments'
if __name__ == '__main__':
    main(sys.argv[1:])

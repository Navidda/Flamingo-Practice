import sys, os, json, time
import xml.etree.ElementTree as ET
from shutil import copytree, rmtree, copyfile

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
    copytree(os.path.dirname(__file__)+'/base_template', 'templates')
    os.mkdir('posts')
    edit_html(data, 'templates/index.html')
    edit_html(data, 'templates/about.html')

def create_post():
    id = raw_input('Post ID: ')
    title = raw_input('Title: ')
    text = raw_input('Write your post: ')
    t = time.time()
    data = json.dumps([title, text, t, id])
    fo = open('posts/'+id+'.json', 'w')
    fo.write(data)
    fo.close()

def second_item(a):
    return a[2];

def update_index():
    ps = os.listdir('posts')
    posts = []
    for id in ps:
        fo = open('posts/'+id, "r")
        data = fo.read()
        fo.close()
        posts.append(json.loads(data))
    posts.sort(key=second_item)
    insert_posts(posts)

def insert_posts(posts):
    address = 'result/index.html'
    tree = ET.parse(address)
    root = tree.getroot()
    for elem in root.iter('div'):
        if elem.get('class') == 'posts':
            for post in posts:
                li = ET.SubElement(elem, 'li')
                link = ET.SubElement(li, 'a')
                link.set('href', 'post_'+post[3]+'.html')
                link.text = post[0]
                sp = ET.SubElement(li, 'span')
                time_string = time.asctime( time.localtime(post[2]) )
                sp.text = "Written at " + time_string

    tree.write(address)

def edit_post_html(address, post):
    tree = ET.parse(address)
    root = tree.getroot()
    for elem in root.iter('post-title'):
        elem.text = post[0]
    for elem in root.iter('post-date'):
        elem.text = time.asctime( time.localtime(post[2]))
    for elem in root.iter('post-text'):
        elem.text = post[1]

    tree.write(address)

def create_posts():
    address = 'result/post_'
    dirs = os.listdir('posts')
    for dir in dirs:
        fo = open('posts/'+dir, "r")
        data = fo.read()
        fo.close()
        post = json.loads(data)
        address = 'result/post_'+post[3]+'.html'
        copyfile('result/post.html', address)
        edit_post_html(address, post)

def compile():
    dirs = os.listdir('.')
    if 'result' in dirs:
        rmtree('result')
    copytree('templates', 'result')
    create_posts()
    update_index()

def main(args):
    if len(args) == 2 and args[0] == 'create' and args[1] == 'weblog':
        create_weblog()
    elif len(args) == 2 and args[0] == 'create' and args[1] == 'post':
        create_post()
    elif len(args) == 1 and args[0] == 'compile':
        compile()
    else:
        print 'Invalid arguments'
if __name__ == '__main__':
    main(sys.argv[1:])

#encoding=utf8
import fanfou
import json

def query(key):
  args = key.split(' ')
  if len(args) > 1:
    content = args[2:].join(' ')
    content_length = len(content)
    return {
      'Title': '饭否',
      'SubTitle': content_length + ' 字 ' + key
    }


def write_file(content):
  account_str = json.dumps(content)
  f = open('./config.json', 'w')
  f.write(account_str)
  f.close()

def read_file():
  f = open('./config.json', 'r')
  content = f.read()
  f.close()
  account = json.loads(content)
  return account

def post(text):
  account = read_file()
  ff = fanfou.XAuth(account, account.username, account.password)
  ff.request('/statuses/update', 'POST', {'status': text})

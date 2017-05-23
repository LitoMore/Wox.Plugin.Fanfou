import fanfou
import json

# ff = fanfou.XAuth('key', 'secret', 'username', 'password')

def query(key):
  action = key.split(' ')[1]
  if action == 'config':
    account = read_file()
    account['key'] = key.split(' ')[2]
    account['secret'] = key.split(' ')[3]
    write_file(account)
  elif action == 'login':
    account = read_file()
    account['username'] = key.split(' ')[2]
    account['password'] = key.split(' ')[3]
    write_file(account)
  else:
    post(key)

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

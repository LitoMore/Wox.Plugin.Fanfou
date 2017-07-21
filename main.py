# encoding = utf8

import fanfou
import json
import os
from wox import Wox


class Main(Wox):
    def query(self, query):
        default = [{
            'Title': '饭否',
            'SubTitle': '你在做什么？',
            'IcoPath': 'Images/wox-fanfou.png'
        }]
        if query == '':
            return default
        else:
            args = query.split(' ')
            if args[0] == 'config' and len(args) == 3:
                key = args[1]
                secret = args[2]
                count = len(secret) % 2
                return [{
                    'Title': '饭否',
                    'SubTitle': '配置 Consumer Key 与 Consumer Secret' + ' ' * count,
                    'IcoPath': 'Images/wox-fanfou.png',
                    'JsonRPCAction': {
                        'method': 'write_consumer',
                        'parameters': [key, secret]
                    }
                }]
            elif args[0] == 'login' and len(args) == 3:
                username = args[1]
                password = args[2]
                count = len(password) % 2
                return [{
                    'Title': '饭否登录',
                    'SubTitle': '登录饭否账号' + ' ' * count,
                    'IcoPath': 'Images/wox-fanfou.png',
                    'JsonRPCAction': {
                        'method': 'write_account',
                        'parameters': [username, password]
                    }
                }]
            else:
                count = str(len(query))
                res = count + ' 字'
                return [{
                    'Title': '饭否',
                    'SubTitle': res,
                    'IcoPath': 'Images/wox-fanfou.png',
                    'JsonRPCAction': {
                        'method': 'post',
                        'parameters': [query]
                    }
                }]

    def write_consumer(self, key, secret):
        account_str = json.dumps({
            'key': key,
            'secret': secret
        })
        f = open(os.path.expanduser('~') + '\\wox-fanfou-config.json', 'w')
        f.write(account_str)
        f.close()

    def write_account(self, username, password):
        consumer = self.read_file()
        account_str = json.dumps({
            'key': consumer['key'],
            'secret': consumer['secret'],
            'username': username,
            'password': password
        })
        f = open(os.path.expanduser('~') + '\\wox-fanfou-config.json', 'w')
        f.write(account_str)
        f.close()

    def read_file(self):
        f = open(os.path.expanduser('~') + '\\wox-fanfou-config.json', 'r')
        content = f.read()
        f.close()
        account = json.loads(content)
        return account

    def post(self, text):
        account = self.read_file()
        ff = fanfou.XAuth({
            'key': account['key'],
            'secret': account['secret']
        }, account['username'], account['password'])
        ff.request('/statuses/update', 'POST', {'status': text})

if __name__ == "__main__":
    Main()

# encoding = utf8

import fanfou
import json
import os
from wox import Wox


class Main(Wox):
    def query(self, query):
        default = [{
            'Title': '饭否',
            'SubTitle': '你在做什么？'
        }]
        if query == '':
            return default
        else:
            args = query.split(' ')
            if args[0] == 'config' and len(args) == 3:
                key = args[1]
                secret = args[2]
                return [{
                    'Title': '饭否',
                    'SubTitle': '配置 Consumer Key 与 Consumer Secret',
                    'JsonRPCAction': {
                        'method': 'write_file',
                        'parameters': [{
                            'key': key,
                            'secret': secret
                        }]
                    }
                }]
            elif args[0] == 'login' and len(args) == 3:
                username = args[1]
                password = args[2]
                return [{
                    'Title': '饭否',
                    'SubTitle': '登陆饭否账号'
                }]
            else:
                count = str(len(query))
                res = count + ' 字'
                return [{
                    'Title': '饭否',
                    'SubTitle': res
                }]

    def write_file(self, content):
        account_str = json.dumps(content)
        f = open('config.json', 'w')
        f.write(account_str)
        f.close()

    def read_file(self):
        f = open('config.json', 'r')
        content = f.read()
        f.close()
        account = json.loads(content)
        return account

    def post(self, text):
        account = self.read_file()
        ff = fanfou.XAuth(account, account.username, account.password)
        ff.request('/statuses/update', 'POST', {'status': text})

if __name__ == "__main__":
    Main()

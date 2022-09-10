import sys, os

if sys.platform == 'linux':
    if os.getcwd() != os.path.dirname(__file__):
        os.chdir(os.path.dirname(__file__))

with open('.gitignore', 'w') as w_f:
    w_f.write('.gitignore')

files = os.listdir()
add_extension = ['txt', 'gif', 'csv', '.py']

for file_ in files:
    if file_[-3:] in add_extension:
        with open ('.gitignore', 'a') as a_f:
            a_f.write('\n' + file_)
    else:
        continue
    
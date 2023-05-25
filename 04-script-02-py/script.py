import os
import sys

try:
    bash_command_arg = sys.argv[1]
    if os.path.isdir(bash_command_arg):
        if os.path.exists(f'{bash_command_arg}/.git'):
            bash_command = [f'cd {bash_command_arg}', "git status", ]
            result_os = os.popen(' && '.join(bash_command)).read()
            for result in result_os.split('\n'):
                if result.find('modified') != -1:
                    prepare_result = result.replace('\tmodified:   ', '')
                    print(prepare_result)
        else:
            sys.exit("not a git repository")
    else:
        sys.exit("Directory is not exists")
except IndexError as e:
    print("Directory is not exists")



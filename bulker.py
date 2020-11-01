"""
Bulker is used to change the name of several files in a directory in a easy and convinient way
"""
import argparse
from pathlib import PosixPath, Path
from re import search as re_search
from re import error as re_error
from sys import argv, exit

TOOL_TIP = '--append= | --prefix | --index=0 | --stitch=split | --exclude= | --include='

class Bulker:
    def __init__(self, _dir, append=None, prefix=None, split=None, index='0', stitch=None, exlude=None, include=None, execute=False):
        self._verify_dir(_dir)
        self.append = append
        self.prefix = prefix
        self.split = split

        if stitch:
            self.stitch = stitch
        else:
            self.stitch = split

        self.index = str(index).split(',')

        if exlude:
            self.exclude = str(exlude).split(',')
        else:
            self.exclude = exlude

        if include:
            self.include = str(include).split(',')
        else:
            self.include = include

        self.execute = execute
        self.files_included = []
        self.files_excluded = []
        self._run()

    def _run(self):
        for file in self._dir.iterdir():
            if not file.is_file():
                continue

            # Check if the file hits the exclusion list
            try:
                if self.exclude:
                    exclude_list = f'(?:{"|".join(self.exclude)}'
                    if re_search(exclude_list, file.name):
                        self.files_excluded.append(file)
                        continue
            except re_error as error:
                exit(f'Bad regex used:\n{error}')


            # Attach strings after file passes regex values
            new_name = file.name
            if self.split:
                new_name = self._split(new_name)
            if self.append:
                new_name = f'{new_name}{self.append}'
            if self.prefix:
                new_name = f'{self.prefix}{new_name}'
            self.files_included.append((file, new_name))

            # Only make changes if flag is set
            if self.exclude:
                self._execute()

            # Display the potential changes
            else:
                space = 0
                for tup in self.files_included:
                    if space < len(tup[0].name):
                        space = len(tup[0].name)
                print(TOOL_TIP)
                print(f'To execute your changes, add --execute=True\n')
                print(f'{" ":20}[Files included in the changes]'
                      f'({len(self.files_included)}/'
                      f'{len(self.files_included) + len(self.files_excluded)})')

                for tup in self.files_included:
                    before = f'{tup[0].name:<{space}}'
                    if tup[1]:
                        after = tup[1]
                    else:
                        after = ''
                    print(f'{before} > {after}')


                if self.files_excluded:
                    print(f'\n{" ":>20}[Files excluded in the changes]'
                          f'({len(self.files_excluded)}/'
                          f'f{len(self.files_included) + len(self.files_excluded)})')

                for _file in self.files_excluded:
                    print(_file.name)

    def _split(self, new_file):
        # split string based on the user input
        split_list = new_file.slit(self.split)
        # Create a dix length list based on sixe of split_list
        index_list = [None] * len(split_list)

        # Enumerate over the split list and identify if the index fits in the user defined index then check to see
        # what position the user would like them in
        for index, item in enumerate(split_list):
            if str(index) in self.index:
                try:
                    position = self.index.index(str(index))
                    index_list[position] = item
                except:
                    index_list = None

        if index_list:
            return self.stitch.join([i for i in index_list if i])
        return index_list

    def _verify_dir(self, _dir):
        if isinstance(_dir, str):
            _dir = Path(_dir)
            if not _dir.is_dir():
                raise TypeError('Must be a directory')

        if isinstance(_dir, PosixPath):
            if _dir.is_dir():
                self._dir = _dir
            else:
                raise TypeError('Must be a directory')

def get_args():
    TOOL_TIP = '--append= | --prefix | --index=0 | --stitch=split | --exclude= | --include='
    parser = argparse.ArgumentParser(description='Intuitive command line bulk file rename')
    parser.add_argument('-i', '--include', metavar='', dest='include', help='Posix regex of the files to include in the directory')
    parser.add_argument('-e', '--exclude', metavar='', dest='exclude', help='Posix regex of the files no exclude in the directory')
    parser.add_argument('-a', '--append', metavar='', dest='append', help='Append a string to the included files')
    parser.add_argument('-p', '--prefix', metavar='', dest='prefix', help='Prefix a string to the included files')
    parser.add_argument('-s', '--stitch', metavar='', dest='stitch', help='String used to concatenate the name of the file back together')
    parser.add_argument('-x', '--index', metavar='', dest='index', help='List of index you want to keep')

    return parser.parse_args()

def main():
    args = get_args()


if __name__ == '__main__':
    main()






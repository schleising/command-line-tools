#!/opt/homebrew/bin/python3.11

import sys
from pathlib import Path

if __name__ == '__main__':
    if len(sys.argv) > 1:
        req_in_file = Path(sys.argv[1])

        if req_in_file.is_file():
            req_out_file = req_in_file.parent / f'{req_in_file.stem}_out{req_in_file.suffix}'
            print(f'[dodger_blue1]Input File:[/]  {req_in_file}')
            print(f'Output File: {req_out_file}')
            with (req_in_file.open('r', encoding='utf8') as input_file,
                  req_out_file.open('w', encoding='utf8') as output_file):
                for line in input_file.readlines():
                    output_file.write(f'{line[0:line.find("==")]}\n')

        else:
            print(f'{req_in_file} is not a valid filename')
    else:
        print('You need to specify the filename as a parameter')

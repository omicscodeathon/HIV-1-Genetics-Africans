#!/usr/bin/env python

import sys
import logging


logging.basicConfig(level=logging.INFO,
                    # filename='data_downloader.log',
                    format='%(asctime)s %(levelname)s %(message)s',
                    )


def edit_fasta(file, download_type):
    with open(f'edited_sequence.fasta', 'w') as fasta_edit:
        with open(file, 'r') as fasta:
            for line in fasta.readlines():
                if line.startswith('>'):
                    if download_type == 'manual':
                        fasta_edit.write(line.replace(" |", '_'))
                    elif download_type == 'script':
                        split_line = line.split(" ")
                        fasta_edit.write(f'{split_line[0]}_{split_line[5]}\n')
                else:
                    fasta_edit.write(line)


if __name__ == '__main__':

    if len(sys.argv) > 2:
        edit_fasta(sys.argv[1], sys.argv[2])
    else:
        logging.error("Please input fasta file to edit and how you downloaded the file \n"
                      "\nuse this format:$ python3 fasta_edit.py <fasta_file> <manual or script> \n")


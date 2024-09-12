'''
    Author: Heng-Jui Chang
'''

import csv
import argparse


def read_original_score(args):
    with open(args.orig_file, 'r') as fp:
        rows = csv.reader(fp)
        id2score = {}
        # print(rows)
        for i, row in enumerate(rows):
            # print(row)
            if i % 2 == 1 or i == 0:
                continue
            id2score[row[args.id_col].lower()] = row[args.score_col]
        return id2score


def output_ntucool_list(args, id2score):
    with open(args.cool_grade, 'r', encoding="utf-8", ) as fp:
        rows = csv.reader(fp)
        with open(args.cool_output, 'w', encoding="utf-8", newline='') as fp_out:
            writer = csv.writer(fp_out)
            row_tmp = []
            for i, row in enumerate(rows):
                row_tmp = row.copy()
                row_tmp[2] = row_tmp[2].replace("@ntu.edu.tw", "")
                # print(row[2].replace("@ntu.edu.tw", ""))
                print(row)
                # print(id2score)
                if i == 0 and i == 1:
                    writer.writerow(row + [args.title])
                elif i == 2:
                    writer.writerow(row + [''])
                elif id2score.get(row_tmp[2], None):
                    writer.writerow(row + [id2score[row_tmp[2]]])
                else:
                    writer.writerow(row + ['0'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Original score file
    parser.add_argument(
        '--orig-file', type=str, help='Original score file including ID.')
    parser.add_argument(
        '--id-col', type=int, help='The column index for IDs.')
    parser.add_argument(
        '--score-col', type=int, help='The column index for scores.')

    # NTU COOL file
    parser.add_argument(
        '--cool-grade', type=str, help='Original NTU COOL grade file.')
    parser.add_argument(
        '--cool-output', type=str, help='The output file name.')
    parser.add_argument(
        '--title', type=str, help='The title for the added score\'s column.')

    args = parser.parse_args()

    id2score = read_original_score(args)
    output_ntucool_list(args, id2score)

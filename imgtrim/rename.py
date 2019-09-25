#!/usr/bin/python

import os
import re


def rename_pattern(selected_files, regexp, cnt):
    for old_name in selected_files:
        date_search = re.search(regexp, old_name, re.IGNORECASE)
        new_name = date_search.group(1) + '.' + date_search.group(2) + '.' + date_search.group(3) + '_' + str(cnt) + '.' + date_search.group(4)
        print('Old name:' + old_name + ' | New name:' + new_name)
        os.rename(old_name, new_name)
        cnt = cnt + 1
    return cnt


def main():
    work_dir = os.path.dirname(os.path.realpath(__file__))
    print('Rename files in dir: ' + work_dir)

    all_img_files = []
    for subdir, dirs, files in os.walk(work_dir):
        for file in files:
            all_img_files.append(file)

    regexp_exprs = ['^IMG_(\\d\\d\\d\\d)(\\d\\d)(\\d\\d)_.+\\.(je?pg)$',
                    '^PHOTO_(\\d\\d\\d\\d)(\\d\\d)(\\d\\d)_.+\\.(je?pg)$',
                    '^MVIMG_(\\d\\d\\d\\d)(\\d\\d)(\\d\\d)_.+\\.(je?pg)$',
                    '^Pic_(\\d\\d\\d\\d)_(\\d\\d)_(\\d\\d)_.+\\.(je?pg)$',
                    '^VID_(\\d\\d\\d\\d)(\\d\\d)(\\d\\d)_.+\\.(mp4)$',
                    '^(\\d\\d\\d\\d)-(\\d\\d)-(\\d\\d)-.+\\.(mp4)$',
                    ]

    cnt = 1
    for regexp in regexp_exprs:
        selected_files = list(filter(re.compile(regexp).search, all_img_files))
        print('-----')
        cnt = rename_pattern(selected_files, regexp, cnt)
        print('Renamed: ' + str(cnt - 1))
        print('')

    print('Total renamed: ' + str(cnt - 1))


if __name__ == "__main__":
    main()
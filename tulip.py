import argparse
import subprocess
import datetime


class AppConsts:
    days_in_week = 7
    comment_symbol = "#"
    space_symbol = " "


def first_sunday(year: int) -> datetime.date:
    d = datetime.date(year=year, month=1, day=1)
    next_sunday = d + datetime.timedelta(AppConsts.days_in_week - 1 - d.weekday()) if d.weekday() != 6 else d
    return next_sunday


def commit_at(date: datetime.date) -> int:
    with open(".tulip", "a") as tulip_file:
        tulip_file.write(" ")
    ret_code = subprocess.run(["git", "add", ".tulip"]).returncode
    ret_code &= subprocess.run(
        ["git", "commit", "-m", "tulip automatic commit", "--date", date.strftime("%b %d %Y")]).returncode
    return ret_code


def main():
    parser = argparse.ArgumentParser(description='Tulip: Draw images on your GitHub `Contributing` graph.')
    parser.add_argument('--year', type=int, default=2019, help='a year to commit the picture')
    args = parser.parse_args()
    with open("data.txt") as data_file:
        lines = [line.strip() for line in data_file.readlines() if len(line) and line[0] != AppConsts.comment_symbol]
    lines = lines[:min(AppConsts.days_in_week, len(lines))]

    first_day = first_sunday(args.year)

    for vertical_offset, line in enumerate(lines):
        for horisontal_offset, char in enumerate(line):
            if char == AppConsts.comment_symbol:
                continue
            commit_day = first_day + datetime.timedelta(horisontal_offset * AppConsts.days_in_week + vertical_offset)
            commit_at(commit_day)


if __name__ == "__main__":
    main()

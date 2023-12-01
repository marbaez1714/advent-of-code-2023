import re


def part_one(lines: "list[str]"):
    sum = 0

    for line in lines:
        line = re.sub(r"\D", "", line)
        sum += int(line[0] + line[-1])

    print("Part One: " + str(sum))


def part_two(lines: "list[str]"):
    def format_line(line: str):
        return (
            line.replace("one", "one1one")
            .replace("two", "two2two")
            .replace("three", "three3three")
            .replace("four", "four4four")
            .replace("five", "five5five")
            .replace("six", "six6six")
            .replace("seven", "seven7seven")
            .replace("eight", "eight8eight")
            .replace("nine", "nine9nine")
        )

    sum = 0

    for line in lines:
        line = re.sub(r"\D", "", format_line(line))
        sum += int(line[0] + line[-1])

    print("Part Two: " + str(sum))


with open("day-1/input.txt", "r") as file:
    lines = file.readlines()

    part_one(lines)
    part_two(lines)

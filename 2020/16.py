#!/usr/bin/env python3
import re
import pprint as pp


Rules = {}
ValidTickets = []
IllegalFields = []
ValidFields = []
Debug = True


def parse_rule(line: str):
    m = re.compile(
        r"^(?P<name>[^:]+):\s+(?P<lo1>\d+)-(?P<hi1>\d+)\s+or\s+(?P<lo2>\d+)-(?P<hi2>\d+)"
    ).search(line)
    if not m:
        return

    name = m.group("name")
    lo1 = int(m.group("lo1"))
    hi1 = int(m.group("hi1"))
    lo2 = int(m.group("lo2"))
    hi2 = int(m.group("hi2"))
    Rules[name] = [range(lo1, hi1 + 1), range(lo2, hi2 + 1)]
    print(line, ":", name, "=>", Rules[name]) if Debug else None


def parse_nearby_ticket(line: str):
    ticket = [int(value) for value in line.split(",")]
    for i, value in enumerate(ticket):
        matching_fields = get_matching_fields(value)
        if len(matching_fields) == 0:
            print("Field=", value, " did not match any rule", sep="") if Debug else None
            IllegalFields.append(value)
            break
        elif i >= len(ValidFields):
            ValidFields.append(matching_fields)
        else:
            ValidFields[i].intersection_update(matching_fields)

    else:
        ValidTickets.append(ticket)


def get_matching_fields(value: int) -> set:
    matching_fields = set()
    for name, ranges in Rules.items():
        for chk_range in ranges:
            if value in chk_range:
                matching_fields.add(name)
                break
    return matching_fields


def uniquify_fields():
    for i in range(len(ValidFields)):
        matching_fields = ValidFields[i]
        if len(matching_fields) == 1:
            remove_field_from_all_but(list(matching_fields)[0], i)


def remove_field_from_all_but(field, index_to_avoid):
    for i in range(len(ValidFields)):
        if i == index_to_avoid:
            continue
        ValidFields[i].discard(field)


done_parsing_rules = False
with open("16_in.txt") as file:
    for line in file:
        line = line.strip()
        if len(line) == 0:
            continue

        if re.compile("your ticket").match(line):
            done_parsing_rules = True
            line = next(file).strip()
            my_ticket = [int(field) for field in line.split(",")]
            ValidTickets.append(my_ticket)
            continue

        if re.compile("nearby tickets").match(line):
            continue

        if not done_parsing_rules:
            parse_rule(line)
        else:
            parse_nearby_ticket(line)


print("Ticket error scanning rate=", sum(IllegalFields), sep="")
pp.pprint(ValidFields) if Debug else None

# Keep calling this same function recursively till every field is unique
has_duplicates = True
while has_duplicates:
    for matching_fields in ValidFields:
        if len(matching_fields) > 1:
            uniquify_fields()
            break
    else:
        has_duplicates = False
ValidFields = [x.pop() for x in ValidFields]
pp.pprint(ValidFields) if Debug else None
pp.pprint(ValidTickets[0])

product = 1
for i in range(len(ValidFields)):
    if re.compile("^departure").match(ValidFields[i]):
        product *= ValidTickets[0][i]
print(product)

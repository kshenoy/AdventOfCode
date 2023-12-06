#!/usr/bin/env python3

import pprint as pp
import re

Rules = {}
Msgs = []


def parse_rule(line: str):
    rule_num, rule_str = line.split(":")
    rule_num = int(rule_num)
    rule_str = rule_str.strip(' "')
    if (len(rule_str) == 1) and rule_str.isalpha():
        Rules[rule_num] = rule_str
    else:
        Rules[rule_num] = []
        for c in rule_str.split(" "):
            if c.isdigit():
                Rules[rule_num].append(int(c))
            else:
                Rules[rule_num].append(c)


parse_rules = True
with open("19_in.txt") as file:
    for line in file:
        line = line.strip()
        if len(line) == 0:
            parse_rules = False
            continue

        if parse_rules:
            parse_rule(line)
        else:
            Msgs.append(line)
# pp.pprint(Rules)


def expand_rule(rule_num: int) -> str:
    if type(Rules[rule_num]) != type(""):
        for i, sub_rule in enumerate(Rules[rule_num]):
            if type(sub_rule) == type(1):
                Rules[rule_num][i] = expand_rule(sub_rule)

        if "|" in Rules[rule_num]:
            Rules[rule_num] = "(" + "".join(Rules[rule_num]) + ")"
        else:
            Rules[rule_num] = "".join(Rules[rule_num])

    return Rules[rule_num]


expand_rule(0)
# pp.pprint(Rules)

num_matches = 0
pat = re.compile("^" + Rules[0] + "$")
for msg in Msgs:
    if pat.match(msg):
        num_matches += 1

print("No. matches=", num_matches, sep="")

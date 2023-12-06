import pprint

pp = pprint.PrettyPrinter(indent=2, width=120)

NumElvesToTrack = 3

# Read in the word list.
# The with statement automatically closes the file after the block
with open("1_in.txt") as file:
    lines = [line.strip() for line in file.readlines()]

tracker = {}


def updateTracker(elf, calories):
    tracker[elf] = calories
    if len(tracker) > NumElvesToTrack:
        poorestElf = sorted(tracker, key=tracker.get, reverse=True).pop()
        tracker.pop(poorestElf)


elf = 1
calories = 0
for line in lines:
    if line:
        calories += int(line)
    else:
        updateTracker(elf, calories)
        elf += 1
        calories = 0
updateTracker(elf, calories)

# pp.pprint(tracker)
richestElf = sorted(tracker, key=tracker.get)[-1]
print(
    "Sum of "
    + str(NumElvesToTrack)
    + "-highest calories is "
    + str(sum(tracker.values()))
    + ". The elf with most calories is #"
    + str(richestElf)
    + " with "
    + str(tracker[richestElf])
    + " calories!"
)

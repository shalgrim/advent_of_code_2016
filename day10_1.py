import re
from collections import defaultdict

BOT_PATT = re.compile(
    r'bot (?P<givebot>\d+) gives low to (?P<lotype>\S+) (?P<lobot>\d+) and high to (?P<hitype>\S+) (?P<hibot>\d+)'
)
VALUE_PATT = re.compile(r'value (?P<val>\d+) goes to bot (?P<getbot>\d+)')


def make_bot_rules(bot_lines):
    bot_rules = {}

    for line in bot_lines:
        match = BOT_PATT.match(line)
        bot_rules[int(match.group('givebot'))] = {
            'lo': int(match.group('lobot')),
            'lotype': match.group('lotype'),
            'hi': int(match.group('hibot')),
            'hitype': match.group('hitype'),
        }

    return bot_rules


def make_value_rules(value_lines):
    value_rules = defaultdict(list)

    for line in value_lines:
        match = VALUE_PATT.match(line)
        value_rules[int(match.group('getbot'))].append(int(match.group('val')))

    return value_rules


def main(lines):
    bot_rules, value_rules = create_rules(lines)

    bots = initialize_outputs_with_val_rules(value_rules)
    outputs = {}

    while True:
        bots_with_two = [bot for bot, bot_has in bots.items() if len(bot_has) == 2]

        for bot in bots_with_two:
            if sorted(bots[bot]) == [17, 61]:
                return bot
            process_bot_rules(bot, bot_rules, bots, outputs)


def process_bot_rules(bot, bot_rules, bots, outputs):
    lo = min(bots[bot])
    hi = max(bots[bot])
    if bot_rules[bot]['lotype'] == 'bot':
        bots[bot_rules[bot]['lo']].append(lo)
    else:
        outputs[bot_rules[bot]['lo']] = lo
    if bot_rules[bot]['hitype'] == 'bot':
        bots[bot_rules[bot]['hi']].append(hi)
    else:
        outputs[bot_rules[bot]['hi']] = lo
    bots[bot].clear()


def initialize_outputs_with_val_rules(value_rules):
    bots = defaultdict(list)
    for getbot, val_list in value_rules.items():
        bots[getbot].extend(val_list)
    return bots


def create_rules(lines):
    bot_lines = [line for line in lines if line[0] == 'b']
    value_lines = [line for line in lines if line[0] == 'v']
    bot_rules = make_bot_rules(bot_lines)
    value_rules = make_value_rules(value_lines)
    return bot_rules, value_rules


if __name__ == '__main__':
    with open('data/input10.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))

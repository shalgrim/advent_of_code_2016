from day10_1 import create_rules, initialize_outputs_with_val_rules, process_bot_rules


def main(lines):
    bot_rules, value_rules = create_rules(lines)

    bots = initialize_outputs_with_val_rules(value_rules)
    outputs = {}

    while not (0 in outputs and 1 in outputs and 2 in outputs):
        bots_with_two = [bot for bot, bot_has in bots.items() if len(bot_has) == 2]

        for bot in bots_with_two:
            process_bot_rules(bot, bot_rules, bots, outputs)

    return outputs[0] * outputs[1] * outputs[2]


if __name__ == '__main__':
    with open('data/input10.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))

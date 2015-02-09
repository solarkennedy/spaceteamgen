#!/usr/bin/env python
import argparse
import random


def weighted_choice(choices):
    """Weighted choice pattern
    http://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice
    """
    total = sum(w for c, w in choices)
    r = random.uniform(0, total)
    upto = 0
    for c, w in choices:
        if upto + w > r:
            return c
        upto += w


def verb():
    return "No verbs yet"


def achievement():
    return "No achievements yet"


def off():
    off_verb = random.choice(load_file('OffVerbs.txt'))
    noun = random.choice(load_nouns())
    return "%s %s!" % (off_verb, noun)


def on():
    on_verb = random.choice(load_file('OnVerbs.txt'))
    noun = random.choice(load_nouns())
    return "%s %s!" % (on_verb, noun)


def mundane():
    actions = load_file('MundaneActions.txt')
    action = random.choice(actions)
    verb, noun = action.split(',')
    return "%s %s!" % (verb, noun)


def load_file(filename):
    return map(str.strip, open(filename).readlines())


def load_nouns():
    return load_file('Nouns.txt')


# List of tuples, (thing, weight)
THINGS_TO_SAY = [
    (verb, 5),
    (achievement, 3),
    (off, 1),
    (on, 1),
    (mundane, 1)
]


def parse_args():
    parser = argparse.ArgumentParser(description='Prints a spaceteam-like command.')
    parser.add_argument('action', nargs='?', default=False,
                        choices=['verb', 'achievement', 'off', 'on', 'mundane'],
                        help="optional type of command you want to print.")
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    if args.action:
        # Seems dangerous?
        print(locals()[args.action]())
    else:
        action = weighted_choice(THINGS_TO_SAY)
        print(action())

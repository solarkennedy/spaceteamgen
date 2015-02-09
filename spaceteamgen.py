#!/usr/bin/env python
import argparse
import os
import random
import sys

FILE = {
    'offverbs': 'OffVerbs.txt',
    'onverbs': 'OnVerbs.txt',
    'mundaneactions': 'MundaneActions.txt',
    'adjectivesbefore': 'AdjectivesBefore.txt',
    'verbs': 'Verbs.txt',
    'nouns': 'Nouns.txt',
    'prefixparts': 'PrefixParts.txt',
    'baseparts': 'BaseParts.txt',
}


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
    verb = random.choice(load_verbs())
    part = get_part()
    return "%s %s!" % (verb, part)


def off():
    off_verb = random.choice(load_file(FILE['offverbs']))
    noun = get_noun()
    return "%s %s!" % (off_verb, noun)


def on():
    on_verb = random.choice(load_file(FILE['onverbs']))
    noun = get_noun()
    return "%s %s!" % (on_verb, noun)


def mundane():
    actions = load_file(FILE['mundaneactions'])
    action = random.choice(actions)
    verb, noun = action.split(',')
    return "%s %s!" % (verb, noun)


def setting():
    """Returns a string to set a part to a certain value.
    Like 'Set Psi-Condenser to 5!'
    """
    setting_verb = get_setting_verb()
    part = get_part()
    value = get_value()
    return "%s %s to %s!" % (setting_verb, part, value)


def get_noun():
    """Returns a fancy prefixed noun"""
    return random.choice(load_nouns())


def get_adjective():
    return random.choice(load_file(FILE['adjectivesbefore']))


def get_part():
    adjective = get_adjective()
    prefix = random.choice(load_file(FILE['prefixparts']))
    base_part = random.choice(load_file(FILE['baseparts']))
    return "%s %s%s" % (adjective, prefix, base_part)


def get_setting_verb():
    settings = ['Set', 'Increase', 'Decrease', 'Configure', 'Drop']
    return random.choice(settings)


def get_value():
    values = ['Full Power', 'Maximum', '1', '2', '3', '4', '5']
    return random.choice(values)


def load_file(filename):
    return map(str.strip, open(filename).readlines())


def load_nouns():
    return load_file(FILE['nouns'])


def load_verbs():
    return load_file(FILE['verbs'])


def validate_files():
    for f in FILE.values():
        if os.path.isfile(f) is not True:
            err = "%s is missing! Make sure this file is available.\n" % f
            sys.stderr.write(err)
            sys.exit(1)


# List of tuples, (thing, weight)
THINGS_TO_SAY = [
    (verb, 5),
    (setting, 5),
    (off, 1),
    (on, 1),
    (mundane, 1)
]


def parse_args():
    parser = argparse.ArgumentParser(
        description='Prints a spaceteam-like command.')
    choices = [x[0].__name__ for x in THINGS_TO_SAY]
    parser.add_argument('action', nargs='?', default=False,
                        choices=choices,
                        help="optional type of command you want to print.")
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    validate_files()
    if args.action:
        # Seems dangerous?
        print(locals()[args.action]())
    else:
        action = weighted_choice(THINGS_TO_SAY)
        print(action())

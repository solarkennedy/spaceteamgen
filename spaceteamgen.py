#!/usr/bin/env python
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
    pass


def achievement():
    pass


def off():
    pass


def on():
    pass


def mundane():
    actions = load_file('MundaneActions.txt')
    action = random.choice(actions)
    verb, noun = action.split(',')
    return "%s %s!" % (verb, noun)


def load_file(filename):
    return open(filename).readlines()


# List of tuples, (thing, weight)
THINGS_TO_SAY = [
    (verb, 10),
    (achievement, 1),
    (off, 2),
    (on, 2),
    (mundane, 1)
]


if __name__ == '__main__':
    action = weighted_choice(THINGS_TO_SAY)
    print action()

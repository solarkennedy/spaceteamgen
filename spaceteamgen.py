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
    return "No verbs yet"


def achievement():
    return "No achievements yet"


def off():
    return "No off commands yet"


def on():
    return "No on commands yet"


def mundane():
    actions = load_file('MundaneActions.txt')
    action = random.choice(actions).strip()
    verb, noun = action.split(',')
    return "%s %s!" % (verb, noun)


def load_file(filename):
    return open(filename).readlines()


# List of tuples, (thing, weight)
THINGS_TO_SAY = [
    (verb, 0),
    (achievement, 0),
    (off, 0),
    (on, 0),
    (mundane, 1)
]


if __name__ == '__main__':
    action = weighted_choice(THINGS_TO_SAY)
    print(action())

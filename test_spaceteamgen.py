import mock

import contextlib

import spaceteamgen


def test_weighted_choice():
    """This isn't a very good test"""
    choices = [('test', 1), ('test2', 1)]
    with mock.patch('random.uniform', autospec=True, return_value=0):
        actual = spaceteamgen.weighted_choice(choices)
        assert actual == 'test'


def test_mundane():
    mundane_actions = ['Foo,Bar']
    with mock.patch('spaceteamgen.load_file', autospec=True, return_value=mundane_actions):
        assert spaceteamgen.mundane() == 'Foo Bar!'


def test_on():
    on_verbs = ['Activate']
    nouns = ['Thing']
    with contextlib.nested(
        mock.patch('spaceteamgen.load_file',
                   autospec=True, return_value=on_verbs),
        mock.patch('spaceteamgen.load_nouns',
                   autospec=True, return_value=nouns)
    ):
        assert spaceteamgen.on() == 'Activate Thing!'


def test_off():
    off_verbs = ['DeActivate']
    nouns = ['Thing']
    with mock.patch('spaceteamgen.load_file', autospec=True, return_value=off_verbs), \
            mock.patch('spaceteamgen.load_nouns', autospec=True, return_value=nouns):
        assert spaceteamgen.off() == 'DeActivate Thing!'


def test_achievement():
    pass


def test_verb():
    pass

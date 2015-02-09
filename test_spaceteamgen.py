import mock


import spaceteamgen


def test_weighted_choice():
    """This isn't a very good test"""
    choices = [('test', 1), ('test2', 1)]
    with mock.patch('random.uniform', autospec=True, return_value=0):
        actual = spaceteamgen.weighted_choice(choices)
        assert actual == 'test'


def test_mundane():
    mundane_actions = ['Foo,Bar']
    with mock.patch('spaceteamgen.load_file', autospec=True,
                    return_value=mundane_actions):
        assert spaceteamgen.mundane() == 'Foo Bar!'


def test_on():
    on_verbs = ['Activate']
    noun = 'Thing'
    with mock.patch('spaceteamgen.load_file',
                    autospec=True, return_value=on_verbs), \
        mock.patch('spaceteamgen.get_noun',
                   autospec=True, return_value=noun):
        assert spaceteamgen.on() == 'Activate Thing!'


def test_off():
    off_verbs = ['DeActivate']
    noun = 'Thing'
    with mock.patch('spaceteamgen.load_file', autospec=True,
                    return_value=off_verbs), \
        mock.patch('spaceteamgen.get_noun', autospec=True,
                   return_value=noun):
        assert spaceteamgen.off() == 'DeActivate Thing!'


def test_verb():
    verbs = ['do']
    part = 'thing'
    with mock.patch('spaceteamgen.load_verbs',
                    autospec=True, return_value=verbs), \
        mock.patch('spaceteamgen.get_part', autospec=True, return_value=part):
        assert spaceteamgen.verb() == 'do thing!'

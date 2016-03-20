import random


class Library:
    """This is the library of information to have a conversation.
    For now it is going to be a python dictionary containing some pre-existing
    words and phrases"""

    def __init__(self):

        self.library = {
            'greeting': {'phrases': ['hello', 'hi', 'hey', 'yo', 'howdy'],
                         'response': ['greeting', 'prompt']},
            'prompt': {'phrases': ["how's it going?", "what's up?",
                                   "how are you?"],
                       'response': ['good', 'ask after']},
            'filler': {'phrases': ['yeah', 'ok', 'right on', 'alright',
                                   'k', 'heh'],
                       'response': ['filler']},
            'good': {'phrases': ['doing good', "I'm doing good", "I'm well"],
                     'response': ['affirm']},
            'affirm': {'phrases': ['good!', 'glad to hear', 'awesome!', ':)'],
                       'response': []},
            'ask after': {'phrases': ['and yourself?', 'yourself?',
                                      'how about you?'],
                          'response': ['good']}
        }

    def get_phrase_types(self, phrases):
        """Given a list of phrases, find what types the phrase falls under"""
        phrase_types = []
        for phrase in phrases:
            for known_type in self.library.keys():
                if phrase in self.library[known_type]['phrases']:
                    phrase_types.append(known_type)
        return phrase_types

    def get_responses(self, phrase_types):
        """Given a list of phrase_types that the input list belongs to
        return a list of phrases to respond with"""
        responses = []
        for phrase_type in phrase_types:
            responses.extend(self.library[phrase_type]['response'])
        return responses

    def get_phrases(self, phrase_types):
        """Given a list of phrase types, return a list of phrases to
        say in the order of phrase types"""
        phrases = []
        for phrase_type in phrase_types:
            index = random.randrange(
                0, len(self.library[phrase_type]['phrases']))
            phrases.append(self.library[phrase_type]['phrases'][index])
        return phrases

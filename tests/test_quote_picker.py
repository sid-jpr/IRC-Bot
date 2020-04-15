import os

from twisted.trial import unittest
from talkback.quote_picker import QuotePicker


class TestQuotePicker(unittest.TestCase):
    
    QUOTE1 = (
        "I do not fear computers. I fear lack of them. "
        "– Isaac Asimov"
    )
    QUOTE2 = (
        "A computer once beat me at chess, but it was no match for me at kick boxing. "
        "– Emo Philips"
    )

    def test_pick(self):
        picker = QuotePicker(
            os.path.join(os.path.dirname(__file__), "test_quotes.txt")
        )
        quote = picker.pick()
        self.assertIn(quote, (self.QUOTE1, self.QUOTE2),
                      "Got unexpected quote: '%s'" % (quote))
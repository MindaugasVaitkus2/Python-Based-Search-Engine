import unittest

from buscasrc.core.filters.tokens_filters.stop_words_filter import StopWordsFilter


class TestStopWordsFilter(unittest.TestCase):
    def test_filter_tokens(self):
        input_tokens = ["why","would","you","schedule","a","vote","on","a","bill","that","is","at","17%","approval?"]

        stopwordsfilter = StopWordsFilter(input_tokens)

        self.assertEquals(stopwordsfilter.filter_tokens(), ["schedule","vote","bill","17%","approval?"])

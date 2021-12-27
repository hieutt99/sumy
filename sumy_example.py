# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
# from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words



LANGUAGE = "vietnamese"
SENTENCES_COUNT = 10

test = 'Trường Đại học Bách khoa tại Hà Nội (Hanoi University of Science and Technology) chính là trường đại học chuyên ngành kỹ thuật đầu ngành tại Việt Nam, thành viên của Bộ Giáo dục và Đào tạo, được xếp vào nhóm đại học trọng điểm quốc gia Việt Nam. Trường cũng là thành viên của Hiệp hội các trường đại học kỹ thuật hàng đầu khu vực Châu Á - Thái Bình Dương AOTULE (Asia-Oceania Top University League on Engineering). Tầm nhìn trở thành một đại học nghiên cứu hàng đầu khu vực với nòng cốt là kỹ thuật và công nghệ, tác động quan trọng vào phát triển nền kinh tế tri thức và góp phần gìn giữ an ninh, hòa bình đất nước, tiên phong trong hệ thống giáo dục đại học Việt Nam (Công bố ngày 15 tháng 02 năm 2017 kèm theo Quyết định số 244/QĐ-ĐHBK-HCTH).'



if __name__ == "__main__":
    # url = "https://en.wikipedia.org/wiki/Automatic_summarization"
    # parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    # or for plain text files
    # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
    parser = PlaintextParser.from_string(test, Tokenizer(LANGUAGE))
    print(parser.document._paragraphs)

    # stemmer = Stemmer(LANGUAGE)

    # summarizer = TextRankSummarizer(stemmer)
    # summarizer.stop_words = get_stop_words(LANGUAGE)
    summarizer = TextRankSummarizer()

    # for sentence in summarizer(parser.document, SENTENCES_COUNT):
    #     print(sentence)
    sents = summarizer(parser.document, SENTENCES_COUNT)
    print(sents)
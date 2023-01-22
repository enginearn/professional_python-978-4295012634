#!/usr/bin/env python3

import re

def get_matches_for_pattern(pattern: str, string: str) -> list[str]:
    matches = pattern.findall(string)
    return [match[0] for match in matches]

product_review = """
This is a fine milk, but the product line appears
to be limited in available colors. I couldn't only find white.
"""

sentence_pattern = re.compile(r'(.*?\.)(\s|&)', re.DOTALL)
# matches = sentence_pattern.findall(product_review)
sentences = get_matches_for_pattern(sentence_pattern, product_review)

word_pattern = re.compile(r"([\w\-']+)([\s,.])?")
for sentence in sentences:
    # matches = word_pattern.findall(sentence)
    words = get_matches_for_pattern(word_pattern, sentence)
    print(words)


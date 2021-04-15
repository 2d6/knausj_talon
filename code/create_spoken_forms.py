from typing import List, Optional, Dict
import itertools
from talon import registry
import re

from .extensions import _file_extensions_defaults
from .numbers import digits_map
from .abbreviate import abbreviations

# TODO: 'Whats application': 'WhatsApp' (Should keep "whats app" as well?)
# TODO: 'V O X': 'VOX' (should keep "VOX" as well?)
# Could handle by handling all alternatives for these, or by having hardcoded list of things that we want to handle specially

DEFAULT_MINIMUM_TERM_LENGTH = 3

SMALL_WORD = r"[A-Z]?[a-z]+"
# TODO: We want "AXEvery" to be ["AX", "Every"]
UPPERCASE_WORD = r"[A-Z]+"
FILE_EXTENSIONS_REGEX = "|".join(
    re.escape(file_extension) for file_extension in _file_extensions_defaults.values()
)
DIGITS_REGEX = r"\d"
FULL_REGEX = re.compile(
    "|".join([DIGITS_REGEX, FILE_EXTENSIONS_REGEX, SMALL_WORD, UPPERCASE_WORD,])
)

REVERSE_PRONUNCIATION_MAP = {
    **{value: key for key, value in abbreviations.items()},
    **{value: key for key, value in _file_extensions_defaults.items()},
    **{str(value): key for key, value in digits_map.items()},
}


def create_single_spoken_form(source: str):
    normalized_source = source.lower()
    try:
        mapped_source = REVERSE_PRONUNCIATION_MAP[normalized_source]
    except KeyError:
        mapped_source = source
    if mapped_source.isupper():
        mapped_source = " ".join(mapped_source)
    return mapped_source


def create_spoken_forms(
    source: str,
    words_to_exclude: Optional[List[str]] = None,
    minimum_term_length=DEFAULT_MINIMUM_TERM_LENGTH,
) -> List[str]:
    if words_to_exclude is None:
        words_to_exclude = []

    pieces = list(FULL_REGEX.finditer(source))
    # print([piece.group(0) for piece in pieces])

    term_sequence = " ".join(
        [create_single_spoken_form(piece.group(0)) for piece in pieces]
    ).split(" ")
    # print(term_sequence)

    terms = [
        term.strip()
        for term in set(
            term_sequence
            + list(itertools.accumulate([f"{term} " for term in term_sequence]))
        )
    ]

    terms = [
        term
        for term in terms
        if term not in words_to_exclude and len(term) >= minimum_term_length
    ]
    # print(terms)

    if source not in terms:
        terms.append(source)
    return terms


def create_spoken_forms_for_list(
    source_list: List[str],
    words_to_exclude: Optional[List[str]] = None,
    minimum_term_length=DEFAULT_MINIMUM_TERM_LENGTH,
) -> Dict[str, str]:
    if words_to_exclude is None:
        words_to_exclude = []

    result = {}

    # todo: figure out what to do with ambiquities
    ambiguities = {}
    for source in source_list:
        terms = create_spoken_forms(source, words_to_exclude, minimum_term_length)
        for term in terms:
            if (
                term not in ambiguities
                and term not in words_to_exclude
                and len(term) >= minimum_term_length
            ):
                if term in result and result[term] != source:
                    # result.pop(term)
                    if term not in ambiguities:
                        ambiguities[term] = []

                    ambiguities[term].append(source)
                else:
                    result[term] = source
    # print(str(result))
    return result
    # print(terms)


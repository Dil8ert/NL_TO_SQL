import spacy

# Import the Matcher
from spacy.matcher import Matcher

# Load a pipeline and create the nlp object
nlp = spacy.load("en_core_web_sm")
def NLP_SQL(text):
    doc = nlp(text)
    # Initialize the matcher with the shared vocab
    matcher = Matcher(nlp.vocab)

    # Add the pattern to the matcher
    pattern = [{"POS": "PROPN"}]
    matcher.add("PATTERN_1", [pattern])

    # Process some text

    matched = []

    # Call the matcher on the doc
    matches = matcher(doc)
    for token in doc:
        if(token.pos_ == 'PROPN'):
            if(doc[token.i+1].pos_ == 'ADP'):
                starts_at = token.text
                ends_at = doc[token.i+2].text

    

    sql = "SELECT * FROM TRAINS WHERE START = '{}' AND ENDS = '{}'".format(starts_at,ends_at)
    print(sql)
    return sql

# NLP_SQL("List trains available from bombay to goa.")
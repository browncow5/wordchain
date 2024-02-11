import requests
import logging
#from ddtrace import tracer,patch; patch(logging=True)

# Configure the logging
FORMAT = ('%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] '
          '[dd.service=%(dd.service)s dd.env=%(dd.env)s dd.version=%(dd.version)s dd.trace_id=%(dd.trace_id)s dd.span_id=%(dd.span_id)s] '
          '- %(message)s')
logging.basicConfig(format=FORMAT, level=logging.INFO)
logger = logging.getLogger(__name__)


#@tracer.wrap(service="compound-words", resource="generate-compound-word-list")
def generateCompoundWordList(root_word, length):
    logger.info("Running generateCompoundWordList")
    result = [root_word] + recursive_compound_search(root_word, length)
    return result


#@tracer.wrap(service="compound-words", resource="recursive-compound-word-search")
def recursive_compound_search(root_word, length, current_depth=1):
    if current_depth == length:
        return []

    logger.info(f"Recursion depth: {current_depth}")
    compound_words = find_compound_words(root_word, length)
    ordered_compound_words = sorted(compound_words, key=lambda object: object[1] + object[3], reverse=True)
    logger.info(f"Ordered compound words: {ordered_compound_words}")

    if not compound_words:
        return []

    second_part = str(ordered_compound_words[0][2])
    logger.info(f"Pushing: {second_part} to list")
    return [second_part] + recursive_compound_search(second_part, length, current_depth + 1)


# Gets the frequency of the compound word as well as the second part
# and add the data to an object that is returned. 
#@tracer.wrap(service="compound-words", resource="find-compound-words")
def find_compound_words(root_word, length):
    logger.info(f"Finding compound words for root word '{root_word}'...")
    url = f"https://api.datamuse.com/words?sp={root_word}????*&max=8"
    response = requests.get(url)
    words = [word["word"] for word in response.json()]
    compound_words = [word for word in words if len(word) > len(root_word)]
    logger.info(f"Found compound words: {compound_words}")

    verified_compound_words = []
    for word in compound_words:
        second_part = word[len(root_word):]
        # remove leading spaces and hyphens
        second_part = second_part.lstrip(" ")
        second_part = second_part.lstrip("-")
        second_part_freq = get_word_frequency(second_part)
        compound_word_freq = get_word_frequency(word)

        if second_part_freq > 1:
            verified_compound_words.append((word, compound_word_freq ,second_part, second_part_freq))
#            logger.info(f"Pushing {second_part} to Verified compound words")

    logger.info(f"Verified compound words: {verified_compound_words}")
    return verified_compound_words

    
def get_word_frequency(inputWord):
    url = f"https://api.datamuse.com/words?sp={inputWord}&max=1&md=f"
    response = requests.get(url)
    data = response.json()

    forbidden_words = ["ing", "a", "er", "ism", "nt", "nts"]

    if len(data) > 0:
        if inputWord in forbidden_words:
            logger.info(f"'{inputWord}' is in forbidden list")
            return 0
        ### NOTE this exclues words like "less than"
        # verify that the input word is the same word returned (ssing -> swing)
        if data[0]['word'] == inputWord:
            tags = data[0].get("tags", [])
            for tag in tags:
                if tag.startswith("f:"):
                    frequency = float(tag[2:])
#                    logger.info(f"'{inputWord}' has a frequency({frequency})")
                    return frequency
        else:
            logger.info(f"Input word:'{inputWord}' does not match returned word '{data[0]['word']}'")
            return 0   
    else:
        logger.info(f"'{inputWord}' no data returned")
        return 0

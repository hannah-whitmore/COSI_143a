
import re
import sys
import json

def preprocess_word(word):
    # Remove punctuation
    word = word.strip('\'"?!,.():;')

    # Convert more than 2 letter repetitions to 2 letter. Example: funnnnny --> funny
    #TODO: The next line should implement the functionality in the above comment.
    ##word = YOUR CODE GOES HERE
    p = re.compile(r"(.)\1{2,}", re.DOTALL)
    word = p.sub(r"\1\1", word)

    # Remove - & '
    # TODO: The next line should implement the functionality in the above comment.
    word = word.strip('&')
    word = word.strip('-')
    word = word.strip('\'')
    return word

def is_valid_word(word):
    # Check if word begins with an alphabet
    return (re.search(r'^[a-zA-Z][a-z0-9A-Z\._]*$', word) is not None)


def handle_emojis(tweet):
    # Smile -- :), : ), :-), (:, ( :, (-:, :')
    tweet = re.sub(r'(:\s?\)|:-\)|\(\s?:|\(-:|:\'\))', ' EMO_POS ', tweet)
    # Laugh -- :D, : D, :-D, xD, x-D, XD, X-D
    tweet = re.sub(r'(:\s?D|:-D|x-?D|X-?D)', ' EMO_POS ', tweet)
    # Love -- <3, :*
    tweet = re.sub(r'(<3|:\*)', ' EMO_POS ', tweet)
    # Wink -- ;-), ;), ;-D, ;D, (;,  (-;
    tweet = re.sub(r'(;-?\)|;-?D|\(-?;)', ' EMO_POS ', tweet)
    # Sad -- :-(, : (, :(, ):, )-:
    tweet = re.sub(r'(:\s?\(|:-\(|\)\s?:|\)-:)', ' EMO_NEG ', tweet)
    # Cry -- :,(, :'(, :"(
    tweet = re.sub(r'(:,\(|:\'\(|:"\()', ' EMO_NEG ', tweet)
    return tweet


def preprocess_tweet(tweet):
    processed_tweet = []
    # Convert to lower case
    tweet = tweet.lower()
    # Replaces URLs with the empty string
    tweet = re.sub(r'((www\.[\S]+)|(https?://[\S]+))', ' ', tweet)
    # Replace @handle with the empty string
    tweet = re.sub(r'@[\S]+', '', tweet)

    # Replaces #hashtag with hashtag. Example #DataScience should be DataScience
    # TODO: The next line should implement the functionality in the above comment.
    tweet = tweet.replace('#', '')

    # Remove RT (retweet)
    # TODO: The next line should implement the functionality in the above comment.
    tweet = tweet.replace('RT', '')
    tweet = tweet.replace('rt', '')

    # Replace 2+ dots with space
    # TODO: The next line should implement the functionality in the above commen
    tweet = re.sub('\.\.+', ' ', tweet)

    # Strip space, " and ' from tweet
    tweet = tweet.strip(' "\'')
    # Replace emojis with either EMO_POS or EMO_NEG
    tweet = handle_emojis(tweet)
    # Replace multiple spaces with a single space
    tweet = re.sub(r'\s+', ' ', tweet)
    words = tweet.split()

    for word in words:
        word = preprocess_word(word)
        if is_valid_word(word):
            processed_tweet.append(word)

    return ' '.join(processed_tweet)


def preprocess_json(json_file_name, processed_file_name):
    save_to_file = open(processed_file_name, 'w')
    tweets = open(json_file_name, 'r')
    for line in tweets:
        tweet = json.loads(line)
        if 'text' in tweet:
            raw_tweet = tweet['text']
            processed_tweet = preprocess_tweet(raw_tweet)
            save_to_file.write('%s\n' % (processed_tweet))
    save_to_file.close()
    print('\nSaved processed tweets to: %s' % processed_file_name)
    return processed_file_name


if __name__ == '__main__':

    json_file_name = sys.argv[1]
    processed_file_name = 'clean_tweets.txt'
    preprocess_json(json_file_name, processed_file_name)

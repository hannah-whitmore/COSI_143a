import sys
import statistics

def create_sent_dict(sentiment_file):
    """A function that creates a dictionary which contains terms as keys and their sentiment score as value
        Args:
            sentiment_file (string): The name of a tab-separated file that contains
                                     all terms and scores (e.g., the AFINN file).
        Returns:
            dicitonary: A dictionary with schema d[term] = score
        """
    scores = {}
    sentiment_file = 'AFINN-111.txt' # to read strings from the command line you can use instead open(sys.argv[1])
    sentiment_file = open(sentiment_file, 'r')
    scores = {} # initialize an empty dictionary
    for line in sentiment_file:
        term, score = line.split("\t") # The file is tab-delimited and "\t" means tab character
        scores[term] = int(score) # Conver the score to an integer. It was parsed as a string.
    sentiment_file.close()
    return scores

def get_tweet_sentiment(tweet, sent_scores):
    """A function that find the sentiment of a tweet and outputs a sentiment score.
            Args:
                tweet (string): A clean tweet
                sent_scores (dictionary): The dictionary output by the method create_sent_dict
            Returns:
                score (numeric): The sentiment score of the tweet
        """
    score = 0
    for word in tweet.split():
        if word in sent_scores.keys():
            score = score+ sent_scores.get(word)
    return score

def term_sentiment(sent_scores, tweets_file):
    """A function that creates a dictionary which contains terms as keys and their sentiment score as value
            Args:
                sent_scores (dictionary): A dictionary with terms and their scores (the output of create_sent_dict)
                tweets_file (string): The name of a txt file that contain the clean tweets
            Returns:
                dicitonary: A dictionary with schema d[new_term] = score
            """

    # new_term_sent dicitonary has the new words as its key, and a list as its value
    # once a new word is found, calculate the sentiment of the overall tweet that word is contained in --> score
    # because new words can be found multiple times in different tweets, should keep track of all its tweet sentiments --> value_list
    # at the end, taking the average of this sentiments list should give a good idea of what the word's sentiment is

    new_term_sent = {}
    tweets = open(tweets_file, 'r')
    for tweet in tweets:
        for word in tweet.split():
            if word not in sent_scores.keys(): ## word is not in the dictionary
                score = get_tweet_sentiment(tweet, sent_scores)
                if word in new_term_sent:
                    new_term_sent[word].append(score)
                else:
                    new_term_sent[word] = [score]
    tweets.close()

    for key in new_term_sent.keys():
        value_list = new_term_sent.get(key)
        avg = statistics.mean(value_list)
        avg = round(avg, 2)
        new_term_sent[key] = avg
    return new_term_sent

def main():
    sentiment_file = sys.argv[1]
    tweets_file = sys.argv[2]

    # Read the AFINN-111 data into a dictionary
    sent_scores = create_sent_dict(sentiment_file)

    # Derive the sentiment of new terms
    new_term_sent = term_sentiment(sent_scores, tweets_file)

    for term in new_term_sent:
        print(term, new_term_sent[term])


if __name__ == '__main__':
    main()

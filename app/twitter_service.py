path = '../'
from datetime import datetime
from typing import List

import pandas as pd

from musow_pipeline.conf import TOKEN as token
from musow_pipeline.logreg_prediction import PredictPipeline
from musow_pipeline.text_prediction import TextPrediction
from musow_pipeline.twitter_pipeline import TwitterPipeline


# descriptions training set 
archive_desc_training = pd.read_pickle(path+'LOGREG_RELEVANCE/TRAINING_SETS/archive_desc_training_v4.pkl')

# twitter training set 
twitter_training = pd.read_pickle(path+'LOGREG_RELEVANCE/TRAINING_SETS/twitter_training_v2_alt.pkl')

# one time training on twitter
twitter_training_model = PredictPipeline.train(twitter_training, 'tweet', 'Target', 10, 1000, 'twitter_pipeline_june_2022', path)

# one time training on resources
resource_training_model = PredictPipeline.train(archive_desc_training, 'Description', 'Target', 10, 1000, 'resources_pipeline_june_2022',path)

def get_twitter_response(response):
    tweets = TwitterPipeline.search_custom(token, response.word, response.start, response.end, 500, 500)
    #load all search results into a single dataframe 
    tweets_to_classify = TwitterPipeline.classify_tweets(path+'TWITTER_SEARCHES/RAW_SEARCHES/', f'{tweets[0][-16:]}.pkl')
    return tweets_to_classify 

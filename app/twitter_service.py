path = '../'
from datetime import datetime
from typing import List

import pandas as pd

from .musow_pipeline.conf import TOKEN as token
from .musow_pipeline.logreg_prediction import PredictPipeline
from .musow_pipeline.twitter_pipeline import TwitterPipeline


# descriptions training set 
archive_desc_training = pd.read_pickle('app/TRAINING_SETS/archive_desc_training_v4.pkl')

# twitter training set 
twitter_training = pd.read_pickle('app/TRAINING_SETS/twitter_training_v2_alt.pkl')

def get_twitter_response(response):
    tweets = TwitterPipeline.search_custom(response["token"], response["word"], response["start"].strftime("%Y-%m-%dT%H:%M:%SZ"), response["end"].strftime("%Y-%m-%dT%H:%M:%SZ"), 500, 500)
    #load all search results into a single dataframe 
    tweets_to_classify = TwitterPipeline.classify_tweets('app/TWITTER_SEARCHES/RAW_SEARCHES/', f'{tweets[0][-16:]}.pkl')
    return tweets_to_classify 

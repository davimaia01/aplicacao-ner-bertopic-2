import pandas as pd
import numpy as np
from topicmodeling import TopicModeling

def read_csv(file_path):
    """
    Reads a csv file and returns a DataFrame
    """

    df = pd.DataFrame({'x': [1]})
    df = pd.read_csv(file_path)
    # df.sample(replace=True)
    df.head()
    docs = list(df.loc[:, "data"].values)
    
    return TopicModeling(docs)

   
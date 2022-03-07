from copy import deepcopy
import json
from bertopic import BERTopic


def getTopicModel():
    topic_model = BERTopic(language="Portuguese", min_topic_size=2)
    return topic_model


def getRepresentativeDocs(topic_model, topic_id):
    return topic_model.get_representative_docs(topic_id)


def TopicModeling(docs):
    topic_model = getTopicModel()
    # print(topic_model.fit_transform(list(docs)))
    topics, probs = topic_model.fit_transform(list(docs))

    # for tpc in list(tpcs.keys()):
    #     if (tpc != -1):
    #         print(getRepresentativeDocs(topic_model, tpc))

    #     # representativeDocs.append()

    topics = topic_model.get_topics(),

    probs = probs
    representative_docs = topic_model.get_representative_docs()
    frequency = topic_model.get_topic_freq()
    topic_info = topic_model.get_topic_info()

    return probs, topics, representative_docs, frequency, topic_info

"""
This AI help your for your write
"""
from torchtext.legacy import data, datasets
TEXT = data.Field(sequential=True, batch_first=True, lower=True)
LABEL = data.Field(sequential=False, batch_first=True)

trainset, testset = datasets.IMDB.splits(TEXT, LABEL)
print('훈련 데이터의 크기 : {}' .format(len(trainset)))
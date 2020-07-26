import codecs
import timeit
import pandas as pd

'''Moving Average'''
def sma(closeList=[], term=5):
    return list(pd.Series(closeList).rolling(term).mean())

'''Exponentially weighted Moving Average'''
def ema(closeList=[], term=5):
    s = pd.Series(closeList)
    sma = s.rolling(term).mean()[:term]
    return list(pd.concat([sma, s[term:]]).ewm(span=term, adjust=False).mean())


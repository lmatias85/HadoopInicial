import csv
import sys


def reducer_count():
    word = None
    count = None
    current_word = None
    current_count = 0

    for line in sys.stdin:
        line = line.strip()
        word, count = line.split('\t', 1)
        try:
            count = int(count)
        except ValueError:
            continue
        if current_word == word:
            current_count += count   
        else: 
            if current_word:
                print('{}\t{}'.format(current_word, current_count))
            current_count = count        
            current_word = word

    if current_word == word:
        print('{}\t{}'.format(current_word, current_count))

def reducer_least(size):
    leasts = {}
    for line in sys.stdin:
        least_size = len(leasts)
        line = line.strip()
        key, value = line.split('\t', 1)
        try:
            value = float(value)
        except ValueError:
            continue
        if least_size < size:
            leasts[key] = value
        else:
            if value < float(leasts[list(leasts.keys())[0]]):
                old_key = list(leasts.keys())[0]
                leasts[key] = leasts.pop(old_key)
                leasts[key] = value
        leasts = {k: v for k,v in sorted(leasts.items(), key=lambda item:item[1], reverse=True)}
    leasts = {k: v for k,v in sorted(leasts.items(), key=lambda item:item[1], reverse=False)}        
    for key, value in (leasts.items()):
        print('{}\t{}'.format(key,value))

def reducer_top(size):
    tops = {}
    for line in sys.stdin:
        top_size = len(tops)
        line = line.strip()
        key, value = line.split('\t', 1)
        try:
            value = float(value)
        except ValueError:
            continue
        if top_size < size:
            tops[key] = value
        else:
            if value < float(tops[list(tops.keys())[0]]):
                old_key = list(tops.keys())[0]
                tops[key] = tops.pop(old_key)
                tops[key] = value
        tops = {k: v for k,v in sorted(tops.items(), key=lambda item:item[1], reverse=True)}
    for key, value in (tops.items()):
        print('{}\t{}'.format(key,value)) 


if __name__ == "__main__":
    '''1-2'''
    #reducer_count()
    '''3'''
    #reducer_least(10)
    '''4'''
    #reducer_top(20)
    '''5'''
    #reducer_top(5)
    '''6'''
    #reducer_least(5)
    '''7'''
    #reducer_top(3)
    '''8'''
    #reducer_least(3)
    '''9'''
    reducer_count()
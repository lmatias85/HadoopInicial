import sys
import csv

def mapper_count(field):
    #with open('./hadoop_ecosystem_fundamentals_1/IMDBMovies/movie_metadata.csv',newline='', encoding='utf8') as csvfile:
    with open('movie_metadata.csv',newline='', encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            hdr_color = row[field].strip()
            if hdr_color is not None and hdr_color != '':
                print('{}\t{}'.format(hdr_color,1))

def mapper_least(field_to_count, field_amount, size):
    #with open('./hadoop_ecosystem_fundamentals_1/IMDBMovies/movie_metadata.csv',newline='', encoding='utf8') as csvfile:
    with open('movie_metadata.csv',newline='', encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        least_dict = {}     
        for row in reader:
            least_dict_size = len(least_dict)
            key = row[field_to_count].strip()
            value = row[field_amount].strip()
            try:
                value = float(value)
            except:
                continue
            if least_dict_size < size:
                least_dict[key] = value
            else:
                if value < float(least_dict[list(least_dict.keys())[0]]):
                    old_key = list(least_dict.keys())[0]
                    least_dict[key] = least_dict.pop(old_key)
                    least_dict[key] = value
            least_dict = {k: v for k,v in sorted(least_dict.items(), key=lambda item:item[1], reverse=True)}
    least_dict = {k: v for k,v in sorted(least_dict.items(), key=lambda item:item[1], reverse=False)}            
    for key, value in (least_dict.items()):
        print('{}\t{}'.format(key,value))

def mapper_top(field_to_count, field_amount, size):
    #with open('./hadoop_ecosystem_fundamentals_1/IMDBMovies/movie_metadata.csv',newline='', encoding='utf8') as csvfile:
    with open('movie_metadata.csv',newline='', encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        top_dict = {}     
        for row in reader:
            top_dict_size = len(top_dict)
            key = row[field_to_count].strip()
            value = row[field_amount].strip()
            try:
                value = float(value)
            except:
                continue
            if top_dict_size < size:
                top_dict[key] = value
            else:
                if value > float(top_dict[list(top_dict.keys())[0]]):
                    old_key = list(top_dict.keys())[0]
                    top_dict[key] = top_dict.pop(old_key)
                    top_dict[key] = value
            top_dict = {k: v for k,v in sorted(top_dict.items(), key=lambda item:item[1], reverse=False)}
    top_dict = {k: v for k,v in sorted(top_dict.items(), key=lambda item:item[1], reverse=True)}
    for key, value in (top_dict.items()):        
        print('{}\t{}'.format(key,value)) 

if __name__ == '__main__':
    '''1 '''
    #mapper_count('color')
    '''2 '''
    #mapper_count('director_name')
    '''3 '''
    #mapper_least('movie_title','imdb_score',10)
    '''4 '''
    #mapper_top('movie_title','duration', 20)
    '''5 '''
    #mapper_top('movie_title','gross', 5)
    '''6 '''
    #mapper_least('movie_title','gross',5)
    '''7 '''
    #mapper_top('movie_title','budget', 3)
    '''8 '''
    #mapper_least('movie_title','budget',3)
    '''9 '''
    mapper_count('title_year')
import json
import string

from pgsql import query
import sql
import requests


def get_movie_data(title):
    headers = {"Authorization": "9855f49b"}
    request_url = f"https://www.omdbapi.com/?t={title}&apikey=686eed26"
    return requests.get(request_url, headers=headers).json()


if __name__ == '__main__':
    # get some movie data from the API
    # print(get_movie_data('WarGames'))
    query(sql.create_schema, 'create schema')
    query(sql.create_table, 'create table')
    query(sql.truncate_table, 'truncate table')

    '''
    # reading movies.json file
    file_read = open('./datasets/json/movies.json', 'r')
    data = json.loads(file_read.read())
    file_read.close()

    # to keep distinct movie titles
    distinct_movies = set()

    # get distinct titles
    for item in data:
        if item["year"] >= 2018:
            # print(item["title"])
            distinct_movies.add(item["title"])

    # loop through distinct movies and download all movie records from API and save to file
    x = 1
    # creat empty list to keep list of movies
    list_api_data = []
    for i in distinct_movies:
        print(i)
        api_data = get_movie_data(i)
        if api_data["Response"] == "True" and 'English' in api_data["Language"]:  # and api_data["Year"] >= "2018"
            list_api_data.append(api_data)
            print(api_data)
            x += 1
 
    with open("./datasets/json/api_movies.json", "w") as outfile:
        json.dump(list_api_data, outfile, indent=1)
    print(x)  # 184 movies returned from api 228 without year fil
'''
    # reading movies.json file
    file_read = open('./datasets/json/api_movies.json', 'r')
    data = json.loads(file_read.read())
    file_read.close()
    record = []

    for row in data:
        if row['Title'] != "W":
            # print(type(row))
            # print(dict(filter(lambda item: 'N/A' in item[0], row.items())))
            record.append(row['Title'])
            record.append(row['Rated'])
            record.append(row['Released'])
            record.append((row['Runtime']).strip(' min'))
            record.append((row['Genre']).split(','))
            record.append(row['Director'])
            record.append((row['Writer']).split(','))
            record.append((row['Actors']).split(','))
            record.append(row['Plot'])
            record.append(row['Awards'])
            record.append(row['Poster'])

            joinedlist = lambda record: [element for item in record for element in joinedlist(item)] if type(record) is list else [record]
            na_rec2 = joinedlist(record)

            if 'N/A' not in na_rec2:
                # print(na_rec2)
                query(sql.insert_movie, record)
            # if 'N/A' not in list(filter(lambda rec: 'N/A' in rec, record)):
            #    print(record)
                # query(sql.insert_movie, record)
            record = []

    # print(record)


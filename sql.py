
create_schema = ('''
    create schema if not exists petl2
''')

create_table = ('''
    create table if not exists petl2.movie_list(
        title text,
        rated text,
        released date,
        runtime integer,
        genre text[],
        director text,
        writers text[],
        actors text[],
        plot text,
        awards text,
        poster text
    )
''')

truncate_table = ('''
    TRUNCATE TABLE petl2.movie_list
''')

insert_movie = ('''
    INSERT INTO petl2.movie_list 
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
''')

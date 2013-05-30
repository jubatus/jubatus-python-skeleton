#!/usr/bin/env python

host = 'localhost'
port = 9199
name = ''

import jubatus
from jubatus.recommender.types import datum

client = jubatus.Recommender(host, port)

client.update_row(name, 
                  "user01", 
                  datum([],
                        [("movie_A", 5.0),
                         ("movie_B", 2.0),
                         ("movie_C", 3.0)]))

client.update_row(name, 
                  "user02",
                  datum([],
                        [("movie_A", 2.0),
                         ("movie_B", 5.0),
                         ("movie_C", 1.0)]))

client.update_row(name, 
                  "user03", 
                  datum([],
                        [("movie_A", 5.0),
                         ("movie_B", 1.0),
                         ("movie_C", 4.0)]))

for id in client.get_all_rows(name):
    result = client.similar_row_from_id(name, id, 3)
    print id, "is similar to:"
    print " ",
    for score in result:
        print "%s (%f)," % (score[0], score[1]),
    print

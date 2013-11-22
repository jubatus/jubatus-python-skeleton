#!/usr/bin/env python

host = '127.0.0.1'
port = 9199
name = ''

import jubatus
from jubatus.common import Datum

client = jubatus.Recommender(host, port, name)

client.update_row("user01", 
                  Datum({"movie_A": 5.0,
                         "movie_B": 2.0,
                         "movie_C": 3.0}))

client.update_row("user02",
                  Datum({"movie_A": 2.0,
                         "movie_B": 5.0,
                         "movie_C": 1.0}))

client.update_row("user03", 
                  Datum({"movie_A": 5.0,
                         "movie_B": 1.0,
                         "movie_C": 4.0}))

for id in client.get_all_rows():
    result = client.similar_row_from_id(id, 3)
    print id, "is similar to:"
    print " ",
    for score in result:
        print "%s (%f)," % (score.id, score.score),
    print

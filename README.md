Skeleton of Jubatus Client Application in Python
=================================================

Requirements
------------

* Jubatus server 0.5.0+
* jubatus package ( install via `pip install jubatus` )

Usage
-----

To test the client, run:

```
$ jubarecommender --configpath /usr/local/share/jubatus/example/config/recommender/lsh.json &
$ python client.py
```

We assume that Jubatus was installed into /usr/local/. Otherwise, please modify the path.

Now, write your own code in `client.py`, then run the client again.

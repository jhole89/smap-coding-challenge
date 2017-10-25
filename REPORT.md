# Architecture
I tried to process and store the data into the default sqlite database in
the most simple way possible that aligned to python and django best
principles. I took a streaming approach to the data, whereby once a record
is read and loaded as a model it was saved straight away to avoid any data
loss in the event of a later failure. As a future improvement I would have
liked to make the import function take a keyword parameter for the
directories/files to pass, however the spec didn't allow for this.

Given that after aggregating the consumption data per user we have a small
json object, I felt that we could ship all the user aggregated data to
the front end, and perform any further aggregation depending on what we
wanted to display in the html. I initially looking into using d3js for
the aggregation charts (elements of this can still be seen in the front
end rollup aggregations to get per area and per tariff aggregations),
however ended up using chartjs instead as this provided simpler multigraphs,
along with a standard html table of all user-aggregations (limited to 40
for readability).

If I had a larger dataset that supported it I would have like to look at
doing some predictive analysis on the energy readings to try and train
a simple supervised algorithm for predicting energy usage over time, and
display this in the front end summary instead, but that was out of scope.

# Correctness
I believe I have addressed all of the requirements, except the optional
detail view. However I did design the aggregations with the detailed view
in mind for extensibility, e.g even with the summary view I parse over
as much data as I had from the backend (given that it was a small amount
of data) and did further rollup on the front end.

# Code quality
We are PEP8 compliant and this can be checked using `pep8 consumption`.
In terms of the Python code I have tried to document my work where possible
to show the intention behind certain methods, and avoided over complication.
In terms of the javascript/html I have tried to make methods as reusable
as possible, given that most of the aggregations and plotting we being repeated
for both graphs.

# Testing
The majority of our tests covers the Model classes and their associated
methods.  For this I have used pytest with django bindings.
Django typically uses unittest as it's default testing framework,
however I prefer pytest as it removes much of UnitTest's boilerplate,
allows for more compact testing, and provides better isolated tests via
conftest.

We can run the test coverage from dashboard/consumption using
`pytest tests.py` like so:

```
pytest tests.py
====================================== test session starts ============================================
platform darwin -- Python 2.7.13, pytest-3.2.1, py-1.4.34, pluggy-0.4.0
rootdir: /Users/lutmanj/PycharmProjects/smap-coding-challenge/dashboard/consumption, inifile:
plugins: django-3.1.2
collected 3 items

tests.py ...

==================================== 3 passed in 0.30 seconds =========================================
```

One area that I acknowledge lacks test coverage is under
dashboard/consumption/management/commands/import. There is currently no
testing of the handle method for importing data, something I would like
to rectify, however this would require breaking out the method into
multiple methods which could be better tested. I did consider this
however as these would be methods that are only used once within the
handle method this did seem a bit overkill and could lend itself to becoming
spaghetti code.  As a compromise I suppose I could have made these into
internal/private methods within the handle method, so would note that as
something to discuss with the reviewer in a PR.

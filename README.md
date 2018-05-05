# HN queries indexer and search API

This project aims at building an index of the query terms used in searches on the hacker news website.

The index can be queried with a date prefix (year, year-month, year-month-day etc) to get :

- The number of distinct query terms used for the given time interval.
- The most popular query terms in the given time interval.


## Usage

First, the `indexer` must be used to build the index from a `.tsv` raw data. Refer to `indexer/README` file for instructions and details.

The API, which uses the built index directly from its `indices` directory is a Ruby on Rails API application. Refer to `api/REAMDE` for further usage instructions.

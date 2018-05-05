# HN queries indexer

## Environment

Python 3.4.2

## Usage

This script takes a valid `.tsv` file path as argument.

The `.tsv` file must have the following foramt :

```
2015-08-01 00:03:43     http%3A%2F%2Ftechacute.com%2F10-essentials-every-desk-needs%2F
2015-08-01 00:03:43     %22http%3A%2F%2Fmiamiherald.typepad.com%2Fnakedpolitics%2F2015%2F07%2Fjeb-bushs-mixed-record-devolving-mount-tallahassee.html%22
```


`python main.py hn_logs.tsv`

### Description

This script takes a `.tsv` file path as argument, and builds the following indices:


### indices/events.json

This index is tree with each level corresponding to a date level (year, month, day, hours ...) son each level, the "queries" dict holds the query terms count for the current date level.

```
{
  "2015" : {
    "queries": {
      "1" : 2,
      "2" : 1
    },
    "01" : {
      "queries": {
        "1" : 2,
        "2" : 1
      }
      ...
    }
  }
}
```


### indices/queries.json

In the `events.json` index described above, each query term is stored as an integer key, in order not to duplicate the actual query term string on each date level.

The `queries.json` index holds the `(query id, query term)` dict.

```
{
  "1" : 'query term 1',
  "2" : 'query term 2',
  ...
}
```

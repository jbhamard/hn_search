# HN Queries search server

This application uses two indices (see `indices` directory) that must be built with the `hn search indexer` provided in this repository.


## API

This is a rails API server which exposes two endpoints, with
`<DATE_PREFIX>` is a string following the patterns : "YYYY", "YYYY-MM", ..., "YYYY-MM-DD hh:mm:ss"
`<SIZE>` is an integer

### Query term total count

`GET /1/queries/count/<DATE_PREFIX>`

with

`<DATE_PREFIX>` is a string following the patterns : "YYYY", "YYYY-MM", ..., "YYYY-MM-DD hh:mm:ss"

Response :

```
{
  "count": <integer>
}
```

### Query term popularity

`GET /1/queries/popular/<DATE_PREFIX>?size=<SIZE>`

with

`<DATE_PREFIX>` is a string following the patterns : "YYYY", "YYYY-MM", ..., "YYYY-MM-DD hh:mm:ss"
`<SIZE>` is an integer

Response :

```
{
  queries: [
    { query: "http%3A%2F%2Fwww.getsidekick.com%2Fblog%2Fbody-language-advice", count: 6675 },
    { query: "http%3A%2F%2Fwebboard.yenta4.com%2Ftopic%2F568045", count: 4652 },
    { query: "http%3A%2F%2Fwebboard.yenta4.com%2Ftopic%2F379035%3Fsort%3D1", count: 3100 }
  ]
}
```

## Running

Make sure you are using the ruby version set in `.ruby-version`

In you gemset, install bundler :

`gem install bundler`


then

`bundle install`


then start the server

`bundle exec rails server`








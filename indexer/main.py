import sys
import csv
import json
from datetime import datetime


def index_event(events_index, date_keys, query):
  current_date_key = str(date_keys[0])
  current_date_key_dict = events_index.get(current_date_key, dict([('queries', {})]))
  current_date_key_dict['queries'][query] = current_date_key_dict['queries'].get(query, 0) + 1
  events_index[current_date_key] = current_date_key_dict

  if len(date_keys) > 1:
    next_date_keys = date_keys[1:]
    index_event(events_index[current_date_key], next_date_keys, query)


def index_query(query, queries_ids, queries_index):
  queries_ids[query] = queries_ids.get(query, len(queries_ids) + 1)
  query_id = queries_ids[query]
  queries_index[query_id] = query
  return query_id


def index_search_event(event, events_index, queries_ids, queries_index):
  date = datetime.strptime(event[0], '%Y-%m-%d %H:%M:%S')
  query = event[1]
  date_keys = [date.year, date.month, date.day, date.hour, date.minute, date.second]

  query_id = index_query(query, queries_ids, queries_index)
  index_event(events_index, date_keys, query_id)


def build_index(filename):
  with open(filename) as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')

    #open indices, creating files if necessary
    with open('./indices/events.json', 'a+') as events_index_file, \
         open('./indices/queries.json', 'a+') as queries_index_file:

      events_index_file.seek(0)
      queries_index_file.seek(0)

      try:
        events_index = json.load(events_index_file)
      except ValueError:
        events_index = {}

      try:
        queries_index = json.load(queries_index_file)
      except ValueError:
        queries_index = {}

      queries_ids = dict((v,k) for k,v in queries_index.items())

      #process each search event
      for row in reader:
        index_search_event(row, events_index, queries_ids, queries_index)

      #save indices
      events_index_file.seek(0)
      events_index_file.truncate()
      queries_index_file.seek(0)
      queries_index_file.truncate()

      json.dump(events_index, events_index_file)
      json.dump(queries_index, queries_index_file)

    print('done')


if __name__ == '__main__':
  if len(sys.argv) == 2:
    filename = sys.argv[1]
  build_index(filename)
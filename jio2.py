import json
from algoliasearch.search_client import SearchClient

client = SearchClient.create('3YP0HP3WSH', 'aace3f18430a49e185d2c1111602e4b1')
index = client.init_index('prod_mart_groceries_products_popularity')

index.set_settings({"paginationLimitedTo": 12000})


hits = []

for hit in index.browse_objects({'query': ''}):
    hits.append(hit)

with open('jioJson', 'w') as f:
    json.dump(hits, f)
from crawlfrontier.settings.default_settings import MIDDLEWARES
from logging import INFO, DEBUG

MAX_REQUESTS = 0
MAX_NEXT_REQUESTS = 4096
CONSUMER_BATCH_SIZE = 1024
NEW_BATCH_DELAY = 5.0
JSONRPC_PORT=6014


#--------------------------------------------------------
# Url storage
#--------------------------------------------------------
BACKEND = 'crawlfrontier.contrib.backends.hbase.HBaseBackend'
HBASE_DROP_ALL_TABLES = False
HBASE_THRIFT_PORT = 9090
HBASE_THRIFT_HOST = [{thrift_servers_list}]
HBASE_QUEUE_PARTITIONS = 12
HBASE_METADATA_TABLE = 'metadata'

MIDDLEWARES.extend([
    'crawlfrontier.contrib.middlewares.domain.DomainMiddleware',
    'crawlfrontier.contrib.middlewares.fingerprint.DomainFingerprintMiddleware'
])

KAFKA_LOCATION = '{kafka_location}:9092'
FRONTIER_GROUP = 'scrapy-crawler'
INCOMING_TOPIC = 'frontier-done'
OUTGOING_TOPIC = 'frontier-todo'
SCORING_GROUP = 'scrapy-scoring'
SCORING_TOPIC = 'frontier-score'

#--------------------------------------------------------
# Logging
#--------------------------------------------------------
LOGGING_EVENTS_ENABLED = False
LOGGING_MANAGER_ENABLED = True
LOGGING_BACKEND_ENABLED = True
LOGGING_BACKEND_LOGLEVEL = DEBUG
LOGGING_DEBUGGING_ENABLED = False



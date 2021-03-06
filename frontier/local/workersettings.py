from crawlfrontier.settings.default_settings import MIDDLEWARES
from logging import INFO, DEBUG

MAX_REQUESTS = 0
MAX_NEXT_REQUESTS = 4096
CONSUMER_BATCH_SIZE = 1024
NEW_BATCH_DELAY = 5.0


#--------------------------------------------------------
# Url storage
#--------------------------------------------------------
BACKEND = 'crawlfrontier.contrib.backends.hbase.HBaseBackend'
HBASE_DROP_ALL_TABLES = False
HBASE_THRIFT_PORT = 9090
HBASE_THRIFT_HOST = ['localhost']
HBASE_QUEUE_PARTITIONS = 2
HBASE_METADATA_TABLE = 'metadata'

MIDDLEWARES.extend([
    'crawlfrontier.contrib.middlewares.domain.DomainMiddleware',
    'crawlfrontier.contrib.middlewares.fingerprint.DomainFingerprintMiddleware'
])

KAFKA_LOCATION = 'localhost:9092'
FRONTIER_GROUP = 'scrapy-crawler'
INCOMING_TOPIC = 'frontier-done'
OUTGOING_TOPIC = 'frontier-todo'
SCORING_GROUP = 'scrapy-scoring'
SCORING_TOPIC = 'frontier-score'

KAFKA_LOCATION_HH = 'localhost:9092'
FRONTERA_INCOMING_TOPIC = 'hh-incoming'
FRONTERA_RESULTS_TOPIC = 'hh-results'

ZOOKEEPER_LOCATION = 'localhost:2181'

#--------------------------------------------------------
# Logging
#--------------------------------------------------------
LOGGING_EVENTS_ENABLED = False
LOGGING_MANAGER_ENABLED = True
LOGGING_BACKEND_ENABLED = True
LOGGING_BACKEND_LOGLEVEL = DEBUG
LOGGING_DEBUGGING_ENABLED = False



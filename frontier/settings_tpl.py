from crawlfrontier.settings.default_settings import MIDDLEWARES

MAX_REQUESTS = 0
MAX_NEXT_REQUESTS = 256
OVERUSED_SLOT_FACTOR = 1.0

MIDDLEWARES.extend([
    'crawlfrontier.contrib.middlewares.domain.DomainMiddleware',
    'crawlfrontier.contrib.middlewares.fingerprint.DomainFingerprintMiddleware'
])

#--------------------------------------------------------
# Crawl frontier backend
#--------------------------------------------------------
BACKEND = 'crawlfrontier.contrib.backends.remote.KafkaOverusedBackend'
KAFKA_LOCATION = '{kafka_location}:9092'

#--------------------------------------------------------
# Logging
#--------------------------------------------------------
LOGGING_ENABLED = True
LOGGING_EVENTS_ENABLED = False
LOGGING_MANAGER_ENABLED = False
LOGGING_BACKEND_ENABLED = False
LOGGING_DEBUGGING_ENABLED = False



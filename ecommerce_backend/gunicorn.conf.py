import multiprocessing

# Number of worker processes
workers = multiprocessing.cpu_count() * 2 + 1

# Worker class
worker_class = 'sync'

# Bind address and port
bind = '127.0.0.1:9000'

# Timeout in seconds (increase if needed)
timeout = 120

# Log level
loglevel = 'debug'

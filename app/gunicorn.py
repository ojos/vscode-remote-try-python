# -*- coding: utf-8 -*-
import multiprocessing
import os

# Server Socket
bind = '0.0.0.0:8000'
backlog = 2048

# Worker Processes
workers = multiprocessing.cpu_count()
worker_class = 'egg:meinheld#gunicorn_worker'
threads = multiprocessing.cpu_count()
worker_connections = 1000
max_requests = 0
max_requests_jitter = 0
timeout = 60
graceful_timeout = 60
keepalive = 20

# Security
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190

# Debugging
debug = False
reload = False
spew = False
check_config = False

# Server Mechanics
preload_app = False
daemon = False
raw_env = []
pidfile = '/var/run/gunicorn.pid'
worker_tmp_dir = None
# user = ''
umask = 0
tmp_upload_dir = None

# Process Naming
proc_name = 'admin'


def post_fork(server, worker):
    server.log.info('Worker spawned (pid: %s)', worker.pid)


def pre_fork(server, worker):
    pass


def pre_exec(server):
    server.log.info('Forked child, re-executing.')


def when_ready(server):
    server.log.info('Server is ready. Spwawning workers')

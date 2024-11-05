import multiprocessing
import os

workers = multiprocessing.cpu_count() * 2 + 1
bind = "0.0.0.0:8000"
chdir = "/app"
module = "core.wsgi:application"

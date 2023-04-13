import os
DATASET_DIR = "/data/SEC-10k/"
LOGGING_DIR = "/data/SEC-10k/logs/"

if not os.path.exists(DATASET_DIR):
	os.mkdir(DATASET_DIR)

if not os.path.exists(LOGGING_DIR):
	os.mkdir(LOGGING_DIR)
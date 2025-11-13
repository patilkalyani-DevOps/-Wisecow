import os
import shutil
import datetime
import logging

logging.basicConfig(filename="backup.log", level=logging.INFO)

source_dir = "/home/user/data"
backup_dir = "/home/user/backups"
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
backup_path = os.path.join(backup_dir, f"backup_{timestamp}")

try:
    shutil.copytree(source_dir, backup_path)
    logging.info(f"Backup successful: {backup_path}")
except Exception as e:
    logging.error(f"Backup failed: {str(e)}")

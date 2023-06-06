#!/bin/bash

# Script Name:                  Ops301d8 Day 05
# Author:                       Your Name: Nick Van Noort
# Date of latest revision:      06/05/2023
# Purpose:                      Purpose



# create the backup directory if it doesn't exist
mkdir -p log_backups


# Print file size before compression
echo "Size of log files before compression:"
du -h "/var/log/syslog"
du -h "/var/log/wtmp"


# Compress the file
zip -r full_syslog-$(date +%Y%m%d%H%M%S).zip /var/log/syslog /var/log/wtmp

# Print file size after compression
echo "Size of log files after compression:"
du -h full_syslog-$(date +%Y%m%d%H%M%S).zip

# Compare the sizes
echo "Comparison of the original and compressed file sizes:"
echo "Original:"

du -h "/var/log/syslog"
du -h "/var/log/wtmp"

echo "Compressed"

du -h full_syslog-$(date +%Y%m%d%H%M%S).zip

#!/bin/bash

# Script Name:                  Ops301d8 Day 02
# Author:                       Your Name: Nick Van Noort
# Date of latest revision:      05/31/2023
# Purpose:                      Purpose

# Get the current date and time
current_date_time=$(date '+%Y-%m-%d_%H-%M-%S')

# Define the source and destination
src="/var/log/syslog"
dest="./syslog_${current_date_time}"

# Copy the file
cp $src $dest

#!/bin/bash

rsync -av --link-dest=/var/tmp/Backups/$(date --date=yesterday +"%F") /home/jonas/Segurtasuna/ /var/tmp/Backups/$(date '+%F')

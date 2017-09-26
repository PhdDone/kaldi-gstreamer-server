#!/bin/bash

if [ $# != 1 ]; then
  echo Usage: $0 date
  exit 1
fi

date=$1
mv kaldigstserver/reference-content.json reference-content.json.$1
python load_ref.py $date

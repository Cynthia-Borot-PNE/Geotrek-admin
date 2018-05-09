#!/usr/bin/env bash

cd /app/src

./update.sh

./manage.py loaddata minimal
./manage.py loaddata cirkwi
./manage.py loaddata basic

# copy media files for fixtures
for dir in `find geotrek/ -type d -name upload`; do pushd `dirname $$dir` > /dev/null; cp -R upload/* /app/src/var/media/upload/ ; popd > /dev/null; done
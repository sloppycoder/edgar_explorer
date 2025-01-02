#!/bin/sh

cd "$(dirname "$0")"

if [ -f ".env" ]; then
    source .env
fi

if [ "$DATABASE_URL" = "" ]; then
    echo DATABASE_URL not set, aborting.
    exit 1
fi

current_revision=$(aerich history | tail -n 1)
latest_revision=$(aerich heads | tail -n 1)

if [ "$current_revision" != "$latest_revision" ]; then
  echo "Schema is not up to date. Applying latest revision..."
  aerich upgrade
else
  echo "Schema is already up to date."
fi
/bin/sleep 100000

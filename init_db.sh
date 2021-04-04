#!/bin/bash
set -eux

pip install fhir.resources
pip install fhirbase
pip install fhirclient

THISDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

#Demo PostgreSQL Database initialisation
psql postgres -c "CREATE USER carta PASSWORD 'password'"

#The -O flag below sets the user: createdb -O DBUSER DBNAME
createdb -O carta carta

psql postgres -c "ALTER ROLE CARTA SUPERUSER"

wget -O fhirbase-linux-amd64 https://github.com/fhirbase/fhirbase/releases/download/v0.0.6/fhirbase-linux-amd64?_ga=2.205532759.556026196.1617411701-717493598.1617411701
chmod +x fhirbase-linux-amd64
./fhirbase-linux-amd64 --host localhost -p 5432 -d carta -U carta -W password --fhir=3.3.0 init
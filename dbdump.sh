# bash script for dumping project database. receives dump name as arg
python3 manage.py dumpdata -a --format json --natural-foreign --natural-primary -o $1.json

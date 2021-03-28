# Google Fit to Nextcloud Health importer

Python script to generate SQL for importing weight data from 
Google Fit to Nextcloud Health.

## Usage

Create a takeout from Google Fit.

Identify and download the Google Fit file, naming it `fit.json` for example.

Create a Python virtualenv and install the requirements in `requirements.txt`.

Access your Nextcloud database and find your person ID from the table
`oc_health_persons`.

Run script:

```bash
python create_import_weight_sql.py <fit_json_file> <person_id> > output.sql
```

The `output.sql` will now hopefully contain a list of insert statements.
Copy this to your Nextcloud database server and run the SQL.

## License

MIT

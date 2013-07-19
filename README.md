Denver Street Construction API
==============

API for Denver Streets/Sidewalks closures

Using
==============

GET: `/`

GET: `/closures`

Returns a list of current closures.

GET: `/closures?current_location=??&radius=1`

Returns all closures within a radius in miles (default radius will be equal to 1).

Development
==============
Pivotal Tracker:
https://www.pivotaltracker.com/projects/768887

You need:
* Python 2.7.3
* Postgresql 9.1
* Postgis for Postgresql 9.1 (http://linfiniti.com/2012/05/installing-postgis-2-0-on-ubuntu/). 
  * For OSX users, you can install via brew
  * For Linux users, you can install via your package management of choice
 

=======

To start the server locally, run `python app.py` and visit 
http://0.0.0.0:5000 in your browser

=======
Database setup
(From http://www.geoalchemy.org/tutorial.html)
<!-- sudo su postgres -->

```sh
# Create a new superuser if gisuser does not exist already
createuser -P -s denverstreetsuser
```

Copy config.yaml.example to config.yaml. Open it up.
Edit the database settings with the correct username and password you set.

Fill in postgis_extensions_dir with the postgis install directory that contains your postgis.sql and spatial_ref_sys.sql files.

Open up your python REPL in the app root directory and type the following:
```python
import database
database.create_db()
```

Now in your shell, type the following:
```sh
createlang plpgsql denver_streets
createlang plpgsql denver_streets_test

psql -d denver_streets -f {your postgis extensions directory}/postgis.sql
psql -d denver_streets_test -f {your postgis extensions directory}/postgis.sql
```

(postgis.sql should have spatial_ref_sys.sql and lwpostgis.sql mentioned int he tutorial above.)


Go back to your python REPL and init the database:
```
import database
database.init_db()
````

This will create the tables. Do the same thing with FLASK_ENV=test. 

To drop tables (not the database!), type ```database.drop_db()``` in said REPL session.
To drop the database, type ```database.destroy_db()```

If you want to make sure that PostGIS is correctly installed, run the following:
sudo -u postgres psql -d denver_streets[_test] -c "SELECT postgis_full_version()"
You should get something like:

                                     postgis_full_version
------------------------------------------------------------------------------------------------------
POSTGIS="1.5.2" GEOS="3.2.2-CAPI-1.6.2" PROJ="Rel. 4.7.1, 23 September 2009" LIBXML="2.7.7" USE_STATS
(1 row)


Tests are currently a giant mess. Sorry! To run tests, run `./run_tests`. 

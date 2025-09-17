Database setup and seeding

There are two ways to create the database for this project. Prefer the Flask-Migrate workflow when developing migrations.

1) Recommended: Flask-Migrate (requires pipenv and project dependencies)

    pipenv install
    pipenv shell
    cd server
    export FLASK_APP=app.py
    export FLASK_RUN_PORT=5555

    # Initialize migrations (only once per repo)
    flask db init
    # Create migration for current models
    flask db migrate -m "initial migration"
    flask db upgrade head

    # Seed the DB
    python seed.py

2) Fallback: Create DB directly (no alembic migrations)

If you can't run `flask db migrate`, use the helper script that creates tables from the models and seeds them. This is safe for local development but not for schema management in production.

    pipenv install
    pipenv shell
    python server/create_db.py

This will create (or replace) `server/app.db` and insert example data.

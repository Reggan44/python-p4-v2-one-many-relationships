#!/usr/bin/env python3
"""Create the SQLite database and seed it without using Flask-Migrate.

Use this if you can't or don't want to run `flask db migrate`/`flask db upgrade`.

Run from the project root inside your pipenv shell:

    pipenv shell
    python server/create_db.py

This will drop existing tables, create tables from `models.py`, and insert seed data.
"""
import datetime
from app import app
from models import db, Employee, Review, Onboarding


def create_and_seed():
    with app.app_context():
        # Drop and recreate tables (safe for development)
        db.drop_all()
        db.create_all()

        # Seed data
        Employee.query.delete()
        Review.query.delete()
        Onboarding.query.delete()

        uri = Employee(name="Uri Lee", hire_date=datetime.datetime(2022, 5, 17))
        tristan = Employee(name="Tristan Tal", hire_date=datetime.datetime(2020, 1, 30))
        db.session.add_all([uri, tristan])
        db.session.commit()

        uri_2023 = Review(year=2023, summary="Great web developer!", employee=uri)
        tristan_2021 = Review(year=2021, summary="Good coding skills, often late to work", employee=tristan)
        tristan_2022 = Review(year=2022, summary="Strong coding skills, takes long lunches", employee=tristan)
        tristan_2023 = Review(year=2023, summary="Awesome coding skills, dedicated worker", employee=tristan)
        db.session.add_all([uri_2023, tristan_2021, tristan_2022, tristan_2023])
        db.session.commit()

        uri_onboarding = Onboarding(orientation=datetime.datetime(2023, 3, 27), employee=uri)
        tristan_onboarding = Onboarding(
            orientation=datetime.datetime(2020, 1, 20, 14, 30), forms_complete=True, employee=tristan
        )
        db.session.add_all([uri_onboarding, tristan_onboarding])
        db.session.commit()

        print("Database created and seeded: server/app.db")


if __name__ == "__main__":
    create_and_seed()

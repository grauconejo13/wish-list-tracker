# Wish List Tracker

**Keep the surprise. Skip the duplicates.**

A public learning project built with Django + HTMX. A recipient can maintain a wish list while other shoppers secretly claim gifts to avoid duplicates.

## Current MVP foundation

- Create wish lists for birthdays, Christmas, or other occasions
- Add wishlist items with links, price, and notes
- Claim or release an item with HTMX partial updates
- Keep the claimant name out of the rendered claimed-item state
- Django admin for inspecting demo data
- SQLite for local development
- Responsive server-rendered interface

The current version is intentionally small. Authentication and true recipient-vs-shopper permissions are the next security boundary before this should be treated as a multi-user application.

## Stack

- Python
- Django 5.2+
- HTMX
- SQLite for local development

PostgreSQL is the planned production database when deployed.

## Run locally

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000`.

Run tests with:

```bash
python manage.py test
```

## Surprise rule

A claim records who claimed the item in the database, but the claimed-item partial intentionally renders only **Claimed by another shopper**. Full recipient-aware permissions will be added with authentication in a later iteration.

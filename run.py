from app import create_app
from app.models import init_db, DATA

app = create_app()

if __name__ == '__main__':
    init_db(initial_records=[
        {"title": "1984", "author": "George Orwell", "year": 1949},
        {"title": "Sapiens", "author": "Yuval Noah Harari", "year": 2011}
    ])
    app.run(debug=True)

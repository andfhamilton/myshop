import os
import click

from src import create_app

# Create the Flask application
app = create_app()

@click.group()
def cli():
    pass

@click.command()
def create_db():
    """Creates all database tables."""
    from app import db
    with app.app_context():
        db.create_all()

@click.command()
def drop_db():
    """Drops all database tables."""
    from app import db
    with app.app_context():
        db.drop_all()
"""
@click.command()


def runserver(port=5000, host='0.0.0.0'):
    //Runs the development server (using Gunicorn).
    from gunicorn.app.wsgiapp import WSGIApplication

    # Configure Gunicorn
    options = {
        'bind': f"{host}:{port}",
        'workers': 1,
    }

    # Run Gunicorn server
    app = WSGIApplication(app)
    app.run(**options)

@cli.command()"""
def shell():
    """Starts an interactive shell with the application context."""
    with app.app_context():
        import IPython
        IPython.embed()

if __name__ == '__main__':
    cli()

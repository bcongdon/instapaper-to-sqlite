import click
import pathlib
import json
import sqlite_utils
from instapaper_to_sqlite import utils
from pyinstapaper.instapaper import Instapaper


@click.group()
@click.version_option()
def cli():
    "Save data from Instapaper to a SQLite database"


@cli.command()
@click.option(
    "-a",
    "--auth",
    type=click.Path(file_okay=True, dir_okay=False, allow_dash=False),
    default="auth.json",
    help="Path to save tokens to, defaults to ./auth.json.",
)
def auth(auth):
    "Save authentication credentials to a JSON file"
    auth_data = {}
    if pathlib.Path(auth).exists():
        auth_data = json.load(open(auth))
    click.echo(
        "In Instapaper, get a Full API key following the process at https://www.instapaper.com/api."
    )
    consumer_id = click.prompt("OAuth Consumer ID")
    consumer_secret = click.prompt("OAuth Consumer Secret")
    login = click.prompt("Instapaper login (email)")
    password = click.prompt("Instapaper password", hide_input=True)
    auth_data.update(
        {
            "instapaper_consumer_id": consumer_id,
            "instapaper_consumer_secret": consumer_secret,
            "instapaper_email": login,
            "instapaper_password": password,
        }
    )

    open(auth, "w").write(json.dumps(auth_data, indent=4) + "\n")
    click.echo()
    click.echo(
        "Your authentication credentials have been saved to {}. You can now import articles by running:".format(
            auth
        )
    )
    click.echo()
    click.echo("    $ instapaper-to-sqlite bookmarks instapaper.db")


BOOKMARK_KEYS = [
    "bookmark_id",
    "title",
    "description",
    "hash",
    "url",
    "progress_timestamp",
    "time",
    "progress",
    "starred",
    "type",
    "private_source",
]


@cli.command()
@click.argument(
    "db_path",
    type=click.Path(file_okay=True, dir_okay=False, allow_dash=False),
    required=True,
)
@click.option(
    "-a",
    "--auth",
    type=click.Path(file_okay=True, dir_okay=False, allow_dash=False),
    default="auth.json",
    help="Path to save tokens to, defaults to auth.json",
)
@click.option(
    "-f",
    "--folder",
    default="archive",
    help="The folder of bookmarks to save",
)
def bookmarks(db_path, auth, folder):
    """Save a folder of bookmarks"""
    db = sqlite_utils.Database(db_path)
    try:
        data = json.load(open(auth))
        consumer_id = data["instapaper_consumer_id"]
        consumer_secret = data["instapaper_consumer_secret"]
        login = data["instapaper_email"]
        password = data["instapaper_password"]
    except (KeyError, FileNotFoundError):
        utils.error(
            "Cannot find authentication data, please run `instapaper-to-sqlite auth`!"
        )
    print("Fetching bookmarks...")
    instapaper = Instapaper(consumer_id, consumer_secret)
    instapaper.login(login, password)

    bookmarks = [
        {key: getattr(entry, key) for key in BOOKMARK_KEYS}
        for entry in instapaper.get_bookmarks(folder, limit=500)
    ]
    print("Downloaded {} bookmarks from folder '{}'.".format(len(bookmarks), folder))
    for b in bookmarks:
        b.update({"folder": folder})
    db["bookmarks"].upsert_all(bookmarks, pk="bookmark_id", alter=True)


if __name__ == "__main__":
    cli()

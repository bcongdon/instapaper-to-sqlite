# instapaper-to-sqlite

[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/bcongdon/instapaper-to-sqlite/blob/master/LICENSE)

Save bookmarks from Instapaper to a SQLite database.

## How to install

    $ git clone https://github.com/bcongdon/instapaper-to-sqlite
    $ cde instapaper-to-sqlite
    $ pip install .

## Authentication

To use `instapaper-to-sqlite`, you'll need a API key for the [Instapaper Full API](https://www.instapaper.com/api). You can request an API key with [this form](https://www.instapaper.com/main/request_oauth_consumer_token). Once you have a key, take note of the consumer ID and consumer secret. Then, run the `auth` command:

    $ instapaper-to-sqlite auth

This will create a file called `auth.json` in your current directory containing the required value. To save the file at
a different path or filename, use the `--auth=myauth.json` option.

## Saving Bookmarks

The `bookmarks` command retrieves all recent bookmarks in a given folder.

    $ instapaper-to-sqlite bookmarks instapaper.db

By default, the `archive` folder is saved. You can specify a different folder with `--folder`:

    $ instapaper-to-sqlite bookmarks instapaper.db --folder=unread
    $ instapaper-to-sqlite bookmarks instapaper.db --folder=starred

## Attribution

This package is heavily inspired by [goodreads-to-sqlite](https://github.com/rixx/goodreads-to-sqlite/) by [Tobias Kunze
](https://github.com/rixx) and [github-to-sqlite](https://github.com/dogsheep/github-to-sqlite/) by [Simon
Willison](https://simonwillison.net/2019/Oct/7/dogsheep/).

This package was designed to fit nicely in the [dogsheep](https://dogsheep.github.io/) / [datasette](https://github.com/simonw/datasette) ecosystems.

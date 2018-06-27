# pgpipelines
Postgres pipeline for Scrapy.

## Installation

    python setup.py install

## Usage

Add below col to settings.py at your scrapy project.

    # settings.py
    from dataset import types

    ITEM_PIPELINES = {
        'pgpipelines.PgPipeline': 300,
    }

    PG_PIPELINE = {
        'connection': 'postgresql://localhost:5432/postgres',
        'table_name': 'scraped_data',
        'col': {
            'table_col1': ('item_key1', types.UnicodeText),
            'table_col2': ('item_key2', types.UnicodeText)
        },
        'bulksize': 200
    }

 + variables description
     + connection: specify postgresql connection url
         + psycopg2 notation
     + table_name: specify table_name
     + col: specify column name for insert table and item key of scrapy, column type for insert table
         + format is "column_name": ("item_key", "column_type")
         + "item_key" is item key of scraping result (defined at items.py, if scrapy template project), access is item.get("item_key")
         + "column_type" is usable dataset.types (omit datetime)
     + bulksize: optional, bulk import items size
         + default is 1000
 + table and columns are created automatically.
 + datetime column is created automatically, insert date is timestamp formats

## TODO
 + primary key
 + indexing
 + upsert and ignore

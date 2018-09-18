# pgpipelines
Postgres pipeline for Scrapy.

## Installation

    python setup.py install

## Usage

Add below  to settings.py at your scrapy project.

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
            'table_col2': ('item_key2', types.Integer)
            'table_col3': ('item_key3', types.Boolean)
        },
        'primary': 'table_col1',
        'indexing': ['table_col2'],
        'auto_datetime': False,
        'bulksize': 200
    }

 + variables description
     + connection: specify postgresql connection url
         + psycopg2 notation
     + table_name: specify table_name
         + if table of this name is not exist, automatically create.
     + col: specify column name for insert table and item key of scrapy, column type for insert table
         + format is "column_name": ("item_key", "column_type")
         + "item_key" is item key of scraping result (defined at items.py, if scrapy template project), access is item.get("item_key")
         + "column_type" is usable dataset.types (omit datetime)
         + if column of this name is not exist, automatically create.
     + primary: optional, specify primary key (column name of specified at 'col')
         + indexing automatically
         + default and invalid primary are None (automatically create primary key - 'id' by dataset)
     + indexing: optional, specify indexing key (column name of specified at 'col')
         + default and invalid primary are None
     + auto_datetime: optional, specify boolean for automatically create 'datetime' column
        + default is False, automatically create
     + bulksize: optional, bulk import items size
         + default is 1000

## TODO
 + upsert and ignore

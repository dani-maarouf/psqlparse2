[![PyPI deploy](https://github.com/dani-maarouf/psqlparse2/actions/workflows/workflow.yml/badge.svg)](https://github.com/dani-maarouf/psqlparse2/actions/workflows/workflow.yml)

# psqlparse2

Python wrapper for [libpg_query](https://github.com/pganalyze/libpg_query).

Inspired by [psqlparse](https://github.com/alculquicondor/psqlparse), which was authored by [alculquicondor](https://github.com/alculquicondor/)

## Overview

[Python protobuf types](./src/psqlparse2/pb/) are generated from `libpg_query/protobuf/pg_query.proto`.
See `gen_proto` in [Makefile](./Makefile) for details.

Additionally, a [Cython wrapper](./src/pg_query/__init__.py) with Python bindings for certain functions
from `libpg_query` is provided. For example, there are wrappers for `pg_query_parse_protobuf` and
`pg_query_deparse_protobuf`, which allow converting between SQL strings and parse trees encoded as protobufs.

[This snippet](https://github.com/dani-maarouf/alembic_utils/blob/1434dca40abbcfcbc7eeaba41e6b8a9884e21c1e/src/alembic_utils/statement.py#L15-L69)
demonstrates how `psqlparse2` can be used to convert a SQL function into a parse tree,
and then manipulate the parse tree before converting it back into a SQL string.

## Installation

```bash
pip install psqlparse2
```

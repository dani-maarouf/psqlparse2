import json

import pytest
from google.protobuf.json_format import MessageToJson

import pg_query
from psqlparse2 import pb_to_query, query_to_pb


def test_query_normalize():
    query = "SELECT 1"
    normalized_query = pg_query.query_normalize(query)
    assert normalized_query == "SELECT $1"


def test_pg_query_json():
    query = "SELECT 1"
    parse_tree_json = pg_query.query_parse_json(query)
    loaded_parse_tree = json.loads(parse_tree_json)
    assert "stmts" in loaded_parse_tree


def test_pg_query_parse_error():
    query = "SELECTa 1"
    with pytest.raises(pg_query.PgQueryExc):
        assert pg_query.query_parse_json(query) is None


def test_pg_protobuf():
    query = "SELECT 1"
    parse_tree_pb = query_to_pb(query)
    parse_tree_json = MessageToJson(parse_tree_pb)
    loaded_parse_tree = json.loads(parse_tree_json)

    parse_tree_json2 = pg_query.query_parse_json(query)
    loaded_parse_tree2 = json.loads(parse_tree_json2)
    assert loaded_parse_tree == loaded_parse_tree2

    deparsed_query = pb_to_query(parse_tree_pb)
    assert deparsed_query == query

from psqlparse2.pb.pg_query_pb2 import ParseResult

import pg_query


def pb_to_query(pb: ParseResult) -> str:
    pb_bytes = pb.SerializeToString()
    return pg_query.query_deparse_protobuf(pb_bytes)


def query_to_pb(query: str) -> ParseResult:
    pb_bytes = pg_query.query_parse_protobuf(query)
    pb = ParseResult()
    pb.ParseFromString(pb_bytes)
    return pb

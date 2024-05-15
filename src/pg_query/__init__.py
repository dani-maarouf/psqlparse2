from typing import Optional
import logging

import cython
import cython.cimports.pg_query as pg_query_h


logger = logging.getLogger(__name__)


@cython.cclass
class PgQueryExc(Exception):
    def __init__(
        self, message: str, function: str, filename: str, lineno: int, cursorpos: int, context: Optional[str] = None
    ):
        self.message: str = message
        self.function: str = function
        self.filename: str = filename
        self.lineno: int = lineno
        self.cursorpos: int = cursorpos
        self.context: str = context or ""

    def __str__(self):
        msg = f"[{self.filename}:{self.function}:{self.lineno}] {self.message}"
        if self.context:
            msg += f"\n{self.context}"
        return msg

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"message={self.message!r}, "
            f"function={self.function!r}, "
            f"filename={self.filename!r}, "
            f"lineno={self.lineno!r}, "
            f"cursorpos={self.cursorpos!r}, "
            f"context={self.context!r}"
            f")"
        )


@cython.cfunc
@cython.returns(PgQueryExc)
@cython.locals(context=cython.p_char, err=pg_query_h.PgQueryError)
def exc_from_pg_query_error(err: pg_query_h.PgQueryError):
    args = {
        "message": "",
        "function": "",
        "filename": "",
        "lineno": err.lineno,
        "cursorpos": err.cursorpos,
        "context": "",
    }
    if err.message is not cython.NULL:
        args["message"] = err.message.decode("utf-8")
    if err.funcname is not cython.NULL:
        args["function"] = err.funcname.decode("utf-8")
    if err.filename is not cython.NULL:
        args["filename"] = err.filename.decode("utf-8")
    if err.context is not cython.NULL:
        args["context"] = err.context.decode("utf-8")
    return PgQueryExc(**args)


@cython.ccall
def query_normalize(query: str) -> str:
    query_bytes = query.encode("utf-8")
    s: cython.p_char = query_bytes
    result: pg_query_h.PgQueryNormalizeResult = pg_query_h.pg_query_normalize(s)
    if result.error is not cython.NULL:
        exc = exc_from_pg_query_error(result.error[0])
        pg_query_h.pg_query_free_normalize_result(result)
        raise exc
    py_str: str = result.normalized_query.decode("utf-8")
    pg_query_h.pg_query_free_normalize_result(result)
    return py_str


@cython.ccall
@cython.returns(str)
def query_parse_json(query: str) -> str:
    query_bytes = query.encode("utf-8")
    s: cython.p_char = query_bytes
    result: pg_query_h.PgQueryParseResult = pg_query_h.pg_query_parse(s)
    if result.error is not cython.NULL:
        exc = exc_from_pg_query_error(result.error[0])
        pg_query_h.pg_query_free_parse_result(result)
        raise exc
    py_str: str = result.parse_tree.decode("utf-8")
    pg_query_h.pg_query_free_parse_result(result)
    return py_str


@cython.ccall
@cython.returns(bytes)
def query_parse_protobuf(query: str) -> bytes:
    query_bytes = query.encode("utf-8")
    s: cython.p_char = query_bytes
    result: pg_query_h.PgQueryProtobufParseResult = pg_query_h.pg_query_parse_protobuf(s)
    if result.error is not cython.NULL:
        exc = exc_from_pg_query_error(result.error[0])
        pg_query_h.pg_query_free_protobuf_parse_result(result)
        raise exc
    result_pb: pg_query_h.PgQueryProtobuf = result.parse_tree
    result_pb_data: cython.p_uchar = cython.cast(cython.p_uchar, result_pb.data)

    byte_result = bytearray(result_pb.len)
    for i in range(result_pb.len):
        byte_result[i] = result_pb_data[i]
    pg_query_h.pg_query_free_protobuf_parse_result(result)
    return bytes(byte_result)


@cython.ccall
@cython.returns(str)
def query_deparse_protobuf(pb_bytes: bytes) -> str:
    pb: pg_query_h.PgQueryProtobuf = cython.declare(pg_query_h.PgQueryProtobuf)
    pb.len = len(pb_bytes)
    pb.data = cython.cast(cython.p_char, pb_bytes)
    result: pg_query_h.PgQueryDeparseResult = pg_query_h.pg_query_deparse_protobuf(pb)
    if result.error is not cython.NULL:
        exc = exc_from_pg_query_error(result.error[0])
        pg_query_h.pg_query_free_deparse_result(result)
        raise exc

    py_str: str = result.query.decode("utf-8")
    pg_query_h.pg_query_free_deparse_result(result)
    return py_str

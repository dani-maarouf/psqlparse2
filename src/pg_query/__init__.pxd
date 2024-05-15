cdef extern from "pg_query.h":
    ctypedef struct PgQueryError:
        char* message
        char* funcname
        char* filename
        int lineno
        int cursorpos
        char* context

    ctypedef struct PgQueryProtobuf:
        size_t len
        char* data

    ctypedef struct PgQueryScanResult:
        PgQueryProtobuf pbuf
        char* stderr_buffer
        PgQueryError* error

    ctypedef struct PgQueryParseResult:
        char* parse_tree
        char* stderr_buffer
        PgQueryError* error

    ctypedef struct PgQueryProtobufParseResult:
        PgQueryProtobuf parse_tree
        char* stderr_buffer
        PgQueryError* error

    ctypedef struct PgQuerySplitStmt:
        int stmt_location
        int stmt_len

    ctypedef struct PgQuerySplitResult:
        PgQuerySplitStmt **stmts
        int n_stmts
        char* stderr_buffer
        PgQueryError* error

    ctypedef struct PgQueryDeparseResult:
        char* query
        PgQueryError* error

    ctypedef struct PgQueryPlpgsqlParseResult:
        char* plpgsql_funcs;
        PgQueryError* error;

    ctypedef struct PgQueryFingerprintResult:
        unsigned long long int fingerprint
        char* fingerprint_str
        char* stderr_buffer
        PgQueryError* error

    ctypedef struct PgQueryNormalizeResult:
        char* normalized_query;
        PgQueryError* error;

    cdef enum PgQueryParseMode:
        PG_QUERY_PARSE_DEFAULT = 0
        PG_QUERY_PARSE_TYPE_NAME = 1
        PG_QUERY_PARSE_PLPGSQL_EXPR = 2
        PG_QUERY_PARSE_PLPGSQL_ASSIGN1 = 3
        PG_QUERY_PARSE_PLPGSQL_ASSIGN2 = 4
        PG_QUERY_PARSE_PLPGSQL_ASSIGN3 = 5

    PgQueryNormalizeResult pg_query_normalize(const char* input);
    PgQueryScanResult pg_query_scan(const char* input);
    PgQueryParseResult pg_query_parse(const char* input);
    PgQueryParseResult pg_query_parse_opts(const char* input, int parser_options);
    PgQueryProtobufParseResult pg_query_parse_protobuf(const char* input);
    PgQueryProtobufParseResult pg_query_parse_protobuf_opts(const char* input, int parser_options);
    PgQueryPlpgsqlParseResult pg_query_parse_plpgsql(const char* input);

    PgQueryFingerprintResult pg_query_fingerprint(const char* input);
    PgQueryFingerprintResult pg_query_fingerprint_opts(const char* input, int parser_options);

    PgQuerySplitResult pg_query_split_with_scanner(const char *input);
    PgQuerySplitResult pg_query_split_with_parser(const char *input);

    PgQueryDeparseResult pg_query_deparse_protobuf(PgQueryProtobuf parse_tree);

    void pg_query_free_normalize_result(PgQueryNormalizeResult result);
    void pg_query_free_scan_result(PgQueryScanResult result);
    void pg_query_free_parse_result(PgQueryParseResult result);
    void pg_query_free_split_result(PgQuerySplitResult result);
    void pg_query_free_deparse_result(PgQueryDeparseResult result);
    void pg_query_free_protobuf_parse_result(PgQueryProtobufParseResult result);
    void pg_query_free_plpgsql_parse_result(PgQueryPlpgsqlParseResult result);
    void pg_query_free_fingerprint_result(PgQueryFingerprintResult result);
    void pg_query_exit();

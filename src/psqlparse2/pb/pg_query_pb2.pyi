from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import (
    ClassVar as _ClassVar,
    Iterable as _Iterable,
    Mapping as _Mapping,
    Optional as _Optional,
    Union as _Union,
)

DESCRIPTOR: _descriptor.FileDescriptor

class OverridingKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OVERRIDING_KIND_UNDEFINED: _ClassVar[OverridingKind]
    OVERRIDING_NOT_SET: _ClassVar[OverridingKind]
    OVERRIDING_USER_VALUE: _ClassVar[OverridingKind]
    OVERRIDING_SYSTEM_VALUE: _ClassVar[OverridingKind]

class QuerySource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    QUERY_SOURCE_UNDEFINED: _ClassVar[QuerySource]
    QSRC_ORIGINAL: _ClassVar[QuerySource]
    QSRC_PARSER: _ClassVar[QuerySource]
    QSRC_INSTEAD_RULE: _ClassVar[QuerySource]
    QSRC_QUAL_INSTEAD_RULE: _ClassVar[QuerySource]
    QSRC_NON_INSTEAD_RULE: _ClassVar[QuerySource]

class SortByDir(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SORT_BY_DIR_UNDEFINED: _ClassVar[SortByDir]
    SORTBY_DEFAULT: _ClassVar[SortByDir]
    SORTBY_ASC: _ClassVar[SortByDir]
    SORTBY_DESC: _ClassVar[SortByDir]
    SORTBY_USING: _ClassVar[SortByDir]

class SortByNulls(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SORT_BY_NULLS_UNDEFINED: _ClassVar[SortByNulls]
    SORTBY_NULLS_DEFAULT: _ClassVar[SortByNulls]
    SORTBY_NULLS_FIRST: _ClassVar[SortByNulls]
    SORTBY_NULLS_LAST: _ClassVar[SortByNulls]

class SetQuantifier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SET_QUANTIFIER_UNDEFINED: _ClassVar[SetQuantifier]
    SET_QUANTIFIER_DEFAULT: _ClassVar[SetQuantifier]
    SET_QUANTIFIER_ALL: _ClassVar[SetQuantifier]
    SET_QUANTIFIER_DISTINCT: _ClassVar[SetQuantifier]

class A_Expr_Kind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    A_EXPR_KIND_UNDEFINED: _ClassVar[A_Expr_Kind]
    AEXPR_OP: _ClassVar[A_Expr_Kind]
    AEXPR_OP_ANY: _ClassVar[A_Expr_Kind]
    AEXPR_OP_ALL: _ClassVar[A_Expr_Kind]
    AEXPR_DISTINCT: _ClassVar[A_Expr_Kind]
    AEXPR_NOT_DISTINCT: _ClassVar[A_Expr_Kind]
    AEXPR_NULLIF: _ClassVar[A_Expr_Kind]
    AEXPR_IN: _ClassVar[A_Expr_Kind]
    AEXPR_LIKE: _ClassVar[A_Expr_Kind]
    AEXPR_ILIKE: _ClassVar[A_Expr_Kind]
    AEXPR_SIMILAR: _ClassVar[A_Expr_Kind]
    AEXPR_BETWEEN: _ClassVar[A_Expr_Kind]
    AEXPR_NOT_BETWEEN: _ClassVar[A_Expr_Kind]
    AEXPR_BETWEEN_SYM: _ClassVar[A_Expr_Kind]
    AEXPR_NOT_BETWEEN_SYM: _ClassVar[A_Expr_Kind]

class RoleSpecType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROLE_SPEC_TYPE_UNDEFINED: _ClassVar[RoleSpecType]
    ROLESPEC_CSTRING: _ClassVar[RoleSpecType]
    ROLESPEC_CURRENT_ROLE: _ClassVar[RoleSpecType]
    ROLESPEC_CURRENT_USER: _ClassVar[RoleSpecType]
    ROLESPEC_SESSION_USER: _ClassVar[RoleSpecType]
    ROLESPEC_PUBLIC: _ClassVar[RoleSpecType]

class TableLikeOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TABLE_LIKE_OPTION_UNDEFINED: _ClassVar[TableLikeOption]
    CREATE_TABLE_LIKE_COMMENTS: _ClassVar[TableLikeOption]
    CREATE_TABLE_LIKE_COMPRESSION: _ClassVar[TableLikeOption]
    CREATE_TABLE_LIKE_CONSTRAINTS: _ClassVar[TableLikeOption]
    CREATE_TABLE_LIKE_DEFAULTS: _ClassVar[TableLikeOption]
    CREATE_TABLE_LIKE_GENERATED: _ClassVar[TableLikeOption]
    CREATE_TABLE_LIKE_IDENTITY: _ClassVar[TableLikeOption]
    CREATE_TABLE_LIKE_INDEXES: _ClassVar[TableLikeOption]
    CREATE_TABLE_LIKE_STATISTICS: _ClassVar[TableLikeOption]
    CREATE_TABLE_LIKE_STORAGE: _ClassVar[TableLikeOption]
    CREATE_TABLE_LIKE_ALL: _ClassVar[TableLikeOption]

class DefElemAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEF_ELEM_ACTION_UNDEFINED: _ClassVar[DefElemAction]
    DEFELEM_UNSPEC: _ClassVar[DefElemAction]
    DEFELEM_SET: _ClassVar[DefElemAction]
    DEFELEM_ADD: _ClassVar[DefElemAction]
    DEFELEM_DROP: _ClassVar[DefElemAction]

class PartitionStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PARTITION_STRATEGY_UNDEFINED: _ClassVar[PartitionStrategy]
    PARTITION_STRATEGY_LIST: _ClassVar[PartitionStrategy]
    PARTITION_STRATEGY_RANGE: _ClassVar[PartitionStrategy]
    PARTITION_STRATEGY_HASH: _ClassVar[PartitionStrategy]

class PartitionRangeDatumKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PARTITION_RANGE_DATUM_KIND_UNDEFINED: _ClassVar[PartitionRangeDatumKind]
    PARTITION_RANGE_DATUM_MINVALUE: _ClassVar[PartitionRangeDatumKind]
    PARTITION_RANGE_DATUM_VALUE: _ClassVar[PartitionRangeDatumKind]
    PARTITION_RANGE_DATUM_MAXVALUE: _ClassVar[PartitionRangeDatumKind]

class RTEKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RTEKIND_UNDEFINED: _ClassVar[RTEKind]
    RTE_RELATION: _ClassVar[RTEKind]
    RTE_SUBQUERY: _ClassVar[RTEKind]
    RTE_JOIN: _ClassVar[RTEKind]
    RTE_FUNCTION: _ClassVar[RTEKind]
    RTE_TABLEFUNC: _ClassVar[RTEKind]
    RTE_VALUES: _ClassVar[RTEKind]
    RTE_CTE: _ClassVar[RTEKind]
    RTE_NAMEDTUPLESTORE: _ClassVar[RTEKind]
    RTE_RESULT: _ClassVar[RTEKind]

class WCOKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WCOKIND_UNDEFINED: _ClassVar[WCOKind]
    WCO_VIEW_CHECK: _ClassVar[WCOKind]
    WCO_RLS_INSERT_CHECK: _ClassVar[WCOKind]
    WCO_RLS_UPDATE_CHECK: _ClassVar[WCOKind]
    WCO_RLS_CONFLICT_CHECK: _ClassVar[WCOKind]
    WCO_RLS_MERGE_UPDATE_CHECK: _ClassVar[WCOKind]
    WCO_RLS_MERGE_DELETE_CHECK: _ClassVar[WCOKind]

class GroupingSetKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROUPING_SET_KIND_UNDEFINED: _ClassVar[GroupingSetKind]
    GROUPING_SET_EMPTY: _ClassVar[GroupingSetKind]
    GROUPING_SET_SIMPLE: _ClassVar[GroupingSetKind]
    GROUPING_SET_ROLLUP: _ClassVar[GroupingSetKind]
    GROUPING_SET_CUBE: _ClassVar[GroupingSetKind]
    GROUPING_SET_SETS: _ClassVar[GroupingSetKind]

class CTEMaterialize(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CTEMATERIALIZE_UNDEFINED: _ClassVar[CTEMaterialize]
    CTEMaterializeDefault: _ClassVar[CTEMaterialize]
    CTEMaterializeAlways: _ClassVar[CTEMaterialize]
    CTEMaterializeNever: _ClassVar[CTEMaterialize]

class SetOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SET_OPERATION_UNDEFINED: _ClassVar[SetOperation]
    SETOP_NONE: _ClassVar[SetOperation]
    SETOP_UNION: _ClassVar[SetOperation]
    SETOP_INTERSECT: _ClassVar[SetOperation]
    SETOP_EXCEPT: _ClassVar[SetOperation]

class ObjectType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OBJECT_TYPE_UNDEFINED: _ClassVar[ObjectType]
    OBJECT_ACCESS_METHOD: _ClassVar[ObjectType]
    OBJECT_AGGREGATE: _ClassVar[ObjectType]
    OBJECT_AMOP: _ClassVar[ObjectType]
    OBJECT_AMPROC: _ClassVar[ObjectType]
    OBJECT_ATTRIBUTE: _ClassVar[ObjectType]
    OBJECT_CAST: _ClassVar[ObjectType]
    OBJECT_COLUMN: _ClassVar[ObjectType]
    OBJECT_COLLATION: _ClassVar[ObjectType]
    OBJECT_CONVERSION: _ClassVar[ObjectType]
    OBJECT_DATABASE: _ClassVar[ObjectType]
    OBJECT_DEFAULT: _ClassVar[ObjectType]
    OBJECT_DEFACL: _ClassVar[ObjectType]
    OBJECT_DOMAIN: _ClassVar[ObjectType]
    OBJECT_DOMCONSTRAINT: _ClassVar[ObjectType]
    OBJECT_EVENT_TRIGGER: _ClassVar[ObjectType]
    OBJECT_EXTENSION: _ClassVar[ObjectType]
    OBJECT_FDW: _ClassVar[ObjectType]
    OBJECT_FOREIGN_SERVER: _ClassVar[ObjectType]
    OBJECT_FOREIGN_TABLE: _ClassVar[ObjectType]
    OBJECT_FUNCTION: _ClassVar[ObjectType]
    OBJECT_INDEX: _ClassVar[ObjectType]
    OBJECT_LANGUAGE: _ClassVar[ObjectType]
    OBJECT_LARGEOBJECT: _ClassVar[ObjectType]
    OBJECT_MATVIEW: _ClassVar[ObjectType]
    OBJECT_OPCLASS: _ClassVar[ObjectType]
    OBJECT_OPERATOR: _ClassVar[ObjectType]
    OBJECT_OPFAMILY: _ClassVar[ObjectType]
    OBJECT_PARAMETER_ACL: _ClassVar[ObjectType]
    OBJECT_POLICY: _ClassVar[ObjectType]
    OBJECT_PROCEDURE: _ClassVar[ObjectType]
    OBJECT_PUBLICATION: _ClassVar[ObjectType]
    OBJECT_PUBLICATION_NAMESPACE: _ClassVar[ObjectType]
    OBJECT_PUBLICATION_REL: _ClassVar[ObjectType]
    OBJECT_ROLE: _ClassVar[ObjectType]
    OBJECT_ROUTINE: _ClassVar[ObjectType]
    OBJECT_RULE: _ClassVar[ObjectType]
    OBJECT_SCHEMA: _ClassVar[ObjectType]
    OBJECT_SEQUENCE: _ClassVar[ObjectType]
    OBJECT_SUBSCRIPTION: _ClassVar[ObjectType]
    OBJECT_STATISTIC_EXT: _ClassVar[ObjectType]
    OBJECT_TABCONSTRAINT: _ClassVar[ObjectType]
    OBJECT_TABLE: _ClassVar[ObjectType]
    OBJECT_TABLESPACE: _ClassVar[ObjectType]
    OBJECT_TRANSFORM: _ClassVar[ObjectType]
    OBJECT_TRIGGER: _ClassVar[ObjectType]
    OBJECT_TSCONFIGURATION: _ClassVar[ObjectType]
    OBJECT_TSDICTIONARY: _ClassVar[ObjectType]
    OBJECT_TSPARSER: _ClassVar[ObjectType]
    OBJECT_TSTEMPLATE: _ClassVar[ObjectType]
    OBJECT_TYPE: _ClassVar[ObjectType]
    OBJECT_USER_MAPPING: _ClassVar[ObjectType]
    OBJECT_VIEW: _ClassVar[ObjectType]

class DropBehavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DROP_BEHAVIOR_UNDEFINED: _ClassVar[DropBehavior]
    DROP_RESTRICT: _ClassVar[DropBehavior]
    DROP_CASCADE: _ClassVar[DropBehavior]

class AlterTableType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALTER_TABLE_TYPE_UNDEFINED: _ClassVar[AlterTableType]
    AT_AddColumn: _ClassVar[AlterTableType]
    AT_AddColumnToView: _ClassVar[AlterTableType]
    AT_ColumnDefault: _ClassVar[AlterTableType]
    AT_CookedColumnDefault: _ClassVar[AlterTableType]
    AT_DropNotNull: _ClassVar[AlterTableType]
    AT_SetNotNull: _ClassVar[AlterTableType]
    AT_DropExpression: _ClassVar[AlterTableType]
    AT_CheckNotNull: _ClassVar[AlterTableType]
    AT_SetStatistics: _ClassVar[AlterTableType]
    AT_SetOptions: _ClassVar[AlterTableType]
    AT_ResetOptions: _ClassVar[AlterTableType]
    AT_SetStorage: _ClassVar[AlterTableType]
    AT_SetCompression: _ClassVar[AlterTableType]
    AT_DropColumn: _ClassVar[AlterTableType]
    AT_AddIndex: _ClassVar[AlterTableType]
    AT_ReAddIndex: _ClassVar[AlterTableType]
    AT_AddConstraint: _ClassVar[AlterTableType]
    AT_ReAddConstraint: _ClassVar[AlterTableType]
    AT_ReAddDomainConstraint: _ClassVar[AlterTableType]
    AT_AlterConstraint: _ClassVar[AlterTableType]
    AT_ValidateConstraint: _ClassVar[AlterTableType]
    AT_AddIndexConstraint: _ClassVar[AlterTableType]
    AT_DropConstraint: _ClassVar[AlterTableType]
    AT_ReAddComment: _ClassVar[AlterTableType]
    AT_AlterColumnType: _ClassVar[AlterTableType]
    AT_AlterColumnGenericOptions: _ClassVar[AlterTableType]
    AT_ChangeOwner: _ClassVar[AlterTableType]
    AT_ClusterOn: _ClassVar[AlterTableType]
    AT_DropCluster: _ClassVar[AlterTableType]
    AT_SetLogged: _ClassVar[AlterTableType]
    AT_SetUnLogged: _ClassVar[AlterTableType]
    AT_DropOids: _ClassVar[AlterTableType]
    AT_SetAccessMethod: _ClassVar[AlterTableType]
    AT_SetTableSpace: _ClassVar[AlterTableType]
    AT_SetRelOptions: _ClassVar[AlterTableType]
    AT_ResetRelOptions: _ClassVar[AlterTableType]
    AT_ReplaceRelOptions: _ClassVar[AlterTableType]
    AT_EnableTrig: _ClassVar[AlterTableType]
    AT_EnableAlwaysTrig: _ClassVar[AlterTableType]
    AT_EnableReplicaTrig: _ClassVar[AlterTableType]
    AT_DisableTrig: _ClassVar[AlterTableType]
    AT_EnableTrigAll: _ClassVar[AlterTableType]
    AT_DisableTrigAll: _ClassVar[AlterTableType]
    AT_EnableTrigUser: _ClassVar[AlterTableType]
    AT_DisableTrigUser: _ClassVar[AlterTableType]
    AT_EnableRule: _ClassVar[AlterTableType]
    AT_EnableAlwaysRule: _ClassVar[AlterTableType]
    AT_EnableReplicaRule: _ClassVar[AlterTableType]
    AT_DisableRule: _ClassVar[AlterTableType]
    AT_AddInherit: _ClassVar[AlterTableType]
    AT_DropInherit: _ClassVar[AlterTableType]
    AT_AddOf: _ClassVar[AlterTableType]
    AT_DropOf: _ClassVar[AlterTableType]
    AT_ReplicaIdentity: _ClassVar[AlterTableType]
    AT_EnableRowSecurity: _ClassVar[AlterTableType]
    AT_DisableRowSecurity: _ClassVar[AlterTableType]
    AT_ForceRowSecurity: _ClassVar[AlterTableType]
    AT_NoForceRowSecurity: _ClassVar[AlterTableType]
    AT_GenericOptions: _ClassVar[AlterTableType]
    AT_AttachPartition: _ClassVar[AlterTableType]
    AT_DetachPartition: _ClassVar[AlterTableType]
    AT_DetachPartitionFinalize: _ClassVar[AlterTableType]
    AT_AddIdentity: _ClassVar[AlterTableType]
    AT_SetIdentity: _ClassVar[AlterTableType]
    AT_DropIdentity: _ClassVar[AlterTableType]
    AT_ReAddStatistics: _ClassVar[AlterTableType]

class GrantTargetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GRANT_TARGET_TYPE_UNDEFINED: _ClassVar[GrantTargetType]
    ACL_TARGET_OBJECT: _ClassVar[GrantTargetType]
    ACL_TARGET_ALL_IN_SCHEMA: _ClassVar[GrantTargetType]
    ACL_TARGET_DEFAULTS: _ClassVar[GrantTargetType]

class VariableSetKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VARIABLE_SET_KIND_UNDEFINED: _ClassVar[VariableSetKind]
    VAR_SET_VALUE: _ClassVar[VariableSetKind]
    VAR_SET_DEFAULT: _ClassVar[VariableSetKind]
    VAR_SET_CURRENT: _ClassVar[VariableSetKind]
    VAR_SET_MULTI: _ClassVar[VariableSetKind]
    VAR_RESET: _ClassVar[VariableSetKind]
    VAR_RESET_ALL: _ClassVar[VariableSetKind]

class ConstrType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONSTR_TYPE_UNDEFINED: _ClassVar[ConstrType]
    CONSTR_NULL: _ClassVar[ConstrType]
    CONSTR_NOTNULL: _ClassVar[ConstrType]
    CONSTR_DEFAULT: _ClassVar[ConstrType]
    CONSTR_IDENTITY: _ClassVar[ConstrType]
    CONSTR_GENERATED: _ClassVar[ConstrType]
    CONSTR_CHECK: _ClassVar[ConstrType]
    CONSTR_PRIMARY: _ClassVar[ConstrType]
    CONSTR_UNIQUE: _ClassVar[ConstrType]
    CONSTR_EXCLUSION: _ClassVar[ConstrType]
    CONSTR_FOREIGN: _ClassVar[ConstrType]
    CONSTR_ATTR_DEFERRABLE: _ClassVar[ConstrType]
    CONSTR_ATTR_NOT_DEFERRABLE: _ClassVar[ConstrType]
    CONSTR_ATTR_DEFERRED: _ClassVar[ConstrType]
    CONSTR_ATTR_IMMEDIATE: _ClassVar[ConstrType]

class ImportForeignSchemaType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IMPORT_FOREIGN_SCHEMA_TYPE_UNDEFINED: _ClassVar[ImportForeignSchemaType]
    FDW_IMPORT_SCHEMA_ALL: _ClassVar[ImportForeignSchemaType]
    FDW_IMPORT_SCHEMA_LIMIT_TO: _ClassVar[ImportForeignSchemaType]
    FDW_IMPORT_SCHEMA_EXCEPT: _ClassVar[ImportForeignSchemaType]

class RoleStmtType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROLE_STMT_TYPE_UNDEFINED: _ClassVar[RoleStmtType]
    ROLESTMT_ROLE: _ClassVar[RoleStmtType]
    ROLESTMT_USER: _ClassVar[RoleStmtType]
    ROLESTMT_GROUP: _ClassVar[RoleStmtType]

class FetchDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FETCH_DIRECTION_UNDEFINED: _ClassVar[FetchDirection]
    FETCH_FORWARD: _ClassVar[FetchDirection]
    FETCH_BACKWARD: _ClassVar[FetchDirection]
    FETCH_ABSOLUTE: _ClassVar[FetchDirection]
    FETCH_RELATIVE: _ClassVar[FetchDirection]

class FunctionParameterMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FUNCTION_PARAMETER_MODE_UNDEFINED: _ClassVar[FunctionParameterMode]
    FUNC_PARAM_IN: _ClassVar[FunctionParameterMode]
    FUNC_PARAM_OUT: _ClassVar[FunctionParameterMode]
    FUNC_PARAM_INOUT: _ClassVar[FunctionParameterMode]
    FUNC_PARAM_VARIADIC: _ClassVar[FunctionParameterMode]
    FUNC_PARAM_TABLE: _ClassVar[FunctionParameterMode]
    FUNC_PARAM_DEFAULT: _ClassVar[FunctionParameterMode]

class TransactionStmtKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRANSACTION_STMT_KIND_UNDEFINED: _ClassVar[TransactionStmtKind]
    TRANS_STMT_BEGIN: _ClassVar[TransactionStmtKind]
    TRANS_STMT_START: _ClassVar[TransactionStmtKind]
    TRANS_STMT_COMMIT: _ClassVar[TransactionStmtKind]
    TRANS_STMT_ROLLBACK: _ClassVar[TransactionStmtKind]
    TRANS_STMT_SAVEPOINT: _ClassVar[TransactionStmtKind]
    TRANS_STMT_RELEASE: _ClassVar[TransactionStmtKind]
    TRANS_STMT_ROLLBACK_TO: _ClassVar[TransactionStmtKind]
    TRANS_STMT_PREPARE: _ClassVar[TransactionStmtKind]
    TRANS_STMT_COMMIT_PREPARED: _ClassVar[TransactionStmtKind]
    TRANS_STMT_ROLLBACK_PREPARED: _ClassVar[TransactionStmtKind]

class ViewCheckOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VIEW_CHECK_OPTION_UNDEFINED: _ClassVar[ViewCheckOption]
    NO_CHECK_OPTION: _ClassVar[ViewCheckOption]
    LOCAL_CHECK_OPTION: _ClassVar[ViewCheckOption]
    CASCADED_CHECK_OPTION: _ClassVar[ViewCheckOption]

class DiscardMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DISCARD_MODE_UNDEFINED: _ClassVar[DiscardMode]
    DISCARD_ALL: _ClassVar[DiscardMode]
    DISCARD_PLANS: _ClassVar[DiscardMode]
    DISCARD_SEQUENCES: _ClassVar[DiscardMode]
    DISCARD_TEMP: _ClassVar[DiscardMode]

class ReindexObjectType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REINDEX_OBJECT_TYPE_UNDEFINED: _ClassVar[ReindexObjectType]
    REINDEX_OBJECT_INDEX: _ClassVar[ReindexObjectType]
    REINDEX_OBJECT_TABLE: _ClassVar[ReindexObjectType]
    REINDEX_OBJECT_SCHEMA: _ClassVar[ReindexObjectType]
    REINDEX_OBJECT_SYSTEM: _ClassVar[ReindexObjectType]
    REINDEX_OBJECT_DATABASE: _ClassVar[ReindexObjectType]

class AlterTSConfigType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALTER_TSCONFIG_TYPE_UNDEFINED: _ClassVar[AlterTSConfigType]
    ALTER_TSCONFIG_ADD_MAPPING: _ClassVar[AlterTSConfigType]
    ALTER_TSCONFIG_ALTER_MAPPING_FOR_TOKEN: _ClassVar[AlterTSConfigType]
    ALTER_TSCONFIG_REPLACE_DICT: _ClassVar[AlterTSConfigType]
    ALTER_TSCONFIG_REPLACE_DICT_FOR_TOKEN: _ClassVar[AlterTSConfigType]
    ALTER_TSCONFIG_DROP_MAPPING: _ClassVar[AlterTSConfigType]

class PublicationObjSpecType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PUBLICATION_OBJ_SPEC_TYPE_UNDEFINED: _ClassVar[PublicationObjSpecType]
    PUBLICATIONOBJ_TABLE: _ClassVar[PublicationObjSpecType]
    PUBLICATIONOBJ_TABLES_IN_SCHEMA: _ClassVar[PublicationObjSpecType]
    PUBLICATIONOBJ_TABLES_IN_CUR_SCHEMA: _ClassVar[PublicationObjSpecType]
    PUBLICATIONOBJ_CONTINUATION: _ClassVar[PublicationObjSpecType]

class AlterPublicationAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALTER_PUBLICATION_ACTION_UNDEFINED: _ClassVar[AlterPublicationAction]
    AP_AddObjects: _ClassVar[AlterPublicationAction]
    AP_DropObjects: _ClassVar[AlterPublicationAction]
    AP_SetObjects: _ClassVar[AlterPublicationAction]

class AlterSubscriptionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALTER_SUBSCRIPTION_TYPE_UNDEFINED: _ClassVar[AlterSubscriptionType]
    ALTER_SUBSCRIPTION_OPTIONS: _ClassVar[AlterSubscriptionType]
    ALTER_SUBSCRIPTION_CONNECTION: _ClassVar[AlterSubscriptionType]
    ALTER_SUBSCRIPTION_SET_PUBLICATION: _ClassVar[AlterSubscriptionType]
    ALTER_SUBSCRIPTION_ADD_PUBLICATION: _ClassVar[AlterSubscriptionType]
    ALTER_SUBSCRIPTION_DROP_PUBLICATION: _ClassVar[AlterSubscriptionType]
    ALTER_SUBSCRIPTION_REFRESH: _ClassVar[AlterSubscriptionType]
    ALTER_SUBSCRIPTION_ENABLED: _ClassVar[AlterSubscriptionType]
    ALTER_SUBSCRIPTION_SKIP: _ClassVar[AlterSubscriptionType]

class OnCommitAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ON_COMMIT_ACTION_UNDEFINED: _ClassVar[OnCommitAction]
    ONCOMMIT_NOOP: _ClassVar[OnCommitAction]
    ONCOMMIT_PRESERVE_ROWS: _ClassVar[OnCommitAction]
    ONCOMMIT_DELETE_ROWS: _ClassVar[OnCommitAction]
    ONCOMMIT_DROP: _ClassVar[OnCommitAction]

class ParamKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PARAM_KIND_UNDEFINED: _ClassVar[ParamKind]
    PARAM_EXTERN: _ClassVar[ParamKind]
    PARAM_EXEC: _ClassVar[ParamKind]
    PARAM_SUBLINK: _ClassVar[ParamKind]
    PARAM_MULTIEXPR: _ClassVar[ParamKind]

class CoercionContext(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COERCION_CONTEXT_UNDEFINED: _ClassVar[CoercionContext]
    COERCION_IMPLICIT: _ClassVar[CoercionContext]
    COERCION_ASSIGNMENT: _ClassVar[CoercionContext]
    COERCION_PLPGSQL: _ClassVar[CoercionContext]
    COERCION_EXPLICIT: _ClassVar[CoercionContext]

class CoercionForm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COERCION_FORM_UNDEFINED: _ClassVar[CoercionForm]
    COERCE_EXPLICIT_CALL: _ClassVar[CoercionForm]
    COERCE_EXPLICIT_CAST: _ClassVar[CoercionForm]
    COERCE_IMPLICIT_CAST: _ClassVar[CoercionForm]
    COERCE_SQL_SYNTAX: _ClassVar[CoercionForm]

class BoolExprType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BOOL_EXPR_TYPE_UNDEFINED: _ClassVar[BoolExprType]
    AND_EXPR: _ClassVar[BoolExprType]
    OR_EXPR: _ClassVar[BoolExprType]
    NOT_EXPR: _ClassVar[BoolExprType]

class SubLinkType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUB_LINK_TYPE_UNDEFINED: _ClassVar[SubLinkType]
    EXISTS_SUBLINK: _ClassVar[SubLinkType]
    ALL_SUBLINK: _ClassVar[SubLinkType]
    ANY_SUBLINK: _ClassVar[SubLinkType]
    ROWCOMPARE_SUBLINK: _ClassVar[SubLinkType]
    EXPR_SUBLINK: _ClassVar[SubLinkType]
    MULTIEXPR_SUBLINK: _ClassVar[SubLinkType]
    ARRAY_SUBLINK: _ClassVar[SubLinkType]
    CTE_SUBLINK: _ClassVar[SubLinkType]

class RowCompareType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROW_COMPARE_TYPE_UNDEFINED: _ClassVar[RowCompareType]
    ROWCOMPARE_LT: _ClassVar[RowCompareType]
    ROWCOMPARE_LE: _ClassVar[RowCompareType]
    ROWCOMPARE_EQ: _ClassVar[RowCompareType]
    ROWCOMPARE_GE: _ClassVar[RowCompareType]
    ROWCOMPARE_GT: _ClassVar[RowCompareType]
    ROWCOMPARE_NE: _ClassVar[RowCompareType]

class MinMaxOp(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MIN_MAX_OP_UNDEFINED: _ClassVar[MinMaxOp]
    IS_GREATEST: _ClassVar[MinMaxOp]
    IS_LEAST: _ClassVar[MinMaxOp]

class SQLValueFunctionOp(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SQLVALUE_FUNCTION_OP_UNDEFINED: _ClassVar[SQLValueFunctionOp]
    SVFOP_CURRENT_DATE: _ClassVar[SQLValueFunctionOp]
    SVFOP_CURRENT_TIME: _ClassVar[SQLValueFunctionOp]
    SVFOP_CURRENT_TIME_N: _ClassVar[SQLValueFunctionOp]
    SVFOP_CURRENT_TIMESTAMP: _ClassVar[SQLValueFunctionOp]
    SVFOP_CURRENT_TIMESTAMP_N: _ClassVar[SQLValueFunctionOp]
    SVFOP_LOCALTIME: _ClassVar[SQLValueFunctionOp]
    SVFOP_LOCALTIME_N: _ClassVar[SQLValueFunctionOp]
    SVFOP_LOCALTIMESTAMP: _ClassVar[SQLValueFunctionOp]
    SVFOP_LOCALTIMESTAMP_N: _ClassVar[SQLValueFunctionOp]
    SVFOP_CURRENT_ROLE: _ClassVar[SQLValueFunctionOp]
    SVFOP_CURRENT_USER: _ClassVar[SQLValueFunctionOp]
    SVFOP_USER: _ClassVar[SQLValueFunctionOp]
    SVFOP_SESSION_USER: _ClassVar[SQLValueFunctionOp]
    SVFOP_CURRENT_CATALOG: _ClassVar[SQLValueFunctionOp]
    SVFOP_CURRENT_SCHEMA: _ClassVar[SQLValueFunctionOp]

class XmlExprOp(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    XML_EXPR_OP_UNDEFINED: _ClassVar[XmlExprOp]
    IS_XMLCONCAT: _ClassVar[XmlExprOp]
    IS_XMLELEMENT: _ClassVar[XmlExprOp]
    IS_XMLFOREST: _ClassVar[XmlExprOp]
    IS_XMLPARSE: _ClassVar[XmlExprOp]
    IS_XMLPI: _ClassVar[XmlExprOp]
    IS_XMLROOT: _ClassVar[XmlExprOp]
    IS_XMLSERIALIZE: _ClassVar[XmlExprOp]
    IS_DOCUMENT: _ClassVar[XmlExprOp]

class XmlOptionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    XML_OPTION_TYPE_UNDEFINED: _ClassVar[XmlOptionType]
    XMLOPTION_DOCUMENT: _ClassVar[XmlOptionType]
    XMLOPTION_CONTENT: _ClassVar[XmlOptionType]

class JsonEncoding(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    JSON_ENCODING_UNDEFINED: _ClassVar[JsonEncoding]
    JS_ENC_DEFAULT: _ClassVar[JsonEncoding]
    JS_ENC_UTF8: _ClassVar[JsonEncoding]
    JS_ENC_UTF16: _ClassVar[JsonEncoding]
    JS_ENC_UTF32: _ClassVar[JsonEncoding]

class JsonFormatType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    JSON_FORMAT_TYPE_UNDEFINED: _ClassVar[JsonFormatType]
    JS_FORMAT_DEFAULT: _ClassVar[JsonFormatType]
    JS_FORMAT_JSON: _ClassVar[JsonFormatType]
    JS_FORMAT_JSONB: _ClassVar[JsonFormatType]

class JsonConstructorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    JSON_CONSTRUCTOR_TYPE_UNDEFINED: _ClassVar[JsonConstructorType]
    JSCTOR_JSON_OBJECT: _ClassVar[JsonConstructorType]
    JSCTOR_JSON_ARRAY: _ClassVar[JsonConstructorType]
    JSCTOR_JSON_OBJECTAGG: _ClassVar[JsonConstructorType]
    JSCTOR_JSON_ARRAYAGG: _ClassVar[JsonConstructorType]

class JsonValueType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    JSON_VALUE_TYPE_UNDEFINED: _ClassVar[JsonValueType]
    JS_TYPE_ANY: _ClassVar[JsonValueType]
    JS_TYPE_OBJECT: _ClassVar[JsonValueType]
    JS_TYPE_ARRAY: _ClassVar[JsonValueType]
    JS_TYPE_SCALAR: _ClassVar[JsonValueType]

class NullTestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NULL_TEST_TYPE_UNDEFINED: _ClassVar[NullTestType]
    IS_NULL: _ClassVar[NullTestType]
    IS_NOT_NULL: _ClassVar[NullTestType]

class BoolTestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BOOL_TEST_TYPE_UNDEFINED: _ClassVar[BoolTestType]
    IS_TRUE: _ClassVar[BoolTestType]
    IS_NOT_TRUE: _ClassVar[BoolTestType]
    IS_FALSE: _ClassVar[BoolTestType]
    IS_NOT_FALSE: _ClassVar[BoolTestType]
    IS_UNKNOWN: _ClassVar[BoolTestType]
    IS_NOT_UNKNOWN: _ClassVar[BoolTestType]

class CmdType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CMD_TYPE_UNDEFINED: _ClassVar[CmdType]
    CMD_UNKNOWN: _ClassVar[CmdType]
    CMD_SELECT: _ClassVar[CmdType]
    CMD_UPDATE: _ClassVar[CmdType]
    CMD_INSERT: _ClassVar[CmdType]
    CMD_DELETE: _ClassVar[CmdType]
    CMD_MERGE: _ClassVar[CmdType]
    CMD_UTILITY: _ClassVar[CmdType]
    CMD_NOTHING: _ClassVar[CmdType]

class JoinType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    JOIN_TYPE_UNDEFINED: _ClassVar[JoinType]
    JOIN_INNER: _ClassVar[JoinType]
    JOIN_LEFT: _ClassVar[JoinType]
    JOIN_FULL: _ClassVar[JoinType]
    JOIN_RIGHT: _ClassVar[JoinType]
    JOIN_SEMI: _ClassVar[JoinType]
    JOIN_ANTI: _ClassVar[JoinType]
    JOIN_RIGHT_ANTI: _ClassVar[JoinType]
    JOIN_UNIQUE_OUTER: _ClassVar[JoinType]
    JOIN_UNIQUE_INNER: _ClassVar[JoinType]

class AggStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGG_STRATEGY_UNDEFINED: _ClassVar[AggStrategy]
    AGG_PLAIN: _ClassVar[AggStrategy]
    AGG_SORTED: _ClassVar[AggStrategy]
    AGG_HASHED: _ClassVar[AggStrategy]
    AGG_MIXED: _ClassVar[AggStrategy]

class AggSplit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGG_SPLIT_UNDEFINED: _ClassVar[AggSplit]
    AGGSPLIT_SIMPLE: _ClassVar[AggSplit]
    AGGSPLIT_INITIAL_SERIAL: _ClassVar[AggSplit]
    AGGSPLIT_FINAL_DESERIAL: _ClassVar[AggSplit]

class SetOpCmd(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SET_OP_CMD_UNDEFINED: _ClassVar[SetOpCmd]
    SETOPCMD_INTERSECT: _ClassVar[SetOpCmd]
    SETOPCMD_INTERSECT_ALL: _ClassVar[SetOpCmd]
    SETOPCMD_EXCEPT: _ClassVar[SetOpCmd]
    SETOPCMD_EXCEPT_ALL: _ClassVar[SetOpCmd]

class SetOpStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SET_OP_STRATEGY_UNDEFINED: _ClassVar[SetOpStrategy]
    SETOP_SORTED: _ClassVar[SetOpStrategy]
    SETOP_HASHED: _ClassVar[SetOpStrategy]

class OnConflictAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ON_CONFLICT_ACTION_UNDEFINED: _ClassVar[OnConflictAction]
    ONCONFLICT_NONE: _ClassVar[OnConflictAction]
    ONCONFLICT_NOTHING: _ClassVar[OnConflictAction]
    ONCONFLICT_UPDATE: _ClassVar[OnConflictAction]

class LimitOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LIMIT_OPTION_UNDEFINED: _ClassVar[LimitOption]
    LIMIT_OPTION_DEFAULT: _ClassVar[LimitOption]
    LIMIT_OPTION_COUNT: _ClassVar[LimitOption]
    LIMIT_OPTION_WITH_TIES: _ClassVar[LimitOption]

class LockClauseStrength(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOCK_CLAUSE_STRENGTH_UNDEFINED: _ClassVar[LockClauseStrength]
    LCS_NONE: _ClassVar[LockClauseStrength]
    LCS_FORKEYSHARE: _ClassVar[LockClauseStrength]
    LCS_FORSHARE: _ClassVar[LockClauseStrength]
    LCS_FORNOKEYUPDATE: _ClassVar[LockClauseStrength]
    LCS_FORUPDATE: _ClassVar[LockClauseStrength]

class LockWaitPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOCK_WAIT_POLICY_UNDEFINED: _ClassVar[LockWaitPolicy]
    LockWaitBlock: _ClassVar[LockWaitPolicy]
    LockWaitSkip: _ClassVar[LockWaitPolicy]
    LockWaitError: _ClassVar[LockWaitPolicy]

class LockTupleMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOCK_TUPLE_MODE_UNDEFINED: _ClassVar[LockTupleMode]
    LockTupleKeyShare: _ClassVar[LockTupleMode]
    LockTupleShare: _ClassVar[LockTupleMode]
    LockTupleNoKeyExclusive: _ClassVar[LockTupleMode]
    LockTupleExclusive: _ClassVar[LockTupleMode]

class KeywordKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NO_KEYWORD: _ClassVar[KeywordKind]
    UNRESERVED_KEYWORD: _ClassVar[KeywordKind]
    COL_NAME_KEYWORD: _ClassVar[KeywordKind]
    TYPE_FUNC_NAME_KEYWORD: _ClassVar[KeywordKind]
    RESERVED_KEYWORD: _ClassVar[KeywordKind]

class Token(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NUL: _ClassVar[Token]
    ASCII_36: _ClassVar[Token]
    ASCII_37: _ClassVar[Token]
    ASCII_40: _ClassVar[Token]
    ASCII_41: _ClassVar[Token]
    ASCII_42: _ClassVar[Token]
    ASCII_43: _ClassVar[Token]
    ASCII_44: _ClassVar[Token]
    ASCII_45: _ClassVar[Token]
    ASCII_46: _ClassVar[Token]
    ASCII_47: _ClassVar[Token]
    ASCII_58: _ClassVar[Token]
    ASCII_59: _ClassVar[Token]
    ASCII_60: _ClassVar[Token]
    ASCII_61: _ClassVar[Token]
    ASCII_62: _ClassVar[Token]
    ASCII_63: _ClassVar[Token]
    ASCII_91: _ClassVar[Token]
    ASCII_92: _ClassVar[Token]
    ASCII_93: _ClassVar[Token]
    ASCII_94: _ClassVar[Token]
    IDENT: _ClassVar[Token]
    UIDENT: _ClassVar[Token]
    FCONST: _ClassVar[Token]
    SCONST: _ClassVar[Token]
    USCONST: _ClassVar[Token]
    BCONST: _ClassVar[Token]
    XCONST: _ClassVar[Token]
    Op: _ClassVar[Token]
    ICONST: _ClassVar[Token]
    PARAM: _ClassVar[Token]
    TYPECAST: _ClassVar[Token]
    DOT_DOT: _ClassVar[Token]
    COLON_EQUALS: _ClassVar[Token]
    EQUALS_GREATER: _ClassVar[Token]
    LESS_EQUALS: _ClassVar[Token]
    GREATER_EQUALS: _ClassVar[Token]
    NOT_EQUALS: _ClassVar[Token]
    SQL_COMMENT: _ClassVar[Token]
    C_COMMENT: _ClassVar[Token]
    ABORT_P: _ClassVar[Token]
    ABSENT: _ClassVar[Token]
    ABSOLUTE_P: _ClassVar[Token]
    ACCESS: _ClassVar[Token]
    ACTION: _ClassVar[Token]
    ADD_P: _ClassVar[Token]
    ADMIN: _ClassVar[Token]
    AFTER: _ClassVar[Token]
    AGGREGATE: _ClassVar[Token]
    ALL: _ClassVar[Token]
    ALSO: _ClassVar[Token]
    ALTER: _ClassVar[Token]
    ALWAYS: _ClassVar[Token]
    ANALYSE: _ClassVar[Token]
    ANALYZE: _ClassVar[Token]
    AND: _ClassVar[Token]
    ANY: _ClassVar[Token]
    ARRAY: _ClassVar[Token]
    AS: _ClassVar[Token]
    ASC: _ClassVar[Token]
    ASENSITIVE: _ClassVar[Token]
    ASSERTION: _ClassVar[Token]
    ASSIGNMENT: _ClassVar[Token]
    ASYMMETRIC: _ClassVar[Token]
    ATOMIC: _ClassVar[Token]
    AT: _ClassVar[Token]
    ATTACH: _ClassVar[Token]
    ATTRIBUTE: _ClassVar[Token]
    AUTHORIZATION: _ClassVar[Token]
    BACKWARD: _ClassVar[Token]
    BEFORE: _ClassVar[Token]
    BEGIN_P: _ClassVar[Token]
    BETWEEN: _ClassVar[Token]
    BIGINT: _ClassVar[Token]
    BINARY: _ClassVar[Token]
    BIT: _ClassVar[Token]
    BOOLEAN_P: _ClassVar[Token]
    BOTH: _ClassVar[Token]
    BREADTH: _ClassVar[Token]
    BY: _ClassVar[Token]
    CACHE: _ClassVar[Token]
    CALL: _ClassVar[Token]
    CALLED: _ClassVar[Token]
    CASCADE: _ClassVar[Token]
    CASCADED: _ClassVar[Token]
    CASE: _ClassVar[Token]
    CAST: _ClassVar[Token]
    CATALOG_P: _ClassVar[Token]
    CHAIN: _ClassVar[Token]
    CHAR_P: _ClassVar[Token]
    CHARACTER: _ClassVar[Token]
    CHARACTERISTICS: _ClassVar[Token]
    CHECK: _ClassVar[Token]
    CHECKPOINT: _ClassVar[Token]
    CLASS: _ClassVar[Token]
    CLOSE: _ClassVar[Token]
    CLUSTER: _ClassVar[Token]
    COALESCE: _ClassVar[Token]
    COLLATE: _ClassVar[Token]
    COLLATION: _ClassVar[Token]
    COLUMN: _ClassVar[Token]
    COLUMNS: _ClassVar[Token]
    COMMENT: _ClassVar[Token]
    COMMENTS: _ClassVar[Token]
    COMMIT: _ClassVar[Token]
    COMMITTED: _ClassVar[Token]
    COMPRESSION: _ClassVar[Token]
    CONCURRENTLY: _ClassVar[Token]
    CONFIGURATION: _ClassVar[Token]
    CONFLICT: _ClassVar[Token]
    CONNECTION: _ClassVar[Token]
    CONSTRAINT: _ClassVar[Token]
    CONSTRAINTS: _ClassVar[Token]
    CONTENT_P: _ClassVar[Token]
    CONTINUE_P: _ClassVar[Token]
    CONVERSION_P: _ClassVar[Token]
    COPY: _ClassVar[Token]
    COST: _ClassVar[Token]
    CREATE: _ClassVar[Token]
    CROSS: _ClassVar[Token]
    CSV: _ClassVar[Token]
    CUBE: _ClassVar[Token]
    CURRENT_P: _ClassVar[Token]
    CURRENT_CATALOG: _ClassVar[Token]
    CURRENT_DATE: _ClassVar[Token]
    CURRENT_ROLE: _ClassVar[Token]
    CURRENT_SCHEMA: _ClassVar[Token]
    CURRENT_TIME: _ClassVar[Token]
    CURRENT_TIMESTAMP: _ClassVar[Token]
    CURRENT_USER: _ClassVar[Token]
    CURSOR: _ClassVar[Token]
    CYCLE: _ClassVar[Token]
    DATA_P: _ClassVar[Token]
    DATABASE: _ClassVar[Token]
    DAY_P: _ClassVar[Token]
    DEALLOCATE: _ClassVar[Token]
    DEC: _ClassVar[Token]
    DECIMAL_P: _ClassVar[Token]
    DECLARE: _ClassVar[Token]
    DEFAULT: _ClassVar[Token]
    DEFAULTS: _ClassVar[Token]
    DEFERRABLE: _ClassVar[Token]
    DEFERRED: _ClassVar[Token]
    DEFINER: _ClassVar[Token]
    DELETE_P: _ClassVar[Token]
    DELIMITER: _ClassVar[Token]
    DELIMITERS: _ClassVar[Token]
    DEPENDS: _ClassVar[Token]
    DEPTH: _ClassVar[Token]
    DESC: _ClassVar[Token]
    DETACH: _ClassVar[Token]
    DICTIONARY: _ClassVar[Token]
    DISABLE_P: _ClassVar[Token]
    DISCARD: _ClassVar[Token]
    DISTINCT: _ClassVar[Token]
    DO: _ClassVar[Token]
    DOCUMENT_P: _ClassVar[Token]
    DOMAIN_P: _ClassVar[Token]
    DOUBLE_P: _ClassVar[Token]
    DROP: _ClassVar[Token]
    EACH: _ClassVar[Token]
    ELSE: _ClassVar[Token]
    ENABLE_P: _ClassVar[Token]
    ENCODING: _ClassVar[Token]
    ENCRYPTED: _ClassVar[Token]
    END_P: _ClassVar[Token]
    ENUM_P: _ClassVar[Token]
    ESCAPE: _ClassVar[Token]
    EVENT: _ClassVar[Token]
    EXCEPT: _ClassVar[Token]
    EXCLUDE: _ClassVar[Token]
    EXCLUDING: _ClassVar[Token]
    EXCLUSIVE: _ClassVar[Token]
    EXECUTE: _ClassVar[Token]
    EXISTS: _ClassVar[Token]
    EXPLAIN: _ClassVar[Token]
    EXPRESSION: _ClassVar[Token]
    EXTENSION: _ClassVar[Token]
    EXTERNAL: _ClassVar[Token]
    EXTRACT: _ClassVar[Token]
    FALSE_P: _ClassVar[Token]
    FAMILY: _ClassVar[Token]
    FETCH: _ClassVar[Token]
    FILTER: _ClassVar[Token]
    FINALIZE: _ClassVar[Token]
    FIRST_P: _ClassVar[Token]
    FLOAT_P: _ClassVar[Token]
    FOLLOWING: _ClassVar[Token]
    FOR: _ClassVar[Token]
    FORCE: _ClassVar[Token]
    FOREIGN: _ClassVar[Token]
    FORMAT: _ClassVar[Token]
    FORWARD: _ClassVar[Token]
    FREEZE: _ClassVar[Token]
    FROM: _ClassVar[Token]
    FULL: _ClassVar[Token]
    FUNCTION: _ClassVar[Token]
    FUNCTIONS: _ClassVar[Token]
    GENERATED: _ClassVar[Token]
    GLOBAL: _ClassVar[Token]
    GRANT: _ClassVar[Token]
    GRANTED: _ClassVar[Token]
    GREATEST: _ClassVar[Token]
    GROUP_P: _ClassVar[Token]
    GROUPING: _ClassVar[Token]
    GROUPS: _ClassVar[Token]
    HANDLER: _ClassVar[Token]
    HAVING: _ClassVar[Token]
    HEADER_P: _ClassVar[Token]
    HOLD: _ClassVar[Token]
    HOUR_P: _ClassVar[Token]
    IDENTITY_P: _ClassVar[Token]
    IF_P: _ClassVar[Token]
    ILIKE: _ClassVar[Token]
    IMMEDIATE: _ClassVar[Token]
    IMMUTABLE: _ClassVar[Token]
    IMPLICIT_P: _ClassVar[Token]
    IMPORT_P: _ClassVar[Token]
    IN_P: _ClassVar[Token]
    INCLUDE: _ClassVar[Token]
    INCLUDING: _ClassVar[Token]
    INCREMENT: _ClassVar[Token]
    INDENT: _ClassVar[Token]
    INDEX: _ClassVar[Token]
    INDEXES: _ClassVar[Token]
    INHERIT: _ClassVar[Token]
    INHERITS: _ClassVar[Token]
    INITIALLY: _ClassVar[Token]
    INLINE_P: _ClassVar[Token]
    INNER_P: _ClassVar[Token]
    INOUT: _ClassVar[Token]
    INPUT_P: _ClassVar[Token]
    INSENSITIVE: _ClassVar[Token]
    INSERT: _ClassVar[Token]
    INSTEAD: _ClassVar[Token]
    INT_P: _ClassVar[Token]
    INTEGER: _ClassVar[Token]
    INTERSECT: _ClassVar[Token]
    INTERVAL: _ClassVar[Token]
    INTO: _ClassVar[Token]
    INVOKER: _ClassVar[Token]
    IS: _ClassVar[Token]
    ISNULL: _ClassVar[Token]
    ISOLATION: _ClassVar[Token]
    JOIN: _ClassVar[Token]
    JSON: _ClassVar[Token]
    JSON_ARRAY: _ClassVar[Token]
    JSON_ARRAYAGG: _ClassVar[Token]
    JSON_OBJECT: _ClassVar[Token]
    JSON_OBJECTAGG: _ClassVar[Token]
    KEY: _ClassVar[Token]
    KEYS: _ClassVar[Token]
    LABEL: _ClassVar[Token]
    LANGUAGE: _ClassVar[Token]
    LARGE_P: _ClassVar[Token]
    LAST_P: _ClassVar[Token]
    LATERAL_P: _ClassVar[Token]
    LEADING: _ClassVar[Token]
    LEAKPROOF: _ClassVar[Token]
    LEAST: _ClassVar[Token]
    LEFT: _ClassVar[Token]
    LEVEL: _ClassVar[Token]
    LIKE: _ClassVar[Token]
    LIMIT: _ClassVar[Token]
    LISTEN: _ClassVar[Token]
    LOAD: _ClassVar[Token]
    LOCAL: _ClassVar[Token]
    LOCALTIME: _ClassVar[Token]
    LOCALTIMESTAMP: _ClassVar[Token]
    LOCATION: _ClassVar[Token]
    LOCK_P: _ClassVar[Token]
    LOCKED: _ClassVar[Token]
    LOGGED: _ClassVar[Token]
    MAPPING: _ClassVar[Token]
    MATCH: _ClassVar[Token]
    MATCHED: _ClassVar[Token]
    MATERIALIZED: _ClassVar[Token]
    MAXVALUE: _ClassVar[Token]
    MERGE: _ClassVar[Token]
    METHOD: _ClassVar[Token]
    MINUTE_P: _ClassVar[Token]
    MINVALUE: _ClassVar[Token]
    MODE: _ClassVar[Token]
    MONTH_P: _ClassVar[Token]
    MOVE: _ClassVar[Token]
    NAME_P: _ClassVar[Token]
    NAMES: _ClassVar[Token]
    NATIONAL: _ClassVar[Token]
    NATURAL: _ClassVar[Token]
    NCHAR: _ClassVar[Token]
    NEW: _ClassVar[Token]
    NEXT: _ClassVar[Token]
    NFC: _ClassVar[Token]
    NFD: _ClassVar[Token]
    NFKC: _ClassVar[Token]
    NFKD: _ClassVar[Token]
    NO: _ClassVar[Token]
    NONE: _ClassVar[Token]
    NORMALIZE: _ClassVar[Token]
    NORMALIZED: _ClassVar[Token]
    NOT: _ClassVar[Token]
    NOTHING: _ClassVar[Token]
    NOTIFY: _ClassVar[Token]
    NOTNULL: _ClassVar[Token]
    NOWAIT: _ClassVar[Token]
    NULL_P: _ClassVar[Token]
    NULLIF: _ClassVar[Token]
    NULLS_P: _ClassVar[Token]
    NUMERIC: _ClassVar[Token]
    OBJECT_P: _ClassVar[Token]
    OF: _ClassVar[Token]
    OFF: _ClassVar[Token]
    OFFSET: _ClassVar[Token]
    OIDS: _ClassVar[Token]
    OLD: _ClassVar[Token]
    ON: _ClassVar[Token]
    ONLY: _ClassVar[Token]
    OPERATOR: _ClassVar[Token]
    OPTION: _ClassVar[Token]
    OPTIONS: _ClassVar[Token]
    OR: _ClassVar[Token]
    ORDER: _ClassVar[Token]
    ORDINALITY: _ClassVar[Token]
    OTHERS: _ClassVar[Token]
    OUT_P: _ClassVar[Token]
    OUTER_P: _ClassVar[Token]
    OVER: _ClassVar[Token]
    OVERLAPS: _ClassVar[Token]
    OVERLAY: _ClassVar[Token]
    OVERRIDING: _ClassVar[Token]
    OWNED: _ClassVar[Token]
    OWNER: _ClassVar[Token]
    PARALLEL: _ClassVar[Token]
    PARAMETER: _ClassVar[Token]
    PARSER: _ClassVar[Token]
    PARTIAL: _ClassVar[Token]
    PARTITION: _ClassVar[Token]
    PASSING: _ClassVar[Token]
    PASSWORD: _ClassVar[Token]
    PLACING: _ClassVar[Token]
    PLANS: _ClassVar[Token]
    POLICY: _ClassVar[Token]
    POSITION: _ClassVar[Token]
    PRECEDING: _ClassVar[Token]
    PRECISION: _ClassVar[Token]
    PRESERVE: _ClassVar[Token]
    PREPARE: _ClassVar[Token]
    PREPARED: _ClassVar[Token]
    PRIMARY: _ClassVar[Token]
    PRIOR: _ClassVar[Token]
    PRIVILEGES: _ClassVar[Token]
    PROCEDURAL: _ClassVar[Token]
    PROCEDURE: _ClassVar[Token]
    PROCEDURES: _ClassVar[Token]
    PROGRAM: _ClassVar[Token]
    PUBLICATION: _ClassVar[Token]
    QUOTE: _ClassVar[Token]
    RANGE: _ClassVar[Token]
    READ: _ClassVar[Token]
    REAL: _ClassVar[Token]
    REASSIGN: _ClassVar[Token]
    RECHECK: _ClassVar[Token]
    RECURSIVE: _ClassVar[Token]
    REF_P: _ClassVar[Token]
    REFERENCES: _ClassVar[Token]
    REFERENCING: _ClassVar[Token]
    REFRESH: _ClassVar[Token]
    REINDEX: _ClassVar[Token]
    RELATIVE_P: _ClassVar[Token]
    RELEASE: _ClassVar[Token]
    RENAME: _ClassVar[Token]
    REPEATABLE: _ClassVar[Token]
    REPLACE: _ClassVar[Token]
    REPLICA: _ClassVar[Token]
    RESET: _ClassVar[Token]
    RESTART: _ClassVar[Token]
    RESTRICT: _ClassVar[Token]
    RETURN: _ClassVar[Token]
    RETURNING: _ClassVar[Token]
    RETURNS: _ClassVar[Token]
    REVOKE: _ClassVar[Token]
    RIGHT: _ClassVar[Token]
    ROLE: _ClassVar[Token]
    ROLLBACK: _ClassVar[Token]
    ROLLUP: _ClassVar[Token]
    ROUTINE: _ClassVar[Token]
    ROUTINES: _ClassVar[Token]
    ROW: _ClassVar[Token]
    ROWS: _ClassVar[Token]
    RULE: _ClassVar[Token]
    SAVEPOINT: _ClassVar[Token]
    SCALAR: _ClassVar[Token]
    SCHEMA: _ClassVar[Token]
    SCHEMAS: _ClassVar[Token]
    SCROLL: _ClassVar[Token]
    SEARCH: _ClassVar[Token]
    SECOND_P: _ClassVar[Token]
    SECURITY: _ClassVar[Token]
    SELECT: _ClassVar[Token]
    SEQUENCE: _ClassVar[Token]
    SEQUENCES: _ClassVar[Token]
    SERIALIZABLE: _ClassVar[Token]
    SERVER: _ClassVar[Token]
    SESSION: _ClassVar[Token]
    SESSION_USER: _ClassVar[Token]
    SET: _ClassVar[Token]
    SETS: _ClassVar[Token]
    SETOF: _ClassVar[Token]
    SHARE: _ClassVar[Token]
    SHOW: _ClassVar[Token]
    SIMILAR: _ClassVar[Token]
    SIMPLE: _ClassVar[Token]
    SKIP: _ClassVar[Token]
    SMALLINT: _ClassVar[Token]
    SNAPSHOT: _ClassVar[Token]
    SOME: _ClassVar[Token]
    SQL_P: _ClassVar[Token]
    STABLE: _ClassVar[Token]
    STANDALONE_P: _ClassVar[Token]
    START: _ClassVar[Token]
    STATEMENT: _ClassVar[Token]
    STATISTICS: _ClassVar[Token]
    STDIN: _ClassVar[Token]
    STDOUT: _ClassVar[Token]
    STORAGE: _ClassVar[Token]
    STORED: _ClassVar[Token]
    STRICT_P: _ClassVar[Token]
    STRIP_P: _ClassVar[Token]
    SUBSCRIPTION: _ClassVar[Token]
    SUBSTRING: _ClassVar[Token]
    SUPPORT: _ClassVar[Token]
    SYMMETRIC: _ClassVar[Token]
    SYSID: _ClassVar[Token]
    SYSTEM_P: _ClassVar[Token]
    SYSTEM_USER: _ClassVar[Token]
    TABLE: _ClassVar[Token]
    TABLES: _ClassVar[Token]
    TABLESAMPLE: _ClassVar[Token]
    TABLESPACE: _ClassVar[Token]
    TEMP: _ClassVar[Token]
    TEMPLATE: _ClassVar[Token]
    TEMPORARY: _ClassVar[Token]
    TEXT_P: _ClassVar[Token]
    THEN: _ClassVar[Token]
    TIES: _ClassVar[Token]
    TIME: _ClassVar[Token]
    TIMESTAMP: _ClassVar[Token]
    TO: _ClassVar[Token]
    TRAILING: _ClassVar[Token]
    TRANSACTION: _ClassVar[Token]
    TRANSFORM: _ClassVar[Token]
    TREAT: _ClassVar[Token]
    TRIGGER: _ClassVar[Token]
    TRIM: _ClassVar[Token]
    TRUE_P: _ClassVar[Token]
    TRUNCATE: _ClassVar[Token]
    TRUSTED: _ClassVar[Token]
    TYPE_P: _ClassVar[Token]
    TYPES_P: _ClassVar[Token]
    UESCAPE: _ClassVar[Token]
    UNBOUNDED: _ClassVar[Token]
    UNCOMMITTED: _ClassVar[Token]
    UNENCRYPTED: _ClassVar[Token]
    UNION: _ClassVar[Token]
    UNIQUE: _ClassVar[Token]
    UNKNOWN: _ClassVar[Token]
    UNLISTEN: _ClassVar[Token]
    UNLOGGED: _ClassVar[Token]
    UNTIL: _ClassVar[Token]
    UPDATE: _ClassVar[Token]
    USER: _ClassVar[Token]
    USING: _ClassVar[Token]
    VACUUM: _ClassVar[Token]
    VALID: _ClassVar[Token]
    VALIDATE: _ClassVar[Token]
    VALIDATOR: _ClassVar[Token]
    VALUE_P: _ClassVar[Token]
    VALUES: _ClassVar[Token]
    VARCHAR: _ClassVar[Token]
    VARIADIC: _ClassVar[Token]
    VARYING: _ClassVar[Token]
    VERBOSE: _ClassVar[Token]
    VERSION_P: _ClassVar[Token]
    VIEW: _ClassVar[Token]
    VIEWS: _ClassVar[Token]
    VOLATILE: _ClassVar[Token]
    WHEN: _ClassVar[Token]
    WHERE: _ClassVar[Token]
    WHITESPACE_P: _ClassVar[Token]
    WINDOW: _ClassVar[Token]
    WITH: _ClassVar[Token]
    WITHIN: _ClassVar[Token]
    WITHOUT: _ClassVar[Token]
    WORK: _ClassVar[Token]
    WRAPPER: _ClassVar[Token]
    WRITE: _ClassVar[Token]
    XML_P: _ClassVar[Token]
    XMLATTRIBUTES: _ClassVar[Token]
    XMLCONCAT: _ClassVar[Token]
    XMLELEMENT: _ClassVar[Token]
    XMLEXISTS: _ClassVar[Token]
    XMLFOREST: _ClassVar[Token]
    XMLNAMESPACES: _ClassVar[Token]
    XMLPARSE: _ClassVar[Token]
    XMLPI: _ClassVar[Token]
    XMLROOT: _ClassVar[Token]
    XMLSERIALIZE: _ClassVar[Token]
    XMLTABLE: _ClassVar[Token]
    YEAR_P: _ClassVar[Token]
    YES_P: _ClassVar[Token]
    ZONE: _ClassVar[Token]
    FORMAT_LA: _ClassVar[Token]
    NOT_LA: _ClassVar[Token]
    NULLS_LA: _ClassVar[Token]
    WITH_LA: _ClassVar[Token]
    WITHOUT_LA: _ClassVar[Token]
    MODE_TYPE_NAME: _ClassVar[Token]
    MODE_PLPGSQL_EXPR: _ClassVar[Token]
    MODE_PLPGSQL_ASSIGN1: _ClassVar[Token]
    MODE_PLPGSQL_ASSIGN2: _ClassVar[Token]
    MODE_PLPGSQL_ASSIGN3: _ClassVar[Token]
    UMINUS: _ClassVar[Token]

OVERRIDING_KIND_UNDEFINED: OverridingKind
OVERRIDING_NOT_SET: OverridingKind
OVERRIDING_USER_VALUE: OverridingKind
OVERRIDING_SYSTEM_VALUE: OverridingKind
QUERY_SOURCE_UNDEFINED: QuerySource
QSRC_ORIGINAL: QuerySource
QSRC_PARSER: QuerySource
QSRC_INSTEAD_RULE: QuerySource
QSRC_QUAL_INSTEAD_RULE: QuerySource
QSRC_NON_INSTEAD_RULE: QuerySource
SORT_BY_DIR_UNDEFINED: SortByDir
SORTBY_DEFAULT: SortByDir
SORTBY_ASC: SortByDir
SORTBY_DESC: SortByDir
SORTBY_USING: SortByDir
SORT_BY_NULLS_UNDEFINED: SortByNulls
SORTBY_NULLS_DEFAULT: SortByNulls
SORTBY_NULLS_FIRST: SortByNulls
SORTBY_NULLS_LAST: SortByNulls
SET_QUANTIFIER_UNDEFINED: SetQuantifier
SET_QUANTIFIER_DEFAULT: SetQuantifier
SET_QUANTIFIER_ALL: SetQuantifier
SET_QUANTIFIER_DISTINCT: SetQuantifier
A_EXPR_KIND_UNDEFINED: A_Expr_Kind
AEXPR_OP: A_Expr_Kind
AEXPR_OP_ANY: A_Expr_Kind
AEXPR_OP_ALL: A_Expr_Kind
AEXPR_DISTINCT: A_Expr_Kind
AEXPR_NOT_DISTINCT: A_Expr_Kind
AEXPR_NULLIF: A_Expr_Kind
AEXPR_IN: A_Expr_Kind
AEXPR_LIKE: A_Expr_Kind
AEXPR_ILIKE: A_Expr_Kind
AEXPR_SIMILAR: A_Expr_Kind
AEXPR_BETWEEN: A_Expr_Kind
AEXPR_NOT_BETWEEN: A_Expr_Kind
AEXPR_BETWEEN_SYM: A_Expr_Kind
AEXPR_NOT_BETWEEN_SYM: A_Expr_Kind
ROLE_SPEC_TYPE_UNDEFINED: RoleSpecType
ROLESPEC_CSTRING: RoleSpecType
ROLESPEC_CURRENT_ROLE: RoleSpecType
ROLESPEC_CURRENT_USER: RoleSpecType
ROLESPEC_SESSION_USER: RoleSpecType
ROLESPEC_PUBLIC: RoleSpecType
TABLE_LIKE_OPTION_UNDEFINED: TableLikeOption
CREATE_TABLE_LIKE_COMMENTS: TableLikeOption
CREATE_TABLE_LIKE_COMPRESSION: TableLikeOption
CREATE_TABLE_LIKE_CONSTRAINTS: TableLikeOption
CREATE_TABLE_LIKE_DEFAULTS: TableLikeOption
CREATE_TABLE_LIKE_GENERATED: TableLikeOption
CREATE_TABLE_LIKE_IDENTITY: TableLikeOption
CREATE_TABLE_LIKE_INDEXES: TableLikeOption
CREATE_TABLE_LIKE_STATISTICS: TableLikeOption
CREATE_TABLE_LIKE_STORAGE: TableLikeOption
CREATE_TABLE_LIKE_ALL: TableLikeOption
DEF_ELEM_ACTION_UNDEFINED: DefElemAction
DEFELEM_UNSPEC: DefElemAction
DEFELEM_SET: DefElemAction
DEFELEM_ADD: DefElemAction
DEFELEM_DROP: DefElemAction
PARTITION_STRATEGY_UNDEFINED: PartitionStrategy
PARTITION_STRATEGY_LIST: PartitionStrategy
PARTITION_STRATEGY_RANGE: PartitionStrategy
PARTITION_STRATEGY_HASH: PartitionStrategy
PARTITION_RANGE_DATUM_KIND_UNDEFINED: PartitionRangeDatumKind
PARTITION_RANGE_DATUM_MINVALUE: PartitionRangeDatumKind
PARTITION_RANGE_DATUM_VALUE: PartitionRangeDatumKind
PARTITION_RANGE_DATUM_MAXVALUE: PartitionRangeDatumKind
RTEKIND_UNDEFINED: RTEKind
RTE_RELATION: RTEKind
RTE_SUBQUERY: RTEKind
RTE_JOIN: RTEKind
RTE_FUNCTION: RTEKind
RTE_TABLEFUNC: RTEKind
RTE_VALUES: RTEKind
RTE_CTE: RTEKind
RTE_NAMEDTUPLESTORE: RTEKind
RTE_RESULT: RTEKind
WCOKIND_UNDEFINED: WCOKind
WCO_VIEW_CHECK: WCOKind
WCO_RLS_INSERT_CHECK: WCOKind
WCO_RLS_UPDATE_CHECK: WCOKind
WCO_RLS_CONFLICT_CHECK: WCOKind
WCO_RLS_MERGE_UPDATE_CHECK: WCOKind
WCO_RLS_MERGE_DELETE_CHECK: WCOKind
GROUPING_SET_KIND_UNDEFINED: GroupingSetKind
GROUPING_SET_EMPTY: GroupingSetKind
GROUPING_SET_SIMPLE: GroupingSetKind
GROUPING_SET_ROLLUP: GroupingSetKind
GROUPING_SET_CUBE: GroupingSetKind
GROUPING_SET_SETS: GroupingSetKind
CTEMATERIALIZE_UNDEFINED: CTEMaterialize
CTEMaterializeDefault: CTEMaterialize
CTEMaterializeAlways: CTEMaterialize
CTEMaterializeNever: CTEMaterialize
SET_OPERATION_UNDEFINED: SetOperation
SETOP_NONE: SetOperation
SETOP_UNION: SetOperation
SETOP_INTERSECT: SetOperation
SETOP_EXCEPT: SetOperation
OBJECT_TYPE_UNDEFINED: ObjectType
OBJECT_ACCESS_METHOD: ObjectType
OBJECT_AGGREGATE: ObjectType
OBJECT_AMOP: ObjectType
OBJECT_AMPROC: ObjectType
OBJECT_ATTRIBUTE: ObjectType
OBJECT_CAST: ObjectType
OBJECT_COLUMN: ObjectType
OBJECT_COLLATION: ObjectType
OBJECT_CONVERSION: ObjectType
OBJECT_DATABASE: ObjectType
OBJECT_DEFAULT: ObjectType
OBJECT_DEFACL: ObjectType
OBJECT_DOMAIN: ObjectType
OBJECT_DOMCONSTRAINT: ObjectType
OBJECT_EVENT_TRIGGER: ObjectType
OBJECT_EXTENSION: ObjectType
OBJECT_FDW: ObjectType
OBJECT_FOREIGN_SERVER: ObjectType
OBJECT_FOREIGN_TABLE: ObjectType
OBJECT_FUNCTION: ObjectType
OBJECT_INDEX: ObjectType
OBJECT_LANGUAGE: ObjectType
OBJECT_LARGEOBJECT: ObjectType
OBJECT_MATVIEW: ObjectType
OBJECT_OPCLASS: ObjectType
OBJECT_OPERATOR: ObjectType
OBJECT_OPFAMILY: ObjectType
OBJECT_PARAMETER_ACL: ObjectType
OBJECT_POLICY: ObjectType
OBJECT_PROCEDURE: ObjectType
OBJECT_PUBLICATION: ObjectType
OBJECT_PUBLICATION_NAMESPACE: ObjectType
OBJECT_PUBLICATION_REL: ObjectType
OBJECT_ROLE: ObjectType
OBJECT_ROUTINE: ObjectType
OBJECT_RULE: ObjectType
OBJECT_SCHEMA: ObjectType
OBJECT_SEQUENCE: ObjectType
OBJECT_SUBSCRIPTION: ObjectType
OBJECT_STATISTIC_EXT: ObjectType
OBJECT_TABCONSTRAINT: ObjectType
OBJECT_TABLE: ObjectType
OBJECT_TABLESPACE: ObjectType
OBJECT_TRANSFORM: ObjectType
OBJECT_TRIGGER: ObjectType
OBJECT_TSCONFIGURATION: ObjectType
OBJECT_TSDICTIONARY: ObjectType
OBJECT_TSPARSER: ObjectType
OBJECT_TSTEMPLATE: ObjectType
OBJECT_TYPE: ObjectType
OBJECT_USER_MAPPING: ObjectType
OBJECT_VIEW: ObjectType
DROP_BEHAVIOR_UNDEFINED: DropBehavior
DROP_RESTRICT: DropBehavior
DROP_CASCADE: DropBehavior
ALTER_TABLE_TYPE_UNDEFINED: AlterTableType
AT_AddColumn: AlterTableType
AT_AddColumnToView: AlterTableType
AT_ColumnDefault: AlterTableType
AT_CookedColumnDefault: AlterTableType
AT_DropNotNull: AlterTableType
AT_SetNotNull: AlterTableType
AT_DropExpression: AlterTableType
AT_CheckNotNull: AlterTableType
AT_SetStatistics: AlterTableType
AT_SetOptions: AlterTableType
AT_ResetOptions: AlterTableType
AT_SetStorage: AlterTableType
AT_SetCompression: AlterTableType
AT_DropColumn: AlterTableType
AT_AddIndex: AlterTableType
AT_ReAddIndex: AlterTableType
AT_AddConstraint: AlterTableType
AT_ReAddConstraint: AlterTableType
AT_ReAddDomainConstraint: AlterTableType
AT_AlterConstraint: AlterTableType
AT_ValidateConstraint: AlterTableType
AT_AddIndexConstraint: AlterTableType
AT_DropConstraint: AlterTableType
AT_ReAddComment: AlterTableType
AT_AlterColumnType: AlterTableType
AT_AlterColumnGenericOptions: AlterTableType
AT_ChangeOwner: AlterTableType
AT_ClusterOn: AlterTableType
AT_DropCluster: AlterTableType
AT_SetLogged: AlterTableType
AT_SetUnLogged: AlterTableType
AT_DropOids: AlterTableType
AT_SetAccessMethod: AlterTableType
AT_SetTableSpace: AlterTableType
AT_SetRelOptions: AlterTableType
AT_ResetRelOptions: AlterTableType
AT_ReplaceRelOptions: AlterTableType
AT_EnableTrig: AlterTableType
AT_EnableAlwaysTrig: AlterTableType
AT_EnableReplicaTrig: AlterTableType
AT_DisableTrig: AlterTableType
AT_EnableTrigAll: AlterTableType
AT_DisableTrigAll: AlterTableType
AT_EnableTrigUser: AlterTableType
AT_DisableTrigUser: AlterTableType
AT_EnableRule: AlterTableType
AT_EnableAlwaysRule: AlterTableType
AT_EnableReplicaRule: AlterTableType
AT_DisableRule: AlterTableType
AT_AddInherit: AlterTableType
AT_DropInherit: AlterTableType
AT_AddOf: AlterTableType
AT_DropOf: AlterTableType
AT_ReplicaIdentity: AlterTableType
AT_EnableRowSecurity: AlterTableType
AT_DisableRowSecurity: AlterTableType
AT_ForceRowSecurity: AlterTableType
AT_NoForceRowSecurity: AlterTableType
AT_GenericOptions: AlterTableType
AT_AttachPartition: AlterTableType
AT_DetachPartition: AlterTableType
AT_DetachPartitionFinalize: AlterTableType
AT_AddIdentity: AlterTableType
AT_SetIdentity: AlterTableType
AT_DropIdentity: AlterTableType
AT_ReAddStatistics: AlterTableType
GRANT_TARGET_TYPE_UNDEFINED: GrantTargetType
ACL_TARGET_OBJECT: GrantTargetType
ACL_TARGET_ALL_IN_SCHEMA: GrantTargetType
ACL_TARGET_DEFAULTS: GrantTargetType
VARIABLE_SET_KIND_UNDEFINED: VariableSetKind
VAR_SET_VALUE: VariableSetKind
VAR_SET_DEFAULT: VariableSetKind
VAR_SET_CURRENT: VariableSetKind
VAR_SET_MULTI: VariableSetKind
VAR_RESET: VariableSetKind
VAR_RESET_ALL: VariableSetKind
CONSTR_TYPE_UNDEFINED: ConstrType
CONSTR_NULL: ConstrType
CONSTR_NOTNULL: ConstrType
CONSTR_DEFAULT: ConstrType
CONSTR_IDENTITY: ConstrType
CONSTR_GENERATED: ConstrType
CONSTR_CHECK: ConstrType
CONSTR_PRIMARY: ConstrType
CONSTR_UNIQUE: ConstrType
CONSTR_EXCLUSION: ConstrType
CONSTR_FOREIGN: ConstrType
CONSTR_ATTR_DEFERRABLE: ConstrType
CONSTR_ATTR_NOT_DEFERRABLE: ConstrType
CONSTR_ATTR_DEFERRED: ConstrType
CONSTR_ATTR_IMMEDIATE: ConstrType
IMPORT_FOREIGN_SCHEMA_TYPE_UNDEFINED: ImportForeignSchemaType
FDW_IMPORT_SCHEMA_ALL: ImportForeignSchemaType
FDW_IMPORT_SCHEMA_LIMIT_TO: ImportForeignSchemaType
FDW_IMPORT_SCHEMA_EXCEPT: ImportForeignSchemaType
ROLE_STMT_TYPE_UNDEFINED: RoleStmtType
ROLESTMT_ROLE: RoleStmtType
ROLESTMT_USER: RoleStmtType
ROLESTMT_GROUP: RoleStmtType
FETCH_DIRECTION_UNDEFINED: FetchDirection
FETCH_FORWARD: FetchDirection
FETCH_BACKWARD: FetchDirection
FETCH_ABSOLUTE: FetchDirection
FETCH_RELATIVE: FetchDirection
FUNCTION_PARAMETER_MODE_UNDEFINED: FunctionParameterMode
FUNC_PARAM_IN: FunctionParameterMode
FUNC_PARAM_OUT: FunctionParameterMode
FUNC_PARAM_INOUT: FunctionParameterMode
FUNC_PARAM_VARIADIC: FunctionParameterMode
FUNC_PARAM_TABLE: FunctionParameterMode
FUNC_PARAM_DEFAULT: FunctionParameterMode
TRANSACTION_STMT_KIND_UNDEFINED: TransactionStmtKind
TRANS_STMT_BEGIN: TransactionStmtKind
TRANS_STMT_START: TransactionStmtKind
TRANS_STMT_COMMIT: TransactionStmtKind
TRANS_STMT_ROLLBACK: TransactionStmtKind
TRANS_STMT_SAVEPOINT: TransactionStmtKind
TRANS_STMT_RELEASE: TransactionStmtKind
TRANS_STMT_ROLLBACK_TO: TransactionStmtKind
TRANS_STMT_PREPARE: TransactionStmtKind
TRANS_STMT_COMMIT_PREPARED: TransactionStmtKind
TRANS_STMT_ROLLBACK_PREPARED: TransactionStmtKind
VIEW_CHECK_OPTION_UNDEFINED: ViewCheckOption
NO_CHECK_OPTION: ViewCheckOption
LOCAL_CHECK_OPTION: ViewCheckOption
CASCADED_CHECK_OPTION: ViewCheckOption
DISCARD_MODE_UNDEFINED: DiscardMode
DISCARD_ALL: DiscardMode
DISCARD_PLANS: DiscardMode
DISCARD_SEQUENCES: DiscardMode
DISCARD_TEMP: DiscardMode
REINDEX_OBJECT_TYPE_UNDEFINED: ReindexObjectType
REINDEX_OBJECT_INDEX: ReindexObjectType
REINDEX_OBJECT_TABLE: ReindexObjectType
REINDEX_OBJECT_SCHEMA: ReindexObjectType
REINDEX_OBJECT_SYSTEM: ReindexObjectType
REINDEX_OBJECT_DATABASE: ReindexObjectType
ALTER_TSCONFIG_TYPE_UNDEFINED: AlterTSConfigType
ALTER_TSCONFIG_ADD_MAPPING: AlterTSConfigType
ALTER_TSCONFIG_ALTER_MAPPING_FOR_TOKEN: AlterTSConfigType
ALTER_TSCONFIG_REPLACE_DICT: AlterTSConfigType
ALTER_TSCONFIG_REPLACE_DICT_FOR_TOKEN: AlterTSConfigType
ALTER_TSCONFIG_DROP_MAPPING: AlterTSConfigType
PUBLICATION_OBJ_SPEC_TYPE_UNDEFINED: PublicationObjSpecType
PUBLICATIONOBJ_TABLE: PublicationObjSpecType
PUBLICATIONOBJ_TABLES_IN_SCHEMA: PublicationObjSpecType
PUBLICATIONOBJ_TABLES_IN_CUR_SCHEMA: PublicationObjSpecType
PUBLICATIONOBJ_CONTINUATION: PublicationObjSpecType
ALTER_PUBLICATION_ACTION_UNDEFINED: AlterPublicationAction
AP_AddObjects: AlterPublicationAction
AP_DropObjects: AlterPublicationAction
AP_SetObjects: AlterPublicationAction
ALTER_SUBSCRIPTION_TYPE_UNDEFINED: AlterSubscriptionType
ALTER_SUBSCRIPTION_OPTIONS: AlterSubscriptionType
ALTER_SUBSCRIPTION_CONNECTION: AlterSubscriptionType
ALTER_SUBSCRIPTION_SET_PUBLICATION: AlterSubscriptionType
ALTER_SUBSCRIPTION_ADD_PUBLICATION: AlterSubscriptionType
ALTER_SUBSCRIPTION_DROP_PUBLICATION: AlterSubscriptionType
ALTER_SUBSCRIPTION_REFRESH: AlterSubscriptionType
ALTER_SUBSCRIPTION_ENABLED: AlterSubscriptionType
ALTER_SUBSCRIPTION_SKIP: AlterSubscriptionType
ON_COMMIT_ACTION_UNDEFINED: OnCommitAction
ONCOMMIT_NOOP: OnCommitAction
ONCOMMIT_PRESERVE_ROWS: OnCommitAction
ONCOMMIT_DELETE_ROWS: OnCommitAction
ONCOMMIT_DROP: OnCommitAction
PARAM_KIND_UNDEFINED: ParamKind
PARAM_EXTERN: ParamKind
PARAM_EXEC: ParamKind
PARAM_SUBLINK: ParamKind
PARAM_MULTIEXPR: ParamKind
COERCION_CONTEXT_UNDEFINED: CoercionContext
COERCION_IMPLICIT: CoercionContext
COERCION_ASSIGNMENT: CoercionContext
COERCION_PLPGSQL: CoercionContext
COERCION_EXPLICIT: CoercionContext
COERCION_FORM_UNDEFINED: CoercionForm
COERCE_EXPLICIT_CALL: CoercionForm
COERCE_EXPLICIT_CAST: CoercionForm
COERCE_IMPLICIT_CAST: CoercionForm
COERCE_SQL_SYNTAX: CoercionForm
BOOL_EXPR_TYPE_UNDEFINED: BoolExprType
AND_EXPR: BoolExprType
OR_EXPR: BoolExprType
NOT_EXPR: BoolExprType
SUB_LINK_TYPE_UNDEFINED: SubLinkType
EXISTS_SUBLINK: SubLinkType
ALL_SUBLINK: SubLinkType
ANY_SUBLINK: SubLinkType
ROWCOMPARE_SUBLINK: SubLinkType
EXPR_SUBLINK: SubLinkType
MULTIEXPR_SUBLINK: SubLinkType
ARRAY_SUBLINK: SubLinkType
CTE_SUBLINK: SubLinkType
ROW_COMPARE_TYPE_UNDEFINED: RowCompareType
ROWCOMPARE_LT: RowCompareType
ROWCOMPARE_LE: RowCompareType
ROWCOMPARE_EQ: RowCompareType
ROWCOMPARE_GE: RowCompareType
ROWCOMPARE_GT: RowCompareType
ROWCOMPARE_NE: RowCompareType
MIN_MAX_OP_UNDEFINED: MinMaxOp
IS_GREATEST: MinMaxOp
IS_LEAST: MinMaxOp
SQLVALUE_FUNCTION_OP_UNDEFINED: SQLValueFunctionOp
SVFOP_CURRENT_DATE: SQLValueFunctionOp
SVFOP_CURRENT_TIME: SQLValueFunctionOp
SVFOP_CURRENT_TIME_N: SQLValueFunctionOp
SVFOP_CURRENT_TIMESTAMP: SQLValueFunctionOp
SVFOP_CURRENT_TIMESTAMP_N: SQLValueFunctionOp
SVFOP_LOCALTIME: SQLValueFunctionOp
SVFOP_LOCALTIME_N: SQLValueFunctionOp
SVFOP_LOCALTIMESTAMP: SQLValueFunctionOp
SVFOP_LOCALTIMESTAMP_N: SQLValueFunctionOp
SVFOP_CURRENT_ROLE: SQLValueFunctionOp
SVFOP_CURRENT_USER: SQLValueFunctionOp
SVFOP_USER: SQLValueFunctionOp
SVFOP_SESSION_USER: SQLValueFunctionOp
SVFOP_CURRENT_CATALOG: SQLValueFunctionOp
SVFOP_CURRENT_SCHEMA: SQLValueFunctionOp
XML_EXPR_OP_UNDEFINED: XmlExprOp
IS_XMLCONCAT: XmlExprOp
IS_XMLELEMENT: XmlExprOp
IS_XMLFOREST: XmlExprOp
IS_XMLPARSE: XmlExprOp
IS_XMLPI: XmlExprOp
IS_XMLROOT: XmlExprOp
IS_XMLSERIALIZE: XmlExprOp
IS_DOCUMENT: XmlExprOp
XML_OPTION_TYPE_UNDEFINED: XmlOptionType
XMLOPTION_DOCUMENT: XmlOptionType
XMLOPTION_CONTENT: XmlOptionType
JSON_ENCODING_UNDEFINED: JsonEncoding
JS_ENC_DEFAULT: JsonEncoding
JS_ENC_UTF8: JsonEncoding
JS_ENC_UTF16: JsonEncoding
JS_ENC_UTF32: JsonEncoding
JSON_FORMAT_TYPE_UNDEFINED: JsonFormatType
JS_FORMAT_DEFAULT: JsonFormatType
JS_FORMAT_JSON: JsonFormatType
JS_FORMAT_JSONB: JsonFormatType
JSON_CONSTRUCTOR_TYPE_UNDEFINED: JsonConstructorType
JSCTOR_JSON_OBJECT: JsonConstructorType
JSCTOR_JSON_ARRAY: JsonConstructorType
JSCTOR_JSON_OBJECTAGG: JsonConstructorType
JSCTOR_JSON_ARRAYAGG: JsonConstructorType
JSON_VALUE_TYPE_UNDEFINED: JsonValueType
JS_TYPE_ANY: JsonValueType
JS_TYPE_OBJECT: JsonValueType
JS_TYPE_ARRAY: JsonValueType
JS_TYPE_SCALAR: JsonValueType
NULL_TEST_TYPE_UNDEFINED: NullTestType
IS_NULL: NullTestType
IS_NOT_NULL: NullTestType
BOOL_TEST_TYPE_UNDEFINED: BoolTestType
IS_TRUE: BoolTestType
IS_NOT_TRUE: BoolTestType
IS_FALSE: BoolTestType
IS_NOT_FALSE: BoolTestType
IS_UNKNOWN: BoolTestType
IS_NOT_UNKNOWN: BoolTestType
CMD_TYPE_UNDEFINED: CmdType
CMD_UNKNOWN: CmdType
CMD_SELECT: CmdType
CMD_UPDATE: CmdType
CMD_INSERT: CmdType
CMD_DELETE: CmdType
CMD_MERGE: CmdType
CMD_UTILITY: CmdType
CMD_NOTHING: CmdType
JOIN_TYPE_UNDEFINED: JoinType
JOIN_INNER: JoinType
JOIN_LEFT: JoinType
JOIN_FULL: JoinType
JOIN_RIGHT: JoinType
JOIN_SEMI: JoinType
JOIN_ANTI: JoinType
JOIN_RIGHT_ANTI: JoinType
JOIN_UNIQUE_OUTER: JoinType
JOIN_UNIQUE_INNER: JoinType
AGG_STRATEGY_UNDEFINED: AggStrategy
AGG_PLAIN: AggStrategy
AGG_SORTED: AggStrategy
AGG_HASHED: AggStrategy
AGG_MIXED: AggStrategy
AGG_SPLIT_UNDEFINED: AggSplit
AGGSPLIT_SIMPLE: AggSplit
AGGSPLIT_INITIAL_SERIAL: AggSplit
AGGSPLIT_FINAL_DESERIAL: AggSplit
SET_OP_CMD_UNDEFINED: SetOpCmd
SETOPCMD_INTERSECT: SetOpCmd
SETOPCMD_INTERSECT_ALL: SetOpCmd
SETOPCMD_EXCEPT: SetOpCmd
SETOPCMD_EXCEPT_ALL: SetOpCmd
SET_OP_STRATEGY_UNDEFINED: SetOpStrategy
SETOP_SORTED: SetOpStrategy
SETOP_HASHED: SetOpStrategy
ON_CONFLICT_ACTION_UNDEFINED: OnConflictAction
ONCONFLICT_NONE: OnConflictAction
ONCONFLICT_NOTHING: OnConflictAction
ONCONFLICT_UPDATE: OnConflictAction
LIMIT_OPTION_UNDEFINED: LimitOption
LIMIT_OPTION_DEFAULT: LimitOption
LIMIT_OPTION_COUNT: LimitOption
LIMIT_OPTION_WITH_TIES: LimitOption
LOCK_CLAUSE_STRENGTH_UNDEFINED: LockClauseStrength
LCS_NONE: LockClauseStrength
LCS_FORKEYSHARE: LockClauseStrength
LCS_FORSHARE: LockClauseStrength
LCS_FORNOKEYUPDATE: LockClauseStrength
LCS_FORUPDATE: LockClauseStrength
LOCK_WAIT_POLICY_UNDEFINED: LockWaitPolicy
LockWaitBlock: LockWaitPolicy
LockWaitSkip: LockWaitPolicy
LockWaitError: LockWaitPolicy
LOCK_TUPLE_MODE_UNDEFINED: LockTupleMode
LockTupleKeyShare: LockTupleMode
LockTupleShare: LockTupleMode
LockTupleNoKeyExclusive: LockTupleMode
LockTupleExclusive: LockTupleMode
NO_KEYWORD: KeywordKind
UNRESERVED_KEYWORD: KeywordKind
COL_NAME_KEYWORD: KeywordKind
TYPE_FUNC_NAME_KEYWORD: KeywordKind
RESERVED_KEYWORD: KeywordKind
NUL: Token
ASCII_36: Token
ASCII_37: Token
ASCII_40: Token
ASCII_41: Token
ASCII_42: Token
ASCII_43: Token
ASCII_44: Token
ASCII_45: Token
ASCII_46: Token
ASCII_47: Token
ASCII_58: Token
ASCII_59: Token
ASCII_60: Token
ASCII_61: Token
ASCII_62: Token
ASCII_63: Token
ASCII_91: Token
ASCII_92: Token
ASCII_93: Token
ASCII_94: Token
IDENT: Token
UIDENT: Token
FCONST: Token
SCONST: Token
USCONST: Token
BCONST: Token
XCONST: Token
Op: Token
ICONST: Token
PARAM: Token
TYPECAST: Token
DOT_DOT: Token
COLON_EQUALS: Token
EQUALS_GREATER: Token
LESS_EQUALS: Token
GREATER_EQUALS: Token
NOT_EQUALS: Token
SQL_COMMENT: Token
C_COMMENT: Token
ABORT_P: Token
ABSENT: Token
ABSOLUTE_P: Token
ACCESS: Token
ACTION: Token
ADD_P: Token
ADMIN: Token
AFTER: Token
AGGREGATE: Token
ALL: Token
ALSO: Token
ALTER: Token
ALWAYS: Token
ANALYSE: Token
ANALYZE: Token
AND: Token
ANY: Token
ARRAY: Token
AS: Token
ASC: Token
ASENSITIVE: Token
ASSERTION: Token
ASSIGNMENT: Token
ASYMMETRIC: Token
ATOMIC: Token
AT: Token
ATTACH: Token
ATTRIBUTE: Token
AUTHORIZATION: Token
BACKWARD: Token
BEFORE: Token
BEGIN_P: Token
BETWEEN: Token
BIGINT: Token
BINARY: Token
BIT: Token
BOOLEAN_P: Token
BOTH: Token
BREADTH: Token
BY: Token
CACHE: Token
CALL: Token
CALLED: Token
CASCADE: Token
CASCADED: Token
CASE: Token
CAST: Token
CATALOG_P: Token
CHAIN: Token
CHAR_P: Token
CHARACTER: Token
CHARACTERISTICS: Token
CHECK: Token
CHECKPOINT: Token
CLASS: Token
CLOSE: Token
CLUSTER: Token
COALESCE: Token
COLLATE: Token
COLLATION: Token
COLUMN: Token
COLUMNS: Token
COMMENT: Token
COMMENTS: Token
COMMIT: Token
COMMITTED: Token
COMPRESSION: Token
CONCURRENTLY: Token
CONFIGURATION: Token
CONFLICT: Token
CONNECTION: Token
CONSTRAINT: Token
CONSTRAINTS: Token
CONTENT_P: Token
CONTINUE_P: Token
CONVERSION_P: Token
COPY: Token
COST: Token
CREATE: Token
CROSS: Token
CSV: Token
CUBE: Token
CURRENT_P: Token
CURRENT_CATALOG: Token
CURRENT_DATE: Token
CURRENT_ROLE: Token
CURRENT_SCHEMA: Token
CURRENT_TIME: Token
CURRENT_TIMESTAMP: Token
CURRENT_USER: Token
CURSOR: Token
CYCLE: Token
DATA_P: Token
DATABASE: Token
DAY_P: Token
DEALLOCATE: Token
DEC: Token
DECIMAL_P: Token
DECLARE: Token
DEFAULT: Token
DEFAULTS: Token
DEFERRABLE: Token
DEFERRED: Token
DEFINER: Token
DELETE_P: Token
DELIMITER: Token
DELIMITERS: Token
DEPENDS: Token
DEPTH: Token
DESC: Token
DETACH: Token
DICTIONARY: Token
DISABLE_P: Token
DISCARD: Token
DISTINCT: Token
DO: Token
DOCUMENT_P: Token
DOMAIN_P: Token
DOUBLE_P: Token
DROP: Token
EACH: Token
ELSE: Token
ENABLE_P: Token
ENCODING: Token
ENCRYPTED: Token
END_P: Token
ENUM_P: Token
ESCAPE: Token
EVENT: Token
EXCEPT: Token
EXCLUDE: Token
EXCLUDING: Token
EXCLUSIVE: Token
EXECUTE: Token
EXISTS: Token
EXPLAIN: Token
EXPRESSION: Token
EXTENSION: Token
EXTERNAL: Token
EXTRACT: Token
FALSE_P: Token
FAMILY: Token
FETCH: Token
FILTER: Token
FINALIZE: Token
FIRST_P: Token
FLOAT_P: Token
FOLLOWING: Token
FOR: Token
FORCE: Token
FOREIGN: Token
FORMAT: Token
FORWARD: Token
FREEZE: Token
FROM: Token
FULL: Token
FUNCTION: Token
FUNCTIONS: Token
GENERATED: Token
GLOBAL: Token
GRANT: Token
GRANTED: Token
GREATEST: Token
GROUP_P: Token
GROUPING: Token
GROUPS: Token
HANDLER: Token
HAVING: Token
HEADER_P: Token
HOLD: Token
HOUR_P: Token
IDENTITY_P: Token
IF_P: Token
ILIKE: Token
IMMEDIATE: Token
IMMUTABLE: Token
IMPLICIT_P: Token
IMPORT_P: Token
IN_P: Token
INCLUDE: Token
INCLUDING: Token
INCREMENT: Token
INDENT: Token
INDEX: Token
INDEXES: Token
INHERIT: Token
INHERITS: Token
INITIALLY: Token
INLINE_P: Token
INNER_P: Token
INOUT: Token
INPUT_P: Token
INSENSITIVE: Token
INSERT: Token
INSTEAD: Token
INT_P: Token
INTEGER: Token
INTERSECT: Token
INTERVAL: Token
INTO: Token
INVOKER: Token
IS: Token
ISNULL: Token
ISOLATION: Token
JOIN: Token
JSON: Token
JSON_ARRAY: Token
JSON_ARRAYAGG: Token
JSON_OBJECT: Token
JSON_OBJECTAGG: Token
KEY: Token
KEYS: Token
LABEL: Token
LANGUAGE: Token
LARGE_P: Token
LAST_P: Token
LATERAL_P: Token
LEADING: Token
LEAKPROOF: Token
LEAST: Token
LEFT: Token
LEVEL: Token
LIKE: Token
LIMIT: Token
LISTEN: Token
LOAD: Token
LOCAL: Token
LOCALTIME: Token
LOCALTIMESTAMP: Token
LOCATION: Token
LOCK_P: Token
LOCKED: Token
LOGGED: Token
MAPPING: Token
MATCH: Token
MATCHED: Token
MATERIALIZED: Token
MAXVALUE: Token
MERGE: Token
METHOD: Token
MINUTE_P: Token
MINVALUE: Token
MODE: Token
MONTH_P: Token
MOVE: Token
NAME_P: Token
NAMES: Token
NATIONAL: Token
NATURAL: Token
NCHAR: Token
NEW: Token
NEXT: Token
NFC: Token
NFD: Token
NFKC: Token
NFKD: Token
NO: Token
NONE: Token
NORMALIZE: Token
NORMALIZED: Token
NOT: Token
NOTHING: Token
NOTIFY: Token
NOTNULL: Token
NOWAIT: Token
NULL_P: Token
NULLIF: Token
NULLS_P: Token
NUMERIC: Token
OBJECT_P: Token
OF: Token
OFF: Token
OFFSET: Token
OIDS: Token
OLD: Token
ON: Token
ONLY: Token
OPERATOR: Token
OPTION: Token
OPTIONS: Token
OR: Token
ORDER: Token
ORDINALITY: Token
OTHERS: Token
OUT_P: Token
OUTER_P: Token
OVER: Token
OVERLAPS: Token
OVERLAY: Token
OVERRIDING: Token
OWNED: Token
OWNER: Token
PARALLEL: Token
PARAMETER: Token
PARSER: Token
PARTIAL: Token
PARTITION: Token
PASSING: Token
PASSWORD: Token
PLACING: Token
PLANS: Token
POLICY: Token
POSITION: Token
PRECEDING: Token
PRECISION: Token
PRESERVE: Token
PREPARE: Token
PREPARED: Token
PRIMARY: Token
PRIOR: Token
PRIVILEGES: Token
PROCEDURAL: Token
PROCEDURE: Token
PROCEDURES: Token
PROGRAM: Token
PUBLICATION: Token
QUOTE: Token
RANGE: Token
READ: Token
REAL: Token
REASSIGN: Token
RECHECK: Token
RECURSIVE: Token
REF_P: Token
REFERENCES: Token
REFERENCING: Token
REFRESH: Token
REINDEX: Token
RELATIVE_P: Token
RELEASE: Token
RENAME: Token
REPEATABLE: Token
REPLACE: Token
REPLICA: Token
RESET: Token
RESTART: Token
RESTRICT: Token
RETURN: Token
RETURNING: Token
RETURNS: Token
REVOKE: Token
RIGHT: Token
ROLE: Token
ROLLBACK: Token
ROLLUP: Token
ROUTINE: Token
ROUTINES: Token
ROW: Token
ROWS: Token
RULE: Token
SAVEPOINT: Token
SCALAR: Token
SCHEMA: Token
SCHEMAS: Token
SCROLL: Token
SEARCH: Token
SECOND_P: Token
SECURITY: Token
SELECT: Token
SEQUENCE: Token
SEQUENCES: Token
SERIALIZABLE: Token
SERVER: Token
SESSION: Token
SESSION_USER: Token
SET: Token
SETS: Token
SETOF: Token
SHARE: Token
SHOW: Token
SIMILAR: Token
SIMPLE: Token
SKIP: Token
SMALLINT: Token
SNAPSHOT: Token
SOME: Token
SQL_P: Token
STABLE: Token
STANDALONE_P: Token
START: Token
STATEMENT: Token
STATISTICS: Token
STDIN: Token
STDOUT: Token
STORAGE: Token
STORED: Token
STRICT_P: Token
STRIP_P: Token
SUBSCRIPTION: Token
SUBSTRING: Token
SUPPORT: Token
SYMMETRIC: Token
SYSID: Token
SYSTEM_P: Token
SYSTEM_USER: Token
TABLE: Token
TABLES: Token
TABLESAMPLE: Token
TABLESPACE: Token
TEMP: Token
TEMPLATE: Token
TEMPORARY: Token
TEXT_P: Token
THEN: Token
TIES: Token
TIME: Token
TIMESTAMP: Token
TO: Token
TRAILING: Token
TRANSACTION: Token
TRANSFORM: Token
TREAT: Token
TRIGGER: Token
TRIM: Token
TRUE_P: Token
TRUNCATE: Token
TRUSTED: Token
TYPE_P: Token
TYPES_P: Token
UESCAPE: Token
UNBOUNDED: Token
UNCOMMITTED: Token
UNENCRYPTED: Token
UNION: Token
UNIQUE: Token
UNKNOWN: Token
UNLISTEN: Token
UNLOGGED: Token
UNTIL: Token
UPDATE: Token
USER: Token
USING: Token
VACUUM: Token
VALID: Token
VALIDATE: Token
VALIDATOR: Token
VALUE_P: Token
VALUES: Token
VARCHAR: Token
VARIADIC: Token
VARYING: Token
VERBOSE: Token
VERSION_P: Token
VIEW: Token
VIEWS: Token
VOLATILE: Token
WHEN: Token
WHERE: Token
WHITESPACE_P: Token
WINDOW: Token
WITH: Token
WITHIN: Token
WITHOUT: Token
WORK: Token
WRAPPER: Token
WRITE: Token
XML_P: Token
XMLATTRIBUTES: Token
XMLCONCAT: Token
XMLELEMENT: Token
XMLEXISTS: Token
XMLFOREST: Token
XMLNAMESPACES: Token
XMLPARSE: Token
XMLPI: Token
XMLROOT: Token
XMLSERIALIZE: Token
XMLTABLE: Token
YEAR_P: Token
YES_P: Token
ZONE: Token
FORMAT_LA: Token
NOT_LA: Token
NULLS_LA: Token
WITH_LA: Token
WITHOUT_LA: Token
MODE_TYPE_NAME: Token
MODE_PLPGSQL_EXPR: Token
MODE_PLPGSQL_ASSIGN1: Token
MODE_PLPGSQL_ASSIGN2: Token
MODE_PLPGSQL_ASSIGN3: Token
UMINUS: Token

class ParseResult(_message.Message):
    __slots__ = ("version", "stmts")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    STMTS_FIELD_NUMBER: _ClassVar[int]
    version: int
    stmts: _containers.RepeatedCompositeFieldContainer[RawStmt]
    def __init__(
        self, version: _Optional[int] = ..., stmts: _Optional[_Iterable[_Union[RawStmt, _Mapping]]] = ...
    ) -> None: ...

class ScanResult(_message.Message):
    __slots__ = ("version", "tokens")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    version: int
    tokens: _containers.RepeatedCompositeFieldContainer[ScanToken]
    def __init__(
        self, version: _Optional[int] = ..., tokens: _Optional[_Iterable[_Union[ScanToken, _Mapping]]] = ...
    ) -> None: ...

class Node(_message.Message):
    __slots__ = (
        "alias",
        "range_var",
        "table_func",
        "into_clause",
        "var",
        "param",
        "aggref",
        "grouping_func",
        "window_func",
        "subscripting_ref",
        "func_expr",
        "named_arg_expr",
        "op_expr",
        "distinct_expr",
        "null_if_expr",
        "scalar_array_op_expr",
        "bool_expr",
        "sub_link",
        "sub_plan",
        "alternative_sub_plan",
        "field_select",
        "field_store",
        "relabel_type",
        "coerce_via_io",
        "array_coerce_expr",
        "convert_rowtype_expr",
        "collate_expr",
        "case_expr",
        "case_when",
        "case_test_expr",
        "array_expr",
        "row_expr",
        "row_compare_expr",
        "coalesce_expr",
        "min_max_expr",
        "sqlvalue_function",
        "xml_expr",
        "json_format",
        "json_returning",
        "json_value_expr",
        "json_constructor_expr",
        "json_is_predicate",
        "null_test",
        "boolean_test",
        "coerce_to_domain",
        "coerce_to_domain_value",
        "set_to_default",
        "current_of_expr",
        "next_value_expr",
        "inference_elem",
        "target_entry",
        "range_tbl_ref",
        "join_expr",
        "from_expr",
        "on_conflict_expr",
        "query",
        "type_name",
        "column_ref",
        "param_ref",
        "a_expr",
        "type_cast",
        "collate_clause",
        "role_spec",
        "func_call",
        "a_star",
        "a_indices",
        "a_indirection",
        "a_array_expr",
        "res_target",
        "multi_assign_ref",
        "sort_by",
        "window_def",
        "range_subselect",
        "range_function",
        "range_table_func",
        "range_table_func_col",
        "range_table_sample",
        "column_def",
        "table_like_clause",
        "index_elem",
        "def_elem",
        "locking_clause",
        "xml_serialize",
        "partition_elem",
        "partition_spec",
        "partition_bound_spec",
        "partition_range_datum",
        "partition_cmd",
        "range_tbl_entry",
        "rtepermission_info",
        "range_tbl_function",
        "table_sample_clause",
        "with_check_option",
        "sort_group_clause",
        "grouping_set",
        "window_clause",
        "row_mark_clause",
        "with_clause",
        "infer_clause",
        "on_conflict_clause",
        "ctesearch_clause",
        "ctecycle_clause",
        "common_table_expr",
        "merge_when_clause",
        "merge_action",
        "trigger_transition",
        "json_output",
        "json_key_value",
        "json_object_constructor",
        "json_array_constructor",
        "json_array_query_constructor",
        "json_agg_constructor",
        "json_object_agg",
        "json_array_agg",
        "raw_stmt",
        "insert_stmt",
        "delete_stmt",
        "update_stmt",
        "merge_stmt",
        "select_stmt",
        "set_operation_stmt",
        "return_stmt",
        "plassign_stmt",
        "create_schema_stmt",
        "alter_table_stmt",
        "replica_identity_stmt",
        "alter_table_cmd",
        "alter_collation_stmt",
        "alter_domain_stmt",
        "grant_stmt",
        "object_with_args",
        "access_priv",
        "grant_role_stmt",
        "alter_default_privileges_stmt",
        "copy_stmt",
        "variable_set_stmt",
        "variable_show_stmt",
        "create_stmt",
        "constraint",
        "create_table_space_stmt",
        "drop_table_space_stmt",
        "alter_table_space_options_stmt",
        "alter_table_move_all_stmt",
        "create_extension_stmt",
        "alter_extension_stmt",
        "alter_extension_contents_stmt",
        "create_fdw_stmt",
        "alter_fdw_stmt",
        "create_foreign_server_stmt",
        "alter_foreign_server_stmt",
        "create_foreign_table_stmt",
        "create_user_mapping_stmt",
        "alter_user_mapping_stmt",
        "drop_user_mapping_stmt",
        "import_foreign_schema_stmt",
        "create_policy_stmt",
        "alter_policy_stmt",
        "create_am_stmt",
        "create_trig_stmt",
        "create_event_trig_stmt",
        "alter_event_trig_stmt",
        "create_plang_stmt",
        "create_role_stmt",
        "alter_role_stmt",
        "alter_role_set_stmt",
        "drop_role_stmt",
        "create_seq_stmt",
        "alter_seq_stmt",
        "define_stmt",
        "create_domain_stmt",
        "create_op_class_stmt",
        "create_op_class_item",
        "create_op_family_stmt",
        "alter_op_family_stmt",
        "drop_stmt",
        "truncate_stmt",
        "comment_stmt",
        "sec_label_stmt",
        "declare_cursor_stmt",
        "close_portal_stmt",
        "fetch_stmt",
        "index_stmt",
        "create_stats_stmt",
        "stats_elem",
        "alter_stats_stmt",
        "create_function_stmt",
        "function_parameter",
        "alter_function_stmt",
        "do_stmt",
        "inline_code_block",
        "call_stmt",
        "call_context",
        "rename_stmt",
        "alter_object_depends_stmt",
        "alter_object_schema_stmt",
        "alter_owner_stmt",
        "alter_operator_stmt",
        "alter_type_stmt",
        "rule_stmt",
        "notify_stmt",
        "listen_stmt",
        "unlisten_stmt",
        "transaction_stmt",
        "composite_type_stmt",
        "create_enum_stmt",
        "create_range_stmt",
        "alter_enum_stmt",
        "view_stmt",
        "load_stmt",
        "createdb_stmt",
        "alter_database_stmt",
        "alter_database_refresh_coll_stmt",
        "alter_database_set_stmt",
        "dropdb_stmt",
        "alter_system_stmt",
        "cluster_stmt",
        "vacuum_stmt",
        "vacuum_relation",
        "explain_stmt",
        "create_table_as_stmt",
        "refresh_mat_view_stmt",
        "check_point_stmt",
        "discard_stmt",
        "lock_stmt",
        "constraints_set_stmt",
        "reindex_stmt",
        "create_conversion_stmt",
        "create_cast_stmt",
        "create_transform_stmt",
        "prepare_stmt",
        "execute_stmt",
        "deallocate_stmt",
        "drop_owned_stmt",
        "reassign_owned_stmt",
        "alter_tsdictionary_stmt",
        "alter_tsconfiguration_stmt",
        "publication_table",
        "publication_obj_spec",
        "create_publication_stmt",
        "alter_publication_stmt",
        "create_subscription_stmt",
        "alter_subscription_stmt",
        "drop_subscription_stmt",
        "integer",
        "float",
        "boolean",
        "string",
        "bit_string",
        "list",
        "int_list",
        "oid_list",
        "a_const",
    )
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    RANGE_VAR_FIELD_NUMBER: _ClassVar[int]
    TABLE_FUNC_FIELD_NUMBER: _ClassVar[int]
    INTO_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    VAR_FIELD_NUMBER: _ClassVar[int]
    PARAM_FIELD_NUMBER: _ClassVar[int]
    AGGREF_FIELD_NUMBER: _ClassVar[int]
    GROUPING_FUNC_FIELD_NUMBER: _ClassVar[int]
    WINDOW_FUNC_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTING_REF_FIELD_NUMBER: _ClassVar[int]
    FUNC_EXPR_FIELD_NUMBER: _ClassVar[int]
    NAMED_ARG_EXPR_FIELD_NUMBER: _ClassVar[int]
    OP_EXPR_FIELD_NUMBER: _ClassVar[int]
    DISTINCT_EXPR_FIELD_NUMBER: _ClassVar[int]
    NULL_IF_EXPR_FIELD_NUMBER: _ClassVar[int]
    SCALAR_ARRAY_OP_EXPR_FIELD_NUMBER: _ClassVar[int]
    BOOL_EXPR_FIELD_NUMBER: _ClassVar[int]
    SUB_LINK_FIELD_NUMBER: _ClassVar[int]
    SUB_PLAN_FIELD_NUMBER: _ClassVar[int]
    ALTERNATIVE_SUB_PLAN_FIELD_NUMBER: _ClassVar[int]
    FIELD_SELECT_FIELD_NUMBER: _ClassVar[int]
    FIELD_STORE_FIELD_NUMBER: _ClassVar[int]
    RELABEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    COERCE_VIA_IO_FIELD_NUMBER: _ClassVar[int]
    ARRAY_COERCE_EXPR_FIELD_NUMBER: _ClassVar[int]
    CONVERT_ROWTYPE_EXPR_FIELD_NUMBER: _ClassVar[int]
    COLLATE_EXPR_FIELD_NUMBER: _ClassVar[int]
    CASE_EXPR_FIELD_NUMBER: _ClassVar[int]
    CASE_WHEN_FIELD_NUMBER: _ClassVar[int]
    CASE_TEST_EXPR_FIELD_NUMBER: _ClassVar[int]
    ARRAY_EXPR_FIELD_NUMBER: _ClassVar[int]
    ROW_EXPR_FIELD_NUMBER: _ClassVar[int]
    ROW_COMPARE_EXPR_FIELD_NUMBER: _ClassVar[int]
    COALESCE_EXPR_FIELD_NUMBER: _ClassVar[int]
    MIN_MAX_EXPR_FIELD_NUMBER: _ClassVar[int]
    SQLVALUE_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    XML_EXPR_FIELD_NUMBER: _ClassVar[int]
    JSON_FORMAT_FIELD_NUMBER: _ClassVar[int]
    JSON_RETURNING_FIELD_NUMBER: _ClassVar[int]
    JSON_VALUE_EXPR_FIELD_NUMBER: _ClassVar[int]
    JSON_CONSTRUCTOR_EXPR_FIELD_NUMBER: _ClassVar[int]
    JSON_IS_PREDICATE_FIELD_NUMBER: _ClassVar[int]
    NULL_TEST_FIELD_NUMBER: _ClassVar[int]
    BOOLEAN_TEST_FIELD_NUMBER: _ClassVar[int]
    COERCE_TO_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    COERCE_TO_DOMAIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    SET_TO_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    CURRENT_OF_EXPR_FIELD_NUMBER: _ClassVar[int]
    NEXT_VALUE_EXPR_FIELD_NUMBER: _ClassVar[int]
    INFERENCE_ELEM_FIELD_NUMBER: _ClassVar[int]
    TARGET_ENTRY_FIELD_NUMBER: _ClassVar[int]
    RANGE_TBL_REF_FIELD_NUMBER: _ClassVar[int]
    JOIN_EXPR_FIELD_NUMBER: _ClassVar[int]
    FROM_EXPR_FIELD_NUMBER: _ClassVar[int]
    ON_CONFLICT_EXPR_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    COLUMN_REF_FIELD_NUMBER: _ClassVar[int]
    PARAM_REF_FIELD_NUMBER: _ClassVar[int]
    A_EXPR_FIELD_NUMBER: _ClassVar[int]
    TYPE_CAST_FIELD_NUMBER: _ClassVar[int]
    COLLATE_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    ROLE_SPEC_FIELD_NUMBER: _ClassVar[int]
    FUNC_CALL_FIELD_NUMBER: _ClassVar[int]
    A_STAR_FIELD_NUMBER: _ClassVar[int]
    A_INDICES_FIELD_NUMBER: _ClassVar[int]
    A_INDIRECTION_FIELD_NUMBER: _ClassVar[int]
    A_ARRAY_EXPR_FIELD_NUMBER: _ClassVar[int]
    RES_TARGET_FIELD_NUMBER: _ClassVar[int]
    MULTI_ASSIGN_REF_FIELD_NUMBER: _ClassVar[int]
    SORT_BY_FIELD_NUMBER: _ClassVar[int]
    WINDOW_DEF_FIELD_NUMBER: _ClassVar[int]
    RANGE_SUBSELECT_FIELD_NUMBER: _ClassVar[int]
    RANGE_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    RANGE_TABLE_FUNC_FIELD_NUMBER: _ClassVar[int]
    RANGE_TABLE_FUNC_COL_FIELD_NUMBER: _ClassVar[int]
    RANGE_TABLE_SAMPLE_FIELD_NUMBER: _ClassVar[int]
    COLUMN_DEF_FIELD_NUMBER: _ClassVar[int]
    TABLE_LIKE_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    INDEX_ELEM_FIELD_NUMBER: _ClassVar[int]
    DEF_ELEM_FIELD_NUMBER: _ClassVar[int]
    LOCKING_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    XML_SERIALIZE_FIELD_NUMBER: _ClassVar[int]
    PARTITION_ELEM_FIELD_NUMBER: _ClassVar[int]
    PARTITION_SPEC_FIELD_NUMBER: _ClassVar[int]
    PARTITION_BOUND_SPEC_FIELD_NUMBER: _ClassVar[int]
    PARTITION_RANGE_DATUM_FIELD_NUMBER: _ClassVar[int]
    PARTITION_CMD_FIELD_NUMBER: _ClassVar[int]
    RANGE_TBL_ENTRY_FIELD_NUMBER: _ClassVar[int]
    RTEPERMISSION_INFO_FIELD_NUMBER: _ClassVar[int]
    RANGE_TBL_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    TABLE_SAMPLE_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    WITH_CHECK_OPTION_FIELD_NUMBER: _ClassVar[int]
    SORT_GROUP_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    GROUPING_SET_FIELD_NUMBER: _ClassVar[int]
    WINDOW_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    ROW_MARK_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    WITH_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    INFER_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    ON_CONFLICT_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    CTESEARCH_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    CTECYCLE_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    COMMON_TABLE_EXPR_FIELD_NUMBER: _ClassVar[int]
    MERGE_WHEN_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    MERGE_ACTION_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_TRANSITION_FIELD_NUMBER: _ClassVar[int]
    JSON_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    JSON_KEY_VALUE_FIELD_NUMBER: _ClassVar[int]
    JSON_OBJECT_CONSTRUCTOR_FIELD_NUMBER: _ClassVar[int]
    JSON_ARRAY_CONSTRUCTOR_FIELD_NUMBER: _ClassVar[int]
    JSON_ARRAY_QUERY_CONSTRUCTOR_FIELD_NUMBER: _ClassVar[int]
    JSON_AGG_CONSTRUCTOR_FIELD_NUMBER: _ClassVar[int]
    JSON_OBJECT_AGG_FIELD_NUMBER: _ClassVar[int]
    JSON_ARRAY_AGG_FIELD_NUMBER: _ClassVar[int]
    RAW_STMT_FIELD_NUMBER: _ClassVar[int]
    INSERT_STMT_FIELD_NUMBER: _ClassVar[int]
    DELETE_STMT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_STMT_FIELD_NUMBER: _ClassVar[int]
    MERGE_STMT_FIELD_NUMBER: _ClassVar[int]
    SELECT_STMT_FIELD_NUMBER: _ClassVar[int]
    SET_OPERATION_STMT_FIELD_NUMBER: _ClassVar[int]
    RETURN_STMT_FIELD_NUMBER: _ClassVar[int]
    PLASSIGN_STMT_FIELD_NUMBER: _ClassVar[int]
    CREATE_SCHEMA_STMT_FIELD_NUMBER: _ClassVar[int]
    ALTER_TABLE_STMT_FIELD_NUMBER: _ClassVar[int]
    REPLICA_IDENTITY_STMT_FIELD_NUMBER: _ClassVar[int]
    ALTER_TABLE_CMD_FIELD_NUMBER: _ClassVar[int]
    ALTER_COLLATION_STMT_FIELD_NUMBER: _ClassVar[int]
    ALTER_DOMAIN_STMT_FIELD_NUMBER: _ClassVar[int]
    GRANT_STMT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_WITH_ARGS_FIELD_NUMBER: _ClassVar[int]
    ACCESS_PRIV_FIELD_NUMBER: _ClassVar[int]
    GRANT_ROLE_STMT_FIELD_NUMBER: _ClassVar[int]
    ALTER_DEFAULT_PRIVILEGES_STMT_FIELD_NUMBER: _ClassVar[int]
    COPY_STMT_FIELD_NUMBER: _ClassVar[int]
    VARIABLE_SET_STMT_FIELD_NUMBER: _ClassVar[int]
    VARIABLE_SHOW_STMT_FIELD_NUMBER: _ClassVar[int]
    CREATE_STMT_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TABLE_SPACE_STMT_FIELD_NUMBER: _ClassVar[int]
    DROP_TABLE_SPACE_STMT_FIELD_NUMBER: _ClassVar[int]
    ALTER_TABLE_SPACE_OPTIONS_STMT_FIELD_NUMBER: _ClassVar[int]
    ALTER_TABLE_MOVE_ALL_STMT_FIELD_NUMBER: _ClassVar[int]
    CREATE_EXTENSION_STMT_FIELD_NUMBER: _ClassVar[int]
    ALTER_EXTENSION_STMT_FIELD_NUMBER: _ClassVar[int]
    ALTER_EXTENSION_CONTENTS_STMT_FIELD_NUMBER: _ClassVar[int]
    CREATE_FDW_STMT_FIELD_NUMBER: _ClassVar[int]
    ALTER_FDW_STMT_FIELD_NUMBER: _ClassVar[int]
    CREATE_FOREIGN_SERVER_STMT_FIELD_NUMBER: _ClassVar[int]
    ALTER_FOREIGN_SERVER_STMT_FIELD_NUMBER: _ClassVar[int]
    CREATE_FOREIGN_TABLE_STMT_FIELD_NUMBER: _ClassVar[int]
    CREATE_USER_MAPPING_STMT_FIELD_NUMBER: _ClassVar[int]
    ALTER_USER_MAPPING_STMT_FIELD_NUMBER: _ClassVar[int]
    DROP_USER_MAPPING_STMT_FIELD_NUMBER: _ClassVar[int]
    IMPORT_FOREIGN_SCHEMA_STMT_FIELD_NUMBER: _ClassVar[int]
    CREATE_POLICY_STMT_FIELD_NUMBER: _ClassVar[int]
    ALTER_POLICY_STMT_FIELD_NUMBER: _ClassVar[int]
    CREATE_AM_STMT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TRIG_STMT_FIELD_NUMBER: _ClassVar[int]
    CREATE_EVENT_TRIG_STMT_FIELD_NUMBER: _ClassVar[int]
    ALTER_EVENT_TRIG_STMT_FIELD_NUMBER: _ClassVar[int]
    CREATE_PLANG_STMT_FIELD_NUMBER: _ClassVar[int]
    CREATE_ROLE_STMT_FIELD_NUMBER: _ClassVar[int]
    ALTER_ROLE_STMT_FIELD_NUMBER: _ClassVar[int]
    ALTER_ROLE_SET_STMT_FIELD_NUMBER: _ClassVar[int]
    DROP_ROLE_STMT_FIELD_NUMBER: _ClassVar[int]
    CREATE_SEQ_STMT_FIELD_NUMBER: _ClassVar[int]
    ALTER_SEQ_STMT_FIELD_NUMBER: _ClassVar[int]
    DEFINE_STMT_FIELD_NUMBER: _ClassVar[int]
    CREATE_DOMAIN_STMT_FIELD_NUMBER: _ClassVar[int]
    CREATE_OP_CLASS_STMT_FIELD_NUMBER: _ClassVar[int]
    CREATE_OP_CLASS_ITEM_FIELD_NUMBER: _ClassVar[int]
    CREATE_OP_FAMILY_STMT_FIELD_NUMBER: _ClassVar[int]
    ALTER_OP_FAMILY_STMT_FIELD_NUMBER: _ClassVar[int]
    DROP_STMT_FIELD_NUMBER: _ClassVar[int]
    TRUNCATE_STMT_FIELD_NUMBER: _ClassVar[int]
    COMMENT_STMT_FIELD_NUMBER: _ClassVar[int]
    SEC_LABEL_STMT_FIELD_NUMBER: _ClassVar[int]
    DECLARE_CURSOR_STMT_FIELD_NUMBER: _ClassVar[int]
    CLOSE_PORTAL_STMT_FIELD_NUMBER: _ClassVar[int]
    FETCH_STMT_FIELD_NUMBER: _ClassVar[int]
    INDEX_STMT_FIELD_NUMBER: _ClassVar[int]
    CREATE_STATS_STMT_FIELD_NUMBER: _ClassVar[int]
    STATS_ELEM_FIELD_NUMBER: _ClassVar[int]
    ALTER_STATS_STMT_FIELD_NUMBER: _ClassVar[int]
    CREATE_FUNCTION_STMT_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_PARAMETER_FIELD_NUMBER: _ClassVar[int]
    ALTER_FUNCTION_STMT_FIELD_NUMBER: _ClassVar[int]
    DO_STMT_FIELD_NUMBER: _ClassVar[int]
    INLINE_CODE_BLOCK_FIELD_NUMBER: _ClassVar[int]
    CALL_STMT_FIELD_NUMBER: _ClassVar[int]
    CALL_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    RENAME_STMT_FIELD_NUMBER: _ClassVar[int]
    ALTER_OBJECT_DEPENDS_STMT_FIELD_NUMBER: _ClassVar[int]
    ALTER_OBJECT_SCHEMA_STMT_FIELD_NUMBER: _ClassVar[int]
    ALTER_OWNER_STMT_FIELD_NUMBER: _ClassVar[int]
    ALTER_OPERATOR_STMT_FIELD_NUMBER: _ClassVar[int]
    ALTER_TYPE_STMT_FIELD_NUMBER: _ClassVar[int]
    RULE_STMT_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_STMT_FIELD_NUMBER: _ClassVar[int]
    LISTEN_STMT_FIELD_NUMBER: _ClassVar[int]
    UNLISTEN_STMT_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_STMT_FIELD_NUMBER: _ClassVar[int]
    COMPOSITE_TYPE_STMT_FIELD_NUMBER: _ClassVar[int]
    CREATE_ENUM_STMT_FIELD_NUMBER: _ClassVar[int]
    CREATE_RANGE_STMT_FIELD_NUMBER: _ClassVar[int]
    ALTER_ENUM_STMT_FIELD_NUMBER: _ClassVar[int]
    VIEW_STMT_FIELD_NUMBER: _ClassVar[int]
    LOAD_STMT_FIELD_NUMBER: _ClassVar[int]
    CREATEDB_STMT_FIELD_NUMBER: _ClassVar[int]
    ALTER_DATABASE_STMT_FIELD_NUMBER: _ClassVar[int]
    ALTER_DATABASE_REFRESH_COLL_STMT_FIELD_NUMBER: _ClassVar[int]
    ALTER_DATABASE_SET_STMT_FIELD_NUMBER: _ClassVar[int]
    DROPDB_STMT_FIELD_NUMBER: _ClassVar[int]
    ALTER_SYSTEM_STMT_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_STMT_FIELD_NUMBER: _ClassVar[int]
    VACUUM_STMT_FIELD_NUMBER: _ClassVar[int]
    VACUUM_RELATION_FIELD_NUMBER: _ClassVar[int]
    EXPLAIN_STMT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TABLE_AS_STMT_FIELD_NUMBER: _ClassVar[int]
    REFRESH_MAT_VIEW_STMT_FIELD_NUMBER: _ClassVar[int]
    CHECK_POINT_STMT_FIELD_NUMBER: _ClassVar[int]
    DISCARD_STMT_FIELD_NUMBER: _ClassVar[int]
    LOCK_STMT_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_SET_STMT_FIELD_NUMBER: _ClassVar[int]
    REINDEX_STMT_FIELD_NUMBER: _ClassVar[int]
    CREATE_CONVERSION_STMT_FIELD_NUMBER: _ClassVar[int]
    CREATE_CAST_STMT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TRANSFORM_STMT_FIELD_NUMBER: _ClassVar[int]
    PREPARE_STMT_FIELD_NUMBER: _ClassVar[int]
    EXECUTE_STMT_FIELD_NUMBER: _ClassVar[int]
    DEALLOCATE_STMT_FIELD_NUMBER: _ClassVar[int]
    DROP_OWNED_STMT_FIELD_NUMBER: _ClassVar[int]
    REASSIGN_OWNED_STMT_FIELD_NUMBER: _ClassVar[int]
    ALTER_TSDICTIONARY_STMT_FIELD_NUMBER: _ClassVar[int]
    ALTER_TSCONFIGURATION_STMT_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_TABLE_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_OBJ_SPEC_FIELD_NUMBER: _ClassVar[int]
    CREATE_PUBLICATION_STMT_FIELD_NUMBER: _ClassVar[int]
    ALTER_PUBLICATION_STMT_FIELD_NUMBER: _ClassVar[int]
    CREATE_SUBSCRIPTION_STMT_FIELD_NUMBER: _ClassVar[int]
    ALTER_SUBSCRIPTION_STMT_FIELD_NUMBER: _ClassVar[int]
    DROP_SUBSCRIPTION_STMT_FIELD_NUMBER: _ClassVar[int]
    INTEGER_FIELD_NUMBER: _ClassVar[int]
    FLOAT_FIELD_NUMBER: _ClassVar[int]
    BOOLEAN_FIELD_NUMBER: _ClassVar[int]
    STRING_FIELD_NUMBER: _ClassVar[int]
    BIT_STRING_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    INT_LIST_FIELD_NUMBER: _ClassVar[int]
    OID_LIST_FIELD_NUMBER: _ClassVar[int]
    A_CONST_FIELD_NUMBER: _ClassVar[int]
    alias: Alias
    range_var: RangeVar
    table_func: TableFunc
    into_clause: IntoClause
    var: Var
    param: Param
    aggref: Aggref
    grouping_func: GroupingFunc
    window_func: WindowFunc
    subscripting_ref: SubscriptingRef
    func_expr: FuncExpr
    named_arg_expr: NamedArgExpr
    op_expr: OpExpr
    distinct_expr: DistinctExpr
    null_if_expr: NullIfExpr
    scalar_array_op_expr: ScalarArrayOpExpr
    bool_expr: BoolExpr
    sub_link: SubLink
    sub_plan: SubPlan
    alternative_sub_plan: AlternativeSubPlan
    field_select: FieldSelect
    field_store: FieldStore
    relabel_type: RelabelType
    coerce_via_io: CoerceViaIO
    array_coerce_expr: ArrayCoerceExpr
    convert_rowtype_expr: ConvertRowtypeExpr
    collate_expr: CollateExpr
    case_expr: CaseExpr
    case_when: CaseWhen
    case_test_expr: CaseTestExpr
    array_expr: ArrayExpr
    row_expr: RowExpr
    row_compare_expr: RowCompareExpr
    coalesce_expr: CoalesceExpr
    min_max_expr: MinMaxExpr
    sqlvalue_function: SQLValueFunction
    xml_expr: XmlExpr
    json_format: JsonFormat
    json_returning: JsonReturning
    json_value_expr: JsonValueExpr
    json_constructor_expr: JsonConstructorExpr
    json_is_predicate: JsonIsPredicate
    null_test: NullTest
    boolean_test: BooleanTest
    coerce_to_domain: CoerceToDomain
    coerce_to_domain_value: CoerceToDomainValue
    set_to_default: SetToDefault
    current_of_expr: CurrentOfExpr
    next_value_expr: NextValueExpr
    inference_elem: InferenceElem
    target_entry: TargetEntry
    range_tbl_ref: RangeTblRef
    join_expr: JoinExpr
    from_expr: FromExpr
    on_conflict_expr: OnConflictExpr
    query: Query
    type_name: TypeName
    column_ref: ColumnRef
    param_ref: ParamRef
    a_expr: A_Expr
    type_cast: TypeCast
    collate_clause: CollateClause
    role_spec: RoleSpec
    func_call: FuncCall
    a_star: A_Star
    a_indices: A_Indices
    a_indirection: A_Indirection
    a_array_expr: A_ArrayExpr
    res_target: ResTarget
    multi_assign_ref: MultiAssignRef
    sort_by: SortBy
    window_def: WindowDef
    range_subselect: RangeSubselect
    range_function: RangeFunction
    range_table_func: RangeTableFunc
    range_table_func_col: RangeTableFuncCol
    range_table_sample: RangeTableSample
    column_def: ColumnDef
    table_like_clause: TableLikeClause
    index_elem: IndexElem
    def_elem: DefElem
    locking_clause: LockingClause
    xml_serialize: XmlSerialize
    partition_elem: PartitionElem
    partition_spec: PartitionSpec
    partition_bound_spec: PartitionBoundSpec
    partition_range_datum: PartitionRangeDatum
    partition_cmd: PartitionCmd
    range_tbl_entry: RangeTblEntry
    rtepermission_info: RTEPermissionInfo
    range_tbl_function: RangeTblFunction
    table_sample_clause: TableSampleClause
    with_check_option: WithCheckOption
    sort_group_clause: SortGroupClause
    grouping_set: GroupingSet
    window_clause: WindowClause
    row_mark_clause: RowMarkClause
    with_clause: WithClause
    infer_clause: InferClause
    on_conflict_clause: OnConflictClause
    ctesearch_clause: CTESearchClause
    ctecycle_clause: CTECycleClause
    common_table_expr: CommonTableExpr
    merge_when_clause: MergeWhenClause
    merge_action: MergeAction
    trigger_transition: TriggerTransition
    json_output: JsonOutput
    json_key_value: JsonKeyValue
    json_object_constructor: JsonObjectConstructor
    json_array_constructor: JsonArrayConstructor
    json_array_query_constructor: JsonArrayQueryConstructor
    json_agg_constructor: JsonAggConstructor
    json_object_agg: JsonObjectAgg
    json_array_agg: JsonArrayAgg
    raw_stmt: RawStmt
    insert_stmt: InsertStmt
    delete_stmt: DeleteStmt
    update_stmt: UpdateStmt
    merge_stmt: MergeStmt
    select_stmt: SelectStmt
    set_operation_stmt: SetOperationStmt
    return_stmt: ReturnStmt
    plassign_stmt: PLAssignStmt
    create_schema_stmt: CreateSchemaStmt
    alter_table_stmt: AlterTableStmt
    replica_identity_stmt: ReplicaIdentityStmt
    alter_table_cmd: AlterTableCmd
    alter_collation_stmt: AlterCollationStmt
    alter_domain_stmt: AlterDomainStmt
    grant_stmt: GrantStmt
    object_with_args: ObjectWithArgs
    access_priv: AccessPriv
    grant_role_stmt: GrantRoleStmt
    alter_default_privileges_stmt: AlterDefaultPrivilegesStmt
    copy_stmt: CopyStmt
    variable_set_stmt: VariableSetStmt
    variable_show_stmt: VariableShowStmt
    create_stmt: CreateStmt
    constraint: Constraint
    create_table_space_stmt: CreateTableSpaceStmt
    drop_table_space_stmt: DropTableSpaceStmt
    alter_table_space_options_stmt: AlterTableSpaceOptionsStmt
    alter_table_move_all_stmt: AlterTableMoveAllStmt
    create_extension_stmt: CreateExtensionStmt
    alter_extension_stmt: AlterExtensionStmt
    alter_extension_contents_stmt: AlterExtensionContentsStmt
    create_fdw_stmt: CreateFdwStmt
    alter_fdw_stmt: AlterFdwStmt
    create_foreign_server_stmt: CreateForeignServerStmt
    alter_foreign_server_stmt: AlterForeignServerStmt
    create_foreign_table_stmt: CreateForeignTableStmt
    create_user_mapping_stmt: CreateUserMappingStmt
    alter_user_mapping_stmt: AlterUserMappingStmt
    drop_user_mapping_stmt: DropUserMappingStmt
    import_foreign_schema_stmt: ImportForeignSchemaStmt
    create_policy_stmt: CreatePolicyStmt
    alter_policy_stmt: AlterPolicyStmt
    create_am_stmt: CreateAmStmt
    create_trig_stmt: CreateTrigStmt
    create_event_trig_stmt: CreateEventTrigStmt
    alter_event_trig_stmt: AlterEventTrigStmt
    create_plang_stmt: CreatePLangStmt
    create_role_stmt: CreateRoleStmt
    alter_role_stmt: AlterRoleStmt
    alter_role_set_stmt: AlterRoleSetStmt
    drop_role_stmt: DropRoleStmt
    create_seq_stmt: CreateSeqStmt
    alter_seq_stmt: AlterSeqStmt
    define_stmt: DefineStmt
    create_domain_stmt: CreateDomainStmt
    create_op_class_stmt: CreateOpClassStmt
    create_op_class_item: CreateOpClassItem
    create_op_family_stmt: CreateOpFamilyStmt
    alter_op_family_stmt: AlterOpFamilyStmt
    drop_stmt: DropStmt
    truncate_stmt: TruncateStmt
    comment_stmt: CommentStmt
    sec_label_stmt: SecLabelStmt
    declare_cursor_stmt: DeclareCursorStmt
    close_portal_stmt: ClosePortalStmt
    fetch_stmt: FetchStmt
    index_stmt: IndexStmt
    create_stats_stmt: CreateStatsStmt
    stats_elem: StatsElem
    alter_stats_stmt: AlterStatsStmt
    create_function_stmt: CreateFunctionStmt
    function_parameter: FunctionParameter
    alter_function_stmt: AlterFunctionStmt
    do_stmt: DoStmt
    inline_code_block: InlineCodeBlock
    call_stmt: CallStmt
    call_context: CallContext
    rename_stmt: RenameStmt
    alter_object_depends_stmt: AlterObjectDependsStmt
    alter_object_schema_stmt: AlterObjectSchemaStmt
    alter_owner_stmt: AlterOwnerStmt
    alter_operator_stmt: AlterOperatorStmt
    alter_type_stmt: AlterTypeStmt
    rule_stmt: RuleStmt
    notify_stmt: NotifyStmt
    listen_stmt: ListenStmt
    unlisten_stmt: UnlistenStmt
    transaction_stmt: TransactionStmt
    composite_type_stmt: CompositeTypeStmt
    create_enum_stmt: CreateEnumStmt
    create_range_stmt: CreateRangeStmt
    alter_enum_stmt: AlterEnumStmt
    view_stmt: ViewStmt
    load_stmt: LoadStmt
    createdb_stmt: CreatedbStmt
    alter_database_stmt: AlterDatabaseStmt
    alter_database_refresh_coll_stmt: AlterDatabaseRefreshCollStmt
    alter_database_set_stmt: AlterDatabaseSetStmt
    dropdb_stmt: DropdbStmt
    alter_system_stmt: AlterSystemStmt
    cluster_stmt: ClusterStmt
    vacuum_stmt: VacuumStmt
    vacuum_relation: VacuumRelation
    explain_stmt: ExplainStmt
    create_table_as_stmt: CreateTableAsStmt
    refresh_mat_view_stmt: RefreshMatViewStmt
    check_point_stmt: CheckPointStmt
    discard_stmt: DiscardStmt
    lock_stmt: LockStmt
    constraints_set_stmt: ConstraintsSetStmt
    reindex_stmt: ReindexStmt
    create_conversion_stmt: CreateConversionStmt
    create_cast_stmt: CreateCastStmt
    create_transform_stmt: CreateTransformStmt
    prepare_stmt: PrepareStmt
    execute_stmt: ExecuteStmt
    deallocate_stmt: DeallocateStmt
    drop_owned_stmt: DropOwnedStmt
    reassign_owned_stmt: ReassignOwnedStmt
    alter_tsdictionary_stmt: AlterTSDictionaryStmt
    alter_tsconfiguration_stmt: AlterTSConfigurationStmt
    publication_table: PublicationTable
    publication_obj_spec: PublicationObjSpec
    create_publication_stmt: CreatePublicationStmt
    alter_publication_stmt: AlterPublicationStmt
    create_subscription_stmt: CreateSubscriptionStmt
    alter_subscription_stmt: AlterSubscriptionStmt
    drop_subscription_stmt: DropSubscriptionStmt
    integer: Integer
    float: Float
    boolean: Boolean
    string: String
    bit_string: BitString
    list: List
    int_list: IntList
    oid_list: OidList
    a_const: A_Const
    def __init__(
        self,
        alias: _Optional[_Union[Alias, _Mapping]] = ...,
        range_var: _Optional[_Union[RangeVar, _Mapping]] = ...,
        table_func: _Optional[_Union[TableFunc, _Mapping]] = ...,
        into_clause: _Optional[_Union[IntoClause, _Mapping]] = ...,
        var: _Optional[_Union[Var, _Mapping]] = ...,
        param: _Optional[_Union[Param, _Mapping]] = ...,
        aggref: _Optional[_Union[Aggref, _Mapping]] = ...,
        grouping_func: _Optional[_Union[GroupingFunc, _Mapping]] = ...,
        window_func: _Optional[_Union[WindowFunc, _Mapping]] = ...,
        subscripting_ref: _Optional[_Union[SubscriptingRef, _Mapping]] = ...,
        func_expr: _Optional[_Union[FuncExpr, _Mapping]] = ...,
        named_arg_expr: _Optional[_Union[NamedArgExpr, _Mapping]] = ...,
        op_expr: _Optional[_Union[OpExpr, _Mapping]] = ...,
        distinct_expr: _Optional[_Union[DistinctExpr, _Mapping]] = ...,
        null_if_expr: _Optional[_Union[NullIfExpr, _Mapping]] = ...,
        scalar_array_op_expr: _Optional[_Union[ScalarArrayOpExpr, _Mapping]] = ...,
        bool_expr: _Optional[_Union[BoolExpr, _Mapping]] = ...,
        sub_link: _Optional[_Union[SubLink, _Mapping]] = ...,
        sub_plan: _Optional[_Union[SubPlan, _Mapping]] = ...,
        alternative_sub_plan: _Optional[_Union[AlternativeSubPlan, _Mapping]] = ...,
        field_select: _Optional[_Union[FieldSelect, _Mapping]] = ...,
        field_store: _Optional[_Union[FieldStore, _Mapping]] = ...,
        relabel_type: _Optional[_Union[RelabelType, _Mapping]] = ...,
        coerce_via_io: _Optional[_Union[CoerceViaIO, _Mapping]] = ...,
        array_coerce_expr: _Optional[_Union[ArrayCoerceExpr, _Mapping]] = ...,
        convert_rowtype_expr: _Optional[_Union[ConvertRowtypeExpr, _Mapping]] = ...,
        collate_expr: _Optional[_Union[CollateExpr, _Mapping]] = ...,
        case_expr: _Optional[_Union[CaseExpr, _Mapping]] = ...,
        case_when: _Optional[_Union[CaseWhen, _Mapping]] = ...,
        case_test_expr: _Optional[_Union[CaseTestExpr, _Mapping]] = ...,
        array_expr: _Optional[_Union[ArrayExpr, _Mapping]] = ...,
        row_expr: _Optional[_Union[RowExpr, _Mapping]] = ...,
        row_compare_expr: _Optional[_Union[RowCompareExpr, _Mapping]] = ...,
        coalesce_expr: _Optional[_Union[CoalesceExpr, _Mapping]] = ...,
        min_max_expr: _Optional[_Union[MinMaxExpr, _Mapping]] = ...,
        sqlvalue_function: _Optional[_Union[SQLValueFunction, _Mapping]] = ...,
        xml_expr: _Optional[_Union[XmlExpr, _Mapping]] = ...,
        json_format: _Optional[_Union[JsonFormat, _Mapping]] = ...,
        json_returning: _Optional[_Union[JsonReturning, _Mapping]] = ...,
        json_value_expr: _Optional[_Union[JsonValueExpr, _Mapping]] = ...,
        json_constructor_expr: _Optional[_Union[JsonConstructorExpr, _Mapping]] = ...,
        json_is_predicate: _Optional[_Union[JsonIsPredicate, _Mapping]] = ...,
        null_test: _Optional[_Union[NullTest, _Mapping]] = ...,
        boolean_test: _Optional[_Union[BooleanTest, _Mapping]] = ...,
        coerce_to_domain: _Optional[_Union[CoerceToDomain, _Mapping]] = ...,
        coerce_to_domain_value: _Optional[_Union[CoerceToDomainValue, _Mapping]] = ...,
        set_to_default: _Optional[_Union[SetToDefault, _Mapping]] = ...,
        current_of_expr: _Optional[_Union[CurrentOfExpr, _Mapping]] = ...,
        next_value_expr: _Optional[_Union[NextValueExpr, _Mapping]] = ...,
        inference_elem: _Optional[_Union[InferenceElem, _Mapping]] = ...,
        target_entry: _Optional[_Union[TargetEntry, _Mapping]] = ...,
        range_tbl_ref: _Optional[_Union[RangeTblRef, _Mapping]] = ...,
        join_expr: _Optional[_Union[JoinExpr, _Mapping]] = ...,
        from_expr: _Optional[_Union[FromExpr, _Mapping]] = ...,
        on_conflict_expr: _Optional[_Union[OnConflictExpr, _Mapping]] = ...,
        query: _Optional[_Union[Query, _Mapping]] = ...,
        type_name: _Optional[_Union[TypeName, _Mapping]] = ...,
        column_ref: _Optional[_Union[ColumnRef, _Mapping]] = ...,
        param_ref: _Optional[_Union[ParamRef, _Mapping]] = ...,
        a_expr: _Optional[_Union[A_Expr, _Mapping]] = ...,
        type_cast: _Optional[_Union[TypeCast, _Mapping]] = ...,
        collate_clause: _Optional[_Union[CollateClause, _Mapping]] = ...,
        role_spec: _Optional[_Union[RoleSpec, _Mapping]] = ...,
        func_call: _Optional[_Union[FuncCall, _Mapping]] = ...,
        a_star: _Optional[_Union[A_Star, _Mapping]] = ...,
        a_indices: _Optional[_Union[A_Indices, _Mapping]] = ...,
        a_indirection: _Optional[_Union[A_Indirection, _Mapping]] = ...,
        a_array_expr: _Optional[_Union[A_ArrayExpr, _Mapping]] = ...,
        res_target: _Optional[_Union[ResTarget, _Mapping]] = ...,
        multi_assign_ref: _Optional[_Union[MultiAssignRef, _Mapping]] = ...,
        sort_by: _Optional[_Union[SortBy, _Mapping]] = ...,
        window_def: _Optional[_Union[WindowDef, _Mapping]] = ...,
        range_subselect: _Optional[_Union[RangeSubselect, _Mapping]] = ...,
        range_function: _Optional[_Union[RangeFunction, _Mapping]] = ...,
        range_table_func: _Optional[_Union[RangeTableFunc, _Mapping]] = ...,
        range_table_func_col: _Optional[_Union[RangeTableFuncCol, _Mapping]] = ...,
        range_table_sample: _Optional[_Union[RangeTableSample, _Mapping]] = ...,
        column_def: _Optional[_Union[ColumnDef, _Mapping]] = ...,
        table_like_clause: _Optional[_Union[TableLikeClause, _Mapping]] = ...,
        index_elem: _Optional[_Union[IndexElem, _Mapping]] = ...,
        def_elem: _Optional[_Union[DefElem, _Mapping]] = ...,
        locking_clause: _Optional[_Union[LockingClause, _Mapping]] = ...,
        xml_serialize: _Optional[_Union[XmlSerialize, _Mapping]] = ...,
        partition_elem: _Optional[_Union[PartitionElem, _Mapping]] = ...,
        partition_spec: _Optional[_Union[PartitionSpec, _Mapping]] = ...,
        partition_bound_spec: _Optional[_Union[PartitionBoundSpec, _Mapping]] = ...,
        partition_range_datum: _Optional[_Union[PartitionRangeDatum, _Mapping]] = ...,
        partition_cmd: _Optional[_Union[PartitionCmd, _Mapping]] = ...,
        range_tbl_entry: _Optional[_Union[RangeTblEntry, _Mapping]] = ...,
        rtepermission_info: _Optional[_Union[RTEPermissionInfo, _Mapping]] = ...,
        range_tbl_function: _Optional[_Union[RangeTblFunction, _Mapping]] = ...,
        table_sample_clause: _Optional[_Union[TableSampleClause, _Mapping]] = ...,
        with_check_option: _Optional[_Union[WithCheckOption, _Mapping]] = ...,
        sort_group_clause: _Optional[_Union[SortGroupClause, _Mapping]] = ...,
        grouping_set: _Optional[_Union[GroupingSet, _Mapping]] = ...,
        window_clause: _Optional[_Union[WindowClause, _Mapping]] = ...,
        row_mark_clause: _Optional[_Union[RowMarkClause, _Mapping]] = ...,
        with_clause: _Optional[_Union[WithClause, _Mapping]] = ...,
        infer_clause: _Optional[_Union[InferClause, _Mapping]] = ...,
        on_conflict_clause: _Optional[_Union[OnConflictClause, _Mapping]] = ...,
        ctesearch_clause: _Optional[_Union[CTESearchClause, _Mapping]] = ...,
        ctecycle_clause: _Optional[_Union[CTECycleClause, _Mapping]] = ...,
        common_table_expr: _Optional[_Union[CommonTableExpr, _Mapping]] = ...,
        merge_when_clause: _Optional[_Union[MergeWhenClause, _Mapping]] = ...,
        merge_action: _Optional[_Union[MergeAction, _Mapping]] = ...,
        trigger_transition: _Optional[_Union[TriggerTransition, _Mapping]] = ...,
        json_output: _Optional[_Union[JsonOutput, _Mapping]] = ...,
        json_key_value: _Optional[_Union[JsonKeyValue, _Mapping]] = ...,
        json_object_constructor: _Optional[_Union[JsonObjectConstructor, _Mapping]] = ...,
        json_array_constructor: _Optional[_Union[JsonArrayConstructor, _Mapping]] = ...,
        json_array_query_constructor: _Optional[_Union[JsonArrayQueryConstructor, _Mapping]] = ...,
        json_agg_constructor: _Optional[_Union[JsonAggConstructor, _Mapping]] = ...,
        json_object_agg: _Optional[_Union[JsonObjectAgg, _Mapping]] = ...,
        json_array_agg: _Optional[_Union[JsonArrayAgg, _Mapping]] = ...,
        raw_stmt: _Optional[_Union[RawStmt, _Mapping]] = ...,
        insert_stmt: _Optional[_Union[InsertStmt, _Mapping]] = ...,
        delete_stmt: _Optional[_Union[DeleteStmt, _Mapping]] = ...,
        update_stmt: _Optional[_Union[UpdateStmt, _Mapping]] = ...,
        merge_stmt: _Optional[_Union[MergeStmt, _Mapping]] = ...,
        select_stmt: _Optional[_Union[SelectStmt, _Mapping]] = ...,
        set_operation_stmt: _Optional[_Union[SetOperationStmt, _Mapping]] = ...,
        return_stmt: _Optional[_Union[ReturnStmt, _Mapping]] = ...,
        plassign_stmt: _Optional[_Union[PLAssignStmt, _Mapping]] = ...,
        create_schema_stmt: _Optional[_Union[CreateSchemaStmt, _Mapping]] = ...,
        alter_table_stmt: _Optional[_Union[AlterTableStmt, _Mapping]] = ...,
        replica_identity_stmt: _Optional[_Union[ReplicaIdentityStmt, _Mapping]] = ...,
        alter_table_cmd: _Optional[_Union[AlterTableCmd, _Mapping]] = ...,
        alter_collation_stmt: _Optional[_Union[AlterCollationStmt, _Mapping]] = ...,
        alter_domain_stmt: _Optional[_Union[AlterDomainStmt, _Mapping]] = ...,
        grant_stmt: _Optional[_Union[GrantStmt, _Mapping]] = ...,
        object_with_args: _Optional[_Union[ObjectWithArgs, _Mapping]] = ...,
        access_priv: _Optional[_Union[AccessPriv, _Mapping]] = ...,
        grant_role_stmt: _Optional[_Union[GrantRoleStmt, _Mapping]] = ...,
        alter_default_privileges_stmt: _Optional[_Union[AlterDefaultPrivilegesStmt, _Mapping]] = ...,
        copy_stmt: _Optional[_Union[CopyStmt, _Mapping]] = ...,
        variable_set_stmt: _Optional[_Union[VariableSetStmt, _Mapping]] = ...,
        variable_show_stmt: _Optional[_Union[VariableShowStmt, _Mapping]] = ...,
        create_stmt: _Optional[_Union[CreateStmt, _Mapping]] = ...,
        constraint: _Optional[_Union[Constraint, _Mapping]] = ...,
        create_table_space_stmt: _Optional[_Union[CreateTableSpaceStmt, _Mapping]] = ...,
        drop_table_space_stmt: _Optional[_Union[DropTableSpaceStmt, _Mapping]] = ...,
        alter_table_space_options_stmt: _Optional[_Union[AlterTableSpaceOptionsStmt, _Mapping]] = ...,
        alter_table_move_all_stmt: _Optional[_Union[AlterTableMoveAllStmt, _Mapping]] = ...,
        create_extension_stmt: _Optional[_Union[CreateExtensionStmt, _Mapping]] = ...,
        alter_extension_stmt: _Optional[_Union[AlterExtensionStmt, _Mapping]] = ...,
        alter_extension_contents_stmt: _Optional[_Union[AlterExtensionContentsStmt, _Mapping]] = ...,
        create_fdw_stmt: _Optional[_Union[CreateFdwStmt, _Mapping]] = ...,
        alter_fdw_stmt: _Optional[_Union[AlterFdwStmt, _Mapping]] = ...,
        create_foreign_server_stmt: _Optional[_Union[CreateForeignServerStmt, _Mapping]] = ...,
        alter_foreign_server_stmt: _Optional[_Union[AlterForeignServerStmt, _Mapping]] = ...,
        create_foreign_table_stmt: _Optional[_Union[CreateForeignTableStmt, _Mapping]] = ...,
        create_user_mapping_stmt: _Optional[_Union[CreateUserMappingStmt, _Mapping]] = ...,
        alter_user_mapping_stmt: _Optional[_Union[AlterUserMappingStmt, _Mapping]] = ...,
        drop_user_mapping_stmt: _Optional[_Union[DropUserMappingStmt, _Mapping]] = ...,
        import_foreign_schema_stmt: _Optional[_Union[ImportForeignSchemaStmt, _Mapping]] = ...,
        create_policy_stmt: _Optional[_Union[CreatePolicyStmt, _Mapping]] = ...,
        alter_policy_stmt: _Optional[_Union[AlterPolicyStmt, _Mapping]] = ...,
        create_am_stmt: _Optional[_Union[CreateAmStmt, _Mapping]] = ...,
        create_trig_stmt: _Optional[_Union[CreateTrigStmt, _Mapping]] = ...,
        create_event_trig_stmt: _Optional[_Union[CreateEventTrigStmt, _Mapping]] = ...,
        alter_event_trig_stmt: _Optional[_Union[AlterEventTrigStmt, _Mapping]] = ...,
        create_plang_stmt: _Optional[_Union[CreatePLangStmt, _Mapping]] = ...,
        create_role_stmt: _Optional[_Union[CreateRoleStmt, _Mapping]] = ...,
        alter_role_stmt: _Optional[_Union[AlterRoleStmt, _Mapping]] = ...,
        alter_role_set_stmt: _Optional[_Union[AlterRoleSetStmt, _Mapping]] = ...,
        drop_role_stmt: _Optional[_Union[DropRoleStmt, _Mapping]] = ...,
        create_seq_stmt: _Optional[_Union[CreateSeqStmt, _Mapping]] = ...,
        alter_seq_stmt: _Optional[_Union[AlterSeqStmt, _Mapping]] = ...,
        define_stmt: _Optional[_Union[DefineStmt, _Mapping]] = ...,
        create_domain_stmt: _Optional[_Union[CreateDomainStmt, _Mapping]] = ...,
        create_op_class_stmt: _Optional[_Union[CreateOpClassStmt, _Mapping]] = ...,
        create_op_class_item: _Optional[_Union[CreateOpClassItem, _Mapping]] = ...,
        create_op_family_stmt: _Optional[_Union[CreateOpFamilyStmt, _Mapping]] = ...,
        alter_op_family_stmt: _Optional[_Union[AlterOpFamilyStmt, _Mapping]] = ...,
        drop_stmt: _Optional[_Union[DropStmt, _Mapping]] = ...,
        truncate_stmt: _Optional[_Union[TruncateStmt, _Mapping]] = ...,
        comment_stmt: _Optional[_Union[CommentStmt, _Mapping]] = ...,
        sec_label_stmt: _Optional[_Union[SecLabelStmt, _Mapping]] = ...,
        declare_cursor_stmt: _Optional[_Union[DeclareCursorStmt, _Mapping]] = ...,
        close_portal_stmt: _Optional[_Union[ClosePortalStmt, _Mapping]] = ...,
        fetch_stmt: _Optional[_Union[FetchStmt, _Mapping]] = ...,
        index_stmt: _Optional[_Union[IndexStmt, _Mapping]] = ...,
        create_stats_stmt: _Optional[_Union[CreateStatsStmt, _Mapping]] = ...,
        stats_elem: _Optional[_Union[StatsElem, _Mapping]] = ...,
        alter_stats_stmt: _Optional[_Union[AlterStatsStmt, _Mapping]] = ...,
        create_function_stmt: _Optional[_Union[CreateFunctionStmt, _Mapping]] = ...,
        function_parameter: _Optional[_Union[FunctionParameter, _Mapping]] = ...,
        alter_function_stmt: _Optional[_Union[AlterFunctionStmt, _Mapping]] = ...,
        do_stmt: _Optional[_Union[DoStmt, _Mapping]] = ...,
        inline_code_block: _Optional[_Union[InlineCodeBlock, _Mapping]] = ...,
        call_stmt: _Optional[_Union[CallStmt, _Mapping]] = ...,
        call_context: _Optional[_Union[CallContext, _Mapping]] = ...,
        rename_stmt: _Optional[_Union[RenameStmt, _Mapping]] = ...,
        alter_object_depends_stmt: _Optional[_Union[AlterObjectDependsStmt, _Mapping]] = ...,
        alter_object_schema_stmt: _Optional[_Union[AlterObjectSchemaStmt, _Mapping]] = ...,
        alter_owner_stmt: _Optional[_Union[AlterOwnerStmt, _Mapping]] = ...,
        alter_operator_stmt: _Optional[_Union[AlterOperatorStmt, _Mapping]] = ...,
        alter_type_stmt: _Optional[_Union[AlterTypeStmt, _Mapping]] = ...,
        rule_stmt: _Optional[_Union[RuleStmt, _Mapping]] = ...,
        notify_stmt: _Optional[_Union[NotifyStmt, _Mapping]] = ...,
        listen_stmt: _Optional[_Union[ListenStmt, _Mapping]] = ...,
        unlisten_stmt: _Optional[_Union[UnlistenStmt, _Mapping]] = ...,
        transaction_stmt: _Optional[_Union[TransactionStmt, _Mapping]] = ...,
        composite_type_stmt: _Optional[_Union[CompositeTypeStmt, _Mapping]] = ...,
        create_enum_stmt: _Optional[_Union[CreateEnumStmt, _Mapping]] = ...,
        create_range_stmt: _Optional[_Union[CreateRangeStmt, _Mapping]] = ...,
        alter_enum_stmt: _Optional[_Union[AlterEnumStmt, _Mapping]] = ...,
        view_stmt: _Optional[_Union[ViewStmt, _Mapping]] = ...,
        load_stmt: _Optional[_Union[LoadStmt, _Mapping]] = ...,
        createdb_stmt: _Optional[_Union[CreatedbStmt, _Mapping]] = ...,
        alter_database_stmt: _Optional[_Union[AlterDatabaseStmt, _Mapping]] = ...,
        alter_database_refresh_coll_stmt: _Optional[_Union[AlterDatabaseRefreshCollStmt, _Mapping]] = ...,
        alter_database_set_stmt: _Optional[_Union[AlterDatabaseSetStmt, _Mapping]] = ...,
        dropdb_stmt: _Optional[_Union[DropdbStmt, _Mapping]] = ...,
        alter_system_stmt: _Optional[_Union[AlterSystemStmt, _Mapping]] = ...,
        cluster_stmt: _Optional[_Union[ClusterStmt, _Mapping]] = ...,
        vacuum_stmt: _Optional[_Union[VacuumStmt, _Mapping]] = ...,
        vacuum_relation: _Optional[_Union[VacuumRelation, _Mapping]] = ...,
        explain_stmt: _Optional[_Union[ExplainStmt, _Mapping]] = ...,
        create_table_as_stmt: _Optional[_Union[CreateTableAsStmt, _Mapping]] = ...,
        refresh_mat_view_stmt: _Optional[_Union[RefreshMatViewStmt, _Mapping]] = ...,
        check_point_stmt: _Optional[_Union[CheckPointStmt, _Mapping]] = ...,
        discard_stmt: _Optional[_Union[DiscardStmt, _Mapping]] = ...,
        lock_stmt: _Optional[_Union[LockStmt, _Mapping]] = ...,
        constraints_set_stmt: _Optional[_Union[ConstraintsSetStmt, _Mapping]] = ...,
        reindex_stmt: _Optional[_Union[ReindexStmt, _Mapping]] = ...,
        create_conversion_stmt: _Optional[_Union[CreateConversionStmt, _Mapping]] = ...,
        create_cast_stmt: _Optional[_Union[CreateCastStmt, _Mapping]] = ...,
        create_transform_stmt: _Optional[_Union[CreateTransformStmt, _Mapping]] = ...,
        prepare_stmt: _Optional[_Union[PrepareStmt, _Mapping]] = ...,
        execute_stmt: _Optional[_Union[ExecuteStmt, _Mapping]] = ...,
        deallocate_stmt: _Optional[_Union[DeallocateStmt, _Mapping]] = ...,
        drop_owned_stmt: _Optional[_Union[DropOwnedStmt, _Mapping]] = ...,
        reassign_owned_stmt: _Optional[_Union[ReassignOwnedStmt, _Mapping]] = ...,
        alter_tsdictionary_stmt: _Optional[_Union[AlterTSDictionaryStmt, _Mapping]] = ...,
        alter_tsconfiguration_stmt: _Optional[_Union[AlterTSConfigurationStmt, _Mapping]] = ...,
        publication_table: _Optional[_Union[PublicationTable, _Mapping]] = ...,
        publication_obj_spec: _Optional[_Union[PublicationObjSpec, _Mapping]] = ...,
        create_publication_stmt: _Optional[_Union[CreatePublicationStmt, _Mapping]] = ...,
        alter_publication_stmt: _Optional[_Union[AlterPublicationStmt, _Mapping]] = ...,
        create_subscription_stmt: _Optional[_Union[CreateSubscriptionStmt, _Mapping]] = ...,
        alter_subscription_stmt: _Optional[_Union[AlterSubscriptionStmt, _Mapping]] = ...,
        drop_subscription_stmt: _Optional[_Union[DropSubscriptionStmt, _Mapping]] = ...,
        integer: _Optional[_Union[Integer, _Mapping]] = ...,
        float: _Optional[_Union[Float, _Mapping]] = ...,
        boolean: _Optional[_Union[Boolean, _Mapping]] = ...,
        string: _Optional[_Union[String, _Mapping]] = ...,
        bit_string: _Optional[_Union[BitString, _Mapping]] = ...,
        list: _Optional[_Union[List, _Mapping]] = ...,
        int_list: _Optional[_Union[IntList, _Mapping]] = ...,
        oid_list: _Optional[_Union[OidList, _Mapping]] = ...,
        a_const: _Optional[_Union[A_Const, _Mapping]] = ...,
    ) -> None: ...

class Integer(_message.Message):
    __slots__ = ("ival",)
    IVAL_FIELD_NUMBER: _ClassVar[int]
    ival: int
    def __init__(self, ival: _Optional[int] = ...) -> None: ...

class Float(_message.Message):
    __slots__ = ("fval",)
    FVAL_FIELD_NUMBER: _ClassVar[int]
    fval: str
    def __init__(self, fval: _Optional[str] = ...) -> None: ...

class Boolean(_message.Message):
    __slots__ = ("boolval",)
    BOOLVAL_FIELD_NUMBER: _ClassVar[int]
    boolval: bool
    def __init__(self, boolval: bool = ...) -> None: ...

class String(_message.Message):
    __slots__ = ("sval",)
    SVAL_FIELD_NUMBER: _ClassVar[int]
    sval: str
    def __init__(self, sval: _Optional[str] = ...) -> None: ...

class BitString(_message.Message):
    __slots__ = ("bsval",)
    BSVAL_FIELD_NUMBER: _ClassVar[int]
    bsval: str
    def __init__(self, bsval: _Optional[str] = ...) -> None: ...

class List(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(self, items: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...) -> None: ...

class OidList(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(self, items: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...) -> None: ...

class IntList(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(self, items: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...) -> None: ...

class A_Const(_message.Message):
    __slots__ = ("ival", "fval", "boolval", "sval", "bsval", "isnull", "location")
    IVAL_FIELD_NUMBER: _ClassVar[int]
    FVAL_FIELD_NUMBER: _ClassVar[int]
    BOOLVAL_FIELD_NUMBER: _ClassVar[int]
    SVAL_FIELD_NUMBER: _ClassVar[int]
    BSVAL_FIELD_NUMBER: _ClassVar[int]
    ISNULL_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    ival: Integer
    fval: Float
    boolval: Boolean
    sval: String
    bsval: BitString
    isnull: bool
    location: int
    def __init__(
        self,
        ival: _Optional[_Union[Integer, _Mapping]] = ...,
        fval: _Optional[_Union[Float, _Mapping]] = ...,
        boolval: _Optional[_Union[Boolean, _Mapping]] = ...,
        sval: _Optional[_Union[String, _Mapping]] = ...,
        bsval: _Optional[_Union[BitString, _Mapping]] = ...,
        isnull: bool = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class Alias(_message.Message):
    __slots__ = ("aliasname", "colnames")
    ALIASNAME_FIELD_NUMBER: _ClassVar[int]
    COLNAMES_FIELD_NUMBER: _ClassVar[int]
    aliasname: str
    colnames: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self, aliasname: _Optional[str] = ..., colnames: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...
    ) -> None: ...

class RangeVar(_message.Message):
    __slots__ = ("catalogname", "schemaname", "relname", "inh", "relpersistence", "alias", "location")
    CATALOGNAME_FIELD_NUMBER: _ClassVar[int]
    SCHEMANAME_FIELD_NUMBER: _ClassVar[int]
    RELNAME_FIELD_NUMBER: _ClassVar[int]
    INH_FIELD_NUMBER: _ClassVar[int]
    RELPERSISTENCE_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    catalogname: str
    schemaname: str
    relname: str
    inh: bool
    relpersistence: str
    alias: Alias
    location: int
    def __init__(
        self,
        catalogname: _Optional[str] = ...,
        schemaname: _Optional[str] = ...,
        relname: _Optional[str] = ...,
        inh: bool = ...,
        relpersistence: _Optional[str] = ...,
        alias: _Optional[_Union[Alias, _Mapping]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class TableFunc(_message.Message):
    __slots__ = (
        "ns_uris",
        "ns_names",
        "docexpr",
        "rowexpr",
        "colnames",
        "coltypes",
        "coltypmods",
        "colcollations",
        "colexprs",
        "coldefexprs",
        "notnulls",
        "ordinalitycol",
        "location",
    )
    NS_URIS_FIELD_NUMBER: _ClassVar[int]
    NS_NAMES_FIELD_NUMBER: _ClassVar[int]
    DOCEXPR_FIELD_NUMBER: _ClassVar[int]
    ROWEXPR_FIELD_NUMBER: _ClassVar[int]
    COLNAMES_FIELD_NUMBER: _ClassVar[int]
    COLTYPES_FIELD_NUMBER: _ClassVar[int]
    COLTYPMODS_FIELD_NUMBER: _ClassVar[int]
    COLCOLLATIONS_FIELD_NUMBER: _ClassVar[int]
    COLEXPRS_FIELD_NUMBER: _ClassVar[int]
    COLDEFEXPRS_FIELD_NUMBER: _ClassVar[int]
    NOTNULLS_FIELD_NUMBER: _ClassVar[int]
    ORDINALITYCOL_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    ns_uris: _containers.RepeatedCompositeFieldContainer[Node]
    ns_names: _containers.RepeatedCompositeFieldContainer[Node]
    docexpr: Node
    rowexpr: Node
    colnames: _containers.RepeatedCompositeFieldContainer[Node]
    coltypes: _containers.RepeatedCompositeFieldContainer[Node]
    coltypmods: _containers.RepeatedCompositeFieldContainer[Node]
    colcollations: _containers.RepeatedCompositeFieldContainer[Node]
    colexprs: _containers.RepeatedCompositeFieldContainer[Node]
    coldefexprs: _containers.RepeatedCompositeFieldContainer[Node]
    notnulls: _containers.RepeatedScalarFieldContainer[int]
    ordinalitycol: int
    location: int
    def __init__(
        self,
        ns_uris: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        ns_names: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        docexpr: _Optional[_Union[Node, _Mapping]] = ...,
        rowexpr: _Optional[_Union[Node, _Mapping]] = ...,
        colnames: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        coltypes: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        coltypmods: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        colcollations: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        colexprs: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        coldefexprs: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        notnulls: _Optional[_Iterable[int]] = ...,
        ordinalitycol: _Optional[int] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class IntoClause(_message.Message):
    __slots__ = (
        "rel",
        "col_names",
        "access_method",
        "options",
        "on_commit",
        "table_space_name",
        "view_query",
        "skip_data",
    )
    REL_FIELD_NUMBER: _ClassVar[int]
    COL_NAMES_FIELD_NUMBER: _ClassVar[int]
    ACCESS_METHOD_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ON_COMMIT_FIELD_NUMBER: _ClassVar[int]
    TABLE_SPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_QUERY_FIELD_NUMBER: _ClassVar[int]
    SKIP_DATA_FIELD_NUMBER: _ClassVar[int]
    rel: RangeVar
    col_names: _containers.RepeatedCompositeFieldContainer[Node]
    access_method: str
    options: _containers.RepeatedCompositeFieldContainer[Node]
    on_commit: OnCommitAction
    table_space_name: str
    view_query: Node
    skip_data: bool
    def __init__(
        self,
        rel: _Optional[_Union[RangeVar, _Mapping]] = ...,
        col_names: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        access_method: _Optional[str] = ...,
        options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        on_commit: _Optional[_Union[OnCommitAction, str]] = ...,
        table_space_name: _Optional[str] = ...,
        view_query: _Optional[_Union[Node, _Mapping]] = ...,
        skip_data: bool = ...,
    ) -> None: ...

class Var(_message.Message):
    __slots__ = (
        "xpr",
        "varno",
        "varattno",
        "vartype",
        "vartypmod",
        "varcollid",
        "varnullingrels",
        "varlevelsup",
        "location",
    )
    XPR_FIELD_NUMBER: _ClassVar[int]
    VARNO_FIELD_NUMBER: _ClassVar[int]
    VARATTNO_FIELD_NUMBER: _ClassVar[int]
    VARTYPE_FIELD_NUMBER: _ClassVar[int]
    VARTYPMOD_FIELD_NUMBER: _ClassVar[int]
    VARCOLLID_FIELD_NUMBER: _ClassVar[int]
    VARNULLINGRELS_FIELD_NUMBER: _ClassVar[int]
    VARLEVELSUP_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    varno: int
    varattno: int
    vartype: int
    vartypmod: int
    varcollid: int
    varnullingrels: _containers.RepeatedScalarFieldContainer[int]
    varlevelsup: int
    location: int
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        varno: _Optional[int] = ...,
        varattno: _Optional[int] = ...,
        vartype: _Optional[int] = ...,
        vartypmod: _Optional[int] = ...,
        varcollid: _Optional[int] = ...,
        varnullingrels: _Optional[_Iterable[int]] = ...,
        varlevelsup: _Optional[int] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class Param(_message.Message):
    __slots__ = ("xpr", "paramkind", "paramid", "paramtype", "paramtypmod", "paramcollid", "location")
    XPR_FIELD_NUMBER: _ClassVar[int]
    PARAMKIND_FIELD_NUMBER: _ClassVar[int]
    PARAMID_FIELD_NUMBER: _ClassVar[int]
    PARAMTYPE_FIELD_NUMBER: _ClassVar[int]
    PARAMTYPMOD_FIELD_NUMBER: _ClassVar[int]
    PARAMCOLLID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    paramkind: ParamKind
    paramid: int
    paramtype: int
    paramtypmod: int
    paramcollid: int
    location: int
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        paramkind: _Optional[_Union[ParamKind, str]] = ...,
        paramid: _Optional[int] = ...,
        paramtype: _Optional[int] = ...,
        paramtypmod: _Optional[int] = ...,
        paramcollid: _Optional[int] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class Aggref(_message.Message):
    __slots__ = (
        "xpr",
        "aggfnoid",
        "aggtype",
        "aggcollid",
        "inputcollid",
        "aggargtypes",
        "aggdirectargs",
        "args",
        "aggorder",
        "aggdistinct",
        "aggfilter",
        "aggstar",
        "aggvariadic",
        "aggkind",
        "agglevelsup",
        "aggsplit",
        "aggno",
        "aggtransno",
        "location",
    )
    XPR_FIELD_NUMBER: _ClassVar[int]
    AGGFNOID_FIELD_NUMBER: _ClassVar[int]
    AGGTYPE_FIELD_NUMBER: _ClassVar[int]
    AGGCOLLID_FIELD_NUMBER: _ClassVar[int]
    INPUTCOLLID_FIELD_NUMBER: _ClassVar[int]
    AGGARGTYPES_FIELD_NUMBER: _ClassVar[int]
    AGGDIRECTARGS_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    AGGORDER_FIELD_NUMBER: _ClassVar[int]
    AGGDISTINCT_FIELD_NUMBER: _ClassVar[int]
    AGGFILTER_FIELD_NUMBER: _ClassVar[int]
    AGGSTAR_FIELD_NUMBER: _ClassVar[int]
    AGGVARIADIC_FIELD_NUMBER: _ClassVar[int]
    AGGKIND_FIELD_NUMBER: _ClassVar[int]
    AGGLEVELSUP_FIELD_NUMBER: _ClassVar[int]
    AGGSPLIT_FIELD_NUMBER: _ClassVar[int]
    AGGNO_FIELD_NUMBER: _ClassVar[int]
    AGGTRANSNO_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    aggfnoid: int
    aggtype: int
    aggcollid: int
    inputcollid: int
    aggargtypes: _containers.RepeatedCompositeFieldContainer[Node]
    aggdirectargs: _containers.RepeatedCompositeFieldContainer[Node]
    args: _containers.RepeatedCompositeFieldContainer[Node]
    aggorder: _containers.RepeatedCompositeFieldContainer[Node]
    aggdistinct: _containers.RepeatedCompositeFieldContainer[Node]
    aggfilter: Node
    aggstar: bool
    aggvariadic: bool
    aggkind: str
    agglevelsup: int
    aggsplit: AggSplit
    aggno: int
    aggtransno: int
    location: int
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        aggfnoid: _Optional[int] = ...,
        aggtype: _Optional[int] = ...,
        aggcollid: _Optional[int] = ...,
        inputcollid: _Optional[int] = ...,
        aggargtypes: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        aggdirectargs: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        args: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        aggorder: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        aggdistinct: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        aggfilter: _Optional[_Union[Node, _Mapping]] = ...,
        aggstar: bool = ...,
        aggvariadic: bool = ...,
        aggkind: _Optional[str] = ...,
        agglevelsup: _Optional[int] = ...,
        aggsplit: _Optional[_Union[AggSplit, str]] = ...,
        aggno: _Optional[int] = ...,
        aggtransno: _Optional[int] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class GroupingFunc(_message.Message):
    __slots__ = ("xpr", "args", "refs", "agglevelsup", "location")
    XPR_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    REFS_FIELD_NUMBER: _ClassVar[int]
    AGGLEVELSUP_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    args: _containers.RepeatedCompositeFieldContainer[Node]
    refs: _containers.RepeatedCompositeFieldContainer[Node]
    agglevelsup: int
    location: int
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        args: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        refs: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        agglevelsup: _Optional[int] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class WindowFunc(_message.Message):
    __slots__ = (
        "xpr",
        "winfnoid",
        "wintype",
        "wincollid",
        "inputcollid",
        "args",
        "aggfilter",
        "winref",
        "winstar",
        "winagg",
        "location",
    )
    XPR_FIELD_NUMBER: _ClassVar[int]
    WINFNOID_FIELD_NUMBER: _ClassVar[int]
    WINTYPE_FIELD_NUMBER: _ClassVar[int]
    WINCOLLID_FIELD_NUMBER: _ClassVar[int]
    INPUTCOLLID_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    AGGFILTER_FIELD_NUMBER: _ClassVar[int]
    WINREF_FIELD_NUMBER: _ClassVar[int]
    WINSTAR_FIELD_NUMBER: _ClassVar[int]
    WINAGG_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    winfnoid: int
    wintype: int
    wincollid: int
    inputcollid: int
    args: _containers.RepeatedCompositeFieldContainer[Node]
    aggfilter: Node
    winref: int
    winstar: bool
    winagg: bool
    location: int
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        winfnoid: _Optional[int] = ...,
        wintype: _Optional[int] = ...,
        wincollid: _Optional[int] = ...,
        inputcollid: _Optional[int] = ...,
        args: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        aggfilter: _Optional[_Union[Node, _Mapping]] = ...,
        winref: _Optional[int] = ...,
        winstar: bool = ...,
        winagg: bool = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class SubscriptingRef(_message.Message):
    __slots__ = (
        "xpr",
        "refcontainertype",
        "refelemtype",
        "refrestype",
        "reftypmod",
        "refcollid",
        "refupperindexpr",
        "reflowerindexpr",
        "refexpr",
        "refassgnexpr",
    )
    XPR_FIELD_NUMBER: _ClassVar[int]
    REFCONTAINERTYPE_FIELD_NUMBER: _ClassVar[int]
    REFELEMTYPE_FIELD_NUMBER: _ClassVar[int]
    REFRESTYPE_FIELD_NUMBER: _ClassVar[int]
    REFTYPMOD_FIELD_NUMBER: _ClassVar[int]
    REFCOLLID_FIELD_NUMBER: _ClassVar[int]
    REFUPPERINDEXPR_FIELD_NUMBER: _ClassVar[int]
    REFLOWERINDEXPR_FIELD_NUMBER: _ClassVar[int]
    REFEXPR_FIELD_NUMBER: _ClassVar[int]
    REFASSGNEXPR_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    refcontainertype: int
    refelemtype: int
    refrestype: int
    reftypmod: int
    refcollid: int
    refupperindexpr: _containers.RepeatedCompositeFieldContainer[Node]
    reflowerindexpr: _containers.RepeatedCompositeFieldContainer[Node]
    refexpr: Node
    refassgnexpr: Node
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        refcontainertype: _Optional[int] = ...,
        refelemtype: _Optional[int] = ...,
        refrestype: _Optional[int] = ...,
        reftypmod: _Optional[int] = ...,
        refcollid: _Optional[int] = ...,
        refupperindexpr: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        reflowerindexpr: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        refexpr: _Optional[_Union[Node, _Mapping]] = ...,
        refassgnexpr: _Optional[_Union[Node, _Mapping]] = ...,
    ) -> None: ...

class FuncExpr(_message.Message):
    __slots__ = (
        "xpr",
        "funcid",
        "funcresulttype",
        "funcretset",
        "funcvariadic",
        "funcformat",
        "funccollid",
        "inputcollid",
        "args",
        "location",
    )
    XPR_FIELD_NUMBER: _ClassVar[int]
    FUNCID_FIELD_NUMBER: _ClassVar[int]
    FUNCRESULTTYPE_FIELD_NUMBER: _ClassVar[int]
    FUNCRETSET_FIELD_NUMBER: _ClassVar[int]
    FUNCVARIADIC_FIELD_NUMBER: _ClassVar[int]
    FUNCFORMAT_FIELD_NUMBER: _ClassVar[int]
    FUNCCOLLID_FIELD_NUMBER: _ClassVar[int]
    INPUTCOLLID_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    funcid: int
    funcresulttype: int
    funcretset: bool
    funcvariadic: bool
    funcformat: CoercionForm
    funccollid: int
    inputcollid: int
    args: _containers.RepeatedCompositeFieldContainer[Node]
    location: int
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        funcid: _Optional[int] = ...,
        funcresulttype: _Optional[int] = ...,
        funcretset: bool = ...,
        funcvariadic: bool = ...,
        funcformat: _Optional[_Union[CoercionForm, str]] = ...,
        funccollid: _Optional[int] = ...,
        inputcollid: _Optional[int] = ...,
        args: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class NamedArgExpr(_message.Message):
    __slots__ = ("xpr", "arg", "name", "argnumber", "location")
    XPR_FIELD_NUMBER: _ClassVar[int]
    ARG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ARGNUMBER_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    arg: Node
    name: str
    argnumber: int
    location: int
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        arg: _Optional[_Union[Node, _Mapping]] = ...,
        name: _Optional[str] = ...,
        argnumber: _Optional[int] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class OpExpr(_message.Message):
    __slots__ = ("xpr", "opno", "opresulttype", "opretset", "opcollid", "inputcollid", "args", "location")
    XPR_FIELD_NUMBER: _ClassVar[int]
    OPNO_FIELD_NUMBER: _ClassVar[int]
    OPRESULTTYPE_FIELD_NUMBER: _ClassVar[int]
    OPRETSET_FIELD_NUMBER: _ClassVar[int]
    OPCOLLID_FIELD_NUMBER: _ClassVar[int]
    INPUTCOLLID_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    opno: int
    opresulttype: int
    opretset: bool
    opcollid: int
    inputcollid: int
    args: _containers.RepeatedCompositeFieldContainer[Node]
    location: int
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        opno: _Optional[int] = ...,
        opresulttype: _Optional[int] = ...,
        opretset: bool = ...,
        opcollid: _Optional[int] = ...,
        inputcollid: _Optional[int] = ...,
        args: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class DistinctExpr(_message.Message):
    __slots__ = ("xpr", "opno", "opresulttype", "opretset", "opcollid", "inputcollid", "args", "location")
    XPR_FIELD_NUMBER: _ClassVar[int]
    OPNO_FIELD_NUMBER: _ClassVar[int]
    OPRESULTTYPE_FIELD_NUMBER: _ClassVar[int]
    OPRETSET_FIELD_NUMBER: _ClassVar[int]
    OPCOLLID_FIELD_NUMBER: _ClassVar[int]
    INPUTCOLLID_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    opno: int
    opresulttype: int
    opretset: bool
    opcollid: int
    inputcollid: int
    args: _containers.RepeatedCompositeFieldContainer[Node]
    location: int
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        opno: _Optional[int] = ...,
        opresulttype: _Optional[int] = ...,
        opretset: bool = ...,
        opcollid: _Optional[int] = ...,
        inputcollid: _Optional[int] = ...,
        args: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class NullIfExpr(_message.Message):
    __slots__ = ("xpr", "opno", "opresulttype", "opretset", "opcollid", "inputcollid", "args", "location")
    XPR_FIELD_NUMBER: _ClassVar[int]
    OPNO_FIELD_NUMBER: _ClassVar[int]
    OPRESULTTYPE_FIELD_NUMBER: _ClassVar[int]
    OPRETSET_FIELD_NUMBER: _ClassVar[int]
    OPCOLLID_FIELD_NUMBER: _ClassVar[int]
    INPUTCOLLID_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    opno: int
    opresulttype: int
    opretset: bool
    opcollid: int
    inputcollid: int
    args: _containers.RepeatedCompositeFieldContainer[Node]
    location: int
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        opno: _Optional[int] = ...,
        opresulttype: _Optional[int] = ...,
        opretset: bool = ...,
        opcollid: _Optional[int] = ...,
        inputcollid: _Optional[int] = ...,
        args: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class ScalarArrayOpExpr(_message.Message):
    __slots__ = ("xpr", "opno", "use_or", "inputcollid", "args", "location")
    XPR_FIELD_NUMBER: _ClassVar[int]
    OPNO_FIELD_NUMBER: _ClassVar[int]
    USE_OR_FIELD_NUMBER: _ClassVar[int]
    INPUTCOLLID_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    opno: int
    use_or: bool
    inputcollid: int
    args: _containers.RepeatedCompositeFieldContainer[Node]
    location: int
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        opno: _Optional[int] = ...,
        use_or: bool = ...,
        inputcollid: _Optional[int] = ...,
        args: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class BoolExpr(_message.Message):
    __slots__ = ("xpr", "boolop", "args", "location")
    XPR_FIELD_NUMBER: _ClassVar[int]
    BOOLOP_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    boolop: BoolExprType
    args: _containers.RepeatedCompositeFieldContainer[Node]
    location: int
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        boolop: _Optional[_Union[BoolExprType, str]] = ...,
        args: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class SubLink(_message.Message):
    __slots__ = ("xpr", "sub_link_type", "sub_link_id", "testexpr", "oper_name", "subselect", "location")
    XPR_FIELD_NUMBER: _ClassVar[int]
    SUB_LINK_TYPE_FIELD_NUMBER: _ClassVar[int]
    SUB_LINK_ID_FIELD_NUMBER: _ClassVar[int]
    TESTEXPR_FIELD_NUMBER: _ClassVar[int]
    OPER_NAME_FIELD_NUMBER: _ClassVar[int]
    SUBSELECT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    sub_link_type: SubLinkType
    sub_link_id: int
    testexpr: Node
    oper_name: _containers.RepeatedCompositeFieldContainer[Node]
    subselect: Node
    location: int
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        sub_link_type: _Optional[_Union[SubLinkType, str]] = ...,
        sub_link_id: _Optional[int] = ...,
        testexpr: _Optional[_Union[Node, _Mapping]] = ...,
        oper_name: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        subselect: _Optional[_Union[Node, _Mapping]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class SubPlan(_message.Message):
    __slots__ = (
        "xpr",
        "sub_link_type",
        "testexpr",
        "param_ids",
        "plan_id",
        "plan_name",
        "first_col_type",
        "first_col_typmod",
        "first_col_collation",
        "use_hash_table",
        "unknown_eq_false",
        "parallel_safe",
        "set_param",
        "par_param",
        "args",
        "startup_cost",
        "per_call_cost",
    )
    XPR_FIELD_NUMBER: _ClassVar[int]
    SUB_LINK_TYPE_FIELD_NUMBER: _ClassVar[int]
    TESTEXPR_FIELD_NUMBER: _ClassVar[int]
    PARAM_IDS_FIELD_NUMBER: _ClassVar[int]
    PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    PLAN_NAME_FIELD_NUMBER: _ClassVar[int]
    FIRST_COL_TYPE_FIELD_NUMBER: _ClassVar[int]
    FIRST_COL_TYPMOD_FIELD_NUMBER: _ClassVar[int]
    FIRST_COL_COLLATION_FIELD_NUMBER: _ClassVar[int]
    USE_HASH_TABLE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_EQ_FALSE_FIELD_NUMBER: _ClassVar[int]
    PARALLEL_SAFE_FIELD_NUMBER: _ClassVar[int]
    SET_PARAM_FIELD_NUMBER: _ClassVar[int]
    PAR_PARAM_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    STARTUP_COST_FIELD_NUMBER: _ClassVar[int]
    PER_CALL_COST_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    sub_link_type: SubLinkType
    testexpr: Node
    param_ids: _containers.RepeatedCompositeFieldContainer[Node]
    plan_id: int
    plan_name: str
    first_col_type: int
    first_col_typmod: int
    first_col_collation: int
    use_hash_table: bool
    unknown_eq_false: bool
    parallel_safe: bool
    set_param: _containers.RepeatedCompositeFieldContainer[Node]
    par_param: _containers.RepeatedCompositeFieldContainer[Node]
    args: _containers.RepeatedCompositeFieldContainer[Node]
    startup_cost: float
    per_call_cost: float
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        sub_link_type: _Optional[_Union[SubLinkType, str]] = ...,
        testexpr: _Optional[_Union[Node, _Mapping]] = ...,
        param_ids: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        plan_id: _Optional[int] = ...,
        plan_name: _Optional[str] = ...,
        first_col_type: _Optional[int] = ...,
        first_col_typmod: _Optional[int] = ...,
        first_col_collation: _Optional[int] = ...,
        use_hash_table: bool = ...,
        unknown_eq_false: bool = ...,
        parallel_safe: bool = ...,
        set_param: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        par_param: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        args: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        startup_cost: _Optional[float] = ...,
        per_call_cost: _Optional[float] = ...,
    ) -> None: ...

class AlternativeSubPlan(_message.Message):
    __slots__ = ("xpr", "subplans")
    XPR_FIELD_NUMBER: _ClassVar[int]
    SUBPLANS_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    subplans: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self, xpr: _Optional[_Union[Node, _Mapping]] = ..., subplans: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...
    ) -> None: ...

class FieldSelect(_message.Message):
    __slots__ = ("xpr", "arg", "fieldnum", "resulttype", "resulttypmod", "resultcollid")
    XPR_FIELD_NUMBER: _ClassVar[int]
    ARG_FIELD_NUMBER: _ClassVar[int]
    FIELDNUM_FIELD_NUMBER: _ClassVar[int]
    RESULTTYPE_FIELD_NUMBER: _ClassVar[int]
    RESULTTYPMOD_FIELD_NUMBER: _ClassVar[int]
    RESULTCOLLID_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    arg: Node
    fieldnum: int
    resulttype: int
    resulttypmod: int
    resultcollid: int
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        arg: _Optional[_Union[Node, _Mapping]] = ...,
        fieldnum: _Optional[int] = ...,
        resulttype: _Optional[int] = ...,
        resulttypmod: _Optional[int] = ...,
        resultcollid: _Optional[int] = ...,
    ) -> None: ...

class FieldStore(_message.Message):
    __slots__ = ("xpr", "arg", "newvals", "fieldnums", "resulttype")
    XPR_FIELD_NUMBER: _ClassVar[int]
    ARG_FIELD_NUMBER: _ClassVar[int]
    NEWVALS_FIELD_NUMBER: _ClassVar[int]
    FIELDNUMS_FIELD_NUMBER: _ClassVar[int]
    RESULTTYPE_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    arg: Node
    newvals: _containers.RepeatedCompositeFieldContainer[Node]
    fieldnums: _containers.RepeatedCompositeFieldContainer[Node]
    resulttype: int
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        arg: _Optional[_Union[Node, _Mapping]] = ...,
        newvals: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        fieldnums: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        resulttype: _Optional[int] = ...,
    ) -> None: ...

class RelabelType(_message.Message):
    __slots__ = ("xpr", "arg", "resulttype", "resulttypmod", "resultcollid", "relabelformat", "location")
    XPR_FIELD_NUMBER: _ClassVar[int]
    ARG_FIELD_NUMBER: _ClassVar[int]
    RESULTTYPE_FIELD_NUMBER: _ClassVar[int]
    RESULTTYPMOD_FIELD_NUMBER: _ClassVar[int]
    RESULTCOLLID_FIELD_NUMBER: _ClassVar[int]
    RELABELFORMAT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    arg: Node
    resulttype: int
    resulttypmod: int
    resultcollid: int
    relabelformat: CoercionForm
    location: int
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        arg: _Optional[_Union[Node, _Mapping]] = ...,
        resulttype: _Optional[int] = ...,
        resulttypmod: _Optional[int] = ...,
        resultcollid: _Optional[int] = ...,
        relabelformat: _Optional[_Union[CoercionForm, str]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class CoerceViaIO(_message.Message):
    __slots__ = ("xpr", "arg", "resulttype", "resultcollid", "coerceformat", "location")
    XPR_FIELD_NUMBER: _ClassVar[int]
    ARG_FIELD_NUMBER: _ClassVar[int]
    RESULTTYPE_FIELD_NUMBER: _ClassVar[int]
    RESULTCOLLID_FIELD_NUMBER: _ClassVar[int]
    COERCEFORMAT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    arg: Node
    resulttype: int
    resultcollid: int
    coerceformat: CoercionForm
    location: int
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        arg: _Optional[_Union[Node, _Mapping]] = ...,
        resulttype: _Optional[int] = ...,
        resultcollid: _Optional[int] = ...,
        coerceformat: _Optional[_Union[CoercionForm, str]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class ArrayCoerceExpr(_message.Message):
    __slots__ = ("xpr", "arg", "elemexpr", "resulttype", "resulttypmod", "resultcollid", "coerceformat", "location")
    XPR_FIELD_NUMBER: _ClassVar[int]
    ARG_FIELD_NUMBER: _ClassVar[int]
    ELEMEXPR_FIELD_NUMBER: _ClassVar[int]
    RESULTTYPE_FIELD_NUMBER: _ClassVar[int]
    RESULTTYPMOD_FIELD_NUMBER: _ClassVar[int]
    RESULTCOLLID_FIELD_NUMBER: _ClassVar[int]
    COERCEFORMAT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    arg: Node
    elemexpr: Node
    resulttype: int
    resulttypmod: int
    resultcollid: int
    coerceformat: CoercionForm
    location: int
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        arg: _Optional[_Union[Node, _Mapping]] = ...,
        elemexpr: _Optional[_Union[Node, _Mapping]] = ...,
        resulttype: _Optional[int] = ...,
        resulttypmod: _Optional[int] = ...,
        resultcollid: _Optional[int] = ...,
        coerceformat: _Optional[_Union[CoercionForm, str]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class ConvertRowtypeExpr(_message.Message):
    __slots__ = ("xpr", "arg", "resulttype", "convertformat", "location")
    XPR_FIELD_NUMBER: _ClassVar[int]
    ARG_FIELD_NUMBER: _ClassVar[int]
    RESULTTYPE_FIELD_NUMBER: _ClassVar[int]
    CONVERTFORMAT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    arg: Node
    resulttype: int
    convertformat: CoercionForm
    location: int
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        arg: _Optional[_Union[Node, _Mapping]] = ...,
        resulttype: _Optional[int] = ...,
        convertformat: _Optional[_Union[CoercionForm, str]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class CollateExpr(_message.Message):
    __slots__ = ("xpr", "arg", "coll_oid", "location")
    XPR_FIELD_NUMBER: _ClassVar[int]
    ARG_FIELD_NUMBER: _ClassVar[int]
    COLL_OID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    arg: Node
    coll_oid: int
    location: int
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        arg: _Optional[_Union[Node, _Mapping]] = ...,
        coll_oid: _Optional[int] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class CaseExpr(_message.Message):
    __slots__ = ("xpr", "casetype", "casecollid", "arg", "args", "defresult", "location")
    XPR_FIELD_NUMBER: _ClassVar[int]
    CASETYPE_FIELD_NUMBER: _ClassVar[int]
    CASECOLLID_FIELD_NUMBER: _ClassVar[int]
    ARG_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    DEFRESULT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    casetype: int
    casecollid: int
    arg: Node
    args: _containers.RepeatedCompositeFieldContainer[Node]
    defresult: Node
    location: int
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        casetype: _Optional[int] = ...,
        casecollid: _Optional[int] = ...,
        arg: _Optional[_Union[Node, _Mapping]] = ...,
        args: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        defresult: _Optional[_Union[Node, _Mapping]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class CaseWhen(_message.Message):
    __slots__ = ("xpr", "expr", "result", "location")
    XPR_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    expr: Node
    result: Node
    location: int
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        expr: _Optional[_Union[Node, _Mapping]] = ...,
        result: _Optional[_Union[Node, _Mapping]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class CaseTestExpr(_message.Message):
    __slots__ = ("xpr", "type_id", "type_mod", "collation")
    XPR_FIELD_NUMBER: _ClassVar[int]
    TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_MOD_FIELD_NUMBER: _ClassVar[int]
    COLLATION_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    type_id: int
    type_mod: int
    collation: int
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        type_id: _Optional[int] = ...,
        type_mod: _Optional[int] = ...,
        collation: _Optional[int] = ...,
    ) -> None: ...

class ArrayExpr(_message.Message):
    __slots__ = ("xpr", "array_typeid", "array_collid", "element_typeid", "elements", "multidims", "location")
    XPR_FIELD_NUMBER: _ClassVar[int]
    ARRAY_TYPEID_FIELD_NUMBER: _ClassVar[int]
    ARRAY_COLLID_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_TYPEID_FIELD_NUMBER: _ClassVar[int]
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    MULTIDIMS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    array_typeid: int
    array_collid: int
    element_typeid: int
    elements: _containers.RepeatedCompositeFieldContainer[Node]
    multidims: bool
    location: int
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        array_typeid: _Optional[int] = ...,
        array_collid: _Optional[int] = ...,
        element_typeid: _Optional[int] = ...,
        elements: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        multidims: bool = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class RowExpr(_message.Message):
    __slots__ = ("xpr", "args", "row_typeid", "row_format", "colnames", "location")
    XPR_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    ROW_TYPEID_FIELD_NUMBER: _ClassVar[int]
    ROW_FORMAT_FIELD_NUMBER: _ClassVar[int]
    COLNAMES_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    args: _containers.RepeatedCompositeFieldContainer[Node]
    row_typeid: int
    row_format: CoercionForm
    colnames: _containers.RepeatedCompositeFieldContainer[Node]
    location: int
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        args: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        row_typeid: _Optional[int] = ...,
        row_format: _Optional[_Union[CoercionForm, str]] = ...,
        colnames: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class RowCompareExpr(_message.Message):
    __slots__ = ("xpr", "rctype", "opnos", "opfamilies", "inputcollids", "largs", "rargs")
    XPR_FIELD_NUMBER: _ClassVar[int]
    RCTYPE_FIELD_NUMBER: _ClassVar[int]
    OPNOS_FIELD_NUMBER: _ClassVar[int]
    OPFAMILIES_FIELD_NUMBER: _ClassVar[int]
    INPUTCOLLIDS_FIELD_NUMBER: _ClassVar[int]
    LARGS_FIELD_NUMBER: _ClassVar[int]
    RARGS_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    rctype: RowCompareType
    opnos: _containers.RepeatedCompositeFieldContainer[Node]
    opfamilies: _containers.RepeatedCompositeFieldContainer[Node]
    inputcollids: _containers.RepeatedCompositeFieldContainer[Node]
    largs: _containers.RepeatedCompositeFieldContainer[Node]
    rargs: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        rctype: _Optional[_Union[RowCompareType, str]] = ...,
        opnos: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        opfamilies: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        inputcollids: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        largs: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        rargs: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class CoalesceExpr(_message.Message):
    __slots__ = ("xpr", "coalescetype", "coalescecollid", "args", "location")
    XPR_FIELD_NUMBER: _ClassVar[int]
    COALESCETYPE_FIELD_NUMBER: _ClassVar[int]
    COALESCECOLLID_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    coalescetype: int
    coalescecollid: int
    args: _containers.RepeatedCompositeFieldContainer[Node]
    location: int
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        coalescetype: _Optional[int] = ...,
        coalescecollid: _Optional[int] = ...,
        args: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class MinMaxExpr(_message.Message):
    __slots__ = ("xpr", "minmaxtype", "minmaxcollid", "inputcollid", "op", "args", "location")
    XPR_FIELD_NUMBER: _ClassVar[int]
    MINMAXTYPE_FIELD_NUMBER: _ClassVar[int]
    MINMAXCOLLID_FIELD_NUMBER: _ClassVar[int]
    INPUTCOLLID_FIELD_NUMBER: _ClassVar[int]
    OP_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    minmaxtype: int
    minmaxcollid: int
    inputcollid: int
    op: MinMaxOp
    args: _containers.RepeatedCompositeFieldContainer[Node]
    location: int
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        minmaxtype: _Optional[int] = ...,
        minmaxcollid: _Optional[int] = ...,
        inputcollid: _Optional[int] = ...,
        op: _Optional[_Union[MinMaxOp, str]] = ...,
        args: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class SQLValueFunction(_message.Message):
    __slots__ = ("xpr", "op", "type", "typmod", "location")
    XPR_FIELD_NUMBER: _ClassVar[int]
    OP_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TYPMOD_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    op: SQLValueFunctionOp
    type: int
    typmod: int
    location: int
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        op: _Optional[_Union[SQLValueFunctionOp, str]] = ...,
        type: _Optional[int] = ...,
        typmod: _Optional[int] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class XmlExpr(_message.Message):
    __slots__ = (
        "xpr",
        "op",
        "name",
        "named_args",
        "arg_names",
        "args",
        "xmloption",
        "indent",
        "type",
        "typmod",
        "location",
    )
    XPR_FIELD_NUMBER: _ClassVar[int]
    OP_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMED_ARGS_FIELD_NUMBER: _ClassVar[int]
    ARG_NAMES_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    XMLOPTION_FIELD_NUMBER: _ClassVar[int]
    INDENT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TYPMOD_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    op: XmlExprOp
    name: str
    named_args: _containers.RepeatedCompositeFieldContainer[Node]
    arg_names: _containers.RepeatedCompositeFieldContainer[Node]
    args: _containers.RepeatedCompositeFieldContainer[Node]
    xmloption: XmlOptionType
    indent: bool
    type: int
    typmod: int
    location: int
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        op: _Optional[_Union[XmlExprOp, str]] = ...,
        name: _Optional[str] = ...,
        named_args: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        arg_names: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        args: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        xmloption: _Optional[_Union[XmlOptionType, str]] = ...,
        indent: bool = ...,
        type: _Optional[int] = ...,
        typmod: _Optional[int] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class JsonFormat(_message.Message):
    __slots__ = ("format_type", "encoding", "location")
    FORMAT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    format_type: JsonFormatType
    encoding: JsonEncoding
    location: int
    def __init__(
        self,
        format_type: _Optional[_Union[JsonFormatType, str]] = ...,
        encoding: _Optional[_Union[JsonEncoding, str]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class JsonReturning(_message.Message):
    __slots__ = ("format", "typid", "typmod")
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    TYPID_FIELD_NUMBER: _ClassVar[int]
    TYPMOD_FIELD_NUMBER: _ClassVar[int]
    format: JsonFormat
    typid: int
    typmod: int
    def __init__(
        self,
        format: _Optional[_Union[JsonFormat, _Mapping]] = ...,
        typid: _Optional[int] = ...,
        typmod: _Optional[int] = ...,
    ) -> None: ...

class JsonValueExpr(_message.Message):
    __slots__ = ("raw_expr", "formatted_expr", "format")
    RAW_EXPR_FIELD_NUMBER: _ClassVar[int]
    FORMATTED_EXPR_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    raw_expr: Node
    formatted_expr: Node
    format: JsonFormat
    def __init__(
        self,
        raw_expr: _Optional[_Union[Node, _Mapping]] = ...,
        formatted_expr: _Optional[_Union[Node, _Mapping]] = ...,
        format: _Optional[_Union[JsonFormat, _Mapping]] = ...,
    ) -> None: ...

class JsonConstructorExpr(_message.Message):
    __slots__ = ("xpr", "type", "args", "func", "coercion", "returning", "absent_on_null", "unique", "location")
    XPR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    FUNC_FIELD_NUMBER: _ClassVar[int]
    COERCION_FIELD_NUMBER: _ClassVar[int]
    RETURNING_FIELD_NUMBER: _ClassVar[int]
    ABSENT_ON_NULL_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    type: JsonConstructorType
    args: _containers.RepeatedCompositeFieldContainer[Node]
    func: Node
    coercion: Node
    returning: JsonReturning
    absent_on_null: bool
    unique: bool
    location: int
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        type: _Optional[_Union[JsonConstructorType, str]] = ...,
        args: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        func: _Optional[_Union[Node, _Mapping]] = ...,
        coercion: _Optional[_Union[Node, _Mapping]] = ...,
        returning: _Optional[_Union[JsonReturning, _Mapping]] = ...,
        absent_on_null: bool = ...,
        unique: bool = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class JsonIsPredicate(_message.Message):
    __slots__ = ("expr", "format", "item_type", "unique_keys", "location")
    EXPR_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_KEYS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    expr: Node
    format: JsonFormat
    item_type: JsonValueType
    unique_keys: bool
    location: int
    def __init__(
        self,
        expr: _Optional[_Union[Node, _Mapping]] = ...,
        format: _Optional[_Union[JsonFormat, _Mapping]] = ...,
        item_type: _Optional[_Union[JsonValueType, str]] = ...,
        unique_keys: bool = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class NullTest(_message.Message):
    __slots__ = ("xpr", "arg", "nulltesttype", "argisrow", "location")
    XPR_FIELD_NUMBER: _ClassVar[int]
    ARG_FIELD_NUMBER: _ClassVar[int]
    NULLTESTTYPE_FIELD_NUMBER: _ClassVar[int]
    ARGISROW_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    arg: Node
    nulltesttype: NullTestType
    argisrow: bool
    location: int
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        arg: _Optional[_Union[Node, _Mapping]] = ...,
        nulltesttype: _Optional[_Union[NullTestType, str]] = ...,
        argisrow: bool = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class BooleanTest(_message.Message):
    __slots__ = ("xpr", "arg", "booltesttype", "location")
    XPR_FIELD_NUMBER: _ClassVar[int]
    ARG_FIELD_NUMBER: _ClassVar[int]
    BOOLTESTTYPE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    arg: Node
    booltesttype: BoolTestType
    location: int
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        arg: _Optional[_Union[Node, _Mapping]] = ...,
        booltesttype: _Optional[_Union[BoolTestType, str]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class CoerceToDomain(_message.Message):
    __slots__ = ("xpr", "arg", "resulttype", "resulttypmod", "resultcollid", "coercionformat", "location")
    XPR_FIELD_NUMBER: _ClassVar[int]
    ARG_FIELD_NUMBER: _ClassVar[int]
    RESULTTYPE_FIELD_NUMBER: _ClassVar[int]
    RESULTTYPMOD_FIELD_NUMBER: _ClassVar[int]
    RESULTCOLLID_FIELD_NUMBER: _ClassVar[int]
    COERCIONFORMAT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    arg: Node
    resulttype: int
    resulttypmod: int
    resultcollid: int
    coercionformat: CoercionForm
    location: int
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        arg: _Optional[_Union[Node, _Mapping]] = ...,
        resulttype: _Optional[int] = ...,
        resulttypmod: _Optional[int] = ...,
        resultcollid: _Optional[int] = ...,
        coercionformat: _Optional[_Union[CoercionForm, str]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class CoerceToDomainValue(_message.Message):
    __slots__ = ("xpr", "type_id", "type_mod", "collation", "location")
    XPR_FIELD_NUMBER: _ClassVar[int]
    TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_MOD_FIELD_NUMBER: _ClassVar[int]
    COLLATION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    type_id: int
    type_mod: int
    collation: int
    location: int
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        type_id: _Optional[int] = ...,
        type_mod: _Optional[int] = ...,
        collation: _Optional[int] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class SetToDefault(_message.Message):
    __slots__ = ("xpr", "type_id", "type_mod", "collation", "location")
    XPR_FIELD_NUMBER: _ClassVar[int]
    TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_MOD_FIELD_NUMBER: _ClassVar[int]
    COLLATION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    type_id: int
    type_mod: int
    collation: int
    location: int
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        type_id: _Optional[int] = ...,
        type_mod: _Optional[int] = ...,
        collation: _Optional[int] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class CurrentOfExpr(_message.Message):
    __slots__ = ("xpr", "cvarno", "cursor_name", "cursor_param")
    XPR_FIELD_NUMBER: _ClassVar[int]
    CVARNO_FIELD_NUMBER: _ClassVar[int]
    CURSOR_NAME_FIELD_NUMBER: _ClassVar[int]
    CURSOR_PARAM_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    cvarno: int
    cursor_name: str
    cursor_param: int
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        cvarno: _Optional[int] = ...,
        cursor_name: _Optional[str] = ...,
        cursor_param: _Optional[int] = ...,
    ) -> None: ...

class NextValueExpr(_message.Message):
    __slots__ = ("xpr", "seqid", "type_id")
    XPR_FIELD_NUMBER: _ClassVar[int]
    SEQID_FIELD_NUMBER: _ClassVar[int]
    TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    seqid: int
    type_id: int
    def __init__(
        self, xpr: _Optional[_Union[Node, _Mapping]] = ..., seqid: _Optional[int] = ..., type_id: _Optional[int] = ...
    ) -> None: ...

class InferenceElem(_message.Message):
    __slots__ = ("xpr", "expr", "infercollid", "inferopclass")
    XPR_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    INFERCOLLID_FIELD_NUMBER: _ClassVar[int]
    INFEROPCLASS_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    expr: Node
    infercollid: int
    inferopclass: int
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        expr: _Optional[_Union[Node, _Mapping]] = ...,
        infercollid: _Optional[int] = ...,
        inferopclass: _Optional[int] = ...,
    ) -> None: ...

class TargetEntry(_message.Message):
    __slots__ = ("xpr", "expr", "resno", "resname", "ressortgroupref", "resorigtbl", "resorigcol", "resjunk")
    XPR_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    RESNO_FIELD_NUMBER: _ClassVar[int]
    RESNAME_FIELD_NUMBER: _ClassVar[int]
    RESSORTGROUPREF_FIELD_NUMBER: _ClassVar[int]
    RESORIGTBL_FIELD_NUMBER: _ClassVar[int]
    RESORIGCOL_FIELD_NUMBER: _ClassVar[int]
    RESJUNK_FIELD_NUMBER: _ClassVar[int]
    xpr: Node
    expr: Node
    resno: int
    resname: str
    ressortgroupref: int
    resorigtbl: int
    resorigcol: int
    resjunk: bool
    def __init__(
        self,
        xpr: _Optional[_Union[Node, _Mapping]] = ...,
        expr: _Optional[_Union[Node, _Mapping]] = ...,
        resno: _Optional[int] = ...,
        resname: _Optional[str] = ...,
        ressortgroupref: _Optional[int] = ...,
        resorigtbl: _Optional[int] = ...,
        resorigcol: _Optional[int] = ...,
        resjunk: bool = ...,
    ) -> None: ...

class RangeTblRef(_message.Message):
    __slots__ = ("rtindex",)
    RTINDEX_FIELD_NUMBER: _ClassVar[int]
    rtindex: int
    def __init__(self, rtindex: _Optional[int] = ...) -> None: ...

class JoinExpr(_message.Message):
    __slots__ = (
        "jointype",
        "is_natural",
        "larg",
        "rarg",
        "using_clause",
        "join_using_alias",
        "quals",
        "alias",
        "rtindex",
    )
    JOINTYPE_FIELD_NUMBER: _ClassVar[int]
    IS_NATURAL_FIELD_NUMBER: _ClassVar[int]
    LARG_FIELD_NUMBER: _ClassVar[int]
    RARG_FIELD_NUMBER: _ClassVar[int]
    USING_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    JOIN_USING_ALIAS_FIELD_NUMBER: _ClassVar[int]
    QUALS_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    RTINDEX_FIELD_NUMBER: _ClassVar[int]
    jointype: JoinType
    is_natural: bool
    larg: Node
    rarg: Node
    using_clause: _containers.RepeatedCompositeFieldContainer[Node]
    join_using_alias: Alias
    quals: Node
    alias: Alias
    rtindex: int
    def __init__(
        self,
        jointype: _Optional[_Union[JoinType, str]] = ...,
        is_natural: bool = ...,
        larg: _Optional[_Union[Node, _Mapping]] = ...,
        rarg: _Optional[_Union[Node, _Mapping]] = ...,
        using_clause: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        join_using_alias: _Optional[_Union[Alias, _Mapping]] = ...,
        quals: _Optional[_Union[Node, _Mapping]] = ...,
        alias: _Optional[_Union[Alias, _Mapping]] = ...,
        rtindex: _Optional[int] = ...,
    ) -> None: ...

class FromExpr(_message.Message):
    __slots__ = ("fromlist", "quals")
    FROMLIST_FIELD_NUMBER: _ClassVar[int]
    QUALS_FIELD_NUMBER: _ClassVar[int]
    fromlist: _containers.RepeatedCompositeFieldContainer[Node]
    quals: Node
    def __init__(
        self,
        fromlist: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        quals: _Optional[_Union[Node, _Mapping]] = ...,
    ) -> None: ...

class OnConflictExpr(_message.Message):
    __slots__ = (
        "action",
        "arbiter_elems",
        "arbiter_where",
        "constraint",
        "on_conflict_set",
        "on_conflict_where",
        "excl_rel_index",
        "excl_rel_tlist",
    )
    ACTION_FIELD_NUMBER: _ClassVar[int]
    ARBITER_ELEMS_FIELD_NUMBER: _ClassVar[int]
    ARBITER_WHERE_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    ON_CONFLICT_SET_FIELD_NUMBER: _ClassVar[int]
    ON_CONFLICT_WHERE_FIELD_NUMBER: _ClassVar[int]
    EXCL_REL_INDEX_FIELD_NUMBER: _ClassVar[int]
    EXCL_REL_TLIST_FIELD_NUMBER: _ClassVar[int]
    action: OnConflictAction
    arbiter_elems: _containers.RepeatedCompositeFieldContainer[Node]
    arbiter_where: Node
    constraint: int
    on_conflict_set: _containers.RepeatedCompositeFieldContainer[Node]
    on_conflict_where: Node
    excl_rel_index: int
    excl_rel_tlist: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        action: _Optional[_Union[OnConflictAction, str]] = ...,
        arbiter_elems: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        arbiter_where: _Optional[_Union[Node, _Mapping]] = ...,
        constraint: _Optional[int] = ...,
        on_conflict_set: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        on_conflict_where: _Optional[_Union[Node, _Mapping]] = ...,
        excl_rel_index: _Optional[int] = ...,
        excl_rel_tlist: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class Query(_message.Message):
    __slots__ = (
        "command_type",
        "query_source",
        "can_set_tag",
        "utility_stmt",
        "result_relation",
        "has_aggs",
        "has_window_funcs",
        "has_target_srfs",
        "has_sub_links",
        "has_distinct_on",
        "has_recursive",
        "has_modifying_cte",
        "has_for_update",
        "has_row_security",
        "is_return",
        "cte_list",
        "rtable",
        "rteperminfos",
        "jointree",
        "merge_action_list",
        "merge_use_outer_join",
        "target_list",
        "override",
        "on_conflict",
        "returning_list",
        "group_clause",
        "group_distinct",
        "grouping_sets",
        "having_qual",
        "window_clause",
        "distinct_clause",
        "sort_clause",
        "limit_offset",
        "limit_count",
        "limit_option",
        "row_marks",
        "set_operations",
        "constraint_deps",
        "with_check_options",
        "stmt_location",
        "stmt_len",
    )
    COMMAND_TYPE_FIELD_NUMBER: _ClassVar[int]
    QUERY_SOURCE_FIELD_NUMBER: _ClassVar[int]
    CAN_SET_TAG_FIELD_NUMBER: _ClassVar[int]
    UTILITY_STMT_FIELD_NUMBER: _ClassVar[int]
    RESULT_RELATION_FIELD_NUMBER: _ClassVar[int]
    HAS_AGGS_FIELD_NUMBER: _ClassVar[int]
    HAS_WINDOW_FUNCS_FIELD_NUMBER: _ClassVar[int]
    HAS_TARGET_SRFS_FIELD_NUMBER: _ClassVar[int]
    HAS_SUB_LINKS_FIELD_NUMBER: _ClassVar[int]
    HAS_DISTINCT_ON_FIELD_NUMBER: _ClassVar[int]
    HAS_RECURSIVE_FIELD_NUMBER: _ClassVar[int]
    HAS_MODIFYING_CTE_FIELD_NUMBER: _ClassVar[int]
    HAS_FOR_UPDATE_FIELD_NUMBER: _ClassVar[int]
    HAS_ROW_SECURITY_FIELD_NUMBER: _ClassVar[int]
    IS_RETURN_FIELD_NUMBER: _ClassVar[int]
    CTE_LIST_FIELD_NUMBER: _ClassVar[int]
    RTABLE_FIELD_NUMBER: _ClassVar[int]
    RTEPERMINFOS_FIELD_NUMBER: _ClassVar[int]
    JOINTREE_FIELD_NUMBER: _ClassVar[int]
    MERGE_ACTION_LIST_FIELD_NUMBER: _ClassVar[int]
    MERGE_USE_OUTER_JOIN_FIELD_NUMBER: _ClassVar[int]
    TARGET_LIST_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    ON_CONFLICT_FIELD_NUMBER: _ClassVar[int]
    RETURNING_LIST_FIELD_NUMBER: _ClassVar[int]
    GROUP_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    GROUP_DISTINCT_FIELD_NUMBER: _ClassVar[int]
    GROUPING_SETS_FIELD_NUMBER: _ClassVar[int]
    HAVING_QUAL_FIELD_NUMBER: _ClassVar[int]
    WINDOW_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    DISTINCT_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    SORT_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    LIMIT_COUNT_FIELD_NUMBER: _ClassVar[int]
    LIMIT_OPTION_FIELD_NUMBER: _ClassVar[int]
    ROW_MARKS_FIELD_NUMBER: _ClassVar[int]
    SET_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINT_DEPS_FIELD_NUMBER: _ClassVar[int]
    WITH_CHECK_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    STMT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    STMT_LEN_FIELD_NUMBER: _ClassVar[int]
    command_type: CmdType
    query_source: QuerySource
    can_set_tag: bool
    utility_stmt: Node
    result_relation: int
    has_aggs: bool
    has_window_funcs: bool
    has_target_srfs: bool
    has_sub_links: bool
    has_distinct_on: bool
    has_recursive: bool
    has_modifying_cte: bool
    has_for_update: bool
    has_row_security: bool
    is_return: bool
    cte_list: _containers.RepeatedCompositeFieldContainer[Node]
    rtable: _containers.RepeatedCompositeFieldContainer[Node]
    rteperminfos: _containers.RepeatedCompositeFieldContainer[Node]
    jointree: FromExpr
    merge_action_list: _containers.RepeatedCompositeFieldContainer[Node]
    merge_use_outer_join: bool
    target_list: _containers.RepeatedCompositeFieldContainer[Node]
    override: OverridingKind
    on_conflict: OnConflictExpr
    returning_list: _containers.RepeatedCompositeFieldContainer[Node]
    group_clause: _containers.RepeatedCompositeFieldContainer[Node]
    group_distinct: bool
    grouping_sets: _containers.RepeatedCompositeFieldContainer[Node]
    having_qual: Node
    window_clause: _containers.RepeatedCompositeFieldContainer[Node]
    distinct_clause: _containers.RepeatedCompositeFieldContainer[Node]
    sort_clause: _containers.RepeatedCompositeFieldContainer[Node]
    limit_offset: Node
    limit_count: Node
    limit_option: LimitOption
    row_marks: _containers.RepeatedCompositeFieldContainer[Node]
    set_operations: Node
    constraint_deps: _containers.RepeatedCompositeFieldContainer[Node]
    with_check_options: _containers.RepeatedCompositeFieldContainer[Node]
    stmt_location: int
    stmt_len: int
    def __init__(
        self,
        command_type: _Optional[_Union[CmdType, str]] = ...,
        query_source: _Optional[_Union[QuerySource, str]] = ...,
        can_set_tag: bool = ...,
        utility_stmt: _Optional[_Union[Node, _Mapping]] = ...,
        result_relation: _Optional[int] = ...,
        has_aggs: bool = ...,
        has_window_funcs: bool = ...,
        has_target_srfs: bool = ...,
        has_sub_links: bool = ...,
        has_distinct_on: bool = ...,
        has_recursive: bool = ...,
        has_modifying_cte: bool = ...,
        has_for_update: bool = ...,
        has_row_security: bool = ...,
        is_return: bool = ...,
        cte_list: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        rtable: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        rteperminfos: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        jointree: _Optional[_Union[FromExpr, _Mapping]] = ...,
        merge_action_list: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        merge_use_outer_join: bool = ...,
        target_list: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        override: _Optional[_Union[OverridingKind, str]] = ...,
        on_conflict: _Optional[_Union[OnConflictExpr, _Mapping]] = ...,
        returning_list: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        group_clause: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        group_distinct: bool = ...,
        grouping_sets: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        having_qual: _Optional[_Union[Node, _Mapping]] = ...,
        window_clause: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        distinct_clause: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        sort_clause: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        limit_offset: _Optional[_Union[Node, _Mapping]] = ...,
        limit_count: _Optional[_Union[Node, _Mapping]] = ...,
        limit_option: _Optional[_Union[LimitOption, str]] = ...,
        row_marks: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        set_operations: _Optional[_Union[Node, _Mapping]] = ...,
        constraint_deps: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        with_check_options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        stmt_location: _Optional[int] = ...,
        stmt_len: _Optional[int] = ...,
    ) -> None: ...

class TypeName(_message.Message):
    __slots__ = ("names", "type_oid", "setof", "pct_type", "typmods", "typemod", "array_bounds", "location")
    NAMES_FIELD_NUMBER: _ClassVar[int]
    TYPE_OID_FIELD_NUMBER: _ClassVar[int]
    SETOF_FIELD_NUMBER: _ClassVar[int]
    PCT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TYPMODS_FIELD_NUMBER: _ClassVar[int]
    TYPEMOD_FIELD_NUMBER: _ClassVar[int]
    ARRAY_BOUNDS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    names: _containers.RepeatedCompositeFieldContainer[Node]
    type_oid: int
    setof: bool
    pct_type: bool
    typmods: _containers.RepeatedCompositeFieldContainer[Node]
    typemod: int
    array_bounds: _containers.RepeatedCompositeFieldContainer[Node]
    location: int
    def __init__(
        self,
        names: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        type_oid: _Optional[int] = ...,
        setof: bool = ...,
        pct_type: bool = ...,
        typmods: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        typemod: _Optional[int] = ...,
        array_bounds: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class ColumnRef(_message.Message):
    __slots__ = ("fields", "location")
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.RepeatedCompositeFieldContainer[Node]
    location: int
    def __init__(
        self, fields: _Optional[_Iterable[_Union[Node, _Mapping]]] = ..., location: _Optional[int] = ...
    ) -> None: ...

class ParamRef(_message.Message):
    __slots__ = ("number", "location")
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    number: int
    location: int
    def __init__(self, number: _Optional[int] = ..., location: _Optional[int] = ...) -> None: ...

class A_Expr(_message.Message):
    __slots__ = ("kind", "name", "lexpr", "rexpr", "location")
    KIND_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LEXPR_FIELD_NUMBER: _ClassVar[int]
    REXPR_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    kind: A_Expr_Kind
    name: _containers.RepeatedCompositeFieldContainer[Node]
    lexpr: Node
    rexpr: Node
    location: int
    def __init__(
        self,
        kind: _Optional[_Union[A_Expr_Kind, str]] = ...,
        name: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        lexpr: _Optional[_Union[Node, _Mapping]] = ...,
        rexpr: _Optional[_Union[Node, _Mapping]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class TypeCast(_message.Message):
    __slots__ = ("arg", "type_name", "location")
    ARG_FIELD_NUMBER: _ClassVar[int]
    TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    arg: Node
    type_name: TypeName
    location: int
    def __init__(
        self,
        arg: _Optional[_Union[Node, _Mapping]] = ...,
        type_name: _Optional[_Union[TypeName, _Mapping]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class CollateClause(_message.Message):
    __slots__ = ("arg", "collname", "location")
    ARG_FIELD_NUMBER: _ClassVar[int]
    COLLNAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    arg: Node
    collname: _containers.RepeatedCompositeFieldContainer[Node]
    location: int
    def __init__(
        self,
        arg: _Optional[_Union[Node, _Mapping]] = ...,
        collname: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class RoleSpec(_message.Message):
    __slots__ = ("roletype", "rolename", "location")
    ROLETYPE_FIELD_NUMBER: _ClassVar[int]
    ROLENAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    roletype: RoleSpecType
    rolename: str
    location: int
    def __init__(
        self,
        roletype: _Optional[_Union[RoleSpecType, str]] = ...,
        rolename: _Optional[str] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class FuncCall(_message.Message):
    __slots__ = (
        "funcname",
        "args",
        "agg_order",
        "agg_filter",
        "over",
        "agg_within_group",
        "agg_star",
        "agg_distinct",
        "func_variadic",
        "funcformat",
        "location",
    )
    FUNCNAME_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    AGG_ORDER_FIELD_NUMBER: _ClassVar[int]
    AGG_FILTER_FIELD_NUMBER: _ClassVar[int]
    OVER_FIELD_NUMBER: _ClassVar[int]
    AGG_WITHIN_GROUP_FIELD_NUMBER: _ClassVar[int]
    AGG_STAR_FIELD_NUMBER: _ClassVar[int]
    AGG_DISTINCT_FIELD_NUMBER: _ClassVar[int]
    FUNC_VARIADIC_FIELD_NUMBER: _ClassVar[int]
    FUNCFORMAT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    funcname: _containers.RepeatedCompositeFieldContainer[Node]
    args: _containers.RepeatedCompositeFieldContainer[Node]
    agg_order: _containers.RepeatedCompositeFieldContainer[Node]
    agg_filter: Node
    over: WindowDef
    agg_within_group: bool
    agg_star: bool
    agg_distinct: bool
    func_variadic: bool
    funcformat: CoercionForm
    location: int
    def __init__(
        self,
        funcname: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        args: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        agg_order: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        agg_filter: _Optional[_Union[Node, _Mapping]] = ...,
        over: _Optional[_Union[WindowDef, _Mapping]] = ...,
        agg_within_group: bool = ...,
        agg_star: bool = ...,
        agg_distinct: bool = ...,
        func_variadic: bool = ...,
        funcformat: _Optional[_Union[CoercionForm, str]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class A_Star(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class A_Indices(_message.Message):
    __slots__ = ("is_slice", "lidx", "uidx")
    IS_SLICE_FIELD_NUMBER: _ClassVar[int]
    LIDX_FIELD_NUMBER: _ClassVar[int]
    UIDX_FIELD_NUMBER: _ClassVar[int]
    is_slice: bool
    lidx: Node
    uidx: Node
    def __init__(
        self,
        is_slice: bool = ...,
        lidx: _Optional[_Union[Node, _Mapping]] = ...,
        uidx: _Optional[_Union[Node, _Mapping]] = ...,
    ) -> None: ...

class A_Indirection(_message.Message):
    __slots__ = ("arg", "indirection")
    ARG_FIELD_NUMBER: _ClassVar[int]
    INDIRECTION_FIELD_NUMBER: _ClassVar[int]
    arg: Node
    indirection: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        arg: _Optional[_Union[Node, _Mapping]] = ...,
        indirection: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class A_ArrayExpr(_message.Message):
    __slots__ = ("elements", "location")
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    elements: _containers.RepeatedCompositeFieldContainer[Node]
    location: int
    def __init__(
        self, elements: _Optional[_Iterable[_Union[Node, _Mapping]]] = ..., location: _Optional[int] = ...
    ) -> None: ...

class ResTarget(_message.Message):
    __slots__ = ("name", "indirection", "val", "location")
    NAME_FIELD_NUMBER: _ClassVar[int]
    INDIRECTION_FIELD_NUMBER: _ClassVar[int]
    VAL_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    indirection: _containers.RepeatedCompositeFieldContainer[Node]
    val: Node
    location: int
    def __init__(
        self,
        name: _Optional[str] = ...,
        indirection: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        val: _Optional[_Union[Node, _Mapping]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class MultiAssignRef(_message.Message):
    __slots__ = ("source", "colno", "ncolumns")
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    COLNO_FIELD_NUMBER: _ClassVar[int]
    NCOLUMNS_FIELD_NUMBER: _ClassVar[int]
    source: Node
    colno: int
    ncolumns: int
    def __init__(
        self,
        source: _Optional[_Union[Node, _Mapping]] = ...,
        colno: _Optional[int] = ...,
        ncolumns: _Optional[int] = ...,
    ) -> None: ...

class SortBy(_message.Message):
    __slots__ = ("node", "sortby_dir", "sortby_nulls", "use_op", "location")
    NODE_FIELD_NUMBER: _ClassVar[int]
    SORTBY_DIR_FIELD_NUMBER: _ClassVar[int]
    SORTBY_NULLS_FIELD_NUMBER: _ClassVar[int]
    USE_OP_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    node: Node
    sortby_dir: SortByDir
    sortby_nulls: SortByNulls
    use_op: _containers.RepeatedCompositeFieldContainer[Node]
    location: int
    def __init__(
        self,
        node: _Optional[_Union[Node, _Mapping]] = ...,
        sortby_dir: _Optional[_Union[SortByDir, str]] = ...,
        sortby_nulls: _Optional[_Union[SortByNulls, str]] = ...,
        use_op: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class WindowDef(_message.Message):
    __slots__ = (
        "name",
        "refname",
        "partition_clause",
        "order_clause",
        "frame_options",
        "start_offset",
        "end_offset",
        "location",
    )
    NAME_FIELD_NUMBER: _ClassVar[int]
    REFNAME_FIELD_NUMBER: _ClassVar[int]
    PARTITION_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    ORDER_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    FRAME_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    END_OFFSET_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    refname: str
    partition_clause: _containers.RepeatedCompositeFieldContainer[Node]
    order_clause: _containers.RepeatedCompositeFieldContainer[Node]
    frame_options: int
    start_offset: Node
    end_offset: Node
    location: int
    def __init__(
        self,
        name: _Optional[str] = ...,
        refname: _Optional[str] = ...,
        partition_clause: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        order_clause: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        frame_options: _Optional[int] = ...,
        start_offset: _Optional[_Union[Node, _Mapping]] = ...,
        end_offset: _Optional[_Union[Node, _Mapping]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class RangeSubselect(_message.Message):
    __slots__ = ("lateral", "subquery", "alias")
    LATERAL_FIELD_NUMBER: _ClassVar[int]
    SUBQUERY_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    lateral: bool
    subquery: Node
    alias: Alias
    def __init__(
        self,
        lateral: bool = ...,
        subquery: _Optional[_Union[Node, _Mapping]] = ...,
        alias: _Optional[_Union[Alias, _Mapping]] = ...,
    ) -> None: ...

class RangeFunction(_message.Message):
    __slots__ = ("lateral", "ordinality", "is_rowsfrom", "functions", "alias", "coldeflist")
    LATERAL_FIELD_NUMBER: _ClassVar[int]
    ORDINALITY_FIELD_NUMBER: _ClassVar[int]
    IS_ROWSFROM_FIELD_NUMBER: _ClassVar[int]
    FUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    COLDEFLIST_FIELD_NUMBER: _ClassVar[int]
    lateral: bool
    ordinality: bool
    is_rowsfrom: bool
    functions: _containers.RepeatedCompositeFieldContainer[Node]
    alias: Alias
    coldeflist: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        lateral: bool = ...,
        ordinality: bool = ...,
        is_rowsfrom: bool = ...,
        functions: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        alias: _Optional[_Union[Alias, _Mapping]] = ...,
        coldeflist: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class RangeTableFunc(_message.Message):
    __slots__ = ("lateral", "docexpr", "rowexpr", "namespaces", "columns", "alias", "location")
    LATERAL_FIELD_NUMBER: _ClassVar[int]
    DOCEXPR_FIELD_NUMBER: _ClassVar[int]
    ROWEXPR_FIELD_NUMBER: _ClassVar[int]
    NAMESPACES_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    lateral: bool
    docexpr: Node
    rowexpr: Node
    namespaces: _containers.RepeatedCompositeFieldContainer[Node]
    columns: _containers.RepeatedCompositeFieldContainer[Node]
    alias: Alias
    location: int
    def __init__(
        self,
        lateral: bool = ...,
        docexpr: _Optional[_Union[Node, _Mapping]] = ...,
        rowexpr: _Optional[_Union[Node, _Mapping]] = ...,
        namespaces: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        columns: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        alias: _Optional[_Union[Alias, _Mapping]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class RangeTableFuncCol(_message.Message):
    __slots__ = ("colname", "type_name", "for_ordinality", "is_not_null", "colexpr", "coldefexpr", "location")
    COLNAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    FOR_ORDINALITY_FIELD_NUMBER: _ClassVar[int]
    IS_NOT_NULL_FIELD_NUMBER: _ClassVar[int]
    COLEXPR_FIELD_NUMBER: _ClassVar[int]
    COLDEFEXPR_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    colname: str
    type_name: TypeName
    for_ordinality: bool
    is_not_null: bool
    colexpr: Node
    coldefexpr: Node
    location: int
    def __init__(
        self,
        colname: _Optional[str] = ...,
        type_name: _Optional[_Union[TypeName, _Mapping]] = ...,
        for_ordinality: bool = ...,
        is_not_null: bool = ...,
        colexpr: _Optional[_Union[Node, _Mapping]] = ...,
        coldefexpr: _Optional[_Union[Node, _Mapping]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class RangeTableSample(_message.Message):
    __slots__ = ("relation", "method", "args", "repeatable", "location")
    RELATION_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    REPEATABLE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    relation: Node
    method: _containers.RepeatedCompositeFieldContainer[Node]
    args: _containers.RepeatedCompositeFieldContainer[Node]
    repeatable: Node
    location: int
    def __init__(
        self,
        relation: _Optional[_Union[Node, _Mapping]] = ...,
        method: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        args: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        repeatable: _Optional[_Union[Node, _Mapping]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class ColumnDef(_message.Message):
    __slots__ = (
        "colname",
        "type_name",
        "compression",
        "inhcount",
        "is_local",
        "is_not_null",
        "is_from_type",
        "storage",
        "storage_name",
        "raw_default",
        "cooked_default",
        "identity",
        "identity_sequence",
        "generated",
        "coll_clause",
        "coll_oid",
        "constraints",
        "fdwoptions",
        "location",
    )
    COLNAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    INHCOUNT_FIELD_NUMBER: _ClassVar[int]
    IS_LOCAL_FIELD_NUMBER: _ClassVar[int]
    IS_NOT_NULL_FIELD_NUMBER: _ClassVar[int]
    IS_FROM_TYPE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    RAW_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    COOKED_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    GENERATED_FIELD_NUMBER: _ClassVar[int]
    COLL_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    COLL_OID_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    FDWOPTIONS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    colname: str
    type_name: TypeName
    compression: str
    inhcount: int
    is_local: bool
    is_not_null: bool
    is_from_type: bool
    storage: str
    storage_name: str
    raw_default: Node
    cooked_default: Node
    identity: str
    identity_sequence: RangeVar
    generated: str
    coll_clause: CollateClause
    coll_oid: int
    constraints: _containers.RepeatedCompositeFieldContainer[Node]
    fdwoptions: _containers.RepeatedCompositeFieldContainer[Node]
    location: int
    def __init__(
        self,
        colname: _Optional[str] = ...,
        type_name: _Optional[_Union[TypeName, _Mapping]] = ...,
        compression: _Optional[str] = ...,
        inhcount: _Optional[int] = ...,
        is_local: bool = ...,
        is_not_null: bool = ...,
        is_from_type: bool = ...,
        storage: _Optional[str] = ...,
        storage_name: _Optional[str] = ...,
        raw_default: _Optional[_Union[Node, _Mapping]] = ...,
        cooked_default: _Optional[_Union[Node, _Mapping]] = ...,
        identity: _Optional[str] = ...,
        identity_sequence: _Optional[_Union[RangeVar, _Mapping]] = ...,
        generated: _Optional[str] = ...,
        coll_clause: _Optional[_Union[CollateClause, _Mapping]] = ...,
        coll_oid: _Optional[int] = ...,
        constraints: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        fdwoptions: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class TableLikeClause(_message.Message):
    __slots__ = ("relation", "options", "relation_oid")
    RELATION_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    RELATION_OID_FIELD_NUMBER: _ClassVar[int]
    relation: RangeVar
    options: int
    relation_oid: int
    def __init__(
        self,
        relation: _Optional[_Union[RangeVar, _Mapping]] = ...,
        options: _Optional[int] = ...,
        relation_oid: _Optional[int] = ...,
    ) -> None: ...

class IndexElem(_message.Message):
    __slots__ = ("name", "expr", "indexcolname", "collation", "opclass", "opclassopts", "ordering", "nulls_ordering")
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    INDEXCOLNAME_FIELD_NUMBER: _ClassVar[int]
    COLLATION_FIELD_NUMBER: _ClassVar[int]
    OPCLASS_FIELD_NUMBER: _ClassVar[int]
    OPCLASSOPTS_FIELD_NUMBER: _ClassVar[int]
    ORDERING_FIELD_NUMBER: _ClassVar[int]
    NULLS_ORDERING_FIELD_NUMBER: _ClassVar[int]
    name: str
    expr: Node
    indexcolname: str
    collation: _containers.RepeatedCompositeFieldContainer[Node]
    opclass: _containers.RepeatedCompositeFieldContainer[Node]
    opclassopts: _containers.RepeatedCompositeFieldContainer[Node]
    ordering: SortByDir
    nulls_ordering: SortByNulls
    def __init__(
        self,
        name: _Optional[str] = ...,
        expr: _Optional[_Union[Node, _Mapping]] = ...,
        indexcolname: _Optional[str] = ...,
        collation: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        opclass: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        opclassopts: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        ordering: _Optional[_Union[SortByDir, str]] = ...,
        nulls_ordering: _Optional[_Union[SortByNulls, str]] = ...,
    ) -> None: ...

class DefElem(_message.Message):
    __slots__ = ("defnamespace", "defname", "arg", "defaction", "location")
    DEFNAMESPACE_FIELD_NUMBER: _ClassVar[int]
    DEFNAME_FIELD_NUMBER: _ClassVar[int]
    ARG_FIELD_NUMBER: _ClassVar[int]
    DEFACTION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    defnamespace: str
    defname: str
    arg: Node
    defaction: DefElemAction
    location: int
    def __init__(
        self,
        defnamespace: _Optional[str] = ...,
        defname: _Optional[str] = ...,
        arg: _Optional[_Union[Node, _Mapping]] = ...,
        defaction: _Optional[_Union[DefElemAction, str]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class LockingClause(_message.Message):
    __slots__ = ("locked_rels", "strength", "wait_policy")
    LOCKED_RELS_FIELD_NUMBER: _ClassVar[int]
    STRENGTH_FIELD_NUMBER: _ClassVar[int]
    WAIT_POLICY_FIELD_NUMBER: _ClassVar[int]
    locked_rels: _containers.RepeatedCompositeFieldContainer[Node]
    strength: LockClauseStrength
    wait_policy: LockWaitPolicy
    def __init__(
        self,
        locked_rels: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        strength: _Optional[_Union[LockClauseStrength, str]] = ...,
        wait_policy: _Optional[_Union[LockWaitPolicy, str]] = ...,
    ) -> None: ...

class XmlSerialize(_message.Message):
    __slots__ = ("xmloption", "expr", "type_name", "indent", "location")
    XMLOPTION_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    INDENT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    xmloption: XmlOptionType
    expr: Node
    type_name: TypeName
    indent: bool
    location: int
    def __init__(
        self,
        xmloption: _Optional[_Union[XmlOptionType, str]] = ...,
        expr: _Optional[_Union[Node, _Mapping]] = ...,
        type_name: _Optional[_Union[TypeName, _Mapping]] = ...,
        indent: bool = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class PartitionElem(_message.Message):
    __slots__ = ("name", "expr", "collation", "opclass", "location")
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    COLLATION_FIELD_NUMBER: _ClassVar[int]
    OPCLASS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    expr: Node
    collation: _containers.RepeatedCompositeFieldContainer[Node]
    opclass: _containers.RepeatedCompositeFieldContainer[Node]
    location: int
    def __init__(
        self,
        name: _Optional[str] = ...,
        expr: _Optional[_Union[Node, _Mapping]] = ...,
        collation: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        opclass: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class PartitionSpec(_message.Message):
    __slots__ = ("strategy", "part_params", "location")
    STRATEGY_FIELD_NUMBER: _ClassVar[int]
    PART_PARAMS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    strategy: PartitionStrategy
    part_params: _containers.RepeatedCompositeFieldContainer[Node]
    location: int
    def __init__(
        self,
        strategy: _Optional[_Union[PartitionStrategy, str]] = ...,
        part_params: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class PartitionBoundSpec(_message.Message):
    __slots__ = (
        "strategy",
        "is_default",
        "modulus",
        "remainder",
        "listdatums",
        "lowerdatums",
        "upperdatums",
        "location",
    )
    STRATEGY_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    MODULUS_FIELD_NUMBER: _ClassVar[int]
    REMAINDER_FIELD_NUMBER: _ClassVar[int]
    LISTDATUMS_FIELD_NUMBER: _ClassVar[int]
    LOWERDATUMS_FIELD_NUMBER: _ClassVar[int]
    UPPERDATUMS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    strategy: str
    is_default: bool
    modulus: int
    remainder: int
    listdatums: _containers.RepeatedCompositeFieldContainer[Node]
    lowerdatums: _containers.RepeatedCompositeFieldContainer[Node]
    upperdatums: _containers.RepeatedCompositeFieldContainer[Node]
    location: int
    def __init__(
        self,
        strategy: _Optional[str] = ...,
        is_default: bool = ...,
        modulus: _Optional[int] = ...,
        remainder: _Optional[int] = ...,
        listdatums: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        lowerdatums: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        upperdatums: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class PartitionRangeDatum(_message.Message):
    __slots__ = ("kind", "value", "location")
    KIND_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    kind: PartitionRangeDatumKind
    value: Node
    location: int
    def __init__(
        self,
        kind: _Optional[_Union[PartitionRangeDatumKind, str]] = ...,
        value: _Optional[_Union[Node, _Mapping]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class PartitionCmd(_message.Message):
    __slots__ = ("name", "bound", "concurrent")
    NAME_FIELD_NUMBER: _ClassVar[int]
    BOUND_FIELD_NUMBER: _ClassVar[int]
    CONCURRENT_FIELD_NUMBER: _ClassVar[int]
    name: RangeVar
    bound: PartitionBoundSpec
    concurrent: bool
    def __init__(
        self,
        name: _Optional[_Union[RangeVar, _Mapping]] = ...,
        bound: _Optional[_Union[PartitionBoundSpec, _Mapping]] = ...,
        concurrent: bool = ...,
    ) -> None: ...

class RangeTblEntry(_message.Message):
    __slots__ = (
        "rtekind",
        "relid",
        "relkind",
        "rellockmode",
        "tablesample",
        "perminfoindex",
        "subquery",
        "security_barrier",
        "jointype",
        "joinmergedcols",
        "joinaliasvars",
        "joinleftcols",
        "joinrightcols",
        "join_using_alias",
        "functions",
        "funcordinality",
        "tablefunc",
        "values_lists",
        "ctename",
        "ctelevelsup",
        "self_reference",
        "coltypes",
        "coltypmods",
        "colcollations",
        "enrname",
        "enrtuples",
        "alias",
        "eref",
        "lateral",
        "inh",
        "in_from_cl",
        "security_quals",
    )
    RTEKIND_FIELD_NUMBER: _ClassVar[int]
    RELID_FIELD_NUMBER: _ClassVar[int]
    RELKIND_FIELD_NUMBER: _ClassVar[int]
    RELLOCKMODE_FIELD_NUMBER: _ClassVar[int]
    TABLESAMPLE_FIELD_NUMBER: _ClassVar[int]
    PERMINFOINDEX_FIELD_NUMBER: _ClassVar[int]
    SUBQUERY_FIELD_NUMBER: _ClassVar[int]
    SECURITY_BARRIER_FIELD_NUMBER: _ClassVar[int]
    JOINTYPE_FIELD_NUMBER: _ClassVar[int]
    JOINMERGEDCOLS_FIELD_NUMBER: _ClassVar[int]
    JOINALIASVARS_FIELD_NUMBER: _ClassVar[int]
    JOINLEFTCOLS_FIELD_NUMBER: _ClassVar[int]
    JOINRIGHTCOLS_FIELD_NUMBER: _ClassVar[int]
    JOIN_USING_ALIAS_FIELD_NUMBER: _ClassVar[int]
    FUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    FUNCORDINALITY_FIELD_NUMBER: _ClassVar[int]
    TABLEFUNC_FIELD_NUMBER: _ClassVar[int]
    VALUES_LISTS_FIELD_NUMBER: _ClassVar[int]
    CTENAME_FIELD_NUMBER: _ClassVar[int]
    CTELEVELSUP_FIELD_NUMBER: _ClassVar[int]
    SELF_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    COLTYPES_FIELD_NUMBER: _ClassVar[int]
    COLTYPMODS_FIELD_NUMBER: _ClassVar[int]
    COLCOLLATIONS_FIELD_NUMBER: _ClassVar[int]
    ENRNAME_FIELD_NUMBER: _ClassVar[int]
    ENRTUPLES_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    EREF_FIELD_NUMBER: _ClassVar[int]
    LATERAL_FIELD_NUMBER: _ClassVar[int]
    INH_FIELD_NUMBER: _ClassVar[int]
    IN_FROM_CL_FIELD_NUMBER: _ClassVar[int]
    SECURITY_QUALS_FIELD_NUMBER: _ClassVar[int]
    rtekind: RTEKind
    relid: int
    relkind: str
    rellockmode: int
    tablesample: TableSampleClause
    perminfoindex: int
    subquery: Query
    security_barrier: bool
    jointype: JoinType
    joinmergedcols: int
    joinaliasvars: _containers.RepeatedCompositeFieldContainer[Node]
    joinleftcols: _containers.RepeatedCompositeFieldContainer[Node]
    joinrightcols: _containers.RepeatedCompositeFieldContainer[Node]
    join_using_alias: Alias
    functions: _containers.RepeatedCompositeFieldContainer[Node]
    funcordinality: bool
    tablefunc: TableFunc
    values_lists: _containers.RepeatedCompositeFieldContainer[Node]
    ctename: str
    ctelevelsup: int
    self_reference: bool
    coltypes: _containers.RepeatedCompositeFieldContainer[Node]
    coltypmods: _containers.RepeatedCompositeFieldContainer[Node]
    colcollations: _containers.RepeatedCompositeFieldContainer[Node]
    enrname: str
    enrtuples: float
    alias: Alias
    eref: Alias
    lateral: bool
    inh: bool
    in_from_cl: bool
    security_quals: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        rtekind: _Optional[_Union[RTEKind, str]] = ...,
        relid: _Optional[int] = ...,
        relkind: _Optional[str] = ...,
        rellockmode: _Optional[int] = ...,
        tablesample: _Optional[_Union[TableSampleClause, _Mapping]] = ...,
        perminfoindex: _Optional[int] = ...,
        subquery: _Optional[_Union[Query, _Mapping]] = ...,
        security_barrier: bool = ...,
        jointype: _Optional[_Union[JoinType, str]] = ...,
        joinmergedcols: _Optional[int] = ...,
        joinaliasvars: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        joinleftcols: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        joinrightcols: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        join_using_alias: _Optional[_Union[Alias, _Mapping]] = ...,
        functions: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        funcordinality: bool = ...,
        tablefunc: _Optional[_Union[TableFunc, _Mapping]] = ...,
        values_lists: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        ctename: _Optional[str] = ...,
        ctelevelsup: _Optional[int] = ...,
        self_reference: bool = ...,
        coltypes: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        coltypmods: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        colcollations: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        enrname: _Optional[str] = ...,
        enrtuples: _Optional[float] = ...,
        alias: _Optional[_Union[Alias, _Mapping]] = ...,
        eref: _Optional[_Union[Alias, _Mapping]] = ...,
        lateral: bool = ...,
        inh: bool = ...,
        in_from_cl: bool = ...,
        security_quals: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class RTEPermissionInfo(_message.Message):
    __slots__ = ("relid", "inh", "required_perms", "check_as_user", "selected_cols", "inserted_cols", "updated_cols")
    RELID_FIELD_NUMBER: _ClassVar[int]
    INH_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_PERMS_FIELD_NUMBER: _ClassVar[int]
    CHECK_AS_USER_FIELD_NUMBER: _ClassVar[int]
    SELECTED_COLS_FIELD_NUMBER: _ClassVar[int]
    INSERTED_COLS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_COLS_FIELD_NUMBER: _ClassVar[int]
    relid: int
    inh: bool
    required_perms: int
    check_as_user: int
    selected_cols: _containers.RepeatedScalarFieldContainer[int]
    inserted_cols: _containers.RepeatedScalarFieldContainer[int]
    updated_cols: _containers.RepeatedScalarFieldContainer[int]
    def __init__(
        self,
        relid: _Optional[int] = ...,
        inh: bool = ...,
        required_perms: _Optional[int] = ...,
        check_as_user: _Optional[int] = ...,
        selected_cols: _Optional[_Iterable[int]] = ...,
        inserted_cols: _Optional[_Iterable[int]] = ...,
        updated_cols: _Optional[_Iterable[int]] = ...,
    ) -> None: ...

class RangeTblFunction(_message.Message):
    __slots__ = (
        "funcexpr",
        "funccolcount",
        "funccolnames",
        "funccoltypes",
        "funccoltypmods",
        "funccolcollations",
        "funcparams",
    )
    FUNCEXPR_FIELD_NUMBER: _ClassVar[int]
    FUNCCOLCOUNT_FIELD_NUMBER: _ClassVar[int]
    FUNCCOLNAMES_FIELD_NUMBER: _ClassVar[int]
    FUNCCOLTYPES_FIELD_NUMBER: _ClassVar[int]
    FUNCCOLTYPMODS_FIELD_NUMBER: _ClassVar[int]
    FUNCCOLCOLLATIONS_FIELD_NUMBER: _ClassVar[int]
    FUNCPARAMS_FIELD_NUMBER: _ClassVar[int]
    funcexpr: Node
    funccolcount: int
    funccolnames: _containers.RepeatedCompositeFieldContainer[Node]
    funccoltypes: _containers.RepeatedCompositeFieldContainer[Node]
    funccoltypmods: _containers.RepeatedCompositeFieldContainer[Node]
    funccolcollations: _containers.RepeatedCompositeFieldContainer[Node]
    funcparams: _containers.RepeatedScalarFieldContainer[int]
    def __init__(
        self,
        funcexpr: _Optional[_Union[Node, _Mapping]] = ...,
        funccolcount: _Optional[int] = ...,
        funccolnames: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        funccoltypes: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        funccoltypmods: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        funccolcollations: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        funcparams: _Optional[_Iterable[int]] = ...,
    ) -> None: ...

class TableSampleClause(_message.Message):
    __slots__ = ("tsmhandler", "args", "repeatable")
    TSMHANDLER_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    REPEATABLE_FIELD_NUMBER: _ClassVar[int]
    tsmhandler: int
    args: _containers.RepeatedCompositeFieldContainer[Node]
    repeatable: Node
    def __init__(
        self,
        tsmhandler: _Optional[int] = ...,
        args: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        repeatable: _Optional[_Union[Node, _Mapping]] = ...,
    ) -> None: ...

class WithCheckOption(_message.Message):
    __slots__ = ("kind", "relname", "polname", "qual", "cascaded")
    KIND_FIELD_NUMBER: _ClassVar[int]
    RELNAME_FIELD_NUMBER: _ClassVar[int]
    POLNAME_FIELD_NUMBER: _ClassVar[int]
    QUAL_FIELD_NUMBER: _ClassVar[int]
    CASCADED_FIELD_NUMBER: _ClassVar[int]
    kind: WCOKind
    relname: str
    polname: str
    qual: Node
    cascaded: bool
    def __init__(
        self,
        kind: _Optional[_Union[WCOKind, str]] = ...,
        relname: _Optional[str] = ...,
        polname: _Optional[str] = ...,
        qual: _Optional[_Union[Node, _Mapping]] = ...,
        cascaded: bool = ...,
    ) -> None: ...

class SortGroupClause(_message.Message):
    __slots__ = ("tle_sort_group_ref", "eqop", "sortop", "nulls_first", "hashable")
    TLE_SORT_GROUP_REF_FIELD_NUMBER: _ClassVar[int]
    EQOP_FIELD_NUMBER: _ClassVar[int]
    SORTOP_FIELD_NUMBER: _ClassVar[int]
    NULLS_FIRST_FIELD_NUMBER: _ClassVar[int]
    HASHABLE_FIELD_NUMBER: _ClassVar[int]
    tle_sort_group_ref: int
    eqop: int
    sortop: int
    nulls_first: bool
    hashable: bool
    def __init__(
        self,
        tle_sort_group_ref: _Optional[int] = ...,
        eqop: _Optional[int] = ...,
        sortop: _Optional[int] = ...,
        nulls_first: bool = ...,
        hashable: bool = ...,
    ) -> None: ...

class GroupingSet(_message.Message):
    __slots__ = ("kind", "content", "location")
    KIND_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    kind: GroupingSetKind
    content: _containers.RepeatedCompositeFieldContainer[Node]
    location: int
    def __init__(
        self,
        kind: _Optional[_Union[GroupingSetKind, str]] = ...,
        content: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class WindowClause(_message.Message):
    __slots__ = (
        "name",
        "refname",
        "partition_clause",
        "order_clause",
        "frame_options",
        "start_offset",
        "end_offset",
        "run_condition",
        "start_in_range_func",
        "end_in_range_func",
        "in_range_coll",
        "in_range_asc",
        "in_range_nulls_first",
        "winref",
        "copied_order",
    )
    NAME_FIELD_NUMBER: _ClassVar[int]
    REFNAME_FIELD_NUMBER: _ClassVar[int]
    PARTITION_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    ORDER_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    FRAME_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    END_OFFSET_FIELD_NUMBER: _ClassVar[int]
    RUN_CONDITION_FIELD_NUMBER: _ClassVar[int]
    START_IN_RANGE_FUNC_FIELD_NUMBER: _ClassVar[int]
    END_IN_RANGE_FUNC_FIELD_NUMBER: _ClassVar[int]
    IN_RANGE_COLL_FIELD_NUMBER: _ClassVar[int]
    IN_RANGE_ASC_FIELD_NUMBER: _ClassVar[int]
    IN_RANGE_NULLS_FIRST_FIELD_NUMBER: _ClassVar[int]
    WINREF_FIELD_NUMBER: _ClassVar[int]
    COPIED_ORDER_FIELD_NUMBER: _ClassVar[int]
    name: str
    refname: str
    partition_clause: _containers.RepeatedCompositeFieldContainer[Node]
    order_clause: _containers.RepeatedCompositeFieldContainer[Node]
    frame_options: int
    start_offset: Node
    end_offset: Node
    run_condition: _containers.RepeatedCompositeFieldContainer[Node]
    start_in_range_func: int
    end_in_range_func: int
    in_range_coll: int
    in_range_asc: bool
    in_range_nulls_first: bool
    winref: int
    copied_order: bool
    def __init__(
        self,
        name: _Optional[str] = ...,
        refname: _Optional[str] = ...,
        partition_clause: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        order_clause: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        frame_options: _Optional[int] = ...,
        start_offset: _Optional[_Union[Node, _Mapping]] = ...,
        end_offset: _Optional[_Union[Node, _Mapping]] = ...,
        run_condition: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        start_in_range_func: _Optional[int] = ...,
        end_in_range_func: _Optional[int] = ...,
        in_range_coll: _Optional[int] = ...,
        in_range_asc: bool = ...,
        in_range_nulls_first: bool = ...,
        winref: _Optional[int] = ...,
        copied_order: bool = ...,
    ) -> None: ...

class RowMarkClause(_message.Message):
    __slots__ = ("rti", "strength", "wait_policy", "pushed_down")
    RTI_FIELD_NUMBER: _ClassVar[int]
    STRENGTH_FIELD_NUMBER: _ClassVar[int]
    WAIT_POLICY_FIELD_NUMBER: _ClassVar[int]
    PUSHED_DOWN_FIELD_NUMBER: _ClassVar[int]
    rti: int
    strength: LockClauseStrength
    wait_policy: LockWaitPolicy
    pushed_down: bool
    def __init__(
        self,
        rti: _Optional[int] = ...,
        strength: _Optional[_Union[LockClauseStrength, str]] = ...,
        wait_policy: _Optional[_Union[LockWaitPolicy, str]] = ...,
        pushed_down: bool = ...,
    ) -> None: ...

class WithClause(_message.Message):
    __slots__ = ("ctes", "recursive", "location")
    CTES_FIELD_NUMBER: _ClassVar[int]
    RECURSIVE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    ctes: _containers.RepeatedCompositeFieldContainer[Node]
    recursive: bool
    location: int
    def __init__(
        self,
        ctes: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        recursive: bool = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class InferClause(_message.Message):
    __slots__ = ("index_elems", "where_clause", "conname", "location")
    INDEX_ELEMS_FIELD_NUMBER: _ClassVar[int]
    WHERE_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    CONNAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    index_elems: _containers.RepeatedCompositeFieldContainer[Node]
    where_clause: Node
    conname: str
    location: int
    def __init__(
        self,
        index_elems: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        where_clause: _Optional[_Union[Node, _Mapping]] = ...,
        conname: _Optional[str] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class OnConflictClause(_message.Message):
    __slots__ = ("action", "infer", "target_list", "where_clause", "location")
    ACTION_FIELD_NUMBER: _ClassVar[int]
    INFER_FIELD_NUMBER: _ClassVar[int]
    TARGET_LIST_FIELD_NUMBER: _ClassVar[int]
    WHERE_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    action: OnConflictAction
    infer: InferClause
    target_list: _containers.RepeatedCompositeFieldContainer[Node]
    where_clause: Node
    location: int
    def __init__(
        self,
        action: _Optional[_Union[OnConflictAction, str]] = ...,
        infer: _Optional[_Union[InferClause, _Mapping]] = ...,
        target_list: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        where_clause: _Optional[_Union[Node, _Mapping]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class CTESearchClause(_message.Message):
    __slots__ = ("search_col_list", "search_breadth_first", "search_seq_column", "location")
    SEARCH_COL_LIST_FIELD_NUMBER: _ClassVar[int]
    SEARCH_BREADTH_FIRST_FIELD_NUMBER: _ClassVar[int]
    SEARCH_SEQ_COLUMN_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    search_col_list: _containers.RepeatedCompositeFieldContainer[Node]
    search_breadth_first: bool
    search_seq_column: str
    location: int
    def __init__(
        self,
        search_col_list: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        search_breadth_first: bool = ...,
        search_seq_column: _Optional[str] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class CTECycleClause(_message.Message):
    __slots__ = (
        "cycle_col_list",
        "cycle_mark_column",
        "cycle_mark_value",
        "cycle_mark_default",
        "cycle_path_column",
        "location",
        "cycle_mark_type",
        "cycle_mark_typmod",
        "cycle_mark_collation",
        "cycle_mark_neop",
    )
    CYCLE_COL_LIST_FIELD_NUMBER: _ClassVar[int]
    CYCLE_MARK_COLUMN_FIELD_NUMBER: _ClassVar[int]
    CYCLE_MARK_VALUE_FIELD_NUMBER: _ClassVar[int]
    CYCLE_MARK_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    CYCLE_PATH_COLUMN_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    CYCLE_MARK_TYPE_FIELD_NUMBER: _ClassVar[int]
    CYCLE_MARK_TYPMOD_FIELD_NUMBER: _ClassVar[int]
    CYCLE_MARK_COLLATION_FIELD_NUMBER: _ClassVar[int]
    CYCLE_MARK_NEOP_FIELD_NUMBER: _ClassVar[int]
    cycle_col_list: _containers.RepeatedCompositeFieldContainer[Node]
    cycle_mark_column: str
    cycle_mark_value: Node
    cycle_mark_default: Node
    cycle_path_column: str
    location: int
    cycle_mark_type: int
    cycle_mark_typmod: int
    cycle_mark_collation: int
    cycle_mark_neop: int
    def __init__(
        self,
        cycle_col_list: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        cycle_mark_column: _Optional[str] = ...,
        cycle_mark_value: _Optional[_Union[Node, _Mapping]] = ...,
        cycle_mark_default: _Optional[_Union[Node, _Mapping]] = ...,
        cycle_path_column: _Optional[str] = ...,
        location: _Optional[int] = ...,
        cycle_mark_type: _Optional[int] = ...,
        cycle_mark_typmod: _Optional[int] = ...,
        cycle_mark_collation: _Optional[int] = ...,
        cycle_mark_neop: _Optional[int] = ...,
    ) -> None: ...

class CommonTableExpr(_message.Message):
    __slots__ = (
        "ctename",
        "aliascolnames",
        "ctematerialized",
        "ctequery",
        "search_clause",
        "cycle_clause",
        "location",
        "cterecursive",
        "cterefcount",
        "ctecolnames",
        "ctecoltypes",
        "ctecoltypmods",
        "ctecolcollations",
    )
    CTENAME_FIELD_NUMBER: _ClassVar[int]
    ALIASCOLNAMES_FIELD_NUMBER: _ClassVar[int]
    CTEMATERIALIZED_FIELD_NUMBER: _ClassVar[int]
    CTEQUERY_FIELD_NUMBER: _ClassVar[int]
    SEARCH_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    CYCLE_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    CTERECURSIVE_FIELD_NUMBER: _ClassVar[int]
    CTEREFCOUNT_FIELD_NUMBER: _ClassVar[int]
    CTECOLNAMES_FIELD_NUMBER: _ClassVar[int]
    CTECOLTYPES_FIELD_NUMBER: _ClassVar[int]
    CTECOLTYPMODS_FIELD_NUMBER: _ClassVar[int]
    CTECOLCOLLATIONS_FIELD_NUMBER: _ClassVar[int]
    ctename: str
    aliascolnames: _containers.RepeatedCompositeFieldContainer[Node]
    ctematerialized: CTEMaterialize
    ctequery: Node
    search_clause: CTESearchClause
    cycle_clause: CTECycleClause
    location: int
    cterecursive: bool
    cterefcount: int
    ctecolnames: _containers.RepeatedCompositeFieldContainer[Node]
    ctecoltypes: _containers.RepeatedCompositeFieldContainer[Node]
    ctecoltypmods: _containers.RepeatedCompositeFieldContainer[Node]
    ctecolcollations: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        ctename: _Optional[str] = ...,
        aliascolnames: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        ctematerialized: _Optional[_Union[CTEMaterialize, str]] = ...,
        ctequery: _Optional[_Union[Node, _Mapping]] = ...,
        search_clause: _Optional[_Union[CTESearchClause, _Mapping]] = ...,
        cycle_clause: _Optional[_Union[CTECycleClause, _Mapping]] = ...,
        location: _Optional[int] = ...,
        cterecursive: bool = ...,
        cterefcount: _Optional[int] = ...,
        ctecolnames: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        ctecoltypes: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        ctecoltypmods: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        ctecolcollations: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class MergeWhenClause(_message.Message):
    __slots__ = ("matched", "command_type", "override", "condition", "target_list", "values")
    MATCHED_FIELD_NUMBER: _ClassVar[int]
    COMMAND_TYPE_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    TARGET_LIST_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    matched: bool
    command_type: CmdType
    override: OverridingKind
    condition: Node
    target_list: _containers.RepeatedCompositeFieldContainer[Node]
    values: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        matched: bool = ...,
        command_type: _Optional[_Union[CmdType, str]] = ...,
        override: _Optional[_Union[OverridingKind, str]] = ...,
        condition: _Optional[_Union[Node, _Mapping]] = ...,
        target_list: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        values: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class MergeAction(_message.Message):
    __slots__ = ("matched", "command_type", "override", "qual", "target_list", "update_colnos")
    MATCHED_FIELD_NUMBER: _ClassVar[int]
    COMMAND_TYPE_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    QUAL_FIELD_NUMBER: _ClassVar[int]
    TARGET_LIST_FIELD_NUMBER: _ClassVar[int]
    UPDATE_COLNOS_FIELD_NUMBER: _ClassVar[int]
    matched: bool
    command_type: CmdType
    override: OverridingKind
    qual: Node
    target_list: _containers.RepeatedCompositeFieldContainer[Node]
    update_colnos: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        matched: bool = ...,
        command_type: _Optional[_Union[CmdType, str]] = ...,
        override: _Optional[_Union[OverridingKind, str]] = ...,
        qual: _Optional[_Union[Node, _Mapping]] = ...,
        target_list: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        update_colnos: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class TriggerTransition(_message.Message):
    __slots__ = ("name", "is_new", "is_table")
    NAME_FIELD_NUMBER: _ClassVar[int]
    IS_NEW_FIELD_NUMBER: _ClassVar[int]
    IS_TABLE_FIELD_NUMBER: _ClassVar[int]
    name: str
    is_new: bool
    is_table: bool
    def __init__(self, name: _Optional[str] = ..., is_new: bool = ..., is_table: bool = ...) -> None: ...

class JsonOutput(_message.Message):
    __slots__ = ("type_name", "returning")
    TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    RETURNING_FIELD_NUMBER: _ClassVar[int]
    type_name: TypeName
    returning: JsonReturning
    def __init__(
        self,
        type_name: _Optional[_Union[TypeName, _Mapping]] = ...,
        returning: _Optional[_Union[JsonReturning, _Mapping]] = ...,
    ) -> None: ...

class JsonKeyValue(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: Node
    value: JsonValueExpr
    def __init__(
        self, key: _Optional[_Union[Node, _Mapping]] = ..., value: _Optional[_Union[JsonValueExpr, _Mapping]] = ...
    ) -> None: ...

class JsonObjectConstructor(_message.Message):
    __slots__ = ("exprs", "output", "absent_on_null", "unique", "location")
    EXPRS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    ABSENT_ON_NULL_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    exprs: _containers.RepeatedCompositeFieldContainer[Node]
    output: JsonOutput
    absent_on_null: bool
    unique: bool
    location: int
    def __init__(
        self,
        exprs: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        output: _Optional[_Union[JsonOutput, _Mapping]] = ...,
        absent_on_null: bool = ...,
        unique: bool = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class JsonArrayConstructor(_message.Message):
    __slots__ = ("exprs", "output", "absent_on_null", "location")
    EXPRS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    ABSENT_ON_NULL_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    exprs: _containers.RepeatedCompositeFieldContainer[Node]
    output: JsonOutput
    absent_on_null: bool
    location: int
    def __init__(
        self,
        exprs: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        output: _Optional[_Union[JsonOutput, _Mapping]] = ...,
        absent_on_null: bool = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class JsonArrayQueryConstructor(_message.Message):
    __slots__ = ("query", "output", "format", "absent_on_null", "location")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    ABSENT_ON_NULL_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    query: Node
    output: JsonOutput
    format: JsonFormat
    absent_on_null: bool
    location: int
    def __init__(
        self,
        query: _Optional[_Union[Node, _Mapping]] = ...,
        output: _Optional[_Union[JsonOutput, _Mapping]] = ...,
        format: _Optional[_Union[JsonFormat, _Mapping]] = ...,
        absent_on_null: bool = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class JsonAggConstructor(_message.Message):
    __slots__ = ("output", "agg_filter", "agg_order", "over", "location")
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    AGG_FILTER_FIELD_NUMBER: _ClassVar[int]
    AGG_ORDER_FIELD_NUMBER: _ClassVar[int]
    OVER_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    output: JsonOutput
    agg_filter: Node
    agg_order: _containers.RepeatedCompositeFieldContainer[Node]
    over: WindowDef
    location: int
    def __init__(
        self,
        output: _Optional[_Union[JsonOutput, _Mapping]] = ...,
        agg_filter: _Optional[_Union[Node, _Mapping]] = ...,
        agg_order: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        over: _Optional[_Union[WindowDef, _Mapping]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class JsonObjectAgg(_message.Message):
    __slots__ = ("constructor", "arg", "absent_on_null", "unique")
    CONSTRUCTOR_FIELD_NUMBER: _ClassVar[int]
    ARG_FIELD_NUMBER: _ClassVar[int]
    ABSENT_ON_NULL_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_FIELD_NUMBER: _ClassVar[int]
    constructor: JsonAggConstructor
    arg: JsonKeyValue
    absent_on_null: bool
    unique: bool
    def __init__(
        self,
        constructor: _Optional[_Union[JsonAggConstructor, _Mapping]] = ...,
        arg: _Optional[_Union[JsonKeyValue, _Mapping]] = ...,
        absent_on_null: bool = ...,
        unique: bool = ...,
    ) -> None: ...

class JsonArrayAgg(_message.Message):
    __slots__ = ("constructor", "arg", "absent_on_null")
    CONSTRUCTOR_FIELD_NUMBER: _ClassVar[int]
    ARG_FIELD_NUMBER: _ClassVar[int]
    ABSENT_ON_NULL_FIELD_NUMBER: _ClassVar[int]
    constructor: JsonAggConstructor
    arg: JsonValueExpr
    absent_on_null: bool
    def __init__(
        self,
        constructor: _Optional[_Union[JsonAggConstructor, _Mapping]] = ...,
        arg: _Optional[_Union[JsonValueExpr, _Mapping]] = ...,
        absent_on_null: bool = ...,
    ) -> None: ...

class RawStmt(_message.Message):
    __slots__ = ("stmt", "stmt_location", "stmt_len")
    STMT_FIELD_NUMBER: _ClassVar[int]
    STMT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    STMT_LEN_FIELD_NUMBER: _ClassVar[int]
    stmt: Node
    stmt_location: int
    stmt_len: int
    def __init__(
        self,
        stmt: _Optional[_Union[Node, _Mapping]] = ...,
        stmt_location: _Optional[int] = ...,
        stmt_len: _Optional[int] = ...,
    ) -> None: ...

class InsertStmt(_message.Message):
    __slots__ = ("relation", "cols", "select_stmt", "on_conflict_clause", "returning_list", "with_clause", "override")
    RELATION_FIELD_NUMBER: _ClassVar[int]
    COLS_FIELD_NUMBER: _ClassVar[int]
    SELECT_STMT_FIELD_NUMBER: _ClassVar[int]
    ON_CONFLICT_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    RETURNING_LIST_FIELD_NUMBER: _ClassVar[int]
    WITH_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    relation: RangeVar
    cols: _containers.RepeatedCompositeFieldContainer[Node]
    select_stmt: Node
    on_conflict_clause: OnConflictClause
    returning_list: _containers.RepeatedCompositeFieldContainer[Node]
    with_clause: WithClause
    override: OverridingKind
    def __init__(
        self,
        relation: _Optional[_Union[RangeVar, _Mapping]] = ...,
        cols: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        select_stmt: _Optional[_Union[Node, _Mapping]] = ...,
        on_conflict_clause: _Optional[_Union[OnConflictClause, _Mapping]] = ...,
        returning_list: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        with_clause: _Optional[_Union[WithClause, _Mapping]] = ...,
        override: _Optional[_Union[OverridingKind, str]] = ...,
    ) -> None: ...

class DeleteStmt(_message.Message):
    __slots__ = ("relation", "using_clause", "where_clause", "returning_list", "with_clause")
    RELATION_FIELD_NUMBER: _ClassVar[int]
    USING_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    WHERE_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    RETURNING_LIST_FIELD_NUMBER: _ClassVar[int]
    WITH_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    relation: RangeVar
    using_clause: _containers.RepeatedCompositeFieldContainer[Node]
    where_clause: Node
    returning_list: _containers.RepeatedCompositeFieldContainer[Node]
    with_clause: WithClause
    def __init__(
        self,
        relation: _Optional[_Union[RangeVar, _Mapping]] = ...,
        using_clause: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        where_clause: _Optional[_Union[Node, _Mapping]] = ...,
        returning_list: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        with_clause: _Optional[_Union[WithClause, _Mapping]] = ...,
    ) -> None: ...

class UpdateStmt(_message.Message):
    __slots__ = ("relation", "target_list", "where_clause", "from_clause", "returning_list", "with_clause")
    RELATION_FIELD_NUMBER: _ClassVar[int]
    TARGET_LIST_FIELD_NUMBER: _ClassVar[int]
    WHERE_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    FROM_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    RETURNING_LIST_FIELD_NUMBER: _ClassVar[int]
    WITH_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    relation: RangeVar
    target_list: _containers.RepeatedCompositeFieldContainer[Node]
    where_clause: Node
    from_clause: _containers.RepeatedCompositeFieldContainer[Node]
    returning_list: _containers.RepeatedCompositeFieldContainer[Node]
    with_clause: WithClause
    def __init__(
        self,
        relation: _Optional[_Union[RangeVar, _Mapping]] = ...,
        target_list: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        where_clause: _Optional[_Union[Node, _Mapping]] = ...,
        from_clause: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        returning_list: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        with_clause: _Optional[_Union[WithClause, _Mapping]] = ...,
    ) -> None: ...

class MergeStmt(_message.Message):
    __slots__ = ("relation", "source_relation", "join_condition", "merge_when_clauses", "with_clause")
    RELATION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_RELATION_FIELD_NUMBER: _ClassVar[int]
    JOIN_CONDITION_FIELD_NUMBER: _ClassVar[int]
    MERGE_WHEN_CLAUSES_FIELD_NUMBER: _ClassVar[int]
    WITH_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    relation: RangeVar
    source_relation: Node
    join_condition: Node
    merge_when_clauses: _containers.RepeatedCompositeFieldContainer[Node]
    with_clause: WithClause
    def __init__(
        self,
        relation: _Optional[_Union[RangeVar, _Mapping]] = ...,
        source_relation: _Optional[_Union[Node, _Mapping]] = ...,
        join_condition: _Optional[_Union[Node, _Mapping]] = ...,
        merge_when_clauses: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        with_clause: _Optional[_Union[WithClause, _Mapping]] = ...,
    ) -> None: ...

class SelectStmt(_message.Message):
    __slots__ = (
        "distinct_clause",
        "into_clause",
        "target_list",
        "from_clause",
        "where_clause",
        "group_clause",
        "group_distinct",
        "having_clause",
        "window_clause",
        "values_lists",
        "sort_clause",
        "limit_offset",
        "limit_count",
        "limit_option",
        "locking_clause",
        "with_clause",
        "op",
        "all",
        "larg",
        "rarg",
    )
    DISTINCT_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    INTO_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    TARGET_LIST_FIELD_NUMBER: _ClassVar[int]
    FROM_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    WHERE_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    GROUP_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    GROUP_DISTINCT_FIELD_NUMBER: _ClassVar[int]
    HAVING_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    WINDOW_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    VALUES_LISTS_FIELD_NUMBER: _ClassVar[int]
    SORT_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    LIMIT_COUNT_FIELD_NUMBER: _ClassVar[int]
    LIMIT_OPTION_FIELD_NUMBER: _ClassVar[int]
    LOCKING_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    WITH_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    OP_FIELD_NUMBER: _ClassVar[int]
    ALL_FIELD_NUMBER: _ClassVar[int]
    LARG_FIELD_NUMBER: _ClassVar[int]
    RARG_FIELD_NUMBER: _ClassVar[int]
    distinct_clause: _containers.RepeatedCompositeFieldContainer[Node]
    into_clause: IntoClause
    target_list: _containers.RepeatedCompositeFieldContainer[Node]
    from_clause: _containers.RepeatedCompositeFieldContainer[Node]
    where_clause: Node
    group_clause: _containers.RepeatedCompositeFieldContainer[Node]
    group_distinct: bool
    having_clause: Node
    window_clause: _containers.RepeatedCompositeFieldContainer[Node]
    values_lists: _containers.RepeatedCompositeFieldContainer[Node]
    sort_clause: _containers.RepeatedCompositeFieldContainer[Node]
    limit_offset: Node
    limit_count: Node
    limit_option: LimitOption
    locking_clause: _containers.RepeatedCompositeFieldContainer[Node]
    with_clause: WithClause
    op: SetOperation
    all: bool
    larg: SelectStmt
    rarg: SelectStmt
    def __init__(
        self,
        distinct_clause: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        into_clause: _Optional[_Union[IntoClause, _Mapping]] = ...,
        target_list: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        from_clause: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        where_clause: _Optional[_Union[Node, _Mapping]] = ...,
        group_clause: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        group_distinct: bool = ...,
        having_clause: _Optional[_Union[Node, _Mapping]] = ...,
        window_clause: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        values_lists: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        sort_clause: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        limit_offset: _Optional[_Union[Node, _Mapping]] = ...,
        limit_count: _Optional[_Union[Node, _Mapping]] = ...,
        limit_option: _Optional[_Union[LimitOption, str]] = ...,
        locking_clause: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        with_clause: _Optional[_Union[WithClause, _Mapping]] = ...,
        op: _Optional[_Union[SetOperation, str]] = ...,
        all: bool = ...,
        larg: _Optional[_Union[SelectStmt, _Mapping]] = ...,
        rarg: _Optional[_Union[SelectStmt, _Mapping]] = ...,
    ) -> None: ...

class SetOperationStmt(_message.Message):
    __slots__ = ("op", "all", "larg", "rarg", "col_types", "col_typmods", "col_collations", "group_clauses")
    OP_FIELD_NUMBER: _ClassVar[int]
    ALL_FIELD_NUMBER: _ClassVar[int]
    LARG_FIELD_NUMBER: _ClassVar[int]
    RARG_FIELD_NUMBER: _ClassVar[int]
    COL_TYPES_FIELD_NUMBER: _ClassVar[int]
    COL_TYPMODS_FIELD_NUMBER: _ClassVar[int]
    COL_COLLATIONS_FIELD_NUMBER: _ClassVar[int]
    GROUP_CLAUSES_FIELD_NUMBER: _ClassVar[int]
    op: SetOperation
    all: bool
    larg: Node
    rarg: Node
    col_types: _containers.RepeatedCompositeFieldContainer[Node]
    col_typmods: _containers.RepeatedCompositeFieldContainer[Node]
    col_collations: _containers.RepeatedCompositeFieldContainer[Node]
    group_clauses: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        op: _Optional[_Union[SetOperation, str]] = ...,
        all: bool = ...,
        larg: _Optional[_Union[Node, _Mapping]] = ...,
        rarg: _Optional[_Union[Node, _Mapping]] = ...,
        col_types: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        col_typmods: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        col_collations: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        group_clauses: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class ReturnStmt(_message.Message):
    __slots__ = ("returnval",)
    RETURNVAL_FIELD_NUMBER: _ClassVar[int]
    returnval: Node
    def __init__(self, returnval: _Optional[_Union[Node, _Mapping]] = ...) -> None: ...

class PLAssignStmt(_message.Message):
    __slots__ = ("name", "indirection", "nnames", "val", "location")
    NAME_FIELD_NUMBER: _ClassVar[int]
    INDIRECTION_FIELD_NUMBER: _ClassVar[int]
    NNAMES_FIELD_NUMBER: _ClassVar[int]
    VAL_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    indirection: _containers.RepeatedCompositeFieldContainer[Node]
    nnames: int
    val: SelectStmt
    location: int
    def __init__(
        self,
        name: _Optional[str] = ...,
        indirection: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        nnames: _Optional[int] = ...,
        val: _Optional[_Union[SelectStmt, _Mapping]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class CreateSchemaStmt(_message.Message):
    __slots__ = ("schemaname", "authrole", "schema_elts", "if_not_exists")
    SCHEMANAME_FIELD_NUMBER: _ClassVar[int]
    AUTHROLE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_ELTS_FIELD_NUMBER: _ClassVar[int]
    IF_NOT_EXISTS_FIELD_NUMBER: _ClassVar[int]
    schemaname: str
    authrole: RoleSpec
    schema_elts: _containers.RepeatedCompositeFieldContainer[Node]
    if_not_exists: bool
    def __init__(
        self,
        schemaname: _Optional[str] = ...,
        authrole: _Optional[_Union[RoleSpec, _Mapping]] = ...,
        schema_elts: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        if_not_exists: bool = ...,
    ) -> None: ...

class AlterTableStmt(_message.Message):
    __slots__ = ("relation", "cmds", "objtype", "missing_ok")
    RELATION_FIELD_NUMBER: _ClassVar[int]
    CMDS_FIELD_NUMBER: _ClassVar[int]
    OBJTYPE_FIELD_NUMBER: _ClassVar[int]
    MISSING_OK_FIELD_NUMBER: _ClassVar[int]
    relation: RangeVar
    cmds: _containers.RepeatedCompositeFieldContainer[Node]
    objtype: ObjectType
    missing_ok: bool
    def __init__(
        self,
        relation: _Optional[_Union[RangeVar, _Mapping]] = ...,
        cmds: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        objtype: _Optional[_Union[ObjectType, str]] = ...,
        missing_ok: bool = ...,
    ) -> None: ...

class ReplicaIdentityStmt(_message.Message):
    __slots__ = ("identity_type", "name")
    IDENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    identity_type: str
    name: str
    def __init__(self, identity_type: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class AlterTableCmd(_message.Message):
    __slots__ = ("subtype", "name", "num", "newowner", "behavior", "missing_ok", "recurse")
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    NEWOWNER_FIELD_NUMBER: _ClassVar[int]
    DEF_FIELD_NUMBER: _ClassVar[int]
    BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
    MISSING_OK_FIELD_NUMBER: _ClassVar[int]
    RECURSE_FIELD_NUMBER: _ClassVar[int]
    subtype: AlterTableType
    name: str
    num: int
    newowner: RoleSpec
    behavior: DropBehavior
    missing_ok: bool
    recurse: bool
    def __init__(
        self,
        subtype: _Optional[_Union[AlterTableType, str]] = ...,
        name: _Optional[str] = ...,
        num: _Optional[int] = ...,
        newowner: _Optional[_Union[RoleSpec, _Mapping]] = ...,
        behavior: _Optional[_Union[DropBehavior, str]] = ...,
        missing_ok: bool = ...,
        recurse: bool = ...,
        **kwargs,
    ) -> None: ...

class AlterCollationStmt(_message.Message):
    __slots__ = ("collname",)
    COLLNAME_FIELD_NUMBER: _ClassVar[int]
    collname: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(self, collname: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...) -> None: ...

class AlterDomainStmt(_message.Message):
    __slots__ = ("subtype", "type_name", "name", "behavior", "missing_ok")
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEF_FIELD_NUMBER: _ClassVar[int]
    BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
    MISSING_OK_FIELD_NUMBER: _ClassVar[int]
    subtype: str
    type_name: _containers.RepeatedCompositeFieldContainer[Node]
    name: str
    behavior: DropBehavior
    missing_ok: bool
    def __init__(
        self,
        subtype: _Optional[str] = ...,
        type_name: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        name: _Optional[str] = ...,
        behavior: _Optional[_Union[DropBehavior, str]] = ...,
        missing_ok: bool = ...,
        **kwargs,
    ) -> None: ...

class GrantStmt(_message.Message):
    __slots__ = (
        "is_grant",
        "targtype",
        "objtype",
        "objects",
        "privileges",
        "grantees",
        "grant_option",
        "grantor",
        "behavior",
    )
    IS_GRANT_FIELD_NUMBER: _ClassVar[int]
    TARGTYPE_FIELD_NUMBER: _ClassVar[int]
    OBJTYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    PRIVILEGES_FIELD_NUMBER: _ClassVar[int]
    GRANTEES_FIELD_NUMBER: _ClassVar[int]
    GRANT_OPTION_FIELD_NUMBER: _ClassVar[int]
    GRANTOR_FIELD_NUMBER: _ClassVar[int]
    BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
    is_grant: bool
    targtype: GrantTargetType
    objtype: ObjectType
    objects: _containers.RepeatedCompositeFieldContainer[Node]
    privileges: _containers.RepeatedCompositeFieldContainer[Node]
    grantees: _containers.RepeatedCompositeFieldContainer[Node]
    grant_option: bool
    grantor: RoleSpec
    behavior: DropBehavior
    def __init__(
        self,
        is_grant: bool = ...,
        targtype: _Optional[_Union[GrantTargetType, str]] = ...,
        objtype: _Optional[_Union[ObjectType, str]] = ...,
        objects: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        privileges: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        grantees: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        grant_option: bool = ...,
        grantor: _Optional[_Union[RoleSpec, _Mapping]] = ...,
        behavior: _Optional[_Union[DropBehavior, str]] = ...,
    ) -> None: ...

class ObjectWithArgs(_message.Message):
    __slots__ = ("objname", "objargs", "objfuncargs", "args_unspecified")
    OBJNAME_FIELD_NUMBER: _ClassVar[int]
    OBJARGS_FIELD_NUMBER: _ClassVar[int]
    OBJFUNCARGS_FIELD_NUMBER: _ClassVar[int]
    ARGS_UNSPECIFIED_FIELD_NUMBER: _ClassVar[int]
    objname: _containers.RepeatedCompositeFieldContainer[Node]
    objargs: _containers.RepeatedCompositeFieldContainer[Node]
    objfuncargs: _containers.RepeatedCompositeFieldContainer[Node]
    args_unspecified: bool
    def __init__(
        self,
        objname: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        objargs: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        objfuncargs: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        args_unspecified: bool = ...,
    ) -> None: ...

class AccessPriv(_message.Message):
    __slots__ = ("priv_name", "cols")
    PRIV_NAME_FIELD_NUMBER: _ClassVar[int]
    COLS_FIELD_NUMBER: _ClassVar[int]
    priv_name: str
    cols: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self, priv_name: _Optional[str] = ..., cols: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...
    ) -> None: ...

class GrantRoleStmt(_message.Message):
    __slots__ = ("granted_roles", "grantee_roles", "is_grant", "opt", "grantor", "behavior")
    GRANTED_ROLES_FIELD_NUMBER: _ClassVar[int]
    GRANTEE_ROLES_FIELD_NUMBER: _ClassVar[int]
    IS_GRANT_FIELD_NUMBER: _ClassVar[int]
    OPT_FIELD_NUMBER: _ClassVar[int]
    GRANTOR_FIELD_NUMBER: _ClassVar[int]
    BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
    granted_roles: _containers.RepeatedCompositeFieldContainer[Node]
    grantee_roles: _containers.RepeatedCompositeFieldContainer[Node]
    is_grant: bool
    opt: _containers.RepeatedCompositeFieldContainer[Node]
    grantor: RoleSpec
    behavior: DropBehavior
    def __init__(
        self,
        granted_roles: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        grantee_roles: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        is_grant: bool = ...,
        opt: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        grantor: _Optional[_Union[RoleSpec, _Mapping]] = ...,
        behavior: _Optional[_Union[DropBehavior, str]] = ...,
    ) -> None: ...

class AlterDefaultPrivilegesStmt(_message.Message):
    __slots__ = ("options", "action")
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    options: _containers.RepeatedCompositeFieldContainer[Node]
    action: GrantStmt
    def __init__(
        self,
        options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        action: _Optional[_Union[GrantStmt, _Mapping]] = ...,
    ) -> None: ...

class CopyStmt(_message.Message):
    __slots__ = ("relation", "query", "attlist", "is_from", "is_program", "filename", "options", "where_clause")
    RELATION_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    ATTLIST_FIELD_NUMBER: _ClassVar[int]
    IS_FROM_FIELD_NUMBER: _ClassVar[int]
    IS_PROGRAM_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    WHERE_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    relation: RangeVar
    query: Node
    attlist: _containers.RepeatedCompositeFieldContainer[Node]
    is_from: bool
    is_program: bool
    filename: str
    options: _containers.RepeatedCompositeFieldContainer[Node]
    where_clause: Node
    def __init__(
        self,
        relation: _Optional[_Union[RangeVar, _Mapping]] = ...,
        query: _Optional[_Union[Node, _Mapping]] = ...,
        attlist: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        is_from: bool = ...,
        is_program: bool = ...,
        filename: _Optional[str] = ...,
        options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        where_clause: _Optional[_Union[Node, _Mapping]] = ...,
    ) -> None: ...

class VariableSetStmt(_message.Message):
    __slots__ = ("kind", "name", "args", "is_local")
    KIND_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    IS_LOCAL_FIELD_NUMBER: _ClassVar[int]
    kind: VariableSetKind
    name: str
    args: _containers.RepeatedCompositeFieldContainer[Node]
    is_local: bool
    def __init__(
        self,
        kind: _Optional[_Union[VariableSetKind, str]] = ...,
        name: _Optional[str] = ...,
        args: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        is_local: bool = ...,
    ) -> None: ...

class VariableShowStmt(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateStmt(_message.Message):
    __slots__ = (
        "relation",
        "table_elts",
        "inh_relations",
        "partbound",
        "partspec",
        "of_typename",
        "constraints",
        "options",
        "oncommit",
        "tablespacename",
        "access_method",
        "if_not_exists",
    )
    RELATION_FIELD_NUMBER: _ClassVar[int]
    TABLE_ELTS_FIELD_NUMBER: _ClassVar[int]
    INH_RELATIONS_FIELD_NUMBER: _ClassVar[int]
    PARTBOUND_FIELD_NUMBER: _ClassVar[int]
    PARTSPEC_FIELD_NUMBER: _ClassVar[int]
    OF_TYPENAME_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ONCOMMIT_FIELD_NUMBER: _ClassVar[int]
    TABLESPACENAME_FIELD_NUMBER: _ClassVar[int]
    ACCESS_METHOD_FIELD_NUMBER: _ClassVar[int]
    IF_NOT_EXISTS_FIELD_NUMBER: _ClassVar[int]
    relation: RangeVar
    table_elts: _containers.RepeatedCompositeFieldContainer[Node]
    inh_relations: _containers.RepeatedCompositeFieldContainer[Node]
    partbound: PartitionBoundSpec
    partspec: PartitionSpec
    of_typename: TypeName
    constraints: _containers.RepeatedCompositeFieldContainer[Node]
    options: _containers.RepeatedCompositeFieldContainer[Node]
    oncommit: OnCommitAction
    tablespacename: str
    access_method: str
    if_not_exists: bool
    def __init__(
        self,
        relation: _Optional[_Union[RangeVar, _Mapping]] = ...,
        table_elts: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        inh_relations: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        partbound: _Optional[_Union[PartitionBoundSpec, _Mapping]] = ...,
        partspec: _Optional[_Union[PartitionSpec, _Mapping]] = ...,
        of_typename: _Optional[_Union[TypeName, _Mapping]] = ...,
        constraints: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        oncommit: _Optional[_Union[OnCommitAction, str]] = ...,
        tablespacename: _Optional[str] = ...,
        access_method: _Optional[str] = ...,
        if_not_exists: bool = ...,
    ) -> None: ...

class Constraint(_message.Message):
    __slots__ = (
        "contype",
        "conname",
        "deferrable",
        "initdeferred",
        "location",
        "is_no_inherit",
        "raw_expr",
        "cooked_expr",
        "generated_when",
        "nulls_not_distinct",
        "keys",
        "including",
        "exclusions",
        "options",
        "indexname",
        "indexspace",
        "reset_default_tblspc",
        "access_method",
        "where_clause",
        "pktable",
        "fk_attrs",
        "pk_attrs",
        "fk_matchtype",
        "fk_upd_action",
        "fk_del_action",
        "fk_del_set_cols",
        "old_conpfeqop",
        "old_pktable_oid",
        "skip_validation",
        "initially_valid",
    )
    CONTYPE_FIELD_NUMBER: _ClassVar[int]
    CONNAME_FIELD_NUMBER: _ClassVar[int]
    DEFERRABLE_FIELD_NUMBER: _ClassVar[int]
    INITDEFERRED_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    IS_NO_INHERIT_FIELD_NUMBER: _ClassVar[int]
    RAW_EXPR_FIELD_NUMBER: _ClassVar[int]
    COOKED_EXPR_FIELD_NUMBER: _ClassVar[int]
    GENERATED_WHEN_FIELD_NUMBER: _ClassVar[int]
    NULLS_NOT_DISTINCT_FIELD_NUMBER: _ClassVar[int]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    INCLUDING_FIELD_NUMBER: _ClassVar[int]
    EXCLUSIONS_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    INDEXNAME_FIELD_NUMBER: _ClassVar[int]
    INDEXSPACE_FIELD_NUMBER: _ClassVar[int]
    RESET_DEFAULT_TBLSPC_FIELD_NUMBER: _ClassVar[int]
    ACCESS_METHOD_FIELD_NUMBER: _ClassVar[int]
    WHERE_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    PKTABLE_FIELD_NUMBER: _ClassVar[int]
    FK_ATTRS_FIELD_NUMBER: _ClassVar[int]
    PK_ATTRS_FIELD_NUMBER: _ClassVar[int]
    FK_MATCHTYPE_FIELD_NUMBER: _ClassVar[int]
    FK_UPD_ACTION_FIELD_NUMBER: _ClassVar[int]
    FK_DEL_ACTION_FIELD_NUMBER: _ClassVar[int]
    FK_DEL_SET_COLS_FIELD_NUMBER: _ClassVar[int]
    OLD_CONPFEQOP_FIELD_NUMBER: _ClassVar[int]
    OLD_PKTABLE_OID_FIELD_NUMBER: _ClassVar[int]
    SKIP_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    INITIALLY_VALID_FIELD_NUMBER: _ClassVar[int]
    contype: ConstrType
    conname: str
    deferrable: bool
    initdeferred: bool
    location: int
    is_no_inherit: bool
    raw_expr: Node
    cooked_expr: str
    generated_when: str
    nulls_not_distinct: bool
    keys: _containers.RepeatedCompositeFieldContainer[Node]
    including: _containers.RepeatedCompositeFieldContainer[Node]
    exclusions: _containers.RepeatedCompositeFieldContainer[Node]
    options: _containers.RepeatedCompositeFieldContainer[Node]
    indexname: str
    indexspace: str
    reset_default_tblspc: bool
    access_method: str
    where_clause: Node
    pktable: RangeVar
    fk_attrs: _containers.RepeatedCompositeFieldContainer[Node]
    pk_attrs: _containers.RepeatedCompositeFieldContainer[Node]
    fk_matchtype: str
    fk_upd_action: str
    fk_del_action: str
    fk_del_set_cols: _containers.RepeatedCompositeFieldContainer[Node]
    old_conpfeqop: _containers.RepeatedCompositeFieldContainer[Node]
    old_pktable_oid: int
    skip_validation: bool
    initially_valid: bool
    def __init__(
        self,
        contype: _Optional[_Union[ConstrType, str]] = ...,
        conname: _Optional[str] = ...,
        deferrable: bool = ...,
        initdeferred: bool = ...,
        location: _Optional[int] = ...,
        is_no_inherit: bool = ...,
        raw_expr: _Optional[_Union[Node, _Mapping]] = ...,
        cooked_expr: _Optional[str] = ...,
        generated_when: _Optional[str] = ...,
        nulls_not_distinct: bool = ...,
        keys: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        including: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        exclusions: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        indexname: _Optional[str] = ...,
        indexspace: _Optional[str] = ...,
        reset_default_tblspc: bool = ...,
        access_method: _Optional[str] = ...,
        where_clause: _Optional[_Union[Node, _Mapping]] = ...,
        pktable: _Optional[_Union[RangeVar, _Mapping]] = ...,
        fk_attrs: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        pk_attrs: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        fk_matchtype: _Optional[str] = ...,
        fk_upd_action: _Optional[str] = ...,
        fk_del_action: _Optional[str] = ...,
        fk_del_set_cols: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        old_conpfeqop: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        old_pktable_oid: _Optional[int] = ...,
        skip_validation: bool = ...,
        initially_valid: bool = ...,
    ) -> None: ...

class CreateTableSpaceStmt(_message.Message):
    __slots__ = ("tablespacename", "owner", "location", "options")
    TABLESPACENAME_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    tablespacename: str
    owner: RoleSpec
    location: str
    options: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        tablespacename: _Optional[str] = ...,
        owner: _Optional[_Union[RoleSpec, _Mapping]] = ...,
        location: _Optional[str] = ...,
        options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class DropTableSpaceStmt(_message.Message):
    __slots__ = ("tablespacename", "missing_ok")
    TABLESPACENAME_FIELD_NUMBER: _ClassVar[int]
    MISSING_OK_FIELD_NUMBER: _ClassVar[int]
    tablespacename: str
    missing_ok: bool
    def __init__(self, tablespacename: _Optional[str] = ..., missing_ok: bool = ...) -> None: ...

class AlterTableSpaceOptionsStmt(_message.Message):
    __slots__ = ("tablespacename", "options", "is_reset")
    TABLESPACENAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    IS_RESET_FIELD_NUMBER: _ClassVar[int]
    tablespacename: str
    options: _containers.RepeatedCompositeFieldContainer[Node]
    is_reset: bool
    def __init__(
        self,
        tablespacename: _Optional[str] = ...,
        options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        is_reset: bool = ...,
    ) -> None: ...

class AlterTableMoveAllStmt(_message.Message):
    __slots__ = ("orig_tablespacename", "objtype", "roles", "new_tablespacename", "nowait")
    ORIG_TABLESPACENAME_FIELD_NUMBER: _ClassVar[int]
    OBJTYPE_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    NEW_TABLESPACENAME_FIELD_NUMBER: _ClassVar[int]
    NOWAIT_FIELD_NUMBER: _ClassVar[int]
    orig_tablespacename: str
    objtype: ObjectType
    roles: _containers.RepeatedCompositeFieldContainer[Node]
    new_tablespacename: str
    nowait: bool
    def __init__(
        self,
        orig_tablespacename: _Optional[str] = ...,
        objtype: _Optional[_Union[ObjectType, str]] = ...,
        roles: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        new_tablespacename: _Optional[str] = ...,
        nowait: bool = ...,
    ) -> None: ...

class CreateExtensionStmt(_message.Message):
    __slots__ = ("extname", "if_not_exists", "options")
    EXTNAME_FIELD_NUMBER: _ClassVar[int]
    IF_NOT_EXISTS_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    extname: str
    if_not_exists: bool
    options: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        extname: _Optional[str] = ...,
        if_not_exists: bool = ...,
        options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class AlterExtensionStmt(_message.Message):
    __slots__ = ("extname", "options")
    EXTNAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    extname: str
    options: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self, extname: _Optional[str] = ..., options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...
    ) -> None: ...

class AlterExtensionContentsStmt(_message.Message):
    __slots__ = ("extname", "action", "objtype", "object")
    EXTNAME_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    OBJTYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    extname: str
    action: int
    objtype: ObjectType
    object: Node
    def __init__(
        self,
        extname: _Optional[str] = ...,
        action: _Optional[int] = ...,
        objtype: _Optional[_Union[ObjectType, str]] = ...,
        object: _Optional[_Union[Node, _Mapping]] = ...,
    ) -> None: ...

class CreateFdwStmt(_message.Message):
    __slots__ = ("fdwname", "func_options", "options")
    FDWNAME_FIELD_NUMBER: _ClassVar[int]
    FUNC_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    fdwname: str
    func_options: _containers.RepeatedCompositeFieldContainer[Node]
    options: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        fdwname: _Optional[str] = ...,
        func_options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class AlterFdwStmt(_message.Message):
    __slots__ = ("fdwname", "func_options", "options")
    FDWNAME_FIELD_NUMBER: _ClassVar[int]
    FUNC_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    fdwname: str
    func_options: _containers.RepeatedCompositeFieldContainer[Node]
    options: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        fdwname: _Optional[str] = ...,
        func_options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class CreateForeignServerStmt(_message.Message):
    __slots__ = ("servername", "servertype", "version", "fdwname", "if_not_exists", "options")
    SERVERNAME_FIELD_NUMBER: _ClassVar[int]
    SERVERTYPE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    FDWNAME_FIELD_NUMBER: _ClassVar[int]
    IF_NOT_EXISTS_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    servername: str
    servertype: str
    version: str
    fdwname: str
    if_not_exists: bool
    options: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        servername: _Optional[str] = ...,
        servertype: _Optional[str] = ...,
        version: _Optional[str] = ...,
        fdwname: _Optional[str] = ...,
        if_not_exists: bool = ...,
        options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class AlterForeignServerStmt(_message.Message):
    __slots__ = ("servername", "version", "options", "has_version")
    SERVERNAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    HAS_VERSION_FIELD_NUMBER: _ClassVar[int]
    servername: str
    version: str
    options: _containers.RepeatedCompositeFieldContainer[Node]
    has_version: bool
    def __init__(
        self,
        servername: _Optional[str] = ...,
        version: _Optional[str] = ...,
        options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        has_version: bool = ...,
    ) -> None: ...

class CreateForeignTableStmt(_message.Message):
    __slots__ = ("base_stmt", "servername", "options")
    BASE_STMT_FIELD_NUMBER: _ClassVar[int]
    SERVERNAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    base_stmt: CreateStmt
    servername: str
    options: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        base_stmt: _Optional[_Union[CreateStmt, _Mapping]] = ...,
        servername: _Optional[str] = ...,
        options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class CreateUserMappingStmt(_message.Message):
    __slots__ = ("user", "servername", "if_not_exists", "options")
    USER_FIELD_NUMBER: _ClassVar[int]
    SERVERNAME_FIELD_NUMBER: _ClassVar[int]
    IF_NOT_EXISTS_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    user: RoleSpec
    servername: str
    if_not_exists: bool
    options: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        user: _Optional[_Union[RoleSpec, _Mapping]] = ...,
        servername: _Optional[str] = ...,
        if_not_exists: bool = ...,
        options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class AlterUserMappingStmt(_message.Message):
    __slots__ = ("user", "servername", "options")
    USER_FIELD_NUMBER: _ClassVar[int]
    SERVERNAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    user: RoleSpec
    servername: str
    options: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        user: _Optional[_Union[RoleSpec, _Mapping]] = ...,
        servername: _Optional[str] = ...,
        options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class DropUserMappingStmt(_message.Message):
    __slots__ = ("user", "servername", "missing_ok")
    USER_FIELD_NUMBER: _ClassVar[int]
    SERVERNAME_FIELD_NUMBER: _ClassVar[int]
    MISSING_OK_FIELD_NUMBER: _ClassVar[int]
    user: RoleSpec
    servername: str
    missing_ok: bool
    def __init__(
        self,
        user: _Optional[_Union[RoleSpec, _Mapping]] = ...,
        servername: _Optional[str] = ...,
        missing_ok: bool = ...,
    ) -> None: ...

class ImportForeignSchemaStmt(_message.Message):
    __slots__ = ("server_name", "remote_schema", "local_schema", "list_type", "table_list", "options")
    SERVER_NAME_FIELD_NUMBER: _ClassVar[int]
    REMOTE_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    LOCAL_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    LIST_TYPE_FIELD_NUMBER: _ClassVar[int]
    TABLE_LIST_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    server_name: str
    remote_schema: str
    local_schema: str
    list_type: ImportForeignSchemaType
    table_list: _containers.RepeatedCompositeFieldContainer[Node]
    options: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        server_name: _Optional[str] = ...,
        remote_schema: _Optional[str] = ...,
        local_schema: _Optional[str] = ...,
        list_type: _Optional[_Union[ImportForeignSchemaType, str]] = ...,
        table_list: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class CreatePolicyStmt(_message.Message):
    __slots__ = ("policy_name", "table", "cmd_name", "permissive", "roles", "qual", "with_check")
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    CMD_NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSIVE_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    QUAL_FIELD_NUMBER: _ClassVar[int]
    WITH_CHECK_FIELD_NUMBER: _ClassVar[int]
    policy_name: str
    table: RangeVar
    cmd_name: str
    permissive: bool
    roles: _containers.RepeatedCompositeFieldContainer[Node]
    qual: Node
    with_check: Node
    def __init__(
        self,
        policy_name: _Optional[str] = ...,
        table: _Optional[_Union[RangeVar, _Mapping]] = ...,
        cmd_name: _Optional[str] = ...,
        permissive: bool = ...,
        roles: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        qual: _Optional[_Union[Node, _Mapping]] = ...,
        with_check: _Optional[_Union[Node, _Mapping]] = ...,
    ) -> None: ...

class AlterPolicyStmt(_message.Message):
    __slots__ = ("policy_name", "table", "roles", "qual", "with_check")
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    QUAL_FIELD_NUMBER: _ClassVar[int]
    WITH_CHECK_FIELD_NUMBER: _ClassVar[int]
    policy_name: str
    table: RangeVar
    roles: _containers.RepeatedCompositeFieldContainer[Node]
    qual: Node
    with_check: Node
    def __init__(
        self,
        policy_name: _Optional[str] = ...,
        table: _Optional[_Union[RangeVar, _Mapping]] = ...,
        roles: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        qual: _Optional[_Union[Node, _Mapping]] = ...,
        with_check: _Optional[_Union[Node, _Mapping]] = ...,
    ) -> None: ...

class CreateAmStmt(_message.Message):
    __slots__ = ("amname", "handler_name", "amtype")
    AMNAME_FIELD_NUMBER: _ClassVar[int]
    HANDLER_NAME_FIELD_NUMBER: _ClassVar[int]
    AMTYPE_FIELD_NUMBER: _ClassVar[int]
    amname: str
    handler_name: _containers.RepeatedCompositeFieldContainer[Node]
    amtype: str
    def __init__(
        self,
        amname: _Optional[str] = ...,
        handler_name: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        amtype: _Optional[str] = ...,
    ) -> None: ...

class CreateTrigStmt(_message.Message):
    __slots__ = (
        "replace",
        "isconstraint",
        "trigname",
        "relation",
        "funcname",
        "args",
        "row",
        "timing",
        "events",
        "columns",
        "when_clause",
        "transition_rels",
        "deferrable",
        "initdeferred",
        "constrrel",
    )
    REPLACE_FIELD_NUMBER: _ClassVar[int]
    ISCONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    TRIGNAME_FIELD_NUMBER: _ClassVar[int]
    RELATION_FIELD_NUMBER: _ClassVar[int]
    FUNCNAME_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    ROW_FIELD_NUMBER: _ClassVar[int]
    TIMING_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    WHEN_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    TRANSITION_RELS_FIELD_NUMBER: _ClassVar[int]
    DEFERRABLE_FIELD_NUMBER: _ClassVar[int]
    INITDEFERRED_FIELD_NUMBER: _ClassVar[int]
    CONSTRREL_FIELD_NUMBER: _ClassVar[int]
    replace: bool
    isconstraint: bool
    trigname: str
    relation: RangeVar
    funcname: _containers.RepeatedCompositeFieldContainer[Node]
    args: _containers.RepeatedCompositeFieldContainer[Node]
    row: bool
    timing: int
    events: int
    columns: _containers.RepeatedCompositeFieldContainer[Node]
    when_clause: Node
    transition_rels: _containers.RepeatedCompositeFieldContainer[Node]
    deferrable: bool
    initdeferred: bool
    constrrel: RangeVar
    def __init__(
        self,
        replace: bool = ...,
        isconstraint: bool = ...,
        trigname: _Optional[str] = ...,
        relation: _Optional[_Union[RangeVar, _Mapping]] = ...,
        funcname: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        args: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        row: bool = ...,
        timing: _Optional[int] = ...,
        events: _Optional[int] = ...,
        columns: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        when_clause: _Optional[_Union[Node, _Mapping]] = ...,
        transition_rels: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        deferrable: bool = ...,
        initdeferred: bool = ...,
        constrrel: _Optional[_Union[RangeVar, _Mapping]] = ...,
    ) -> None: ...

class CreateEventTrigStmt(_message.Message):
    __slots__ = ("trigname", "eventname", "whenclause", "funcname")
    TRIGNAME_FIELD_NUMBER: _ClassVar[int]
    EVENTNAME_FIELD_NUMBER: _ClassVar[int]
    WHENCLAUSE_FIELD_NUMBER: _ClassVar[int]
    FUNCNAME_FIELD_NUMBER: _ClassVar[int]
    trigname: str
    eventname: str
    whenclause: _containers.RepeatedCompositeFieldContainer[Node]
    funcname: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        trigname: _Optional[str] = ...,
        eventname: _Optional[str] = ...,
        whenclause: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        funcname: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class AlterEventTrigStmt(_message.Message):
    __slots__ = ("trigname", "tgenabled")
    TRIGNAME_FIELD_NUMBER: _ClassVar[int]
    TGENABLED_FIELD_NUMBER: _ClassVar[int]
    trigname: str
    tgenabled: str
    def __init__(self, trigname: _Optional[str] = ..., tgenabled: _Optional[str] = ...) -> None: ...

class CreatePLangStmt(_message.Message):
    __slots__ = ("replace", "plname", "plhandler", "plinline", "plvalidator", "pltrusted")
    REPLACE_FIELD_NUMBER: _ClassVar[int]
    PLNAME_FIELD_NUMBER: _ClassVar[int]
    PLHANDLER_FIELD_NUMBER: _ClassVar[int]
    PLINLINE_FIELD_NUMBER: _ClassVar[int]
    PLVALIDATOR_FIELD_NUMBER: _ClassVar[int]
    PLTRUSTED_FIELD_NUMBER: _ClassVar[int]
    replace: bool
    plname: str
    plhandler: _containers.RepeatedCompositeFieldContainer[Node]
    plinline: _containers.RepeatedCompositeFieldContainer[Node]
    plvalidator: _containers.RepeatedCompositeFieldContainer[Node]
    pltrusted: bool
    def __init__(
        self,
        replace: bool = ...,
        plname: _Optional[str] = ...,
        plhandler: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        plinline: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        plvalidator: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        pltrusted: bool = ...,
    ) -> None: ...

class CreateRoleStmt(_message.Message):
    __slots__ = ("stmt_type", "role", "options")
    STMT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    stmt_type: RoleStmtType
    role: str
    options: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        stmt_type: _Optional[_Union[RoleStmtType, str]] = ...,
        role: _Optional[str] = ...,
        options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class AlterRoleStmt(_message.Message):
    __slots__ = ("role", "options", "action")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    role: RoleSpec
    options: _containers.RepeatedCompositeFieldContainer[Node]
    action: int
    def __init__(
        self,
        role: _Optional[_Union[RoleSpec, _Mapping]] = ...,
        options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        action: _Optional[int] = ...,
    ) -> None: ...

class AlterRoleSetStmt(_message.Message):
    __slots__ = ("role", "database", "setstmt")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    SETSTMT_FIELD_NUMBER: _ClassVar[int]
    role: RoleSpec
    database: str
    setstmt: VariableSetStmt
    def __init__(
        self,
        role: _Optional[_Union[RoleSpec, _Mapping]] = ...,
        database: _Optional[str] = ...,
        setstmt: _Optional[_Union[VariableSetStmt, _Mapping]] = ...,
    ) -> None: ...

class DropRoleStmt(_message.Message):
    __slots__ = ("roles", "missing_ok")
    ROLES_FIELD_NUMBER: _ClassVar[int]
    MISSING_OK_FIELD_NUMBER: _ClassVar[int]
    roles: _containers.RepeatedCompositeFieldContainer[Node]
    missing_ok: bool
    def __init__(self, roles: _Optional[_Iterable[_Union[Node, _Mapping]]] = ..., missing_ok: bool = ...) -> None: ...

class CreateSeqStmt(_message.Message):
    __slots__ = ("sequence", "options", "owner_id", "for_identity", "if_not_exists")
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    FOR_IDENTITY_FIELD_NUMBER: _ClassVar[int]
    IF_NOT_EXISTS_FIELD_NUMBER: _ClassVar[int]
    sequence: RangeVar
    options: _containers.RepeatedCompositeFieldContainer[Node]
    owner_id: int
    for_identity: bool
    if_not_exists: bool
    def __init__(
        self,
        sequence: _Optional[_Union[RangeVar, _Mapping]] = ...,
        options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        owner_id: _Optional[int] = ...,
        for_identity: bool = ...,
        if_not_exists: bool = ...,
    ) -> None: ...

class AlterSeqStmt(_message.Message):
    __slots__ = ("sequence", "options", "for_identity", "missing_ok")
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    FOR_IDENTITY_FIELD_NUMBER: _ClassVar[int]
    MISSING_OK_FIELD_NUMBER: _ClassVar[int]
    sequence: RangeVar
    options: _containers.RepeatedCompositeFieldContainer[Node]
    for_identity: bool
    missing_ok: bool
    def __init__(
        self,
        sequence: _Optional[_Union[RangeVar, _Mapping]] = ...,
        options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        for_identity: bool = ...,
        missing_ok: bool = ...,
    ) -> None: ...

class DefineStmt(_message.Message):
    __slots__ = ("kind", "oldstyle", "defnames", "args", "definition", "if_not_exists", "replace")
    KIND_FIELD_NUMBER: _ClassVar[int]
    OLDSTYLE_FIELD_NUMBER: _ClassVar[int]
    DEFNAMES_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_FIELD_NUMBER: _ClassVar[int]
    IF_NOT_EXISTS_FIELD_NUMBER: _ClassVar[int]
    REPLACE_FIELD_NUMBER: _ClassVar[int]
    kind: ObjectType
    oldstyle: bool
    defnames: _containers.RepeatedCompositeFieldContainer[Node]
    args: _containers.RepeatedCompositeFieldContainer[Node]
    definition: _containers.RepeatedCompositeFieldContainer[Node]
    if_not_exists: bool
    replace: bool
    def __init__(
        self,
        kind: _Optional[_Union[ObjectType, str]] = ...,
        oldstyle: bool = ...,
        defnames: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        args: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        definition: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        if_not_exists: bool = ...,
        replace: bool = ...,
    ) -> None: ...

class CreateDomainStmt(_message.Message):
    __slots__ = ("domainname", "type_name", "coll_clause", "constraints")
    DOMAINNAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    COLL_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    domainname: _containers.RepeatedCompositeFieldContainer[Node]
    type_name: TypeName
    coll_clause: CollateClause
    constraints: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        domainname: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        type_name: _Optional[_Union[TypeName, _Mapping]] = ...,
        coll_clause: _Optional[_Union[CollateClause, _Mapping]] = ...,
        constraints: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class CreateOpClassStmt(_message.Message):
    __slots__ = ("opclassname", "opfamilyname", "amname", "datatype", "items", "is_default")
    OPCLASSNAME_FIELD_NUMBER: _ClassVar[int]
    OPFAMILYNAME_FIELD_NUMBER: _ClassVar[int]
    AMNAME_FIELD_NUMBER: _ClassVar[int]
    DATATYPE_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    opclassname: _containers.RepeatedCompositeFieldContainer[Node]
    opfamilyname: _containers.RepeatedCompositeFieldContainer[Node]
    amname: str
    datatype: TypeName
    items: _containers.RepeatedCompositeFieldContainer[Node]
    is_default: bool
    def __init__(
        self,
        opclassname: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        opfamilyname: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        amname: _Optional[str] = ...,
        datatype: _Optional[_Union[TypeName, _Mapping]] = ...,
        items: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        is_default: bool = ...,
    ) -> None: ...

class CreateOpClassItem(_message.Message):
    __slots__ = ("itemtype", "name", "number", "order_family", "class_args", "storedtype")
    ITEMTYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    ORDER_FAMILY_FIELD_NUMBER: _ClassVar[int]
    CLASS_ARGS_FIELD_NUMBER: _ClassVar[int]
    STOREDTYPE_FIELD_NUMBER: _ClassVar[int]
    itemtype: int
    name: ObjectWithArgs
    number: int
    order_family: _containers.RepeatedCompositeFieldContainer[Node]
    class_args: _containers.RepeatedCompositeFieldContainer[Node]
    storedtype: TypeName
    def __init__(
        self,
        itemtype: _Optional[int] = ...,
        name: _Optional[_Union[ObjectWithArgs, _Mapping]] = ...,
        number: _Optional[int] = ...,
        order_family: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        class_args: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        storedtype: _Optional[_Union[TypeName, _Mapping]] = ...,
    ) -> None: ...

class CreateOpFamilyStmt(_message.Message):
    __slots__ = ("opfamilyname", "amname")
    OPFAMILYNAME_FIELD_NUMBER: _ClassVar[int]
    AMNAME_FIELD_NUMBER: _ClassVar[int]
    opfamilyname: _containers.RepeatedCompositeFieldContainer[Node]
    amname: str
    def __init__(
        self, opfamilyname: _Optional[_Iterable[_Union[Node, _Mapping]]] = ..., amname: _Optional[str] = ...
    ) -> None: ...

class AlterOpFamilyStmt(_message.Message):
    __slots__ = ("opfamilyname", "amname", "is_drop", "items")
    OPFAMILYNAME_FIELD_NUMBER: _ClassVar[int]
    AMNAME_FIELD_NUMBER: _ClassVar[int]
    IS_DROP_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    opfamilyname: _containers.RepeatedCompositeFieldContainer[Node]
    amname: str
    is_drop: bool
    items: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        opfamilyname: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        amname: _Optional[str] = ...,
        is_drop: bool = ...,
        items: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class DropStmt(_message.Message):
    __slots__ = ("objects", "remove_type", "behavior", "missing_ok", "concurrent")
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    REMOVE_TYPE_FIELD_NUMBER: _ClassVar[int]
    BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
    MISSING_OK_FIELD_NUMBER: _ClassVar[int]
    CONCURRENT_FIELD_NUMBER: _ClassVar[int]
    objects: _containers.RepeatedCompositeFieldContainer[Node]
    remove_type: ObjectType
    behavior: DropBehavior
    missing_ok: bool
    concurrent: bool
    def __init__(
        self,
        objects: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        remove_type: _Optional[_Union[ObjectType, str]] = ...,
        behavior: _Optional[_Union[DropBehavior, str]] = ...,
        missing_ok: bool = ...,
        concurrent: bool = ...,
    ) -> None: ...

class TruncateStmt(_message.Message):
    __slots__ = ("relations", "restart_seqs", "behavior")
    RELATIONS_FIELD_NUMBER: _ClassVar[int]
    RESTART_SEQS_FIELD_NUMBER: _ClassVar[int]
    BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
    relations: _containers.RepeatedCompositeFieldContainer[Node]
    restart_seqs: bool
    behavior: DropBehavior
    def __init__(
        self,
        relations: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        restart_seqs: bool = ...,
        behavior: _Optional[_Union[DropBehavior, str]] = ...,
    ) -> None: ...

class CommentStmt(_message.Message):
    __slots__ = ("objtype", "object", "comment")
    OBJTYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    objtype: ObjectType
    object: Node
    comment: str
    def __init__(
        self,
        objtype: _Optional[_Union[ObjectType, str]] = ...,
        object: _Optional[_Union[Node, _Mapping]] = ...,
        comment: _Optional[str] = ...,
    ) -> None: ...

class SecLabelStmt(_message.Message):
    __slots__ = ("objtype", "object", "provider", "label")
    OBJTYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    objtype: ObjectType
    object: Node
    provider: str
    label: str
    def __init__(
        self,
        objtype: _Optional[_Union[ObjectType, str]] = ...,
        object: _Optional[_Union[Node, _Mapping]] = ...,
        provider: _Optional[str] = ...,
        label: _Optional[str] = ...,
    ) -> None: ...

class DeclareCursorStmt(_message.Message):
    __slots__ = ("portalname", "options", "query")
    PORTALNAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    portalname: str
    options: int
    query: Node
    def __init__(
        self,
        portalname: _Optional[str] = ...,
        options: _Optional[int] = ...,
        query: _Optional[_Union[Node, _Mapping]] = ...,
    ) -> None: ...

class ClosePortalStmt(_message.Message):
    __slots__ = ("portalname",)
    PORTALNAME_FIELD_NUMBER: _ClassVar[int]
    portalname: str
    def __init__(self, portalname: _Optional[str] = ...) -> None: ...

class FetchStmt(_message.Message):
    __slots__ = ("direction", "how_many", "portalname", "ismove")
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    HOW_MANY_FIELD_NUMBER: _ClassVar[int]
    PORTALNAME_FIELD_NUMBER: _ClassVar[int]
    ISMOVE_FIELD_NUMBER: _ClassVar[int]
    direction: FetchDirection
    how_many: int
    portalname: str
    ismove: bool
    def __init__(
        self,
        direction: _Optional[_Union[FetchDirection, str]] = ...,
        how_many: _Optional[int] = ...,
        portalname: _Optional[str] = ...,
        ismove: bool = ...,
    ) -> None: ...

class IndexStmt(_message.Message):
    __slots__ = (
        "idxname",
        "relation",
        "access_method",
        "table_space",
        "index_params",
        "index_including_params",
        "options",
        "where_clause",
        "exclude_op_names",
        "idxcomment",
        "index_oid",
        "old_number",
        "old_create_subid",
        "old_first_relfilelocator_subid",
        "unique",
        "nulls_not_distinct",
        "primary",
        "isconstraint",
        "deferrable",
        "initdeferred",
        "transformed",
        "concurrent",
        "if_not_exists",
        "reset_default_tblspc",
    )
    IDXNAME_FIELD_NUMBER: _ClassVar[int]
    RELATION_FIELD_NUMBER: _ClassVar[int]
    ACCESS_METHOD_FIELD_NUMBER: _ClassVar[int]
    TABLE_SPACE_FIELD_NUMBER: _ClassVar[int]
    INDEX_PARAMS_FIELD_NUMBER: _ClassVar[int]
    INDEX_INCLUDING_PARAMS_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    WHERE_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_OP_NAMES_FIELD_NUMBER: _ClassVar[int]
    IDXCOMMENT_FIELD_NUMBER: _ClassVar[int]
    INDEX_OID_FIELD_NUMBER: _ClassVar[int]
    OLD_NUMBER_FIELD_NUMBER: _ClassVar[int]
    OLD_CREATE_SUBID_FIELD_NUMBER: _ClassVar[int]
    OLD_FIRST_RELFILELOCATOR_SUBID_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_FIELD_NUMBER: _ClassVar[int]
    NULLS_NOT_DISTINCT_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_FIELD_NUMBER: _ClassVar[int]
    ISCONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    DEFERRABLE_FIELD_NUMBER: _ClassVar[int]
    INITDEFERRED_FIELD_NUMBER: _ClassVar[int]
    TRANSFORMED_FIELD_NUMBER: _ClassVar[int]
    CONCURRENT_FIELD_NUMBER: _ClassVar[int]
    IF_NOT_EXISTS_FIELD_NUMBER: _ClassVar[int]
    RESET_DEFAULT_TBLSPC_FIELD_NUMBER: _ClassVar[int]
    idxname: str
    relation: RangeVar
    access_method: str
    table_space: str
    index_params: _containers.RepeatedCompositeFieldContainer[Node]
    index_including_params: _containers.RepeatedCompositeFieldContainer[Node]
    options: _containers.RepeatedCompositeFieldContainer[Node]
    where_clause: Node
    exclude_op_names: _containers.RepeatedCompositeFieldContainer[Node]
    idxcomment: str
    index_oid: int
    old_number: int
    old_create_subid: int
    old_first_relfilelocator_subid: int
    unique: bool
    nulls_not_distinct: bool
    primary: bool
    isconstraint: bool
    deferrable: bool
    initdeferred: bool
    transformed: bool
    concurrent: bool
    if_not_exists: bool
    reset_default_tblspc: bool
    def __init__(
        self,
        idxname: _Optional[str] = ...,
        relation: _Optional[_Union[RangeVar, _Mapping]] = ...,
        access_method: _Optional[str] = ...,
        table_space: _Optional[str] = ...,
        index_params: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        index_including_params: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        where_clause: _Optional[_Union[Node, _Mapping]] = ...,
        exclude_op_names: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        idxcomment: _Optional[str] = ...,
        index_oid: _Optional[int] = ...,
        old_number: _Optional[int] = ...,
        old_create_subid: _Optional[int] = ...,
        old_first_relfilelocator_subid: _Optional[int] = ...,
        unique: bool = ...,
        nulls_not_distinct: bool = ...,
        primary: bool = ...,
        isconstraint: bool = ...,
        deferrable: bool = ...,
        initdeferred: bool = ...,
        transformed: bool = ...,
        concurrent: bool = ...,
        if_not_exists: bool = ...,
        reset_default_tblspc: bool = ...,
    ) -> None: ...

class CreateStatsStmt(_message.Message):
    __slots__ = ("defnames", "stat_types", "exprs", "relations", "stxcomment", "transformed", "if_not_exists")
    DEFNAMES_FIELD_NUMBER: _ClassVar[int]
    STAT_TYPES_FIELD_NUMBER: _ClassVar[int]
    EXPRS_FIELD_NUMBER: _ClassVar[int]
    RELATIONS_FIELD_NUMBER: _ClassVar[int]
    STXCOMMENT_FIELD_NUMBER: _ClassVar[int]
    TRANSFORMED_FIELD_NUMBER: _ClassVar[int]
    IF_NOT_EXISTS_FIELD_NUMBER: _ClassVar[int]
    defnames: _containers.RepeatedCompositeFieldContainer[Node]
    stat_types: _containers.RepeatedCompositeFieldContainer[Node]
    exprs: _containers.RepeatedCompositeFieldContainer[Node]
    relations: _containers.RepeatedCompositeFieldContainer[Node]
    stxcomment: str
    transformed: bool
    if_not_exists: bool
    def __init__(
        self,
        defnames: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        stat_types: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        exprs: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        relations: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        stxcomment: _Optional[str] = ...,
        transformed: bool = ...,
        if_not_exists: bool = ...,
    ) -> None: ...

class StatsElem(_message.Message):
    __slots__ = ("name", "expr")
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    name: str
    expr: Node
    def __init__(self, name: _Optional[str] = ..., expr: _Optional[_Union[Node, _Mapping]] = ...) -> None: ...

class AlterStatsStmt(_message.Message):
    __slots__ = ("defnames", "stxstattarget", "missing_ok")
    DEFNAMES_FIELD_NUMBER: _ClassVar[int]
    STXSTATTARGET_FIELD_NUMBER: _ClassVar[int]
    MISSING_OK_FIELD_NUMBER: _ClassVar[int]
    defnames: _containers.RepeatedCompositeFieldContainer[Node]
    stxstattarget: int
    missing_ok: bool
    def __init__(
        self,
        defnames: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        stxstattarget: _Optional[int] = ...,
        missing_ok: bool = ...,
    ) -> None: ...

class CreateFunctionStmt(_message.Message):
    __slots__ = ("is_procedure", "replace", "funcname", "parameters", "return_type", "options", "sql_body")
    IS_PROCEDURE_FIELD_NUMBER: _ClassVar[int]
    REPLACE_FIELD_NUMBER: _ClassVar[int]
    FUNCNAME_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    RETURN_TYPE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SQL_BODY_FIELD_NUMBER: _ClassVar[int]
    is_procedure: bool
    replace: bool
    funcname: _containers.RepeatedCompositeFieldContainer[Node]
    parameters: _containers.RepeatedCompositeFieldContainer[Node]
    return_type: TypeName
    options: _containers.RepeatedCompositeFieldContainer[Node]
    sql_body: Node
    def __init__(
        self,
        is_procedure: bool = ...,
        replace: bool = ...,
        funcname: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        parameters: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        return_type: _Optional[_Union[TypeName, _Mapping]] = ...,
        options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        sql_body: _Optional[_Union[Node, _Mapping]] = ...,
    ) -> None: ...

class FunctionParameter(_message.Message):
    __slots__ = ("name", "arg_type", "mode", "defexpr")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ARG_TYPE_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    DEFEXPR_FIELD_NUMBER: _ClassVar[int]
    name: str
    arg_type: TypeName
    mode: FunctionParameterMode
    defexpr: Node
    def __init__(
        self,
        name: _Optional[str] = ...,
        arg_type: _Optional[_Union[TypeName, _Mapping]] = ...,
        mode: _Optional[_Union[FunctionParameterMode, str]] = ...,
        defexpr: _Optional[_Union[Node, _Mapping]] = ...,
    ) -> None: ...

class AlterFunctionStmt(_message.Message):
    __slots__ = ("objtype", "func", "actions")
    OBJTYPE_FIELD_NUMBER: _ClassVar[int]
    FUNC_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    objtype: ObjectType
    func: ObjectWithArgs
    actions: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        objtype: _Optional[_Union[ObjectType, str]] = ...,
        func: _Optional[_Union[ObjectWithArgs, _Mapping]] = ...,
        actions: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class DoStmt(_message.Message):
    __slots__ = ("args",)
    ARGS_FIELD_NUMBER: _ClassVar[int]
    args: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(self, args: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...) -> None: ...

class InlineCodeBlock(_message.Message):
    __slots__ = ("source_text", "lang_oid", "lang_is_trusted", "atomic")
    SOURCE_TEXT_FIELD_NUMBER: _ClassVar[int]
    LANG_OID_FIELD_NUMBER: _ClassVar[int]
    LANG_IS_TRUSTED_FIELD_NUMBER: _ClassVar[int]
    ATOMIC_FIELD_NUMBER: _ClassVar[int]
    source_text: str
    lang_oid: int
    lang_is_trusted: bool
    atomic: bool
    def __init__(
        self,
        source_text: _Optional[str] = ...,
        lang_oid: _Optional[int] = ...,
        lang_is_trusted: bool = ...,
        atomic: bool = ...,
    ) -> None: ...

class CallStmt(_message.Message):
    __slots__ = ("funccall", "funcexpr", "outargs")
    FUNCCALL_FIELD_NUMBER: _ClassVar[int]
    FUNCEXPR_FIELD_NUMBER: _ClassVar[int]
    OUTARGS_FIELD_NUMBER: _ClassVar[int]
    funccall: FuncCall
    funcexpr: FuncExpr
    outargs: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        funccall: _Optional[_Union[FuncCall, _Mapping]] = ...,
        funcexpr: _Optional[_Union[FuncExpr, _Mapping]] = ...,
        outargs: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class CallContext(_message.Message):
    __slots__ = ("atomic",)
    ATOMIC_FIELD_NUMBER: _ClassVar[int]
    atomic: bool
    def __init__(self, atomic: bool = ...) -> None: ...

class RenameStmt(_message.Message):
    __slots__ = ("rename_type", "relation_type", "relation", "object", "subname", "newname", "behavior", "missing_ok")
    RENAME_TYPE_FIELD_NUMBER: _ClassVar[int]
    RELATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    RELATION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    SUBNAME_FIELD_NUMBER: _ClassVar[int]
    NEWNAME_FIELD_NUMBER: _ClassVar[int]
    BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
    MISSING_OK_FIELD_NUMBER: _ClassVar[int]
    rename_type: ObjectType
    relation_type: ObjectType
    relation: RangeVar
    object: Node
    subname: str
    newname: str
    behavior: DropBehavior
    missing_ok: bool
    def __init__(
        self,
        rename_type: _Optional[_Union[ObjectType, str]] = ...,
        relation_type: _Optional[_Union[ObjectType, str]] = ...,
        relation: _Optional[_Union[RangeVar, _Mapping]] = ...,
        object: _Optional[_Union[Node, _Mapping]] = ...,
        subname: _Optional[str] = ...,
        newname: _Optional[str] = ...,
        behavior: _Optional[_Union[DropBehavior, str]] = ...,
        missing_ok: bool = ...,
    ) -> None: ...

class AlterObjectDependsStmt(_message.Message):
    __slots__ = ("object_type", "relation", "object", "extname", "remove")
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    RELATION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    EXTNAME_FIELD_NUMBER: _ClassVar[int]
    REMOVE_FIELD_NUMBER: _ClassVar[int]
    object_type: ObjectType
    relation: RangeVar
    object: Node
    extname: String
    remove: bool
    def __init__(
        self,
        object_type: _Optional[_Union[ObjectType, str]] = ...,
        relation: _Optional[_Union[RangeVar, _Mapping]] = ...,
        object: _Optional[_Union[Node, _Mapping]] = ...,
        extname: _Optional[_Union[String, _Mapping]] = ...,
        remove: bool = ...,
    ) -> None: ...

class AlterObjectSchemaStmt(_message.Message):
    __slots__ = ("object_type", "relation", "object", "newschema", "missing_ok")
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    RELATION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    NEWSCHEMA_FIELD_NUMBER: _ClassVar[int]
    MISSING_OK_FIELD_NUMBER: _ClassVar[int]
    object_type: ObjectType
    relation: RangeVar
    object: Node
    newschema: str
    missing_ok: bool
    def __init__(
        self,
        object_type: _Optional[_Union[ObjectType, str]] = ...,
        relation: _Optional[_Union[RangeVar, _Mapping]] = ...,
        object: _Optional[_Union[Node, _Mapping]] = ...,
        newschema: _Optional[str] = ...,
        missing_ok: bool = ...,
    ) -> None: ...

class AlterOwnerStmt(_message.Message):
    __slots__ = ("object_type", "relation", "object", "newowner")
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    RELATION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    NEWOWNER_FIELD_NUMBER: _ClassVar[int]
    object_type: ObjectType
    relation: RangeVar
    object: Node
    newowner: RoleSpec
    def __init__(
        self,
        object_type: _Optional[_Union[ObjectType, str]] = ...,
        relation: _Optional[_Union[RangeVar, _Mapping]] = ...,
        object: _Optional[_Union[Node, _Mapping]] = ...,
        newowner: _Optional[_Union[RoleSpec, _Mapping]] = ...,
    ) -> None: ...

class AlterOperatorStmt(_message.Message):
    __slots__ = ("opername", "options")
    OPERNAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    opername: ObjectWithArgs
    options: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        opername: _Optional[_Union[ObjectWithArgs, _Mapping]] = ...,
        options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class AlterTypeStmt(_message.Message):
    __slots__ = ("type_name", "options")
    TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    type_name: _containers.RepeatedCompositeFieldContainer[Node]
    options: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        type_name: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class RuleStmt(_message.Message):
    __slots__ = ("relation", "rulename", "where_clause", "event", "instead", "actions", "replace")
    RELATION_FIELD_NUMBER: _ClassVar[int]
    RULENAME_FIELD_NUMBER: _ClassVar[int]
    WHERE_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    INSTEAD_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    REPLACE_FIELD_NUMBER: _ClassVar[int]
    relation: RangeVar
    rulename: str
    where_clause: Node
    event: CmdType
    instead: bool
    actions: _containers.RepeatedCompositeFieldContainer[Node]
    replace: bool
    def __init__(
        self,
        relation: _Optional[_Union[RangeVar, _Mapping]] = ...,
        rulename: _Optional[str] = ...,
        where_clause: _Optional[_Union[Node, _Mapping]] = ...,
        event: _Optional[_Union[CmdType, str]] = ...,
        instead: bool = ...,
        actions: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        replace: bool = ...,
    ) -> None: ...

class NotifyStmt(_message.Message):
    __slots__ = ("conditionname", "payload")
    CONDITIONNAME_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    conditionname: str
    payload: str
    def __init__(self, conditionname: _Optional[str] = ..., payload: _Optional[str] = ...) -> None: ...

class ListenStmt(_message.Message):
    __slots__ = ("conditionname",)
    CONDITIONNAME_FIELD_NUMBER: _ClassVar[int]
    conditionname: str
    def __init__(self, conditionname: _Optional[str] = ...) -> None: ...

class UnlistenStmt(_message.Message):
    __slots__ = ("conditionname",)
    CONDITIONNAME_FIELD_NUMBER: _ClassVar[int]
    conditionname: str
    def __init__(self, conditionname: _Optional[str] = ...) -> None: ...

class TransactionStmt(_message.Message):
    __slots__ = ("kind", "options", "savepoint_name", "gid", "chain")
    KIND_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SAVEPOINT_NAME_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    CHAIN_FIELD_NUMBER: _ClassVar[int]
    kind: TransactionStmtKind
    options: _containers.RepeatedCompositeFieldContainer[Node]
    savepoint_name: str
    gid: str
    chain: bool
    def __init__(
        self,
        kind: _Optional[_Union[TransactionStmtKind, str]] = ...,
        options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        savepoint_name: _Optional[str] = ...,
        gid: _Optional[str] = ...,
        chain: bool = ...,
    ) -> None: ...

class CompositeTypeStmt(_message.Message):
    __slots__ = ("typevar", "coldeflist")
    TYPEVAR_FIELD_NUMBER: _ClassVar[int]
    COLDEFLIST_FIELD_NUMBER: _ClassVar[int]
    typevar: RangeVar
    coldeflist: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        typevar: _Optional[_Union[RangeVar, _Mapping]] = ...,
        coldeflist: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class CreateEnumStmt(_message.Message):
    __slots__ = ("type_name", "vals")
    TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    VALS_FIELD_NUMBER: _ClassVar[int]
    type_name: _containers.RepeatedCompositeFieldContainer[Node]
    vals: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        type_name: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        vals: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class CreateRangeStmt(_message.Message):
    __slots__ = ("type_name", "params")
    TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    type_name: _containers.RepeatedCompositeFieldContainer[Node]
    params: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        type_name: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        params: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class AlterEnumStmt(_message.Message):
    __slots__ = ("type_name", "old_val", "new_val", "new_val_neighbor", "new_val_is_after", "skip_if_new_val_exists")
    TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    OLD_VAL_FIELD_NUMBER: _ClassVar[int]
    NEW_VAL_FIELD_NUMBER: _ClassVar[int]
    NEW_VAL_NEIGHBOR_FIELD_NUMBER: _ClassVar[int]
    NEW_VAL_IS_AFTER_FIELD_NUMBER: _ClassVar[int]
    SKIP_IF_NEW_VAL_EXISTS_FIELD_NUMBER: _ClassVar[int]
    type_name: _containers.RepeatedCompositeFieldContainer[Node]
    old_val: str
    new_val: str
    new_val_neighbor: str
    new_val_is_after: bool
    skip_if_new_val_exists: bool
    def __init__(
        self,
        type_name: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        old_val: _Optional[str] = ...,
        new_val: _Optional[str] = ...,
        new_val_neighbor: _Optional[str] = ...,
        new_val_is_after: bool = ...,
        skip_if_new_val_exists: bool = ...,
    ) -> None: ...

class ViewStmt(_message.Message):
    __slots__ = ("view", "aliases", "query", "replace", "options", "with_check_option")
    VIEW_FIELD_NUMBER: _ClassVar[int]
    ALIASES_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    REPLACE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    WITH_CHECK_OPTION_FIELD_NUMBER: _ClassVar[int]
    view: RangeVar
    aliases: _containers.RepeatedCompositeFieldContainer[Node]
    query: Node
    replace: bool
    options: _containers.RepeatedCompositeFieldContainer[Node]
    with_check_option: ViewCheckOption
    def __init__(
        self,
        view: _Optional[_Union[RangeVar, _Mapping]] = ...,
        aliases: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        query: _Optional[_Union[Node, _Mapping]] = ...,
        replace: bool = ...,
        options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        with_check_option: _Optional[_Union[ViewCheckOption, str]] = ...,
    ) -> None: ...

class LoadStmt(_message.Message):
    __slots__ = ("filename",)
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    def __init__(self, filename: _Optional[str] = ...) -> None: ...

class CreatedbStmt(_message.Message):
    __slots__ = ("dbname", "options")
    DBNAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    dbname: str
    options: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self, dbname: _Optional[str] = ..., options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...
    ) -> None: ...

class AlterDatabaseStmt(_message.Message):
    __slots__ = ("dbname", "options")
    DBNAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    dbname: str
    options: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self, dbname: _Optional[str] = ..., options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...
    ) -> None: ...

class AlterDatabaseRefreshCollStmt(_message.Message):
    __slots__ = ("dbname",)
    DBNAME_FIELD_NUMBER: _ClassVar[int]
    dbname: str
    def __init__(self, dbname: _Optional[str] = ...) -> None: ...

class AlterDatabaseSetStmt(_message.Message):
    __slots__ = ("dbname", "setstmt")
    DBNAME_FIELD_NUMBER: _ClassVar[int]
    SETSTMT_FIELD_NUMBER: _ClassVar[int]
    dbname: str
    setstmt: VariableSetStmt
    def __init__(
        self, dbname: _Optional[str] = ..., setstmt: _Optional[_Union[VariableSetStmt, _Mapping]] = ...
    ) -> None: ...

class DropdbStmt(_message.Message):
    __slots__ = ("dbname", "missing_ok", "options")
    DBNAME_FIELD_NUMBER: _ClassVar[int]
    MISSING_OK_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    dbname: str
    missing_ok: bool
    options: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        dbname: _Optional[str] = ...,
        missing_ok: bool = ...,
        options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class AlterSystemStmt(_message.Message):
    __slots__ = ("setstmt",)
    SETSTMT_FIELD_NUMBER: _ClassVar[int]
    setstmt: VariableSetStmt
    def __init__(self, setstmt: _Optional[_Union[VariableSetStmt, _Mapping]] = ...) -> None: ...

class ClusterStmt(_message.Message):
    __slots__ = ("relation", "indexname", "params")
    RELATION_FIELD_NUMBER: _ClassVar[int]
    INDEXNAME_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    relation: RangeVar
    indexname: str
    params: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        relation: _Optional[_Union[RangeVar, _Mapping]] = ...,
        indexname: _Optional[str] = ...,
        params: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class VacuumStmt(_message.Message):
    __slots__ = ("options", "rels", "is_vacuumcmd")
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    RELS_FIELD_NUMBER: _ClassVar[int]
    IS_VACUUMCMD_FIELD_NUMBER: _ClassVar[int]
    options: _containers.RepeatedCompositeFieldContainer[Node]
    rels: _containers.RepeatedCompositeFieldContainer[Node]
    is_vacuumcmd: bool
    def __init__(
        self,
        options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        rels: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        is_vacuumcmd: bool = ...,
    ) -> None: ...

class VacuumRelation(_message.Message):
    __slots__ = ("relation", "oid", "va_cols")
    RELATION_FIELD_NUMBER: _ClassVar[int]
    OID_FIELD_NUMBER: _ClassVar[int]
    VA_COLS_FIELD_NUMBER: _ClassVar[int]
    relation: RangeVar
    oid: int
    va_cols: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        relation: _Optional[_Union[RangeVar, _Mapping]] = ...,
        oid: _Optional[int] = ...,
        va_cols: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class ExplainStmt(_message.Message):
    __slots__ = ("query", "options")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    query: Node
    options: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        query: _Optional[_Union[Node, _Mapping]] = ...,
        options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class CreateTableAsStmt(_message.Message):
    __slots__ = ("query", "into", "objtype", "is_select_into", "if_not_exists")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    INTO_FIELD_NUMBER: _ClassVar[int]
    OBJTYPE_FIELD_NUMBER: _ClassVar[int]
    IS_SELECT_INTO_FIELD_NUMBER: _ClassVar[int]
    IF_NOT_EXISTS_FIELD_NUMBER: _ClassVar[int]
    query: Node
    into: IntoClause
    objtype: ObjectType
    is_select_into: bool
    if_not_exists: bool
    def __init__(
        self,
        query: _Optional[_Union[Node, _Mapping]] = ...,
        into: _Optional[_Union[IntoClause, _Mapping]] = ...,
        objtype: _Optional[_Union[ObjectType, str]] = ...,
        is_select_into: bool = ...,
        if_not_exists: bool = ...,
    ) -> None: ...

class RefreshMatViewStmt(_message.Message):
    __slots__ = ("concurrent", "skip_data", "relation")
    CONCURRENT_FIELD_NUMBER: _ClassVar[int]
    SKIP_DATA_FIELD_NUMBER: _ClassVar[int]
    RELATION_FIELD_NUMBER: _ClassVar[int]
    concurrent: bool
    skip_data: bool
    relation: RangeVar
    def __init__(
        self, concurrent: bool = ..., skip_data: bool = ..., relation: _Optional[_Union[RangeVar, _Mapping]] = ...
    ) -> None: ...

class CheckPointStmt(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DiscardStmt(_message.Message):
    __slots__ = ("target",)
    TARGET_FIELD_NUMBER: _ClassVar[int]
    target: DiscardMode
    def __init__(self, target: _Optional[_Union[DiscardMode, str]] = ...) -> None: ...

class LockStmt(_message.Message):
    __slots__ = ("relations", "mode", "nowait")
    RELATIONS_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    NOWAIT_FIELD_NUMBER: _ClassVar[int]
    relations: _containers.RepeatedCompositeFieldContainer[Node]
    mode: int
    nowait: bool
    def __init__(
        self,
        relations: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        mode: _Optional[int] = ...,
        nowait: bool = ...,
    ) -> None: ...

class ConstraintsSetStmt(_message.Message):
    __slots__ = ("constraints", "deferred")
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    DEFERRED_FIELD_NUMBER: _ClassVar[int]
    constraints: _containers.RepeatedCompositeFieldContainer[Node]
    deferred: bool
    def __init__(
        self, constraints: _Optional[_Iterable[_Union[Node, _Mapping]]] = ..., deferred: bool = ...
    ) -> None: ...

class ReindexStmt(_message.Message):
    __slots__ = ("kind", "relation", "name", "params")
    KIND_FIELD_NUMBER: _ClassVar[int]
    RELATION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    kind: ReindexObjectType
    relation: RangeVar
    name: str
    params: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        kind: _Optional[_Union[ReindexObjectType, str]] = ...,
        relation: _Optional[_Union[RangeVar, _Mapping]] = ...,
        name: _Optional[str] = ...,
        params: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class CreateConversionStmt(_message.Message):
    __slots__ = ("conversion_name", "for_encoding_name", "to_encoding_name", "func_name")
    CONVERSION_NAME_FIELD_NUMBER: _ClassVar[int]
    FOR_ENCODING_NAME_FIELD_NUMBER: _ClassVar[int]
    TO_ENCODING_NAME_FIELD_NUMBER: _ClassVar[int]
    FUNC_NAME_FIELD_NUMBER: _ClassVar[int]
    DEF_FIELD_NUMBER: _ClassVar[int]
    conversion_name: _containers.RepeatedCompositeFieldContainer[Node]
    for_encoding_name: str
    to_encoding_name: str
    func_name: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        conversion_name: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        for_encoding_name: _Optional[str] = ...,
        to_encoding_name: _Optional[str] = ...,
        func_name: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        **kwargs,
    ) -> None: ...

class CreateCastStmt(_message.Message):
    __slots__ = ("sourcetype", "targettype", "func", "context", "inout")
    SOURCETYPE_FIELD_NUMBER: _ClassVar[int]
    TARGETTYPE_FIELD_NUMBER: _ClassVar[int]
    FUNC_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    INOUT_FIELD_NUMBER: _ClassVar[int]
    sourcetype: TypeName
    targettype: TypeName
    func: ObjectWithArgs
    context: CoercionContext
    inout: bool
    def __init__(
        self,
        sourcetype: _Optional[_Union[TypeName, _Mapping]] = ...,
        targettype: _Optional[_Union[TypeName, _Mapping]] = ...,
        func: _Optional[_Union[ObjectWithArgs, _Mapping]] = ...,
        context: _Optional[_Union[CoercionContext, str]] = ...,
        inout: bool = ...,
    ) -> None: ...

class CreateTransformStmt(_message.Message):
    __slots__ = ("replace", "type_name", "lang", "fromsql", "tosql")
    REPLACE_FIELD_NUMBER: _ClassVar[int]
    TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    LANG_FIELD_NUMBER: _ClassVar[int]
    FROMSQL_FIELD_NUMBER: _ClassVar[int]
    TOSQL_FIELD_NUMBER: _ClassVar[int]
    replace: bool
    type_name: TypeName
    lang: str
    fromsql: ObjectWithArgs
    tosql: ObjectWithArgs
    def __init__(
        self,
        replace: bool = ...,
        type_name: _Optional[_Union[TypeName, _Mapping]] = ...,
        lang: _Optional[str] = ...,
        fromsql: _Optional[_Union[ObjectWithArgs, _Mapping]] = ...,
        tosql: _Optional[_Union[ObjectWithArgs, _Mapping]] = ...,
    ) -> None: ...

class PrepareStmt(_message.Message):
    __slots__ = ("name", "argtypes", "query")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ARGTYPES_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    name: str
    argtypes: _containers.RepeatedCompositeFieldContainer[Node]
    query: Node
    def __init__(
        self,
        name: _Optional[str] = ...,
        argtypes: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        query: _Optional[_Union[Node, _Mapping]] = ...,
    ) -> None: ...

class ExecuteStmt(_message.Message):
    __slots__ = ("name", "params")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    name: str
    params: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self, name: _Optional[str] = ..., params: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...
    ) -> None: ...

class DeallocateStmt(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DropOwnedStmt(_message.Message):
    __slots__ = ("roles", "behavior")
    ROLES_FIELD_NUMBER: _ClassVar[int]
    BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
    roles: _containers.RepeatedCompositeFieldContainer[Node]
    behavior: DropBehavior
    def __init__(
        self,
        roles: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        behavior: _Optional[_Union[DropBehavior, str]] = ...,
    ) -> None: ...

class ReassignOwnedStmt(_message.Message):
    __slots__ = ("roles", "newrole")
    ROLES_FIELD_NUMBER: _ClassVar[int]
    NEWROLE_FIELD_NUMBER: _ClassVar[int]
    roles: _containers.RepeatedCompositeFieldContainer[Node]
    newrole: RoleSpec
    def __init__(
        self,
        roles: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        newrole: _Optional[_Union[RoleSpec, _Mapping]] = ...,
    ) -> None: ...

class AlterTSDictionaryStmt(_message.Message):
    __slots__ = ("dictname", "options")
    DICTNAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    dictname: _containers.RepeatedCompositeFieldContainer[Node]
    options: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        dictname: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class AlterTSConfigurationStmt(_message.Message):
    __slots__ = ("kind", "cfgname", "tokentype", "dicts", "override", "replace", "missing_ok")
    KIND_FIELD_NUMBER: _ClassVar[int]
    CFGNAME_FIELD_NUMBER: _ClassVar[int]
    TOKENTYPE_FIELD_NUMBER: _ClassVar[int]
    DICTS_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    REPLACE_FIELD_NUMBER: _ClassVar[int]
    MISSING_OK_FIELD_NUMBER: _ClassVar[int]
    kind: AlterTSConfigType
    cfgname: _containers.RepeatedCompositeFieldContainer[Node]
    tokentype: _containers.RepeatedCompositeFieldContainer[Node]
    dicts: _containers.RepeatedCompositeFieldContainer[Node]
    override: bool
    replace: bool
    missing_ok: bool
    def __init__(
        self,
        kind: _Optional[_Union[AlterTSConfigType, str]] = ...,
        cfgname: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        tokentype: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        dicts: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        override: bool = ...,
        replace: bool = ...,
        missing_ok: bool = ...,
    ) -> None: ...

class PublicationTable(_message.Message):
    __slots__ = ("relation", "where_clause", "columns")
    RELATION_FIELD_NUMBER: _ClassVar[int]
    WHERE_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    relation: RangeVar
    where_clause: Node
    columns: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        relation: _Optional[_Union[RangeVar, _Mapping]] = ...,
        where_clause: _Optional[_Union[Node, _Mapping]] = ...,
        columns: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class PublicationObjSpec(_message.Message):
    __slots__ = ("pubobjtype", "name", "pubtable", "location")
    PUBOBJTYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PUBTABLE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    pubobjtype: PublicationObjSpecType
    name: str
    pubtable: PublicationTable
    location: int
    def __init__(
        self,
        pubobjtype: _Optional[_Union[PublicationObjSpecType, str]] = ...,
        name: _Optional[str] = ...,
        pubtable: _Optional[_Union[PublicationTable, _Mapping]] = ...,
        location: _Optional[int] = ...,
    ) -> None: ...

class CreatePublicationStmt(_message.Message):
    __slots__ = ("pubname", "options", "pubobjects", "for_all_tables")
    PUBNAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PUBOBJECTS_FIELD_NUMBER: _ClassVar[int]
    FOR_ALL_TABLES_FIELD_NUMBER: _ClassVar[int]
    pubname: str
    options: _containers.RepeatedCompositeFieldContainer[Node]
    pubobjects: _containers.RepeatedCompositeFieldContainer[Node]
    for_all_tables: bool
    def __init__(
        self,
        pubname: _Optional[str] = ...,
        options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        pubobjects: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        for_all_tables: bool = ...,
    ) -> None: ...

class AlterPublicationStmt(_message.Message):
    __slots__ = ("pubname", "options", "pubobjects", "for_all_tables", "action")
    PUBNAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PUBOBJECTS_FIELD_NUMBER: _ClassVar[int]
    FOR_ALL_TABLES_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    pubname: str
    options: _containers.RepeatedCompositeFieldContainer[Node]
    pubobjects: _containers.RepeatedCompositeFieldContainer[Node]
    for_all_tables: bool
    action: AlterPublicationAction
    def __init__(
        self,
        pubname: _Optional[str] = ...,
        options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        pubobjects: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        for_all_tables: bool = ...,
        action: _Optional[_Union[AlterPublicationAction, str]] = ...,
    ) -> None: ...

class CreateSubscriptionStmt(_message.Message):
    __slots__ = ("subname", "conninfo", "publication", "options")
    SUBNAME_FIELD_NUMBER: _ClassVar[int]
    CONNINFO_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    subname: str
    conninfo: str
    publication: _containers.RepeatedCompositeFieldContainer[Node]
    options: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        subname: _Optional[str] = ...,
        conninfo: _Optional[str] = ...,
        publication: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class AlterSubscriptionStmt(_message.Message):
    __slots__ = ("kind", "subname", "conninfo", "publication", "options")
    KIND_FIELD_NUMBER: _ClassVar[int]
    SUBNAME_FIELD_NUMBER: _ClassVar[int]
    CONNINFO_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    kind: AlterSubscriptionType
    subname: str
    conninfo: str
    publication: _containers.RepeatedCompositeFieldContainer[Node]
    options: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(
        self,
        kind: _Optional[_Union[AlterSubscriptionType, str]] = ...,
        subname: _Optional[str] = ...,
        conninfo: _Optional[str] = ...,
        publication: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
        options: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...,
    ) -> None: ...

class DropSubscriptionStmt(_message.Message):
    __slots__ = ("subname", "missing_ok", "behavior")
    SUBNAME_FIELD_NUMBER: _ClassVar[int]
    MISSING_OK_FIELD_NUMBER: _ClassVar[int]
    BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
    subname: str
    missing_ok: bool
    behavior: DropBehavior
    def __init__(
        self,
        subname: _Optional[str] = ...,
        missing_ok: bool = ...,
        behavior: _Optional[_Union[DropBehavior, str]] = ...,
    ) -> None: ...

class ScanToken(_message.Message):
    __slots__ = ("start", "end", "token", "keyword_kind")
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_KIND_FIELD_NUMBER: _ClassVar[int]
    start: int
    end: int
    token: Token
    keyword_kind: KeywordKind
    def __init__(
        self,
        start: _Optional[int] = ...,
        end: _Optional[int] = ...,
        token: _Optional[_Union[Token, str]] = ...,
        keyword_kind: _Optional[_Union[KeywordKind, str]] = ...,
    ) -> None: ...

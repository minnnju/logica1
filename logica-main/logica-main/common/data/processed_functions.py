#!/usr/bin/python
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Built-in StandardSQL functions."""

import csv
import io

def GetCsv():
  return csv.reader(io.StringIO(CSV_DATA))

CSV_DATA = u"""function,sql_function,aggregates,has_repeated_args,min_args,max_args
$add,+,false,0,2,2
$and,AND,false,1,1,1
$array_at_offset,ARRAY[OFFSET()],false,0,2,2
$array_at_ordinal,ARRAY[ORDINAL()],false,0,2,2
$between,BETWEEN,false,0,3,3
$bitwise_and,&,false,0,2,2
$bitwise_left_shift,<<,false,0,2,2
$bitwise_not,~,false,0,1,1
$bitwise_or,|,false,0,2,2
$bitwise_right_shift,>>,false,0,2,2
$bitwise_xor,^,false,0,2,2
$case_no_value,CASE,false,2,1,1
$case_with_value,CASE,false,2,2,2
$count_star,COUNT(*),true,0,0,0
$divide,/,false,0,2,2
$equal,=,false,0,2,2
$extract,EXTRACT,false,0,2,3
$extract_date,EXTRACT,false,0,1,2
$extract_datetime,EXTRACT,false,0,1,2
$extract_time,EXTRACT,false,0,1,2
$greater,>,false,0,2,2
$greater_or_equal,>=,false,0,2,2
$in,IN,false,1,1,1
$in_array,IN UNNEST,false,0,2,2
$is_false,IS FALSE,false,0,1,1
$is_null,IS NULL,false,0,1,1
$is_true,IS TRUE,false,0,1,1
$less,<,false,0,2,2
$less_or_equal,<=,false,0,2,2
$like,LIKE,false,0,2,2
$make_array,ARRAY[...],false,1,0,0
$multiply,*,false,0,2,2
$not,NOT,false,0,1,1
$not_equal,!=,false,0,2,2
$or,OR,false,1,1,1
$safe_array_at_offset,ARRAY[SAFE_OFFSET()],false,0,2,2
$safe_array_at_ordinal,ARRAY[SAFE_ORDINAL()],false,0,2,2
$subtract,-,false,0,2,2
$unary_minus,-,false,0,1,1
abs,ABS,false,0,1,1
acos,ACOS,false,0,1,1
acosh,ACOSH,false,0,1,1
aead.decrypt_bytes,AEAD.DECRYPT_BYTES,false,0,3,3
aead.decrypt_string,AEAD.DECRYPT_STRING,false,0,3,3
aead.encrypt,AEAD.ENCRYPT,false,0,3,3
any_value,ANY_VALUE,true,0,1,1
approx_count_distinct,APPROX_COUNT_DISTINCT,true,0,1,1
approx_quantiles,APPROX_QUANTILES,true,0,2,2
approx_top_count,APPROX_TOP_COUNT,true,0,2,2
approx_top_sum,APPROX_TOP_SUM,true,0,3,3
array_agg,ARRAY_AGG,true,0,1,1
array_concat,ARRAY_CONCAT,false,1,1,1
array_concat_agg,ARRAY_CONCAT_AGG,true,0,1,1
array_length,ARRAY_LENGTH,false,0,1,1
array_reverse,ARRAY_REVERSE,false,0,1,1
array_to_string,ARRAY_TO_STRING,false,0,2,3
asin,ASIN,false,0,1,1
asinh,ASINH,false,0,1,1
atan,ATAN,false,0,1,1
atan2,ATAN2,false,0,2,2
atanh,ATANH,false,0,1,1
avg,AVG,true,0,1,1
bit_and,BIT_AND,true,0,1,1
bit_cast_to_int32,BIT_CAST_TO_INT32,false,0,1,1
bit_cast_to_int64,BIT_CAST_TO_INT64,false,0,1,1
bit_cast_to_uint32,BIT_CAST_TO_UINT32,false,0,1,1
bit_cast_to_uint64,BIT_CAST_TO_UINT64,false,0,1,1
bit_count,BIT_COUNT,false,0,1,1
bit_or,BIT_OR,true,0,1,1
bit_xor,BIT_XOR,true,0,1,1
byte_length,BYTE_LENGTH,false,0,1,1
ceil,CEIL,false,0,1,1
char_length,CHAR_LENGTH,false,0,1,1
coalesce,COALESCE,false,1,0,0
code_points_to_bytes,CODE_POINTS_TO_BYTES,false,0,1,1
code_points_to_string,CODE_POINTS_TO_STRING,false,0,1,1
concat,CONCAT,false,1,1,1
corr,CORR,true,0,2,2
cos,COS,false,0,1,1
cosh,COSH,false,0,1,1
count,COUNT,true,0,1,1
countif,COUNTIF,true,0,1,1
covar_pop,COVAR_POP,true,0,2,2
covar_samp,COVAR_SAMP,true,0,2,2
cume_dist,CUME_DIST,false,0,0,0
current_date,CURRENT_DATE,false,0,0,1
current_datetime,CURRENT_DATETIME,false,0,0,1
current_time,CURRENT_TIME,false,0,0,1
current_timestamp,CURRENT_TIMESTAMP,false,0,0,0
date,DATE,false,0,1,3
date_add,DATE_ADD,false,0,2,2
date_diff,DATE_DIFF,false,0,3,3
date_from_unix_date,DATE_FROM_UNIX_DATE,false,0,1,1
date_sub,DATE_SUB,false,0,2,2
date_trunc,DATE_TRUNC,false,0,2,2
datetime,DATETIME,false,0,1,6
datetime_add,DATETIME_ADD,false,0,2,2
datetime_diff,DATETIME_DIFF,false,0,3,3
datetime_sub,DATETIME_SUB,false,0,2,2
datetime_trunc,DATETIME_TRUNC,false,0,2,2
dense_rank,DENSE_RANK,false,0,0,0
div,DIV,false,0,2,2
ends_with,ENDS_WITH,false,0,2,2
error,ERROR,false,0,1,1
exp,EXP,false,0,1,1
farm_fingerprint,FARM_FINGERPRINT,false,0,1,1
first_value,FIRST_VALUE,false,0,1,1
floor,FLOOR,false,0,1,1
format,FORMAT,false,1,1,1
format_date,FORMAT_DATE,false,0,2,2
format_datetime,FORMAT_DATETIME,false,0,2,2
format_time,FORMAT_TIME,false,0,2,2
format_timestamp,FORMAT_TIMESTAMP,false,0,2,3
from_base32,FROM_BASE32,false,0,1,1
from_base64,FROM_BASE64,false,0,1,1
from_hex,FROM_HEX,false,0,1,1
from_proto,FROM_PROTO,false,0,1,1
generate_array,GENERATE_ARRAY,false,0,2,3
generate_date_array,GENERATE_DATE_ARRAY,false,0,2,4
generate_timestamp_array,GENERATE_TIMESTAMP_ARRAY,false,0,4,4
generate_uuid,GENERATE_UUID,false,0,0,0
greatest,GREATEST,false,1,0,0
hll_count.extract,HLL_COUNT.EXTRACT,false,0,1,1
hll_count.init,HLL_COUNT.INIT,true,0,1,2
hll_count.merge,HLL_COUNT.MERGE,true,0,1,1
hll_count.merge_partial,HLL_COUNT.MERGE_PARTIAL,true,0,1,1
ieee_divide,IEEE_DIVIDE,false,0,2,2
if,IF,false,0,3,3
ifnull,IFNULL,false,0,2,2
is_inf,IS_INF,false,0,1,1
is_nan,IS_NAN,false,0,1,1
json_extract,JSON_EXTRACT,false,0,2,2
json_extract_scalar,JSON_EXTRACT_SCALAR,false,0,2,2
json_query,JSON_QUERY,false,0,2,2
json_value,JSON_VALUE,false,0,2,2
keys.add_key_from_raw_bytes,KEYS.ADD_KEY_FROM_RAW_BYTES,false,0,3,3
keys.keyset_from_json,KEYS.KEYSET_FROM_JSON,false,0,1,1
keys.keyset_length,KEYS.KEYSET_LENGTH,false,0,1,1
keys.keyset_to_json,KEYS.KEYSET_TO_JSON,false,0,1,1
keys.new_keyset,KEYS.NEW_KEYSET,false,0,1,1
keys.rotate_keyset,KEYS.ROTATE_KEYSET,false,0,2,2
lag,LAG,false,0,1,3
last_value,LAST_VALUE,false,0,1,1
lead,LEAD,false,0,1,3
least,LEAST,false,1,0,0
length,LENGTH,false,0,1,1
ln,LN,false,0,1,1
log,LOG,false,0,1,2
log10,LOG10,false,0,1,1
logical_and,LOGICAL_AND,true,0,1,1
logical_or,LOGICAL_OR,true,0,1,1
lower,LOWER,false,0,1,1
lpad,LPAD,false,0,2,3
ltrim,LTRIM,false,0,1,2
max,MAX,true,0,1,1
md5,MD5,false,0,1,1
min,MIN,true,0,1,1
mod,MOD,false,0,2,2
net.format_ip,NET.FORMAT_IP,false,0,1,1
net.format_packed_ip,NET.FORMAT_PACKED_IP,false,0,1,1
net.host,NET.HOST,false,0,1,1
net.ip_from_string,NET.IP_FROM_STRING,false,0,1,1
net.ip_in_net,NET.IP_IN_NET,false,0,2,2
net.ip_net_mask,NET.IP_NET_MASK,false,0,2,2
net.ip_to_string,NET.IP_TO_STRING,false,0,1,1
net.ip_trunc,NET.IP_TRUNC,false,0,2,2
net.ipv4_from_int64,NET.IPV4_FROM_INT64,false,0,1,1
net.ipv4_to_int64,NET.IPV4_TO_INT64,false,0,1,1
net.make_net,NET.MAKE_NET,false,0,2,2
net.parse_ip,NET.PARSE_IP,false,0,1,1
net.parse_packed_ip,NET.PARSE_PACKED_IP,false,0,1,1
net.public_suffix,NET.PUBLIC_SUFFIX,false,0,1,1
net.reg_domain,NET.REG_DOMAIN,false,0,1,1
net.safe_ip_from_string,NET.SAFE_IP_FROM_STRING,false,0,1,1
normalize,NORMALIZE,false,0,1,2
normalize_and_casefold,NORMALIZE_AND_CASEFOLD,false,0,1,2
nth_value,NTH_VALUE,false,0,2,2
ntile,NTILE,false,0,1,1
nullif,NULLIF,false,0,2,2
parse_date,PARSE_DATE,false,0,2,2
parse_datetime,PARSE_DATETIME,false,0,2,2
parse_time,PARSE_TIME,false,0,2,2
parse_timestamp,PARSE_TIMESTAMP,false,0,2,3
percent_rank,PERCENT_RANK,false,0,0,0
percentile_cont,PERCENTILE_CONT,false,0,2,2
percentile_disc,PERCENTILE_DISC,false,0,2,2
pow,POW,false,0,2,2
proto_default_if_null,PROTO_DEFAULT_IF_NULL,false,0,1,1
rand,RAND,false,0,0,0
range_bucket,RANGE_BUCKET,false,0,2,2
rank,RANK,false,0,0,0
regexp_contains,REGEXP_CONTAINS,false,0,2,2
regexp_extract,REGEXP_EXTRACT,false,0,2,2
regexp_extract_all,REGEXP_EXTRACT_ALL,false,0,2,2
regexp_match,REGEXP_MATCH,false,0,2,2
regexp_replace,REGEXP_REPLACE,false,0,3,3
repeat,REPEAT,false,0,2,2
replace,REPLACE,false,0,3,3
reverse,REVERSE,false,0,1,1
round,ROUND,false,0,1,2
row_number,ROW_NUMBER,false,0,0,0
rpad,RPAD,false,0,2,3
rtrim,RTRIM,false,0,1,2
safe_add,SAFE_ADD,false,0,2,2
safe_convert_bytes_to_string,SAFE_CONVERT_BYTES_TO_STRING,false,0,1,1
safe_divide,SAFE_DIVIDE,false,0,2,2
safe_multiply,SAFE_MULTIPLY,false,0,2,2
safe_negate,SAFE_NEGATE,false,0,1,1
safe_subtract,SAFE_SUBTRACT,false,0,2,2
session_user,SESSION_USER,false,0,0,0
sha1,SHA1,false,0,1,1
sha256,SHA256,false,0,1,1
sha512,SHA512,false,0,1,1
sign,SIGN,false,0,1,1
sin,SIN,false,0,1,1
sinh,SINH,false,0,1,1
split,SPLIT,false,0,1,2
sqrt,SQRT,false,0,1,1
st_accum,ST_ACCUM,true,0,1,1
st_area,ST_AREA,false,0,1,2
st_asbinary,ST_ASBINARY,false,0,1,1
st_asgeojson,ST_ASGEOJSON,false,0,1,2
st_askml,ST_ASKML,false,0,1,1
st_astext,ST_ASTEXT,false,0,1,1
st_boundary,ST_BOUNDARY,false,0,1,1
st_buffer,ST_BUFFER,false,0,2,4
st_bufferwithtolerance,ST_BUFFERWITHTOLERANCE,false,0,3,4
st_centroid,ST_CENTROID,false,0,1,1
st_centroid_agg,ST_CENTROID_AGG,true,0,1,1
st_closestpoint,ST_CLOSESTPOINT,false,0,2,3
st_contains,ST_CONTAINS,false,0,2,2
st_coveredby,ST_COVEREDBY,false,0,2,2
st_covers,ST_COVERS,false,0,2,2
st_difference,ST_DIFFERENCE,false,0,2,2
st_dimension,ST_DIMENSION,false,0,1,1
st_disjoint,ST_DISJOINT,false,0,2,2
st_distance,ST_DISTANCE,false,0,2,3
st_dwithin,ST_DWITHIN,false,0,3,4
st_equals,ST_EQUALS,false,0,2,2
st_geogfromgeojson,ST_GEOGFROMGEOJSON,false,0,1,1
st_geogfromkml,ST_GEOGFROMKML,false,0,1,1
st_geogfromtext,ST_GEOGFROMTEXT,false,0,1,2
st_geogfromwkb,ST_GEOGFROMWKB,false,0,1,1
st_geogpoint,ST_GEOGPOINT,false,0,2,2
st_geogpointfromgeohash,ST_GEOGPOINTFROMGEOHASH,false,0,1,1
st_geohash,ST_GEOHASH,false,0,1,2
st_intersection,ST_INTERSECTION,false,0,2,2
st_intersects,ST_INTERSECTS,false,0,2,2
st_intersectsbox,ST_INTERSECTSBOX,false,0,5,5
st_iscollection,ST_ISCOLLECTION,false,0,1,1
st_isempty,ST_ISEMPTY,false,0,1,1
st_length,ST_LENGTH,false,0,1,2
st_makeline,ST_MAKELINE,false,0,1,2
st_makepolygon,ST_MAKEPOLYGON,false,0,1,2
st_makepolygonoriented,ST_MAKEPOLYGONORIENTED,false,0,1,1
st_maxdistance,ST_MAXDISTANCE,false,0,2,3
st_numpoints,ST_NUMPOINTS,false,0,1,1
st_perimeter,ST_PERIMETER,false,0,1,2
st_simplify,ST_SIMPLIFY,false,0,2,2
st_snaptogrid,ST_SNAPTOGRID,false,0,2,2
st_touches,ST_TOUCHES,false,0,2,2
st_unaryunion,ST_UNARYUNION,false,0,1,1
st_union,ST_UNION,false,0,1,2
st_union_agg,ST_UNION_AGG,true,0,1,1
st_within,ST_WITHIN,false,0,2,2
st_x,ST_X,false,0,1,1
st_y,ST_Y,false,0,1,1
starts_with,STARTS_WITH,false,0,2,2
stddev_pop,STDDEV_POP,true,0,1,1
stddev_samp,STDDEV_SAMP,true,0,1,1
string,STRING,false,0,1,2
string_agg,STRING_AGG,true,0,1,2
strpos,STRPOS,false,0,2,2
substr,SUBSTR,false,0,2,3
sum,SUM,true,0,1,1
tan,TAN,false,0,1,1
tanh,TANH,false,0,1,1
time,TIME,false,0,1,3
time_add,TIME_ADD,false,0,2,2
time_diff,TIME_DIFF,false,0,3,3
time_sub,TIME_SUB,false,0,2,2
time_trunc,TIME_TRUNC,false,0,2,2
timestamp,TIMESTAMP,false,0,1,2
timestamp_add,TIMESTAMP_ADD,false,0,2,2
timestamp_diff,TIMESTAMP_DIFF,false,0,3,3
timestamp_from_unix_micros,TIMESTAMP_FROM_UNIX_MICROS,false,0,1,1
timestamp_from_unix_millis,TIMESTAMP_FROM_UNIX_MILLIS,false,0,1,1
timestamp_from_unix_seconds,TIMESTAMP_FROM_UNIX_SECONDS,false,0,1,1
timestamp_micros,TIMESTAMP_MICROS,false,0,1,1
timestamp_millis,TIMESTAMP_MILLIS,false,0,1,1
timestamp_seconds,TIMESTAMP_SECONDS,false,0,1,1
timestamp_sub,TIMESTAMP_SUB,false,0,2,2
timestamp_trunc,TIMESTAMP_TRUNC,false,0,2,3
to_base32,TO_BASE32,false,0,1,1
to_base64,TO_BASE64,false,0,1,1
to_code_points,TO_CODE_POINTS,false,0,1,1
to_hex,TO_HEX,false,0,1,1
to_json_string,TO_JSON_STRING,false,0,1,2
to_proto,TO_PROTO,false,0,1,1
trim,TRIM,false,0,1,2
trunc,TRUNC,false,0,1,2
unix_date,UNIX_DATE,false,0,1,1
unix_micros,UNIX_MICROS,false,0,1,1
unix_millis,UNIX_MILLIS,false,0,1,1
unix_seconds,UNIX_SECONDS,false,0,1,1
upper,UPPER,false,0,1,1
var_pop,VAR_POP,true,0,1,1
var_samp,VAR_SAMP,true,0,1,1
""";
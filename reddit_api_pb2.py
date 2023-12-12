# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: reddit_api.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10reddit_api.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x17\n\x04User\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"\x83\x02\n\x04Post\x12\x0f\n\x07post_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0c\n\x04text\x18\x03 \x01(\t\x12\x11\n\tvideo_url\x18\x04 \x01(\t\x12\x11\n\timage_url\x18\x05 \x01(\t\x12\x11\n\tauthor_id\x18\x06 \x01(\t\x12\r\n\x05score\x18\x07 \x01(\x05\x12\x1e\n\x05state\x18\x08 \x01(\x0e\x32\x0f.Post.PostState\x12\x34\n\x10publication_date\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"/\n\tPostState\x12\n\n\x06NORMAL\x10\x00\x12\n\n\x06LOCKED\x10\x01\x12\n\n\x06HIDDEN\x10\x02\"\xd1\x01\n\x07\x43omment\x12\x12\n\ncomment_id\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x11\n\tauthor_id\x18\x03 \x01(\t\x12\r\n\x05score\x18\x04 \x01(\x05\x12$\n\x05state\x18\x05 \x01(\x0e\x32\x15.Comment.CommentState\x12\x34\n\x10publication_date\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"&\n\x0c\x43ommentState\x12\n\n\x06NORMAL\x10\x00\x12\n\n\x06HIDDEN\x10\x01\"2\n\x0fVotePostRequest\x12\x0f\n\x07post_id\x18\x01 \x01(\t\x12\x0e\n\x06upvote\x18\x02 \x01(\x08\"!\n\x0eGetPostRequest\x12\x0f\n\x07post_id\x18\x01 \x01(\t\"8\n\x12VoteCommentRequest\x12\x12\n\ncomment_id\x18\x01 \x01(\t\x12\x0e\n\x06upvote\x18\x02 \x01(\x08\"7\n\x15GetTopCommentsRequest\x12\x0f\n\x07post_id\x18\x01 \x01(\t\x12\r\n\x05limit\x18\x02 \x01(\x05\"?\n\x1a\x45xpandCommentBranchRequest\x12\x12\n\ncomment_id\x18\x01 \x01(\t\x12\r\n\x05limit\x18\x02 \x01(\x05\"\xa3\x01\n\x13TopCommentsResponse\x12\x1e\n\x0ctop_comments\x18\x01 \x03(\x0b\x32\x08.Comment\x12\x39\n\x0bhas_replies\x18\x02 \x03(\x0b\x32$.TopCommentsResponse.HasRepliesEntry\x1a\x31\n\x0fHasRepliesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\"i\n\x1b\x45xpandCommentBranchResponse\x12#\n\x11\x65xpanded_comments\x18\x01 \x03(\x0b\x32\x08.Comment\x12%\n\x07replies\x18\x02 \x03(\x0b\x32\x14.TopCommentsResponse2\xd4\x02\n\tRedditApi\x12\x1a\n\nCreatePost\x12\x05.Post\x1a\x05.Post\x12#\n\x08VotePost\x12\x10.VotePostRequest\x1a\x05.Post\x12!\n\x07GetPost\x12\x0f.GetPostRequest\x1a\x05.Post\x12#\n\rCreateComment\x12\x08.Comment\x1a\x08.Comment\x12,\n\x0bVoteComment\x12\x13.VoteCommentRequest\x1a\x08.Comment\x12>\n\x0eGetTopComments\x12\x16.GetTopCommentsRequest\x1a\x14.TopCommentsResponse\x12P\n\x13\x45xpandCommentBranch\x12\x1b.ExpandCommentBranchRequest\x1a\x1c.ExpandCommentBranchResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'reddit_api_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TOPCOMMENTSRESPONSE_HASREPLIESENTRY']._options = None
  _globals['_TOPCOMMENTSRESPONSE_HASREPLIESENTRY']._serialized_options = b'8\001'
  _globals['_USER']._serialized_start=53
  _globals['_USER']._serialized_end=76
  _globals['_POST']._serialized_start=79
  _globals['_POST']._serialized_end=338
  _globals['_POST_POSTSTATE']._serialized_start=291
  _globals['_POST_POSTSTATE']._serialized_end=338
  _globals['_COMMENT']._serialized_start=341
  _globals['_COMMENT']._serialized_end=550
  _globals['_COMMENT_COMMENTSTATE']._serialized_start=512
  _globals['_COMMENT_COMMENTSTATE']._serialized_end=550
  _globals['_VOTEPOSTREQUEST']._serialized_start=552
  _globals['_VOTEPOSTREQUEST']._serialized_end=602
  _globals['_GETPOSTREQUEST']._serialized_start=604
  _globals['_GETPOSTREQUEST']._serialized_end=637
  _globals['_VOTECOMMENTREQUEST']._serialized_start=639
  _globals['_VOTECOMMENTREQUEST']._serialized_end=695
  _globals['_GETTOPCOMMENTSREQUEST']._serialized_start=697
  _globals['_GETTOPCOMMENTSREQUEST']._serialized_end=752
  _globals['_EXPANDCOMMENTBRANCHREQUEST']._serialized_start=754
  _globals['_EXPANDCOMMENTBRANCHREQUEST']._serialized_end=817
  _globals['_TOPCOMMENTSRESPONSE']._serialized_start=820
  _globals['_TOPCOMMENTSRESPONSE']._serialized_end=983
  _globals['_TOPCOMMENTSRESPONSE_HASREPLIESENTRY']._serialized_start=934
  _globals['_TOPCOMMENTSRESPONSE_HASREPLIESENTRY']._serialized_end=983
  _globals['_EXPANDCOMMENTBRANCHRESPONSE']._serialized_start=985
  _globals['_EXPANDCOMMENTBRANCHRESPONSE']._serialized_end=1090
  _globals['_REDDITAPI']._serialized_start=1093
  _globals['_REDDITAPI']._serialized_end=1433
# @@protoc_insertion_point(module_scope)
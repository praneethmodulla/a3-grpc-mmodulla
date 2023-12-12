from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class Post(_message.Message):
    __slots__ = ("post_id", "title", "text", "video_url", "image_url", "author_id", "score", "state", "publication_date")
    class PostState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NORMAL: _ClassVar[Post.PostState]
        LOCKED: _ClassVar[Post.PostState]
        HIDDEN: _ClassVar[Post.PostState]
    NORMAL: Post.PostState
    LOCKED: Post.PostState
    HIDDEN: Post.PostState
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    VIDEO_URL_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_DATE_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    title: str
    text: str
    video_url: str
    image_url: str
    author_id: str
    score: int
    state: Post.PostState
    publication_date: _timestamp_pb2.Timestamp
    def __init__(self, post_id: _Optional[str] = ..., title: _Optional[str] = ..., text: _Optional[str] = ..., video_url: _Optional[str] = ..., image_url: _Optional[str] = ..., author_id: _Optional[str] = ..., score: _Optional[int] = ..., state: _Optional[_Union[Post.PostState, str]] = ..., publication_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Comment(_message.Message):
    __slots__ = ("comment_id", "text", "author_id", "score", "state", "publication_date")
    class CommentState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NORMAL: _ClassVar[Comment.CommentState]
        HIDDEN: _ClassVar[Comment.CommentState]
    NORMAL: Comment.CommentState
    HIDDEN: Comment.CommentState
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_DATE_FIELD_NUMBER: _ClassVar[int]
    comment_id: str
    text: str
    author_id: str
    score: int
    state: Comment.CommentState
    publication_date: _timestamp_pb2.Timestamp
    def __init__(self, comment_id: _Optional[str] = ..., text: _Optional[str] = ..., author_id: _Optional[str] = ..., score: _Optional[int] = ..., state: _Optional[_Union[Comment.CommentState, str]] = ..., publication_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class VotePostRequest(_message.Message):
    __slots__ = ("post_id", "upvote")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    UPVOTE_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    upvote: bool
    def __init__(self, post_id: _Optional[str] = ..., upvote: bool = ...) -> None: ...

class GetPostRequest(_message.Message):
    __slots__ = ("post_id",)
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    def __init__(self, post_id: _Optional[str] = ...) -> None: ...

class VoteCommentRequest(_message.Message):
    __slots__ = ("comment_id", "upvote")
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    UPVOTE_FIELD_NUMBER: _ClassVar[int]
    comment_id: str
    upvote: bool
    def __init__(self, comment_id: _Optional[str] = ..., upvote: bool = ...) -> None: ...

class GetTopCommentsRequest(_message.Message):
    __slots__ = ("post_id", "limit")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    limit: int
    def __init__(self, post_id: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class ExpandCommentBranchRequest(_message.Message):
    __slots__ = ("comment_id", "limit")
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    comment_id: str
    limit: int
    def __init__(self, comment_id: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class TopCommentsResponse(_message.Message):
    __slots__ = ("top_comments", "has_replies")
    class HasRepliesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
    TOP_COMMENTS_FIELD_NUMBER: _ClassVar[int]
    HAS_REPLIES_FIELD_NUMBER: _ClassVar[int]
    top_comments: _containers.RepeatedCompositeFieldContainer[Comment]
    has_replies: _containers.ScalarMap[str, bool]
    def __init__(self, top_comments: _Optional[_Iterable[_Union[Comment, _Mapping]]] = ..., has_replies: _Optional[_Mapping[str, bool]] = ...) -> None: ...

class ExpandCommentBranchResponse(_message.Message):
    __slots__ = ("expanded_comments", "replies")
    EXPANDED_COMMENTS_FIELD_NUMBER: _ClassVar[int]
    REPLIES_FIELD_NUMBER: _ClassVar[int]
    expanded_comments: _containers.RepeatedCompositeFieldContainer[Comment]
    replies: _containers.RepeatedCompositeFieldContainer[TopCommentsResponse]
    def __init__(self, expanded_comments: _Optional[_Iterable[_Union[Comment, _Mapping]]] = ..., replies: _Optional[_Iterable[_Union[TopCommentsResponse, _Mapping]]] = ...) -> None: ...

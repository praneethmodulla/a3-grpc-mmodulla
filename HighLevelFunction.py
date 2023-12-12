from reddit_api_client import RedditApiClientWrapper
from typing import Optional
from reddit_api_pb2 import Comment

def get_most_upvoted_reply(api_client: RedditApiClientWrapper, post_id: str) -> Optional[Comment]:
    # Retrieve the post
    post = api_client.get_post(post_id)

    if not post:
        return None

    # Retrieve the most upvoted comments under the post
    top_comments_response = api_client.get_top_comments(post_id, limit=1)

    if not top_comments_response.top_comments:
        return None

    most_upvoted_comment = top_comments_response.top_comments[0]

    # Expand the most upvoted comment
    expanded_comment_response = api_client.expand_comment_branch(most_upvoted_comment.comment_id, limit=1)

    if not expanded_comment_response.expanded_comments or not expanded_comment_response.replies:
        return None

    # Check if there are top comments under the first reply
    if expanded_comment_response.replies[0].top_comments:
        return expanded_comment_response.replies[0].top_comments[0]
    else:
        return None
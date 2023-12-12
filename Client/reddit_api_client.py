import grpc
from reddit_api_pb2_grpc import RedditApiStub
from reddit_api_pb2 import Post, Comment, VotePostRequest, GetPostRequest, VoteCommentRequest, GetTopCommentsRequest, ExpandCommentBranchRequest

class RedditApiClientWrapper:
    def __init__(self, host='localhost', port=50051):
        channel = grpc.insecure_channel(f'{host}:{port}')
        self.stub = RedditApiStub(channel)

    def create_post(self, post):
        return self.stub.CreatePost(post)

    def vote_post(self, post_id, upvote=True):
        request = VotePostRequest(post_id=post_id, upvote=upvote)
        return self.stub.VotePost(request)

    def get_post(self, post_id):
        request = GetPostRequest(post_id=post_id)
        return self.stub.GetPost(request)

    def create_comment(self, comment):
        return self.stub.CreateComment(comment)

    def vote_comment(self, comment_id, upvote=True):
        request = VoteCommentRequest(comment_id=comment_id, upvote=upvote)
        return self.stub.VoteComment(request)

    def get_top_comments(self, post_id, limit):
        request = GetTopCommentsRequest(post_id=post_id, limit=limit)
        return self.stub.GetTopComments(request)

    def expand_comment_branch(self, comment_id, limit):
        request = ExpandCommentBranchRequest(comment_id=comment_id, limit=limit)
        return self.stub.ExpandCommentBranch(request)

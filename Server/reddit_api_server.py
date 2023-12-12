from concurrent import futures
import grpc
from reddit_api_pb2_grpc import RedditApiServicer, add_RedditApiServicer_to_server
from reddit_api_pb2 import Post, Comment, VotePostRequest, GetPostRequest, VoteCommentRequest, GetTopCommentsRequest, ExpandCommentBranchRequest, TopCommentsResponse, ExpandCommentBranchResponse

class RedditApiServicer(RedditApiServicer):
    # Placeholder for in-memory storage
    posts = {}
    comments = {}

    def CreatePost(self, request, context):
        # Dummy implementation - store the post in memory
        post_id = str(len(self.posts) + 1)
        request.post_id = post_id
        self.posts[post_id] = request
        return request

    def VotePost(self, request, context):
        # Dummy implementation - update the post score
        post = self.posts.get(request.post_id)
        if post:
            post.score += 1 if request.upvote else -1
        return post

    def GetPost(self, request, context):
        # Dummy implementation - retrieve the post from memory
        return self.posts.get(request.post_id)

    def CreateComment(self, request, context):
        # Dummy implementation - store the comment in memory
        comment_id = str(len(self.comments) + 1)
        request.comment_id = comment_id
        self.comments[comment_id] = request
        return request

    def VoteComment(self, request, context):
        # Dummy implementation - update the comment score
        comment = self.comments.get(request.comment_id)
        if comment:
            comment.score += 1 if request.upvote else -1
        return comment

    def GetTopComments(self, request, context):
        # Dummy implementation - retrieve top comments from memory
        top_comments = sorted(self.comments.values(), key=lambda c: c.score, reverse=True)[:request.limit]
        response = TopCommentsResponse(top_comments=top_comments)
        return response

    def ExpandCommentBranch(self, request, context):
        # Dummy implementation - expand comment branch from memory
        expanded_comments = []
        replies = []
        comment = self.comments.get(request.comment_id)

        if comment:
            # Expand the comment
            expanded_comments.append(comment)
            # Dummy implementation - retrieve replies from memory
            reply_comments = sorted(self.comments.values(), key=lambda c: c.score, reverse=True)[:request.limit]
            reply_response = TopCommentsResponse(top_comments=reply_comments)
            replies.append(reply_response)

        response = ExpandCommentBranchResponse(expanded_comments=expanded_comments, replies=replies)
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_RedditApiServicer_to_server(RedditApiServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Server started, listening on port 50051')
    server.wait_for_termi
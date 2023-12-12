import unittest
from unittest.mock import Mock
from HighLevelFunction import get_most_upvoted_reply
from reddit_api_pb2 import Post, Comment, TopCommentsResponse, ExpandCommentBranchResponse

class TestGetMostUpvotedReply(unittest.TestCase):
    def test_get_most_upvoted_reply(self):
        # Mock the API client
        api_client = Mock()

        # Mock the expected responses
        mock_post = Post(post_id="123", title="Test Post", text="This is a test post.")
        api_client.get_post.return_value = mock_post
        print("Mock Post:", api_client.get_post.return_value)

        mock_top_comments_response = TopCommentsResponse(
            top_comments=[Comment(comment_id="456", text="Test Comment", score=10)]
        )
        api_client.get_top_comments.return_value = mock_top_comments_response
        print("Mock Top Comments Response:", api_client.get_top_comments.return_value)

        mock_expanded_comment_response = ExpandCommentBranchResponse(
            expanded_comments=[Comment(comment_id="789", text="Test Reply", score=5)],
            replies=[TopCommentsResponse(top_comments=[Comment(comment_id="101", text="Reply Comment", score=8)])]
        )
        api_client.expand_comment_branch.return_value = mock_expanded_comment_response
        print("Mock Expanded Comment Response:", api_client.expand_comment_branch.return_value)

        # Call the high-level function
        result = get_most_upvoted_reply(api_client, post_id="123")
        
        
        
        print("Actual Result:", result)


        # Assert the expected result
        self.assertIsNotNone(result)
        self.assertEqual(result.comment_id, "101")  # Make sure the correct reply is returned

if __name__ == '__main__':
    unittest.main()

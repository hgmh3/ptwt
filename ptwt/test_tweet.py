"""
This test case ensures that all Tweets are
created validate and loaded properly
"""
from django.test import TestCase
from ptwt.models import Tweet

class TweetTestCase(TestCase):
    def setUp(self):
        """
        Initializes the test database with two tweet objects
        """
        Tweet.objects.create(name="test", message="The content")
        Tweet.objects.create(name="test2", message="The content 2")

    def test_tweet_loads(self):
        """
        Loads the two tweet objects from the database
        """
        tweets = Tweet.objects.all()
        self.assertEqual(len(tweets), 2)
        self.assertTrue(tweets[0].validate_message())

    def test_tweet_message(self):
        """
        Tests a tweet containing a message more than 50 characters long
        """
        tweet = Tweet.objects.create(name="test3", message="A message less than 50 characters long")
        self.assertNotEqual(tweet.id, None)

    def test_tweet_validate_message(self):
        """
        Test the submission of a tweet containing a message that has more than 50 characters
        """
        tweet = Tweet(name="test4", message="A message that should be more than 50 characters long")
        self.assertFalse(tweet.validate_message())
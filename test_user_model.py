"""User model tests."""

# run these tests like:
#
#    python -m unittest test_user_model.py


import os
from unittest import TestCase

from models import db, User, Message, Follows

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"


# Now we can import app

from app import app

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.create_all()


class UserModelTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test client, add sample data."""

        User.query.delete()
        Message.query.delete()
        Follows.query.delete()

        self.client = app.test_client()

    def test_user_model(self):
        """Does basic model work?"""

        u = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )

        db.session.add(u)
        db.session.commit()

        # User should have no messages & no followers
        self.assertEqual(len(u.messages), 0)
        self.assertEqual(len(u.followers), 0)

    def test_repr(self):
        """Does the repr() function work correctly?"""

        u = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )
        self.assertEqual(str(u), f"<User #{u.id}: {u.username}, {u.email}>")
    def test_following_functions(self):
        """Do the following checker functions work?"""

        #create the three users to check
        uFollowed = User(
            email="test1@test.com",
            username="testuserFollowed",
            password="HASHED_PASSWORD"
        )

        db.session.add(uFollowed)
        db.session.commit()

        u = User(
            email="test2@test.com",
            username="testuser2",
            password="HASHED_PASSWORD"
        )

        db.session.add(u)
        db.session.commit()

        uFollowing = User(
            email="test3@test.com",
            username="testuserFollowing",
            password="HASHED_PASSWORD"
        )

        db.session.add(uFollowing)
        db.session.commit()

        u.following.append(uFollowed)
        uFollowing.following.append(u)
        db.session.commit()
        u= User.query.get(u.id)

        self.assertTrue(u.is_following(uFollowed))
        self.assertTrue(u.is_followed_by(uFollowing))
        self.assertFalse(u.is_followed_by(uFollowed))
        self.assertFalse(u.is_following(uFollowing))

    def test_authenticate(self):
        """Does the authenticate function work?"""

        u = User.signup(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD",
            image_url= None
        )

        db.session.add(u)
        db.session.commit()
        self.assertTrue(u == User.authenticate("testuser", "HASHED_PASSWORD"))
        self.assertFalse(User.authenticate("testuser","wrongPassword"))
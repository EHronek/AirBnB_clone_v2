#!/usr/bin/python3
import unittest
import MySQLdb
from console import HBNBCommand
import os
from models import storage
from models.state import State


class TestDBStorage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up database connection"""
        cls.conn = MySQLdb.connect(
            host=os.getenv("HBNB_MYSQL_HOST", "localhost"),
            user=os.getenv("HBNB_MYSQL_USER", "root"),
            passwd=os.getenv("HBNB_MYSQL_PWD", "Root@6064"),
            db=os.getenv("HBNB_MYSQL_DB","hbnb_test_db")
        )
        cls.cursor = cls.conn.cursor()

    def test_create_state(self):
        """Test creating a new state"""
        self.cursor.execute("SELECT COUNT(*) FROM states;")
        initial_count = self.cursor.fetchone()[0]

        #Perform the action
        console = HBNBCommand()
        console.onecmd("create State name='California'")

        #Get final count
        self.cursor.execute("SELECT COUNT(*) FROM states;")
        final_count = self.cursor.fetchone()[0]

        #validate the outcome
        self.assertEqual(final_count, initial_count + 1)

    def test_create_state2(self):
        """Testing creating a new state"""
        storage.reload()
        initial_count = len(storage.all())

        state = State(name="california")
        state.save()

        storage.reload()
        final_count = len(storage.all())
        self.assertEqual(final_count, initial_count + 1)



    @classmethod
    def tearDownClass(cls):
        """Close database connection"""
        cls.conn.close()

import pytest
from helpers.get_guilds import get_guilds

# Mock the MongoDB database and collection objects using pytest fixture
@pytest.fixture
def mock_db():
    class MockCollection:
        def find(self, query, projection):
            return [
                {"_id": 1, "name": "Guild 1", "guildId": "123"},
                {"_id": 2, "name": "Guild 2", "guildId": "456"},
                {"_id": 3, "name": "Guild 3", "guildId": "789"},
            ]

    class MockDB:
        def __getitem__(self, item):
            return MockCollection()

    return MockDB()

# Test the get_guilds function
def test_get_guilds(mock_db):
    # Call the function to be tested
    guilds = get_guilds(db=mock_db)

    # Check if the function returns the expected result
    expected_guilds = [
        {"_id": 1, "name": "Guild 1", "guildId": "123"},
        {"_id": 2, "name": "Guild 2", "guildId": "456"},
        {"_id": 3, "name": "Guild 3", "guildId": "789"},
    ]
    assert guilds == expected_guilds

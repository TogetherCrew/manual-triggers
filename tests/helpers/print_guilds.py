from helpers.print_guilds import print_guilds

def test_print_guilds(capsys):
    # Define some sample guilds for testing
    guilds = [
        {"guildId": "123", "name": "Guild 1"},
        {"guildId": "456", "name": "Guild 2"},
        {"guildId": "789", "name": "Guild 3"},
    ]

    # Call the function to be tested
    print_guilds(guilds)

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the printed output matches the expected result
    expected_output = "123 - Guild 1\n456 - Guild 2\n789 - Guild 3\n"
    assert captured.out == expected_output

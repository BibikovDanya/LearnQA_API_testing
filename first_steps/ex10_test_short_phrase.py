def test_short_phrase():
    phrase = input("Enter a phrase shorter than 15 characters: ")
    assert len(phrase) < 15, f"The number of characters in the phrase '{phrase}'  is more 15"

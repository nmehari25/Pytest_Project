import pytest
from lib.music_tracker import MusicTracker
"""
Given an empty list
and nothing #add
expect an empty list returned
"""
def test_an_empty_list():
    _tracker = MusicTracker()
    with pytest.raises(Exception) as e:
        _tracker.add("")
    assert str(e.value) == "No track entered."

"""
Given a track 
#add a track to the list
expect a list with one track
"""
def test_add_single_track():
    _tracker = MusicTracker()
    _tracker.add("My kind of blue")
    assert _tracker.list() == ["My kind of blue"]

"""
Given multiple tracks 
#add a 4 tracks to the list
expect a list with 4 tracks
"""
def test_add_four_tracks():
    _tracker = MusicTracker()
    _tracker.add("My kind of blue")
    _tracker.add("High Times")
    _tracker.add("Overdrive")
    _tracker.add("Everything In Its Right Place")
    assert _tracker.list() == ["My kind of blue", "High Times", "Overdrive", "Everything In Its Right Place"]


"""
Given multiple tracks 
#add a 5 tracks to the list
with one track entered as a non-string type
expect an error message
"""
def test_add_four_tracks_with_one_not_string_type():
    _tracker = MusicTracker()
    _tracker.add("My kind of blue")
    with pytest.raises(Exception) as e:
        _tracker.add(45)
    assert str(e.value) == "Track is not in string format."
    _tracker.add("Overdrive")
    _tracker.add("Everything In Its Right Place")
    assert _tracker.list() == ["My kind of blue", "Overdrive", "Everything In Its Right Place"]

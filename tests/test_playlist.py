# -*- coding: utf-8 -*-
import pytest
from pytube import playlist


def test_construct():
    ob = playlist.Playlist(
        "https://www.youtube.com/watch?v=m5q2GCsteQs&list="
        "PL525f8ds9RvsXDl44X6Wwh9t3fCzFNApw")
    expected = "https://www.youtube.com/" \
               "playlist?list=" \
               "PL525f8ds9RvsXDl44X6Wwh9t3fCzFNApw"

    assert ob.construct_playlist_url() == expected


def test_link_parse():
    ob = playlist.Playlist(
        "https://www.youtube.com/watch?v=m5q2GCsteQs&list="
        "PL525f8ds9RvsXDl44X6Wwh9t3fCzFNApw")

    expected = ["/watch?v=m5q2GCsteQs",
                "/watch?v=5YK63cXyJ2Q",
                "/watch?v=Rzt4rUPFYD4"]
    assert ob.parse_links() == expected


def test_populate():
    ob = playlist.Playlist(
        "https://www.youtube.com/watch?v=m5q2GCsteQs&list="
        "PL525f8ds9RvsXDl44X6Wwh9t3fCzFNApw")
    expected = ["https://www.youtube.com/watch?v=m5q2GCsteQs",
                "https://www.youtube.com/watch?v=5YK63cXyJ2Q",
                "https://www.youtube.com/watch?v=Rzt4rUPFYD4"]

    ob.populate_video_urls()
    assert ob.video_urls == expected

# retroarch-playlist-thumbnail-script
This Python script is designed for RetroArch users who face difficulties in downloading thumbnails for their playlists. It's particularly useful when direct downloads from RetroArch aren't working, or when users prefer a more manual approach. The script processes RetroArch playlists (.lpl files) and selectively copies thumbnails for each game in the playlist.

Thumbnails for all RetroArch games are available at libretro-thumbnails on GitHub. Users can download these thumbnails en masse as ZIP files or clone the repository. However, this leads to having a large number of unnecessary thumbnails. This script solves this issue by filtering and copying only the thumbnails relevant to the games in a user's playlist.

The script matches game entries in the playlist with thumbnails, using both exact and fuzzy matching. It organizes the output into folders corresponding to each playlist's db_name, ensuring users get a structured and minimal set of thumbnails directly relevant to their games.

Usage: After downloading/cloning the thumbnail repository, users run this script, pointing it to their playlist directory and the downloaded thumbnail directory. The script will then create a new directory structure with thumbnails only for the games present in the playlists.

This tool streamlines the process, saving space and time, and enhances the RetroArch gaming experience with relevant visuals.

# RetroArch Thumbnail Filter
##Overview
This Python script assists RetroArch users in managing their game thumbnails, especially useful when facing difficulties in downloading thumbnails directly through RetroArch. It's a handy tool for those preferring a manual approach or when automatic downloads are not functioning properly.

RetroArch uses .lpl files as playlists, which are plain text files in JSON format since version 1.7.5​​. Each playlist item includes details like the game's label, path, and importantly, the db_name, which indicates the corresponding ROM database used for metadata, thumbnails, and game-system-specific icons​​.

##Problem Statement
Sometimes downloading thumbnails using RetroArch just doesn't seem to work for whatever reason. Downloading thumbnail packs for RetroArch can result in acquiring a vast number of unnecessary thumbnails. This script addresses this issue by selectively copying only the thumbnails that are relevant to the games in a user's playlist.

##Thumbnail Structure in RetroArch
RetroArch organizes thumbnails in subfolders named after the playlist, minus the .lpl extension. For example, a playlist named Atari - 2600.lpl would correspond to a thumbnail folder named thumbnails/Atari - 2600/. Inside, subfolders like Named_Boxarts, Named_Snaps, and Named_Titles contain boxarts, in-game snapshots, and title screens, respectively​​.

##Script Functionality
The script processes each game entry in the given RetroArch playlists and matches them with available thumbnails using both exact and fuzzy matching. It places the selected thumbnails into structured output folders corresponding to each playlist's db_name.

##Usage
After downloading or cloning the thumbnail repository from libretro-thumbnails, users run the script, pointing it to their playlist directory and the downloaded thumbnail directory. The script then creates a new directory structure containing only the necessary thumbnails for the games in the playlists.

##Benefits
This script streamlines the thumbnail organization process, saving space and enhancing the RetroArch gaming experience with relevant and specific visuals. Users can also customize which type of thumbnail to display (boxart, in-game snapshot, or title screen) using the RetroArch GUI​​.

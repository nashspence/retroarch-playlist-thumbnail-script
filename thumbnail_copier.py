#!/usr/bin/env python3

import json
import os
import shutil
import sys
from fuzzywuzzy import process

def sanitize_label(label):
    for ch in ['&', '*', '/', ':', '<', '>', '?', '\\', '|']:
        label = label.replace(ch, '_')
    return label

def find_best_match(game_label, thumbnails):
    highest_match = process.extractOne(game_label, thumbnails, score_cutoff=88)
    return highest_match

def process_playlist(playlist_path, thumbnails_base_path, output_base_path):
    print(f"Processing playlist: {playlist_path}")
    with open(playlist_path, 'r') as file:
        playlist = json.load(file)

    for item in playlist['items']:
        game_label = sanitize_label(item['label'])
        db_name = item['db_name'].replace('.lpl', '')
        thumbnails_directory_path = os.path.join(thumbnails_base_path, db_name)
        if not os.path.exists(thumbnails_directory_path):
            print(f"Thumbnail directory not found for db_name: {db_name}")
            continue

        output_directory = os.path.join(output_base_path, db_name)
        os.makedirs(output_directory, exist_ok=True)

        for subdir in ['Named_Boxarts', 'Named_Snaps', 'Named_Titles']:
            found_exact_match = False
            subdir_path = os.path.join(thumbnails_directory_path, subdir)
            if not os.path.exists(subdir_path):
                print(f"Subdirectory {subdir} not found in {thumbnails_directory_path}")
                continue

            exact_match_path = os.path.join(subdir_path, game_label + '.png')
            if os.path.exists(exact_match_path):
                destination_dir = os.path.join(output_directory, subdir)
                os.makedirs(destination_dir, exist_ok=True)
                shutil.copy(exact_match_path, destination_dir)
                found_exact_match = True
                print(f"Exact thumbnail copied for: {game_label} in db_name {db_name} - {subdir}")

            if not found_exact_match:
                thumbnails = [f for f in os.listdir(subdir_path) if os.path.isfile(os.path.join(subdir_path, f))]
                best_match = find_best_match(game_label, thumbnails)
                if best_match:
                    source_file = os.path.join(subdir_path, best_match[0])
                    destination_dir = os.path.join(output_directory, subdir)
                    os.makedirs(destination_dir, exist_ok=True)
                    shutil.copy(source_file, os.path.join(destination_dir, game_label + '.png'))
                    print(f"Thumbnail copied for: {game_label} (Fuzzy Match: {best_match[0]}) in db_name {db_name} - {subdir}")
                else:
                    print(f"No matching thumbnails found for: {game_label} in db_name {db_name} - {subdir}")

def main(playlists_directory, thumbnails_base_path):
    output_base_path = 'selected_thumbnails'
    os.makedirs(output_base_path, exist_ok=True)

    if not os.path.exists(playlists_directory):
        print(f"Playlists directory not found: {playlists_directory}")
        return

    for playlist_file in os.listdir(playlists_directory):
        if playlist_file.startswith('._'):
            continue  # Ignore macOS attribute files

        playlist_path = os.path.join(playlists_directory, playlist_file)
        if os.path.isfile(playlist_path) and playlist_file.endswith('.lpl'):
            process_playlist(playlist_path, thumbnails_base_path, output_base_path)
        else:
            print(f"Skipping non-LPL file: {playlist_file}")

    print("All playlist processing complete.")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python thumbnail_copier.py <playlists_directory_path> <thumbnails_base_directory_path>")
        sys.exit(1)
    
    playlists_directory_path = sys.argv[1]
    thumbnails_base_directory_path = sys.argv[2]
    main(playlists_directory_path, thumbnails_base_directory_path)

import argparse
import os
import shutil
import subprocess
import time
import datetime
from pathlib import Path
import socket
import json

GAME_NAME = "ArkhamSCE"

# The Tabletop Simulator External Editor API listens on port 39999
HOST = "127.0.0.1"  # localhost
PORT = 39999

# Convert the Python dictionary to a JSON string and then encode it to bytes
RELOAD_MSG = json.dumps({"messageID": 1, "scriptStates": []}).encode("utf-8")

def get_current_git_branch():
    try:
        branch = (
            subprocess.check_output(
                ["git", "rev-parse", "--abbrev-ref", "HEAD"], stderr=subprocess.DEVNULL
            )
            .strip()
            .decode("utf-8")
        )
        return branch
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def get_output_folder():
    if os.name == "nt":  # Windows
        return os.path.join(
            os.environ["USERPROFILE"],
            "Documents",
            "My Games",
            "Tabletop Simulator",
            "Saves",
        )
    else:  # macOS, Linux, etc.
        return os.path.join(
            os.path.expanduser("~"), "Library", "Tabletop Simulator", "Saves"
        )


def get_base_command():
    if os.name == "nt":  # Windows
        binary_name = "TTSModManager.exe"

    else:  # macOS, Linux, etc.
        binary_name = "TTSModManager"

    binary_path = os.path.join(os.getcwd(), binary_name)

    # Check for the existence of the binary
    if os.path.exists(binary_path) and os.path.isfile(binary_path):
        using_go = False
        cmd = [binary_path]
    else:
        using_go = True
        cmd = ["go", "run", "main.go"]

    return cmd, using_go


def main():
    # Start the timer and get the current time
    start_time = time.time()
    start_time_formatted = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    parser = argparse.ArgumentParser(description=f"VS Code build script for {GAME_NAME}")
    parser.add_argument(
        "--action",
        required=True,
        choices=["build", "decompose"],
        help="Action to perform: build or decompose.",
    )
    parser.add_argument("--moddir", required=True, help="The mod directory.")
    args = parser.parse_args()

    # Determine folder and command
    output_folder = get_output_folder()
    cmd, using_go = get_base_command()

    # Set up command-line arguments
    mod_dir_arg = ["-moddir", args.moddir]
    mod_file_arg = ["-modfile", os.path.join(output_folder, GAME_NAME + ".json")]
    reverse_arg = ["-reverse"] if args.action == "decompose" else []

    # Final command to execute
    full_cmd = cmd + mod_dir_arg + mod_file_arg + reverse_arg

    # Execute the core command
    branch = get_current_git_branch()

    print(f"{start_time_formatted}")
    print(f"branch: {branch}")
    print(f"action: {args.action}")
    print(f"{' '.join(full_cmd)}")

    if using_go:
        git_directory_path = Path(__file__).resolve().parent.resolve().parent.resolve().parent
        full_ttsmodmanager_path = git_directory_path / "TTSModManager"
        subprocess.run(full_cmd, check=True, cwd=full_ttsmodmanager_path)
    else:
        subprocess.run(full_cmd, check=True)

    # Handle dynamic file copying if the action is 'build'
    if args.action == "build":
        source_file = GAME_NAME + ".png"
        if branch and branch != "main":
            source_file = GAME_NAME + "_dev.png"

        shutil.copy(source_file, os.path.join(output_folder, GAME_NAME + ".png"))

    # Calculate and print the elapsed time
    elapsed_time = time.time() - start_time
    print(f"Execution took {elapsed_time:.2f} seconds.")

    # Attempt to reload the game in TTS
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(RELOAD_MSG)
            print("Running TTS detected - reloading the game.")

    except ConnectionRefusedError:
        print(f"Connection refused. Ensure TTS is running and a savegame is loaded.")


if __name__ == "__main__":
    main()

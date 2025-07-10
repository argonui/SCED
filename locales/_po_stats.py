# This script calculates the translation progress of .po files
# and displays it in a condensed, single-line format.
import os
import polib

# This script assumes it is located inside the 'locales' folder.
# All other .po files will be compared against this one.
MASTER_PO_FILE = "en.po"


def create_progress_bar(percentage, width=25):
    """Creates a simple text-based progress bar."""
    filled_length = int(width * percentage // 100)
    bar = "█" * filled_length + "─" * (width - filled_length)
    return f"[{bar}]"


def calculate_translation_stats_condensed():
    """
    Analyzes all .po files and displays translation progress in a
    condensed format.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    master_path = os.path.join(script_dir, MASTER_PO_FILE)

    if not os.path.exists(master_path):
        print(f"❌ Master file '{MASTER_PO_FILE}' not found.")
        return

    try:
        master_po = polib.pofile(master_path)
        master_strings = {entry.msgid: entry.msgstr for entry in master_po}
    except Exception as e:
        print(f"❌ Could not read master file. Error: {e}")
        return

    # Find the longest filename for clean padding
    po_files = [
        f for f in os.listdir(script_dir) if f.endswith(".po") and f != MASTER_PO_FILE
    ]
    if not po_files:
        print("No language files found to analyze.")
        return

    max_len = max(len(f) for f in po_files)

    print(
        f"Master file '{MASTER_PO_FILE}' loaded with {len(master_strings)} strings.\n"
    )

    # --- Iterate over all other .po files ---
    for filename in sorted(po_files):
        target_path = os.path.join(script_dir, filename)
        try:
            target_po = polib.pofile(target_path)
            translated_count = 0

            for entry in target_po:
                master_str = master_strings.get(entry.msgid)
                # Count as translated ONLY if it's not empty and differs from English.
                if entry.msgstr and entry.msgstr != master_str:
                    translated_count += 1

            total_strings = len(target_po)
            if total_strings == 0:
                continue

            percentage = (translated_count / total_strings) * 100
            progress_bar = create_progress_bar(percentage)

            # Print condensed, right-aligned report line
            print(
                f"{filename:<{max_len}} {progress_bar} "
                f"{percentage:6.2f}% ({translated_count}/{total_strings})"
            )

        except Exception as e:
            print(f"Error processing file {filename}: {e}")


if __name__ == "__main__":
    calculate_translation_stats_condensed()

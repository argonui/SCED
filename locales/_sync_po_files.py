import os
import polib

# This script assumes it is located inside the 'locales' folder.
# The name of the master file that contains all the latest strings.
# All other .po files will be updated based on this one.
MASTER_PO_FILE = "en.po"


def sync_translation_files():
    """
    Synchronizes all .po files in the directory with the master .po file.
    It adds missing entries from the master file to the other files,
    copying over all comments and metadata, and using the master's text
    as a placeholder for the translation.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    master_path = os.path.join(script_dir, MASTER_PO_FILE)

    if not os.path.exists(master_path):
        print(f"Error: Master file '{MASTER_PO_FILE}' not found in '{script_dir}'.")
        return

    print(f"Loading master file: {MASTER_PO_FILE}")
    try:
        master_po = polib.pofile(master_path)
    except Exception as e:
        print(f"Could not read master file. Error: {e}")
        return

    # Create a dictionary of all full entry objects from the master file.
    master_entries = {entry.msgid: entry for entry in master_po}
    print(f"Found {len(master_entries)} strings in master file.")

    # --- Iterate over all other .po files in the directory ---
    for filename in os.listdir(script_dir):
        if filename.endswith(".po") and filename != MASTER_PO_FILE:
            target_path = os.path.join(script_dir, filename)
            print(f"\n--- Checking '{filename}' ---")

            try:
                # Load the target file, also disabling line wrapping.
                target_po = polib.pofile(target_path)

                # Create a set of msgids that already exist in the target file.
                target_msgids = {entry.msgid for entry in target_po}

                new_entries_added = 0

                # --- Compare master to target ---
                for msgid, master_entry in master_entries.items():
                    # If a msgid from the master file is NOT in the target file, add it.
                    if msgid not in target_msgids:
                        print(f"+ Adding missing string: '{msgid}'")

                        # Create a new entry, copying all metadata from the master.
                        # This correctly preserves all comments, flags, etc.
                        new_entry = polib.POEntry(
                            msgid=master_entry.msgid,
                            msgstr=master_entry.msgstr,  # Use English text as placeholder
                            comment=master_entry.comment,
                            tcomment=master_entry.tcomment,
                            occurrences=master_entry.occurrences,
                            flags=master_entry.flags,
                        )
                        target_po.append(new_entry)
                        new_entries_added += 1

                if new_entries_added > 0:
                    print(f"-> {new_entries_added} new string(s) added. Saving file...")
                    target_po.save(target_path)
                else:
                    print("-> File is already up to date.")

            except Exception as e:
                print(f"Error processing file {filename}: {e}")

    print("\nSynchronization complete!")


if __name__ == "__main__":
    # To run this script, you first need to install the 'polib' library:
    # pip install polib
    #
    # Then, place this script inside your 'locales' folder and run it.
    sync_translation_files()

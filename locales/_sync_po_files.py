# This scripts copies missing string and comments from the MASTER_PO_FILE
# to the other .po files in the same folder.
import os
import polib

# This script assumes it is located inside the 'locales' folder.
# All other .po files will be updated based on this one.
MASTER_PO_FILE = "en.po"


def sync_and_reorder_files():
    """
    Synchronizes all .po files with a master file, reordering them to match
    the master's structure and cleaning up multi-line strings.
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

    print(f"Found {len(master_po)} strings in master file.")

    # --- Iterate over all other .po files in the directory ---
    for filename in os.listdir(script_dir):
        if not filename.endswith(".po") or filename == MASTER_PO_FILE:
            continue

        target_path = os.path.join(script_dir, filename)
        print(f"\n--- Processing '{filename}' ---")

        try:
            target_po = polib.pofile(target_path)
            made_changes = False

            # Create a dictionary of existing translations for quick lookup.
            target_entries_dict = {entry.msgid: entry for entry in target_po}

            # This list will hold the newly ordered entries.
            new_ordered_entries = []
            new_strings_count = 0

            # Reorder and Sync based on master file
            for master_entry in master_po:
                # If the string from master exists in the target file, use the existing translation.
                if master_entry.msgid in target_entries_dict:
                    new_ordered_entries.append(target_entries_dict[master_entry.msgid])
                # Otherwise, add the new string from the master file.
                else:
                    new_entry = polib.POEntry(
                        msgid=master_entry.msgid,
                        msgstr=master_entry.msgstr,
                        comment=master_entry.comment,
                        tcomment=master_entry.tcomment,
                        occurrences=master_entry.occurrences,
                        flags=master_entry.flags,
                    )
                    new_ordered_entries.append(new_entry)
                    new_strings_count += 1

            # Check if the order has changed or if new strings were added.
            if len(target_po) != len(new_ordered_entries) or [
                e.msgid for e in target_po
            ] != [e.msgid for e in new_ordered_entries]:
                target_po.clear()
                target_po.extend(new_ordered_entries)
                made_changes = True
                if new_strings_count > 0:
                    print(f"  + Synced and ordered {new_strings_count} new string(s).")
                else:
                    print("  * Reordered strings to match master file.")

            # Save if anything changed
            if made_changes:
                print("  -> Saving changes...")
                target_po.save(target_path)
            else:
                print("  -> File is up to date.")

        except Exception as e:
            print(f"Error processing file {filename}: {e}")

    print("\nSynchronization and reordering complete!")


if __name__ == "__main__":
    sync_and_reorder_files()

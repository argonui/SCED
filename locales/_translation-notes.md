# Translation Workflow Guide

This document outlines the process for adding new translations and maintaining existing ones for this project. Following these steps ensures that all language files are consistent and that the final file for the mod is generated correctly.

## File Overview

Inside the `locales` folder, you will find several key files:

-   **`en.po`**: This is the master file for all translations. It is the "source of truth" and should always contain the complete, up-to-date list of all text strings in English.
-   **`de.po`, `fr.po`, `it.po`, etc.**: These are the language files for German, French, Italian, and so on. Each file contains the translated text for that specific language.
-   **`_sync_po_files.py`**: A Python script for the project owner to automatically update all language files when new text is added to `en.po`.
-   **`_po_to_lua_converter.py`**: A Python script that compiles all the `.po` files into a single `i18nData.ttslua` file that is used by the mod.

---

## Message ID (`msgid`) Naming Conventions

To keep the translation system organized and easy to debug, we use a consistent naming convention for all `msgid` entries. The structure is: `PREFIX_ElementName_suffix`

-   **`PREFIX_`**: A short code indicating which part of the mod the text belongs to. This helps group related strings together.
    -   `OP_` = Option Panel
    -   `DW_` = Download Window
    -   `CARD_` = Card-specific text (Example: Luger P08)
    -   *(etc.)*

-   **`ElementName`**: A descriptive, camelCase name for the UI element itself.
    -   Example: `uiLanguage`, `showTitleSplash`

-   **`_suffix`**: (Optional) A suffix used when an element has multiple translatable parts.
    -   `_tooltip`: For the element's tooltip text.
    -   `_placeholder`: For placeholder text in an input field.
    -   `_option1`, `_option2`: For different options in a dropdown menu.

**Examples:**
-   `OP_uiLanguage`: The main text for the UI Language dropdown in the Options Panel.
-   `OP_uiLanguage_tooltip`: The tooltip text for that same dropdown.
-   `OP_useResourceCounters_option1`: The first option in the "Use Resource Counters" dropdown.

Following this convention is crucial for the automated translation scripts to work correctly.

---

## Workflow 1: Adding a New Language

If you are a contributor who wants to add a language that doesn't exist yet (e.g., Japanese), follow these steps:

1.  **Create the Language File**: Make a copy of the `en.po` file and rename it using the appropriate language code (e.g., `jp.po`).
2.  **Edit the File Header**: Open your new file in a text editor (or a `.po` editor like Poedit). In the header section at the top, change the `Language` and `Language-Team` fields to match your language.
    ```po
    "Language-Team: Japanese\n"
    "Language: jp\n"
    ```
3.  **Translate the Strings**: Go through the file and replace the English text in every `msgstr "..."` line with your translation. Do not change the `msgid "..."` lines. This process can be simplified by using a specialized tool like PoEdit (https://poedit.net/).
4.  **Submit the File**: Once you are done, submit the completed `.po` file. The project owner will handle the rest.

---

## Workflow 2: Adding New Strings (for Project Owner)

When new UI elements, tooltips, or other texts are added to the game, they must be added to all language files for translation.

1.  **Update the Master File**: Add the new text string(s) to the **`en.po`** file first. Make sure to include any necessary comments (`#`) and a unique `msgid`.
2.  **Run the Sync Script**: Open a terminal in the `locales` folder and run the sync script:
    ```bash
    python _sync_po_files.py
    ```
    This script will automatically add the new strings from `en.po` to all other language files (`de.po`, `fr.po`, etc.). It will keep the file order consistent and use the English text as a placeholder for the new translations, making it easy for contributors to see what needs to be translated.

3.  **Inform Contributors**: Let the translation contributors know that new strings are available for translation. They can then update their respective `.po` files.

---

## Final Step: Generating the Game File

This step is typically performed by the project owner before releasing a new version of the mod.

After any new translations have been added or updated, the final mod file needs to be generated.

1.  **Run the Converter Script**: Open a terminal in the `locales` folder and run the converter script:
    ```bash
    python _po_to_lua_converter.py
    ```
2.  **Check the Output**: This script will take all the information from every `.po` file and generate a single, updated `i18nData.ttslua` file in the `src/Global/` directory. This is the file the mod actually uses to display text.

## Summary: When to Use Each Script

-   **`_sync_po_files.py`**:
    -   **Who**: Project Owner
    -   **When**: After adding new text strings to `en.po`.
    -   **Purpose**: To automatically update all other language files with the new, untranslated strings.

-   **`_po_to_lua_converter.py`**:
    -   **Who**: Project Owner
    -   **When**: As the final step before releasing a new version of the mod, after all translation updates have been submitted.
    -   **Purpose**: To compile all `.po` files into the final `i18nData.ttslua` file used by the game.

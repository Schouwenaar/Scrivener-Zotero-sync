# 📚 Scrivener–Zotero–Pandoc Sync Script

This small Python tool automatically syncs your latest Zotero `.bib` export with a Scrivener project, generates a citekey index for quick reference, and compiles your Markdown draft to a properly formatted `.docx` using Pandoc — complete with references and CSL styling.

---

## ✨ Features

* ✅ Automatically copies your latest Zotero `.bib` file to your project folder.
* ✅ Copies your preferred `.csl` citation style.
* ✅ Parses `.bib` with [`python-bibtexparser`](https://github.com/sciunto-org/python-bibtexparser) **v2**.
* ✅ Generates a clean `citekeys.md` index of your references that you can use within Scrivener so you never have to switch apps again.
* ✅ Runs Pandoc to produce a `.docx` with citations resolved.
* ✅ Designed for Mac, feel free to adapt.

---

## ⚡ Quickstart

### 1️⃣ Install requirements

This script auto-installs `bibtexparser` v2 if needed. Make sure you have:

* Python ≥ 3.8
* Pandoc installed and available on your PATH
* Your Zotero `.bib` export and `.csl` style ready

Example manual install:

```bash
pip install --pre bibtexparser
```

---

### 2️⃣ Prepare your folders

By default, the script looks for:

* Your Zotero `.bib` at `~/Zotero/auto/library.bib`
* Your `.csl` style at `~/Zotero/styles/apa-6th-edition.csl`

Adjust paths in `main.py` if needed.

---

### 3️⃣ Run the script

Compile your Scrivener project to Markdown. Then run:

```bash
python main.py /full/path/to/YourScrivenerDraft.md
```

---

## 📌 Notes on `bibtexparser` v2

This project uses the new `bibtexparser` v2 API:

```python
from bibtexparser import loads

with open("library.bib") as f:
    bib_database = loads(f.read())
```

See [python-bibtexparser v2 docs](https://bibtexparser.readthedocs.io/en/latest/) for details.

---

## 🧩 Example output

* `library.bib` and `.csl` are copied next to your `.md` file.
* `citekeys.md` is created: a human-readable list of your BibTeX keys, titles, and years.
* Final output: `YourScrivenerDraft.docx` with references formatted via Pandoc.

---

## 🛠️ Troubleshooting

* Ensure Pandoc is installed and accessible.
* Check that your `.bib` file is up-to-date.
* Adjust paths in the script if you have custom Zotero export folders.

---

## 🗂️ Adjusting the Scrivener Compile Format

To run the sync script automatically when compiling from Scrivener:

1. Open **Compile…** → select **MultiMarkdown** or **Pandoc** as output.
2. Click the **Processing** tab.
3. Enable **Post-process on command-line**.
4. Set the **Path** to your sync script, e.g. `/usr/local/bin/sync-biblio.sh`.
5. Use `<$inputfile>` as the **Arguments** to pass your compiled `.md` file.
6. Save the format for reuse.

Use the **Section Layouts** and **Separators** tabs to tweak headings, front/back matter, and section mappings.

Refer to Scrivener’s documentation for advanced compile settings.

---

**Happy writing and clean citations!**


---

Planned:

1. One self-contained executable
2. Zero hard-coded paths
3. One-click Scrivener hook
4. Cross-platform launcher
5. Friendly errors & docs

---
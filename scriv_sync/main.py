import sys
import subprocess
from pathlib import Path
import shutil
from bibtexparser import loads
from bibtexparser.bparser import BibTexParser

def write_citekeys_md(entries, output_file: Path):
    lines = []
    for entry in entries:
        key = entry.get("ID", "")
        title = entry.get("title", "").replace("\n", " ").strip("{} ")
        year = entry.get("year", "").strip("{} ")
        line = f"- **{key}**"
        if title:
            line += f" — {title}"
        if year:
            line += f" ({year})"
        lines.append(line)
    output_file.write_text("\n".join(lines), encoding="utf-8")

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <full-path-to-md>")
        sys.exit(1)

    md_file = Path(sys.argv[1]).resolve()
    if not md_file.exists():
        print(f"❌ Error: Markdown file not found: {md_file}")
        sys.exit(1)
    
    dir_path = md_file.parent
    print(f"📄 Processing: {md_file}")
    print(f"📂 Working directory: {dir_path}")

    # Source paths
    bib_src = Path.home() / "Zotero/auto/library.bib"
    csl_src = Path.home() / "Zotero/styles/apa-6th-edition.csl"
    bib_dst = dir_path / "library.bib"
    csl_dst = dir_path / "apa-6th-edition.csl"

    print(f"🔗 Zotero .bib source: {bib_src}")
    print(f"🔗 Zotero CSL source:  {csl_src}")

    # Copy bibliography
    if bib_src.exists():
        shutil.copy2(bib_src, bib_dst)
        print(f"✅ Copied bibliography to: {bib_dst}")
        print(f"   Size: {bib_dst.stat().st_size} bytes")
    else:
        print(f"❌ Error: Bibliography file not found at {bib_src}")
        sys.exit(1)

    # Copy CSL
    if csl_src.exists():
        shutil.copy2(csl_src, csl_dst)
        print(f"✅ Copied CSL style to: {csl_dst}")
    else:
        print(f"⚠️ Warning: CSL file not found at {csl_src} — continuing without it")

    # Write citekeys
    citekeys_md = dir_path / "citekeys.md"
    try:
        with open(bib_dst, 'r', encoding='utf-8') as f:
            bib_db = loads(f.read())
        write_citekeys_md(bib_db.entries, citekeys_md)
        print(f"✅ Citekeys written to: {citekeys_md}")
    except Exception as e:
        print(f"❌ Error reading/parsing bibliography: {e}")
        sys.exit(1)

    # Run Pandoc
    output_file = md_file.with_suffix(".docx")
    cmd = [
        "/opt/homebrew/bin/pandoc",
        str(md_file),
        "--citeproc",
        "--bibliography", str(bib_dst),
        "--csl", str(csl_dst),
        "-t", "docx",
        "-o", str(output_file)
    ]

    print(f"🚀 Running Pandoc...")
    print(f"   Command: {' '.join(cmd)}")

    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"✅ Pandoc conversion completed.")
        print(f"   Output file: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Pandoc failed:")
        print(f"   Return code: {e.returncode}")
        print(f"   stdout: {e.stdout}")
        print(f"   stderr: {e.stderr}")
        sys.exit(1)
    except FileNotFoundError:
        print("❌ Pandoc command not found. Check your PATH or use full path.")
        sys.exit(1)

    print("🎉 All tasks completed successfully!")

if __name__ == "__main__":
    main()

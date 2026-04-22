import os
from glob import glob
import re

BASE = os.path.dirname(os.path.abspath(__file__))
# Output to ../output/docs/ (production/latest/output/docs/)
NOTEBOOK_LM_FOLDER = os.path.abspath(os.path.join(BASE, "../output/docs"))
os.makedirs(NOTEBOOK_LM_FOLDER, exist_ok=True)

GROUPS = {
    "classes": "classes.md",
    "modules": "modules.md",
    "types": "types.md",
    "interfaces": "interfaces.md",
    "variables": "variables.md",
    "functions": "functions.md",
}
INDEX_FILE = os.path.join(NOTEBOOK_LM_FOLDER, "index.md")
CHANGELOG_FILE = os.path.join(NOTEBOOK_LM_FOLDER, "changelog.md")
GUIDES_FOLDER = os.path.join(BASE, "../source/guides")  # static content lives in source/
GUIDES_FOLDER_SCRIPTS = os.path.join(BASE, "guides")  # fallback if in scripts/

# Map external doc file names to web URLs if wanted
EXTERNAL_DOC_LINKS = {
    "GeoJSON-Format-RFC-7946.md": "https://www.rfc-editor.org/rfc/rfc7946",
    "Turf-Docs.md": "https://turfjs.org/",
}

def get_sdk_version_from_index_html():
    """Extract the full WME version string from the downloaded source/index.html."""
    html_path = os.path.abspath(os.path.join(BASE, "../source/index.html"))
    if not os.path.exists(html_path):
        # Fallback: check scripts folder (some setups store it there)
        html_path = os.path.join(BASE, "index.html")
    if not os.path.exists(html_path):
        return None
    with open(html_path, encoding="utf8", errors="ignore") as fin:
        content = fin.read()
    m = re.search(r"WME version (v[\w.\-]+)", content)
    return m.group(1) if m else None


def get_sdk_version_and_date(changelog_path):
    # Extract version and date from special front matter
    # Primary version source: source/index.html (WME version string)
    html_version = get_sdk_version_from_index_html()

    if not os.path.exists(changelog_path):
        return (html_version or "(unknown)", "(unknown)")
    with open(changelog_path, encoding="utf8") as fin:
        text = fin.read()
    # Get created date from front matter
    fm_match = re.search(r"^---\s*(.*?)---", text, re.DOTALL|re.MULTILINE)
    created = "(unknown)"
    if fm_match:
        fm = fm_match.group(1)
        created_match = re.search(r"created:\s*([0-9\-]+)", fm)
        if created_match:
            created = created_match.group(1)
    # Version: prefer HTML-extracted full version; fall back to changelog heading
    if html_version:
        version = html_version
    else:
        version_match = re.search(r"^##\s*(v[\w.\-]+)", text, re.MULTILINE)
        version = version_match.group(1) if version_match else "(unknown)"
    return (version, created)

def copy_guides_and_scripts():
    folder = GUIDES_FOLDER if os.path.exists(GUIDES_FOLDER) else GUIDES_FOLDER_SCRIPTS
    if not os.path.exists(folder):
        print(f"No guides folder found at {GUIDES_FOLDER} or {GUIDES_FOLDER_SCRIPTS}")
        return []
    guide_files = sorted(glob(os.path.join(folder, "*.md")))
    out_names = []
    for src_path in guide_files:
        base_name = os.path.basename(src_path)
        dst_path = os.path.join(NOTEBOOK_LM_FOLDER, base_name)
        with open(src_path, encoding="utf8") as fin, open(dst_path, "w", encoding="utf8") as fout:
            fout.write(fin.read())
        print(f"Copied guide/script {src_path} to {dst_path}")
        out_names.append(base_name)
    return out_names

def source_guide_section(external_md_files=None, guides_md_files=None):
    lines = []
    lines.append("## Source Guide\n")
    lines.append("This section describes each documentation source included for NotebookLM comprehension and search.\n")
    lines.append("- **classes.md**: All documented SDK classes, grouped by class. Use for questions about class properties and methods.")
    lines.append("- **modules.md**: All documented modules in the SDK. Use for module structure and contents.")
    lines.append("- **types.md**: SDK type definitions, enums, and type aliases. Useful for type-related queries.")
    lines.append("- **interfaces.md**: All SDK interfaces, with descriptions and members.")
    lines.append("- **variables.md**: Variables and constants exported by the SDK.")
    lines.append("- **functions.md**: All SDK functions, including parameters and return details.")
    lines.append("- **changelog.md**: Historical list of SDK changes and version releases.")
    lines.append("- **Multiple type definition files**: (e.g. geojson_typedefs.md, tufs_typedefs.md, wmeSDK_typedefs.md): The TypeScript type definitions for external types referenced by the SDK.")
    if external_md_files:
        lines.append("- **externalDocs**: Additional external documentation files for referenced libraries and standards, such as Turf and GeoJSON RFCs:")
        for fname in external_md_files:
            url = EXTERNAL_DOC_LINKS.get(fname)
            if url:
                lines.append(f"    - {fname} ([link]({url}))")
            else:
                lines.append(f"    - {fname}")
    lines.append("")
    lines.append("- **Getting Started & example scripts.**")
    
    # Define standard guides
    standard_guides = {
        "how-to-get-started-with-the-wmeSDK.md": "A user walk thru guide to setting up a new script and working with the wme SDK",
        "migration-guide.md": "Waze Map Editor JavaScript SDK: Migration & Prompt Guide",
        "geometry-file-converters.md": "javascript Utils to convert from KML, KMZ, WKT, GPX, GML, and shapefiles(SHP,SHX,DBF).ZIP to geoJSON",
    }
    
    # Add standard guides first
    for fname, desc in standard_guides.items():
        lines.append(f"  - **{fname}**: {desc}")
    
    # Add any script-example files dynamically from guides_md_files
    if guides_md_files:
        script_examples = sorted([f for f in guides_md_files if f.startswith("script-example-")])
        for fname in script_examples:
            # Try to extract title from file content, fallback to filename
            guide_path = os.path.join(NOTEBOOK_LM_FOLDER, fname)
            pretty_title = fname.replace(".md", "").replace("-", " ").replace("script example", "Script Example")
            try:
                with open(guide_path, encoding="utf8") as fin:
                    first_line = fin.readline().strip()
                    m = re.match(r"^#+\s+(.*)", first_line)
                    if m:
                        pretty_title = m.group(1).strip()
            except Exception:
                pass
            lines.append(f"  - **{fname}**: {pretty_title}")
    
    return "\n".join(lines)

def combine_group(group, outname):
    folder = os.path.join(BASE, group)
    files = sorted(glob(os.path.join(folder, "*.md")))
    outpath = os.path.join(NOTEBOOK_LM_FOLDER, outname)
    found_titles = []
    with open(outpath, "w", encoding="utf8") as out:
        for fname in files:
            title = os.path.splitext(os.path.basename(fname))[0]
            found_titles.append(title)
            out.write(f"# {title}\n\n")
            with open(fname, encoding="utf8") as fin:
                content = fin.read().strip()
                out.write(content)
                out.write("\n\n---\n\n")
    print(f"Created grouped markdown: {outpath}")
    return found_titles

def make_changelog():
    src = os.path.join(BASE, "documents", "CHANGELOG.md")
    dst = CHANGELOG_FILE
    if os.path.exists(src):
        with open(src, encoding="utf8") as fin, open(dst, "w", encoding="utf8") as fout:
            fout.write(fin.read())
        print(f"Copied changelog to: {dst}")

def copy_all_typedefs():
    typedef_folder = os.path.join(BASE, "TypeDefs")
    # Get all .d.ts files
    typedef_files = sorted(glob(os.path.join(typedef_folder, "*.d.ts")))
    typedef_output_files = []
    for src_path in typedef_files:
        base_name = os.path.splitext(os.path.basename(src_path))[0]
        dst_name = f"{base_name}.md"
        dst_path = os.path.join(NOTEBOOK_LM_FOLDER, dst_name)
        with open(src_path, encoding="utf8") as fin, open(dst_path, "w", encoding="utf8") as fout:
            fout.write(f"# {base_name} Type Definitions\n\n")
            fout.write("```typescript\n")
            fout.write(fin.read().rstrip("\n"))
            fout.write("\n```\n")
        print(f"Copied {src_path} to: {dst_path}")
        typedef_output_files.append(dst_name)
    return typedef_output_files

def copy_external_docs():
    external_folder = os.path.join(BASE, "externalDocs") if os.path.exists(os.path.join(BASE, "externalDocs")) else os.path.join(BASE, "../source/externalDocs")
    if not os.path.exists(external_folder):
        print(f"No externalDocs folder found at: {external_folder}")
        return []
    out_files = []
    md_files = glob(os.path.join(external_folder, "*.md"))
    for src_path in md_files:
        base_name = os.path.basename(src_path)
        dst_path = os.path.join(NOTEBOOK_LM_FOLDER, base_name)
        with open(src_path, encoding="utf8") as fin, open(dst_path, "w", encoding="utf8") as fout:
            fout.write(fin.read())
        print(f"Copied external doc {src_path} to: {dst_path}")
        out_files.append(base_name)
    return out_files

def build_index(grouped_files, typedef_md_files, external_md_files, sdk_version, sdk_date, guides_md_files=None):
    # Section counts
    section_counts = {group: len(grouped_files.get(group, [])) for group in GROUPS}
    typedef_count = len(typedef_md_files)
    external_count = len(external_md_files)

    # Machine-readable YAML block
    yaml_block = [
        "---",
        f"sdk: WME",
        f"version: {sdk_version}",
        f"generated: {sdk_date}",
        f"sections:",
    ]
    for group, outname in GROUPS.items():
        yaml_block.append(f"  {group}: {outname}")
    yaml_block.append(f"  changelog: changelog.md")
    yaml_block.append("docs:")
    yaml_block.append("  typedefs:")
    for fname in typedef_md_files:
        yaml_block.append(f"    - {fname}")
    yaml_block.append("  external:")
    for fname in external_md_files:
        yaml_block.append(f"    - {fname}")
    yaml_block.append("  guides:")
    for fname in guides_md_files:
        yaml_block.append(f"    - {fname}")
    yaml_block.append("---\n")

    # Top-level TOC
    toc_lines = [
        "## Table of Contents",
        "",
        "- [Source Guide](#source-guide)",
        "- [Classes](#classes)",
        "- [Modules](#modules)",
        "- [Types](#types)",
        "- [Interfaces](#interfaces)",
        "- [Variables](#variables)",
        "- [Functions](#functions)",
        "- [Changelog](#changelog)",
        "- [Type Definition Files](#type-definition-files)",
        "- [External Documentation Files](#external-documentation-files)",
        "- [Getting Started / How-To Guides](#getting-started--how-to-guides)",
        "",
    ]

    # Instructions
    instructions = [
        "> **Use this index to discover available documentation and their content.**",
        "> For searching SDK entities, refer to the Source Guide below, then navigate to the relevant section.",
        "",
        f"> **SDK Version:** {sdk_version}",
        f"> **Docs generated:** {sdk_date}",
        "",
        "> Each section below lists the source file and the entities it contains.",
        "",
    ]

    with open(INDEX_FILE, "w", encoding="utf8") as out:
        # YAML metadata
        out.write("\n".join(yaml_block))
        out.write("\n")
        # TOC and Instructions
        out.write("\n".join(toc_lines))
        out.write("\n")
        out.write("\n".join(instructions))
        out.write("\n")

        # Source guide
        out.write(source_guide_section(external_md_files, guides_md_files))
        out.write("\n")

        # Each main section
        for group, outname in GROUPS.items():
            count = section_counts[group]
            out.write(f"## {group.capitalize()}\n\n")
            out.write(f"- [{outname}]({outname}) — *{count} entries*\n")
            files = grouped_files.get(group, [])
            for fname in files:
                out.write(f"    - {fname}\n")
            out.write("\n")
            # See Also
            out.write("> See Also: [Type Definition Files](#type-definition-files), [External Documentation Files](#external-documentation-files)\n\n")

        # Changelog
        out.write(f"## [Changelog](changelog.md)\n\n")

        # Type Definitions
        out.write("## Type Definition Files\n\n")
        out.write(f"*{typedef_count} files*\n")
        for fname in typedef_md_files:
            out.write(f"- [{fname}]({fname})\n")
        out.write("\n> See Also: [External Documentation Files](#external-documentation-files)\n\n")

        # External docs
        if external_md_files:
            out.write("## External Documentation Files\n\n")
            out.write(f"*{external_count} files*\n")
            for fname in external_md_files:
                url = EXTERNAL_DOC_LINKS.get(fname)
                if url:
                    out.write(f"- [{fname}]({fname}) ([Official Docs]({url}))\n")
                else:
                    out.write(f"- [{fname}]({fname})\n")
            out.write("\n")
        # Contribution info
        #out.write("> *For questions or contributions, contact Jane Doe (janedoe@yourcompany.com).*\n")
        #out.write("\n")
        # Add guides/how-to/scripts section
        if guides_md_files and len(guides_md_files) > 0:
            out.write("## Getting Started / How-To Guides\n\n")
            for fname in guides_md_files:
                # Try to grab "# Title" from .md file for display, fallback to filename
                guide_path = os.path.join(NOTEBOOK_LM_FOLDER, fname)
                pretty = fname.replace("_", " ").replace(".md", "").capitalize()
                try:
                    with open(guide_path, encoding="utf8") as fin:
                        first_line = fin.readline()
                        m = re.match(r"^#\s+(.*)", first_line)
                        if m:
                            pretty = m.group(1).strip()
                except Exception:
                    pass
                out.write(f"- [{pretty}]({fname})\n")
            out.write("\n")
    print(f"Created index: {INDEX_FILE}")

def main():
    grouped_files = {}
    for group, outname in GROUPS.items():
        grouped_files[group] = combine_group(group, outname)
    make_changelog()
    typedef_md_files = copy_all_typedefs()
    external_md_files = copy_external_docs()
    sdk_version, sdk_date = get_sdk_version_and_date(CHANGELOG_FILE)
    guides_md_files = copy_guides_and_scripts() 
    build_index(grouped_files, typedef_md_files, external_md_files, sdk_version, sdk_date, guides_md_files=guides_md_files)

if __name__ == "__main__":
    main()

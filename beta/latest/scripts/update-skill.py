"""
update-skill.py
===============
Pulls the latest WME SDK skill from the Claude Code skills directory.

This script copies the SKILL.md file from ~/.claude/skills/wme-sdk into the
local skills/ folder, keeping it in sync with the main SDK documentation updates.

Path Substitution:
  Automatically converts hardcoded absolute paths to relative paths so that
  the skill works for anyone who clones or forks the repository.
  - Original: production/latest/docs/
  - Replaced: ../../output/docs/ (from skills to output/docs)

Usage:
  py update-skill.py
  py update-skill.py --skill-path /custom/path/to/skill

Output:
  - ../output/skills/SKILL.md -- Copy of the WME SDK skill with paths adjusted for repo
  - Prints status (updated, already current, or error)
"""

import os
import re
import argparse
from pathlib import Path

DEFAULT_SKILL_SOURCE = os.path.expanduser("~/.claude/skills/wme-sdk/SKILL.md")

# Path substitutions for fallback chain
HARDCODED_PATH = "production/latest/docs/"
RELATIVE_PATH = "../../output/docs/"  # From scripts/ to ../output/docs/
GITHUB_PAGES_URL = "https://kid4rm90s.github.io/WME-SDK-Mirror/beta/latest/output/docs/"

# User's local path (replace in repo version with template)
USER_LOCAL_PATH = r"C:\Users\Jstrand\OneDrive - FactSet\Personal\waze stuff\WAZE SDK Mirror\production\latest\output\docs"
TEMPLATE_LOCAL_PATH = "/path/to/your/WME-SDK-Mirror/production/latest/output/docs"


def get_skill_path(custom_path=None):
    """Resolve the skill source path."""
    if custom_path:
        return custom_path
    return DEFAULT_SKILL_SOURCE


def main():
    parser = argparse.ArgumentParser(
        description="Pull latest WME SDK skill from Claude Code skills directory"
    )
    parser.add_argument(
        "--skill-path",
        default=None,
        help=f"Custom path to the skill file (default: {DEFAULT_SKILL_SOURCE})"
    )
    args = parser.parse_args()

    skill_source = get_skill_path(args.skill_path)
    skill_dest = os.path.join(os.getcwd(), "../output/skills", "SKILL.md")

    # Ensure destination directory exists
    os.makedirs(os.path.dirname(skill_dest), exist_ok=True)

    # Check if source exists
    if not os.path.isfile(skill_source):
        print(f"[ERROR] Skill source not found: {skill_source}")
        print(f"        Is the wme-sdk skill installed in ~/.claude/skills/?")
        return 1

    # Copy the skill
    try:
        # Read source to check if update is needed
        with open(skill_source, 'r', encoding='utf-8') as f:
            source_content = f.read()

        # Replace hardcoded path with fallback chain (local + GitHub Pages)
        # The fallback includes paths but NOT backticks (those stay from the original markdown)
        fallback_text = f"{RELATIVE_PATH}` (or `{GITHUB_PAGES_URL}"

        # Replace wrapped in backticks (how it appears in markdown)
        modified_content = source_content.replace(
            f"`{HARDCODED_PATH.replace('/', '\\\\')}",
            f"`{fallback_text}"
        )
        modified_content = modified_content.replace(
            f"`{HARDCODED_PATH}",
            f"`{fallback_text}"
        )
        # Also replace unwrapped (just in case)
        modified_content = modified_content.replace(
            HARDCODED_PATH.replace('/', '\\'),
            fallback_text
        )
        modified_content = modified_content.replace(
            HARDCODED_PATH,
            fallback_text
        )

        # Replace user's local path with template path for repo version
        # This allows people cloning the repo to customize the path easily
        modified_content = modified_content.replace(
            USER_LOCAL_PATH,
            TEMPLATE_LOCAL_PATH
        )
        # Also handle forward slashes (in case user has mixed path)
        modified_content = modified_content.replace(
            USER_LOCAL_PATH.replace('\\', '/'),
            TEMPLATE_LOCAL_PATH
        )

        # Check if destination exists and has same content
        if os.path.isfile(skill_dest):
            with open(skill_dest, 'r', encoding='utf-8') as f:
                dest_content = f.read()
            if modified_content == dest_content:
                print("[OK] Skill is current: skills/SKILL.md")
                return 0

        # Write updated skill with fallback chain
        with open(skill_dest, 'w', encoding='utf-8') as f:
            f.write(modified_content)
        print("[UPDATED] Skill copied with fallback chain for docs discovery")
        print(f"          Destination: skills/SKILL.md")
        print(f"          Fallback chain:")
        print(f"            Primary:  Local at {RELATIVE_PATH}")
        print(f"            Fallback: {GITHUB_PAGES_URL}")
        return 0

    except Exception as e:
        print(f"[ERROR] Failed to update skill: {e}")
        return 1


if __name__ == "__main__":
    exit(main())

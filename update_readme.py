#!/usr/bin/env python3
"""
update_readme.py: Automatically update README.md with:
1. Exact total lesson count in shields.io badge.
2. Volume 3 lesson range in the download table.
3. Permanent latest release download URL for Volume 3 (letz3.pdf).
4. Repository structure tree range (lesson1.tex - lessonN.tex).
"""
import glob
import re
import sys

def main():
    readme_path = "README.md"
    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: {readme_path} not found.", file=sys.stderr)
        sys.exit(1)

    lesson_files = glob.glob("lessons/lesson*.tex")
    lesson_nums = []
    for lf in lesson_files:
        m = re.search(r"lesson(\d+)\.tex", lf)
        if m:
            lesson_nums.append(int(m.group(1)))

    if not lesson_nums:
        print("No lesson files found.", file=sys.stderr)
        return

    max_lesson = max(lesson_nums)
    total_lessons = len(lesson_nums)

    # 1. Update Badge: Volumes-3%20Volumes%20(35%20Lessons) -> (36 Lessons)
    content = re.sub(
        r"badge/Volumes-3%20Volumes%20\(\d+%20Lessons\)-brightgreen\.svg",
        f"badge/Volumes-3%20Volumes%20({total_lessons}%20Lessons)-brightgreen.svg",
        content
    )

    # 2. Update Table: Volume 3 row with permanent latest release URL and updated scope
    latest_v3_url = "https://github.com/tigran-a/elements-of-luxembourgish/releases/latest/download/letz3.pdf"
    content = re.sub(
        r"\|\s*\*\*Volume 3\*\*\s*\|\s*Lessons 32\s*–\s*\d+\+?\s*\|\s*\[\*\*Download `letz3\.pdf`\*\*\]\([^)]+\)\s*\|\s*Active / Growing\s*\|",
        f"| **Volume 3** | Lessons 32 – {max_lesson}+ | [**Download `letz3.pdf`**]({latest_v3_url}) | Active / Growing |",
        content
    )

    # 3. Update Repository Tree: (lesson1.tex - lessonXX.tex)
    content = re.sub(
        r"lesson1\.tex\s*-\s*lesson\d+\.tex",
        f"lesson1.tex - lesson{max_lesson}.tex",
        content
    )

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"README.md successfully updated (Total Lessons: {total_lessons}, Max Lesson: {max_lesson}).")

if __name__ == "__main__":
    main()

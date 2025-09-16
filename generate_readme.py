import os
import re
from collections import defaultdict

FOLDERS = ["0-1000", "1001-2000", "2001-3000", "3001-4000"]

README_FILE = "README.md"

def generate_markdown():
    md_lines = []

    md_lines.append("# 🧠 LeetCode Solutions in Python\n")
    md_lines.append("This repository contains my solutions to various [LeetCode](https://leetcode.com/) problems, written in **Python**.\n")
    md_lines.append("The solutions are grouped by **problem number ranges** for easy navigation.\n\n")
    md_lines.append("---\n")

    total_problems = set()  # track unique problem numbers

    list_problem = []
    for folder in FOLDERS:
        if not os.path.exists(folder):
            continue

        list_problem.append(f"## 📂 {folder}\n\n")
        files = sorted(f for f in os.listdir(folder) if f.endswith(".py"))
        if not files:
            list_problem.append("_No solutions yet in this range._\n\n")
            continue

        # Group by problem number
        problems = defaultdict(list)
        for file in files:
            match = re.match(r"leet_code_(\d+)_?(.*)\.py", file)
            if match:
                problem_number = match.group(1)
                way = match.group(2) or ""  # could be "way_01"
                problems[problem_number].append((way, file))
                total_problems.add(problem_number)  # count unique problem numbers
            else:
                problems[file] = [("", file)]  # fallback if naming is different
                total_problems.add(file)  # still count it as one "problem"


        list_problem.append("| Problem Number | Solutions |\n")
        list_problem.append("|---------------|-----------|\n")

        for problem_number, variants in sorted(problems.items(), key=lambda x: int(x[0])):
            links = " <br> ".join(f"[{way or 'solution'}]({folder}/{file})" for way, file in variants)
            list_problem.append(f"| {problem_number} | {links} |\n")

        list_problem.append("\n")

    # Add total count section
    md_lines.append("---\n")
    md_lines.append(f"### 📊 Total Problems Solved: **{len(total_problems)}**\n\n")
    md_lines.append("---\n")
    md_lines.append("---\n")
    md_lines.extend(list_problem)
    md_lines.append("---\n")
    md_lines.append("---\n")


    return "".join(md_lines)


if __name__ == "__main__":
    markdown_content = generate_markdown()
    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    print(f"✅ README.md generated successfully with grouped solutions!")

#!/usr/bin/env python3
"""
customize.py — Tailors resume.md to a specific job description using Claude.

Usage:
    python customize.py --jd path/to/job.txt --company acme
    uv run customize.py --jd path/to/job.txt --company acme

Output: resume-<company>.md in the same directory as this script.
"""

import argparse
import os
import sys
from pathlib import Path

import anthropic

RESUME_FILE = Path(__file__).parent / "resume.md"
PERSONAL_FILE = Path(__file__).parent / "personal.md"

SYSTEM_PROMPT = """\
You are an expert technical resume writer. You will be given a master resume and a job description.
Your task is to produce a tailored version of the resume that:

1. Reorders and emphasizes experience and skills most relevant to the job description.
2. Adjusts bullet point language to mirror the terminology and priorities in the job posting.
3. Trims or de-emphasizes experience that is not relevant.
4. Keeps the Professional Summary sharp and targeted to this specific role.
5. Does NOT fabricate experience, skills, or credentials not present in the master resume.
6. Preserves all factual details (company names, dates, titles, metrics).
7. Outputs valid Markdown, matching the formatting conventions of the input resume.

Return only the tailored resume — no preamble, no commentary.
"""


def load_personal() -> str:
    if not PERSONAL_FILE.exists():
        return ""
    return PERSONAL_FILE.read_text().strip()


def load_resume() -> str:
    if not RESUME_FILE.exists():
        print(f"Error: resume file not found at {RESUME_FILE}", file=sys.stderr)
        sys.exit(1)
    personal = load_personal()
    resume = RESUME_FILE.read_text()
    if personal:
        return f"{personal}\n\n---\n\n{resume}"
    return resume


def load_job_description(path: str) -> str:
    jd_path = Path(path)
    if not jd_path.exists():
        print(f"Error: job description file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return jd_path.read_text()


def customize_resume(resume: str, job_description: str) -> str:
    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env

    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": (
                    f"## Master Resume\n\n{resume}\n\n"
                    f"## Job Description\n\n{job_description}"
                ),
            }
        ],
    )

    return message.content[0].text


def main():
    parser = argparse.ArgumentParser(
        description="Tailor resume.md to a job description using Claude."
    )
    parser.add_argument(
        "--jd",
        required=True,
        metavar="FILE",
        help="Path to the job description file (.txt or .md)",
    )
    parser.add_argument(
        "--company",
        required=True,
        metavar="NAME",
        help="Company name used to name the output file (e.g. 'acme' → resume-acme.md)",
    )
    args = parser.parse_args()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY environment variable is not set.", file=sys.stderr)
        sys.exit(1)

    resume = load_resume()
    job_description = load_job_description(args.jd)

    print(f"Customizing resume for: {args.company} ...")
    tailored = customize_resume(resume, job_description)

    output_file = Path(__file__).parent / f"resume-{args.company.lower().replace(' ', '-')}.md"
    output_file.write_text(tailored)
    print(f"Written to: {output_file}")


if __name__ == "__main__":
    main()

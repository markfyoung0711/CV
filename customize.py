#!/usr/bin/env python3
"""
customize.py — Tailors resume.md to a specific job description using Claude.

Usage:
    python customize.py --jobname whitpain_pa
    python customize.py   # no jobname: outputs master resume as-is to resume-general.md

job-index.txt format:  <url> = <job_name>
  The job name (right of '=') maps to jd-<job_name>.txt in the same directory.

Output: resume-<company>.md in the same directory as this script.
"""

import argparse
import os
import sys
import time
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
        # Strip the "# Personal Contact Information" heading, keep just the contact lines
        lines = personal.splitlines()
        contact_lines = [l for l in lines if not l.startswith("# ")]
        contact_block = "\n".join(contact_lines).strip()
        # Insert contact block after the first heading line in the resume
        resume_lines = resume.splitlines(keepends=True)
        for i, line in enumerate(resume_lines):
            if line.startswith("# "):
                insert_at = i + 1
                resume_lines.insert(insert_at, f"\n{contact_block}\n")
                break
        return "".join(resume_lines)
    return resume


def load_job_description(job_name: str) -> str:
    jd_path = Path(__file__).parent / f"jd-{job_name}.txt"
    if not jd_path.exists():
        print(f"Error: job description file not found: {jd_path}", file=sys.stderr)
        sys.exit(1)
    return jd_path.read_text()


def customize_resume(resume: str, job_description: str) -> str:
    import httpx
    client = anthropic.Anthropic(http_client=httpx.Client(verify=False))  # reads ANTHROPIC_API_KEY from env

    for attempt in range(4):
        try:
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
        except anthropic.APIStatusError as e:
            if e.status_code == 529 and attempt < 3:
                wait = 2 ** attempt * 5  # 5s, 10s, 20s
                print(f"API overloaded, retrying in {wait}s (attempt {attempt + 1}/3)...")
                time.sleep(wait)
            else:
                raise


def main():
    parser = argparse.ArgumentParser(
        description="Tailor resume.md to a job description using Claude."
    )
    parser.add_argument(
        "--jobname",
        required=False,
        default=None,
        metavar="NAME",
        help="Job name (right of '=' in job-index.txt), used to find jd-<jobname>.txt and name the output. "
             "If omitted, outputs the master resume as-is (with personal details).",
    )
    args = parser.parse_args()

    resume = load_resume()

    if args.jobname is None:
        output_file = Path(__file__).parent / "resume-general.md"
        output_file.write_text(resume)
        print(f"Written to: {output_file}")
        return

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY environment variable is not set.", file=sys.stderr)
        sys.exit(1)

    job_description = load_job_description(args.jobname.lower().replace(" ", "-"))

    print(f"Customizing resume for: {args.jobname} ...")
    tailored = customize_resume(resume, job_description)

    output_file = Path(__file__).parent / f"resume-{args.jobname.lower().replace(' ', '-')}.md"
    output_file.write_text(tailored)
    print(f"Written to: {output_file}")


if __name__ == "__main__":
    main()

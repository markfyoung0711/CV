# Resume Repository - Mark Young

## Purpose

This repo contains Mark Young's master resume and tooling to customize it per job application. `customize.py` reads `resume.md` as the source of truth and uses Claude to tailor the content to a specific job's requirements.

## Files

| File | Description |
|------|-------------|
| `resume.md` | Master resume — full work history, skills, and education. Primary input to `customize.py`. |
| `personal.md` | Contact details (Name, Email, Phone, LinkedIn, GitHub). Injected after the first heading of the resume at build time. |
| `customize.py` | Main script. Builds the resume (see below). |
| `job-index.txt` | Index of job applications. Format: `<url> = <job_name>` per line. |
| `jd-<jobname>.txt` | Job description file for a given job name. |
| `resume-general.md` | Output: master resume with personal details, no tailoring. |
| `resume-<jobname>.md` | Output: Claude-tailored resume for a specific job. |

## Usage

```bash
# Generate general (untailored) resume
python3 customize.py

# Generate a tailored resume for a specific job
python3 customize.py --jobname <jobname>
```

`<jobname>` must match the right-hand side of a line in `job-index.txt` and have a corresponding `jd-<jobname>.txt` file.

Requires the `ANTHROPIC_API_KEY` environment variable to be set when tailoring.

## How It Works

1. **Load resume**: reads `resume.md` and injects contact details from `personal.md` immediately after the first `# Heading` line.
2. **General mode** (`--jobname` omitted): writes the assembled resume directly to `resume-general.md` — no LLM call.
3. **Tailored mode** (`--jobname <name>`): sends the assembled resume + the job description (`jd-<name>.txt`) to Claude (`claude-opus-4-6`) with a system prompt instructing it to reorder/emphasize relevant experience, mirror job-description language, and trim irrelevant content — without fabricating anything.
4. Writes output to `resume-<jobname>.md`.

## System Prompt Behaviour

Claude is instructed to:
- Reorder and emphasize experience relevant to the job description
- Mirror terminology and priorities from the job posting
- Trim or de-emphasize irrelevant experience
- Keep the Professional Summary targeted to the role
- Never fabricate experience, skills, or credentials
- Preserve all factual details (company names, dates, titles, metrics)
- Output valid Markdown matching the input formatting conventions

## Markdown Formatting Note

Contact detail lines in `personal.md` use trailing two-space hard line breaks (`  `) so each field renders on its own line in Markdown viewers.

## About Mark

Senior Software Engineer with 25+ years of experience across financial data systems (Citadel, Jump Trading), game publishing infrastructure (Blizzard/Microsoft), and data engineering (Buckstop Labs). Strong in Python, SQL, C++, DevOps, and technical leadership. Focused on roles where LLMs and AI agents are central to how software is built and operated.

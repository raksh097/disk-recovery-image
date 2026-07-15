# Disk Recovery Image

Digital forensics project focused on disk image recovery, file analysis, and evidence documentation.

## Overview

This 3rd year project explores how data can be recovered and documented from a disk image in a digital forensics workflow. The goal is to understand the recovery process, maintain clean notes, and present findings in a structured way.

## Objectives

- Understand the basics of disk image handling
- Recover accessible files from a disk image
- Document recovery steps clearly
- Practice evidence handling and investigation-style reporting
- Learn how digital forensics workflows are organized

## Project Workflow

1. Prepare or collect a disk image for analysis
2. Inspect the image structure and available partitions
3. Identify recoverable files and metadata
4. Recover selected files safely
5. Record observations, tools used, and recovery results
6. Prepare a short summary report

## Key Concepts

- Disk image analysis
- File recovery
- Metadata review
- Evidence documentation
- Digital forensics process

## Tools and Skills

- Digital forensics basics
- Disk image recovery workflow
- Documentation and reporting
- Git and GitHub

## Source Code

This repository includes a Python-based recovery workflow:

- `main.py` - command-line entry point
- `scanner.py` - scans disk images for known file system signatures
- `extractor.py` - extracts partition data from discovered offsets
- `carver.py` - carves JPG, PNG, and PDF files by signature
- `flag_finder.py` - searches for CTF-style flags inside an image
- `utils/` - logging and binary helper functions

Large disk images, recovered files, virtual environments, and private outputs are intentionally ignored by `.gitignore`.

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the recovery workflow on a local disk image:

```bash
python main.py path/to/image.img
```

Recovered files are written to `output/`, which is not committed to GitHub.

## Learning Outcome

Through this project, I practiced the process of treating disk data as evidence and documenting recovery steps in a professional, repeatable format.

## Future Improvements

- Add screenshots of the recovery workflow
- Include sample report format
- Add tool-specific notes
- Document test cases with different file types

## Author

Rakshitha N P  
4th Year Cybersecurity Student  
Portfolio: <https://raksh097.github.io/raksh097-portfolio/>

# You.com — Research / Answer APIs

Grace R. Nettey's separate learning workspace, created 2026-11-05. **Starter setup; no research experiment has been run.** This folder is ready for hand annotations and code changes. The research narrative stays on the [existing project entry](https://manifoldgrace.github.io/feature-contributions.html#company-gap-18).

## Source code to explore

- [Accessible source code](https://github.com/youdotcom-oss/youdotcom-python-sdk/tree/64263a0029efb956b82da4712d74765ec0f5ee53/src) · [upstream repository](https://github.com/youdotcom-oss/youdotcom-python-sdk)
- Checked revision: `64263a0029efb956b82da4712d74765ec0f5ee53` (default branch `main` at setup).
- Scope: Official API client; cited research results require independent source checking.
- [Licence / repository terms](https://github.com/youdotcom-oss/youdotcom-python-sdk/blob/64263a0029efb956b82da4712d74765ec0f5ee53/LICENSE): MIT.

This workspace starts from scratch. No upstream code, model weights, datasets or credentials have been copied. An SDK does not expose a provider's proprietary service. This source is a possible starting point, not proof that the feature gap has been solved or that it exactly reproduces a cited paper. Check per-file/data/model terms before importing material. Keep an imported revision, its licence and your changes distinguishable.

## First bounded investigation

Fictional pilot: One source supports a compound claim only partly; another is a duplicate of the first.

Observation checks: Scores support per claim; traces duplicate ancestry; records inaccessible evidence.

Add at least one unaffected control and one competing explanation before comparing runs. `project.json` holds the pilot and source manifest; edit `NOTES.md` for your own questions, reading notes and contribution record. Model behaviour, evidence validity and explanations should be recorded separately.

## Start tinkering

1. Clone your collection: `git clone https://github.com/manifoldgrace/ManifoldGrace.git`.
2. Open `learning-projects/companies/18-you-research-support/` and edit `NOTES.md` or `experiment.py`.
3. From the repository root run `python learning-projects/companies/18-you-research-support/experiment.py`. Python 3.10+ and the standard library are sufficient. It prints the planned pilot with `not_run`; it does not contact a model or score a result.
4. Create a JSON observation containing the string fields `case_id`, `observation`, `evidence` and `interpretation`; use `fictional-pilot-01` as the case ID. Run the same command with `--record /path/to/observation.json`. This appends a dated manual record to this folder's local `observations.jsonl`; it does not certify correctness.
5. Replace or extend `experiment.py` when you choose an actual method. Record dependencies, API costs and model/data versions at that point. Do not commit secrets or private institutional records.

For an upstream checkout later, use a separate local directory, retain its licence/notices and record the revision above. No dependency is installed and no upstream program runs automatically. Public access and permission to reuse are separate checks, particularly where no licence was identified.

[Collection index](../../README.md) · [Hand annotations](NOTES.md) · [Starter code](experiment.py) · [Manifest and pilot](project.json)

<!-- research-dossier-link:start -->
## Research, engineering and explanation

[Editable research dossier](RESEARCH.md) · [Online workbench and demo](https://manifoldgrace.github.io/research-project.html?project=company-gap-18) · [Visual roadmap source](ROADMAP.mmd) · [Milestones](milestones.csv) · [Claim-to-evidence register](evidence.csv). The shared [methodological guide](../../RESEARCH-GUIDE.md) defines the structure; this project keeps its own analysis, observations and contributions.
<!-- research-dossier-link:end -->

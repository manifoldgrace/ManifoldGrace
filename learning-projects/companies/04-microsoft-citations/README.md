# Microsoft — Microsoft 365 Copilot

Grace R. Nettey's separate learning workspace, created 2026-11-05. **Starter setup; no research experiment has been run.** This folder is ready for hand annotations and code changes. The research narrative stays on the [existing project entry](https://manifoldgrace.github.io/feature-contributions.html#company-gap-4).

## Source code to explore

- [Accessible source code](https://github.com/microsoft/autogen/tree/d07c667a3239ea4ab7af62a53b0f4ff205a1f23d/python) · [upstream repository](https://github.com/microsoft/autogen)
- Checked revision: `d07c667a3239ea4ab7af62a53b0f4ff205a1f23d` (default branch `main` at setup).
- Scope: Agent framework for a local analogue; not Microsoft 365 Copilot implementation or tenant audit code.
- [Licence / repository terms](https://github.com/microsoft/autogen/blob/d07c667a3239ea4ab7af62a53b0f4ff205a1f23d/LICENSE-CODE): MIT for code; CC-BY-4.0 for documentation.

This workspace starts from scratch. No upstream code, model weights, datasets or credentials have been copied. An SDK does not expose a provider's proprietary service. This source is a possible starting point, not proof that the feature gap has been solved or that it exactly reproduces a cited paper. Check per-file/data/model terms before importing material. Keep an imported revision, its licence and your changes distinguishable.

## First bounded investigation

Fictional pilot: A fictional source is cited, then superseded and access revoked. Compare historical answer pointers with newly retrieved content.

Observation checks: Distinguishes stale pointer from unauthorised access; records version and permissions; tests a local analogue only.

Add at least one unaffected control and one competing explanation before comparing runs. `project.json` holds the pilot and source manifest; edit `NOTES.md` for your own questions, reading notes and contribution record. Model behaviour, evidence validity and explanations should be recorded separately.

## Start tinkering

1. Clone your collection: `git clone https://github.com/manifoldgrace/ManifoldGrace.git`.
2. Open `learning-projects/companies/04-microsoft-citations/` and edit `NOTES.md` or `experiment.py`.
3. From the repository root run `python learning-projects/companies/04-microsoft-citations/experiment.py`. Python 3.10+ and the standard library are sufficient. It prints the planned pilot with `not_run`; it does not contact a model or score a result.
4. Create a JSON observation containing the string fields `case_id`, `observation`, `evidence` and `interpretation`; use `fictional-pilot-01` as the case ID. Run the same command with `--record /path/to/observation.json`. This appends a dated manual record to this folder's local `observations.jsonl`; it does not certify correctness.
5. Replace or extend `experiment.py` when you choose an actual method. Record dependencies, API costs and model/data versions at that point. Do not commit secrets or private institutional records.

For an upstream checkout later, use a separate local directory, retain its licence/notices and record the revision above. No dependency is installed and no upstream program runs automatically. Public access and permission to reuse are separate checks, particularly where no licence was identified.

[Collection index](../../README.md) · [Hand annotations](NOTES.md) · [Starter code](experiment.py) · [Manifest and pilot](project.json)

<!-- research-dossier-link:start -->
## Research, engineering and explanation

[Editable research dossier](RESEARCH.md) · [Online workbench and demo](https://manifoldgrace.github.io/research-project.html?project=company-gap-4) · [Visual roadmap source](ROADMAP.mmd) · [Milestones](milestones.csv) · [Claim-to-evidence register](evidence.csv). The shared [methodological guide](../../RESEARCH-GUIDE.md) defines the structure; this project keeps its own analysis, observations and contributions.
<!-- research-dossier-link:end -->

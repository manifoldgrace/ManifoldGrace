# Evidence integrity, provenance and dependent revision

Grace R. Nettey's separate learning workspace, created 2026-11-05. **Starter setup; no research experiment has been run.** This folder is ready for hand annotations and code changes. The research narrative stays on the [existing project entry](https://manifoldgrace.github.io/emerging-horizon-research.html#avenue-evidence).

## Source code to explore

- [Accessible source code](https://github.com/trungdong/prov/tree/ff97842dfc03906f888d33d9760bc64e15f32d29/src) · [upstream repository](https://github.com/trungdong/prov)
- Checked revision: `ff97842dfc03906f888d33d9760bc64e15f32d29` (default branch `main` at setup).
- Scope: W3C PROV implementation; lineage representation does not itself establish truth or propagate every model inference.
- [Licence / repository terms](https://github.com/trungdong/prov/blob/ff97842dfc03906f888d33d9760bc64e15f32d29/LICENSE): MIT.

This workspace starts from scratch. No upstream code, model weights, datasets or credentials have been copied. An SDK does not expose a provider's proprietary service. This source is a possible starting point, not proof that the feature gap has been solved or that it exactly reproduces a cited paper. Check per-file/data/model terms before importing material. Keep an imported revision, its licence and your changes distinguishable.

## First bounded investigation

Fictional pilot: R1 supports C1 which supports C2; correction R2 supersedes R1 while unrelated C3 stays fixed.

Observation checks: Tracks lineage and supersession; marks dependent conclusions for review; preserves unrelated control.

Add at least one unaffected control and one competing explanation before comparing runs. `project.json` holds the pilot and source manifest; edit `NOTES.md` for your own questions, reading notes and contribution record. Model behaviour, evidence validity and explanations should be recorded separately.

## Start tinkering

1. Clone your collection: `git clone https://github.com/manifoldgrace/ManifoldGrace.git`.
2. Open `learning-projects/avenues/evidence-revision/` and edit `NOTES.md` or `experiment.py`.
3. From the repository root run `python learning-projects/avenues/evidence-revision/experiment.py`. Python 3.10+ and the standard library are sufficient. It prints the planned pilot with `not_run`; it does not contact a model or score a result.
4. Create a JSON observation containing the string fields `case_id`, `observation`, `evidence` and `interpretation`; use `fictional-pilot-01` as the case ID. Run the same command with `--record /path/to/observation.json`. This appends a dated manual record to this folder's local `observations.jsonl`; it does not certify correctness.
5. Replace or extend `experiment.py` when you choose an actual method. Record dependencies, API costs and model/data versions at that point. Do not commit secrets or private institutional records.

For an upstream checkout later, use a separate local directory, retain its licence/notices and record the revision above. No dependency is installed and no upstream program runs automatically. Public access and permission to reuse are separate checks, particularly where no licence was identified.

[Collection index](../../README.md) · [Hand annotations](NOTES.md) · [Starter code](experiment.py) · [Manifest and pilot](project.json)

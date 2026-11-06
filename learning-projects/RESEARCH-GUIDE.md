# Evidence-led research and engineering case studies

Grace R. Nettey's framework for learning, technical investigation and public explanation across the 39 Manifold Grace projects. Prepared with AI assistance on 6 November 2026 for Grace to revise, annotate and develop. This is an adaptable research structure, not a claim of doctoral accreditation, completed experiments or verified originality.

The intended outcome is a defensible understanding of how a system was developed, what its code and interfaces do, how an alternative can be tested, and what the resulting evidence contributes to engineering and society. Depth should follow the question and available resources; a bounded, reproducible finding is more defensible than an unsupported claim of exhaustive coverage.

## Four connected outputs

1. **Research account:** historical lineage, theory, methodological choices, evidence, interpretation and limits.
2. **Annotated engineering artefact:** readable implementation, architecture, experiments and reproducibility instructions.
3. **Educational demonstration:** visual explanation or runnable example whose boundaries are explicit.
4. **Versioned handoff:** reviewed report/code/figures, provenance, accessibility, contribution record and release notes.

## Case-study sections

### 1. Research question, scope and contribution

Define the problem, unit of analysis, intended audience, terms, exclusions and success criteria. State whether the work is exploratory, replication, evaluation, extension or a combination. Record why the question matters and what would count against the proposed answer.

### 2. Historical development and primary evidence

Trace dated milestones through original papers, repositories, releases, design records and originator links. Distinguish first proposal, implementation, release and later interpretation. Attribute documented rationales; label your own reconstruction of why a choice was made as an inference and consider alternatives.

### 3. Source-code inspection and annotated implementation

Record the exact revision, relevant files/functions, dependencies, licences and the path from input to output. Annotate what each important component does, its assumptions and limits. Separate upstream code, your changes, original code and AI assistance. Do not equate an SDK with the proprietary service it accesses.

### 4. Scientific framing and evaluation design

Define constructs, hypotheses or exploratory questions, operational measures and competing explanations. Specify case selection, controls, baselines, interventions, sampling, repetition/seeds where applicable, budgets and uncertainty. Address construct, internal, external and ecological validity. Separate pre-specified tests from post-hoc exploration and statistical significance from practical importance.

### 5. Architecture, interfaces and execution environment

Draw components, data flows, protocols, trust boundaries, state, storage and dependencies. Distinguish observed architecture from proposed designs and unknown internals. Identify where computation runs: browser, local Python, remote API, cloud CPU/GPU or simulator. Discuss latency, memory, cost, access and failure recovery. Include Infrastructure as Code (IaC) or unified communications only where genuinely relevant.

### 6. Comparative design and original contribution

Compare the upstream baseline with your replication, alternative or extension using matched conditions and explicit differences. Explain design choices and trade-offs. Candidate contribution may be a method, negative result, dataset, diagnostic, implementation, synthesis or collaboration; originality remains a claim to investigate through prior-art checking, not an automatic property of hand-written text.

### 7. Implementation and reproducibility

Record environment/dependency versions, setup commands, fictional or authorised data, configuration, deterministic checks and model/API details. Preserve raw inputs/outputs and versioned transformations. Provide a small reproducible example; distinguish a visual demonstration, mock, offline test and live integration. Document changes and rollback/recovery steps.

### 8. Observations, failures and uncertainty

Report observations and failures with denominators, configurations, exceptions, missing runs and relevant uncertainty. Link each claim to raw evidence and scoring rules. Separate observed behaviour from inferred mechanisms, anecdote from repeated findings and tool/harness errors from model failures. Include null and negative results; never invent a chart or completed run.

### 9. Ethical, societal and governance analysis

Consider affected groups, access, power, labour, cultural context, privacy, consent, distribution of benefits/harms and routes of challenge. Explain the ethical or sociotechnical framework used and its limitations. Assess the selected system/version at its evidenced lifecycle stage rather than assuming a universal AI maturity level. Separate normative recommendations from empirical findings.

### 10. Quality assurance, security and the SDLC

Select proportionate checks across requirements, design, implementation, testing, integration, deployment and maintenance. Distinguish scientific evaluation from unit/integration/regression, adversarial, accessibility and user-acceptance testing. Record threat models, permissions, secrets, dependencies, data handling, human review, CI/CD gates and rollback. A check passed or framework referenced is not certification or a guarantee of safety.

### 11. End-to-end plan, milestones and decisions

Map the route from question and literature/code inspection to design, implementation, evaluation, interpretation, review and handoff. For each milestone specify deliverable, acceptance evidence, dependencies, resource budget and next action. Revisit earlier stages when findings change the question. Mark actual versus planned completion explicitly.

### 12. Illustrations, architecture and educational explanation

Use architecture/sequence diagrams for relationships, charts for measured results and annotated screenshots for observed behaviour. Provide captions, legends, units, uncertainty, alt text, source/version and creation method. Keep conceptual illustrations separate from empirical evidence. Pinterest is a discovery lead: locate the original source and reuse permission before uploading an image; record attribution and AI generation where applicable.

### 13. Interpretation, contribution and limitations

Answer the bounded research question at the strength supported by the evidence. Explain what the approach adds, changes or enables, where the baseline remains better and what remains unresolved. Relate conclusions to theories and terminology accurately. Separate demonstrated improvement, suggestive evidence, design proposal and future hypothesis; state limitations and a practical next investigation.

### 14. Accessible handoff, research release and dissemination

Prepare a versioned package of report, code, permitted data/fixtures, figures, environment/run instructions, licence/attribution, limitations, contribution record and change log. Record accessibility review, evidence checks and reproducibility status. Decide whether it is a working note, technical report, preprint, software release or dataset. A public release is not peer review. Link an exact commit/tag and, if actually deposited, a version-specific persistent identifier. Draft originator feedback separately; do not infer receipt, collaboration or endorsement from sending it.

## Evidence and attribution conventions

Use a claim-to-evidence table: claim; source/artifact; date/version; method of checking; contrary evidence; uncertainty; interpretation. A source being accessible is not the same as the claim being established. Distinguish an originator's explicit design rationale from your plausible explanation. A new implementation is not necessarily a new scientific result; a well-designed replication or negative result can still contribute useful knowledge.

For the comparison, distinguish: reproduced baseline; your altered variable; matched conditions; observed difference; uncertainty; practical consequence; unresolved prior art. Trace conceptual, empirical, software and collaborative contributions separately. Editing an AI draft by hand supports authorship of the revision but does not by itself establish novelty or factual correctness.

## Demonstration and runtime boundaries

The site's workbench executes edited HTML/CSS/JavaScript in a sandboxed browser frame. It can show interface behaviour and fictional fixtures immediately. It does not execute Python, host a GPU, call a frontier model, integrate installed apps or validate scientific claims. Python experiments can run locally; model/API integrations require a deliberately configured backend or permitted local model. Secrets belong on the backend. Infrastructure as Code means versioned infrastructure configuration; unified communications concerns voice/video/messaging integrations and is optional.

Browser drafts are stored on the current browser/device when storage is available. They are not synced back to GitHub or the public site. Export a draft before clearing browser data or switching devices; put reviewed text into the repository through its edit/commit workflow. Imported drafts are treated as text, and their demo code does not run until requested. Sandboxing and a restrictive content policy reduce exposure but are not a guarantee against malicious or resource-exhausting scripts; use code you understand.

## A research release in practice

A research release is a deliberately versioned, documented package that another person can inspect, cite and, where feasible, reproduce. Its form can be a technical report, working paper, software/data release or combined research artefact. A portfolio page explains the work; a release fixes the specific evidence and artefacts behind that explanation. Neither a GitHub release nor a DOI establishes peer review or scientific validity.

Before release: reconcile claims with evidence; retain failures and limitations; record exact code/data/model versions and run instructions; check licences, privacy, accessibility and attribution; add release notes and citation metadata; state the scope of any independent review. Use a repository tag/commit for the software version. An archival deposit is optional; if actually made, cite the deposited version's identifier. Keep later corrections and versions discoverable. No tags, DOI deposits, emails or portal submissions are created by this framework setup.

Primary starting points checked 6 November 2026:
- [NIST SSDF 1.1, SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final): secure practices integrated into the SDLC; a methodological reference, not a certification claim.
- [GitHub citation files](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files): root `CITATION.cff` metadata and the repository citation interface. Folder-level records in this collection do not each gain a separate GitHub citation widget.
- [Zenodo version management](https://help.zenodo.org/docs/deposit/manage-versions/): new record versions retain linked histories and separate persistent identifiers.
- [MDN iframe reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe): sandbox and embedded-document behaviour.

## Current setup and authorship

All dossiers begin as editable plans. The pre-existing source manifests and offline experiment starters remain unchanged. No history has been retrospectively invented, no project is marked scientifically evaluated, and no improvement or original discovery is asserted. Grace sets the questions, conducts/reviews the work and makes the final evidential claims; AI-generated prompts and scaffolds should remain identifiable in the contribution record.

"""Shared offline notebook helper; records manual evidence, never model results by implication."""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

def main(project_dir=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, help="Project folder, when using this helper directly")
    parser.add_argument("--record", type=Path, help="JSON manual observation to validate and append")
    parser.add_argument("--output", type=Path, help="Optional alternate JSONL destination")
    args = parser.parse_args()
    folder = project_dir or args.project
    if folder is None:
        parser.error("Pass --project or run a project's experiment.py")
    project = json.loads((Path(folder) / "project.json").read_text())
    if args.record is None:
        print(json.dumps({"project": project["title"], "status": "not_run", "pilot": project["pilot"]}, indent=2))
        return
    try:
        record = json.loads(args.record.read_text())
        if not isinstance(record, dict):
            raise ValueError("observation must be a JSON object")
        for key in ("case_id", "observation", "evidence", "interpretation"):
            if not isinstance(record.get(key), str) or not record[key].strip():
                raise ValueError(key + " must be a nonempty string")
        if record["case_id"] != project["pilot"]["id"]:
            raise ValueError("case_id is not the declared pilot; update project.json deliberately first")
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    envelope = {"recorded_at": datetime.now(timezone.utc).isoformat(), "project_id": project["id"],
                "record_type": "manual_observation_not_independent_validation", "data": record}
    destination = args.output or Path(folder) / "observations.jsonl"
    with destination.open("a", encoding="utf-8") as stream:
        stream.write(json.dumps(envelope, ensure_ascii=False) + "\n")
    print("Manual observation recorded: " + str(destination))

if __name__ == "__main__":
    main(globals().get("PROJECT_DIR"))

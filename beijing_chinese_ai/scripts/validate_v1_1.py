"""Validate the frozen P0-2 data contract for Beijing Chinese AI."""

from __future__ import annotations

import json
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

try:
    from jsonschema import Draft202012Validator, FormatChecker
    from jsonschema.exceptions import SchemaError
except ImportError as exc:  # pragma: no cover - exercised only on a broken runtime
    raise SystemExit(
        "FAIL: jsonschema is required to validate the frozen JSON Schema contracts."
    ) from exc


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = PROJECT_ROOT / "schemas"
MASTER_DIR = PROJECT_ROOT / "data" / "master"
CATALOG_PATH = MASTER_DIR / "ability_catalog.v1.1.json"
VERSION_PATH = MASTER_DIR / "master_data_version.json"

FROZEN_ABILITY_IDS = [
    *(f"BA{i:02d}" for i in range(1, 5)),
    *(f"LU{i:02d}" for i in range(1, 5)),
    *(f"RD{i:02d}" for i in range(1, 9)),
    *(f"CL{i:02d}" for i in range(1, 5)),
    *(f"PO{i:02d}" for i in range(1, 5)),
    *(f"WR{i:02d}" for i in range(1, 7)),
    *(f"OC{i:02d}" for i in range(1, 4)),
    *(f"MC{i:02d}" for i in range(1, 4)),
    *(f"WB{i:02d}" for i in range(1, 4)),
]
FROZEN_ID_SET = set(FROZEN_ABILITY_IDS)
OPERATIONAL_DOMAINS = {"BA", "LU", "RD", "CL", "PO", "WR", "OC", "MC"}
ALL_DOMAINS = OPERATIONAL_DOMAINS | {"WB"}
ABILITY_REFERENCE_KEYS = {
    "ability_id",
    "ability_ids",
    "target_ability_ids",
    "next_review_ability_ids",
    "primary_ability_id",
    "secondary_ability_ids",
}


@dataclass(frozen=True)
class CheckResult:
    code: str
    name: str
    passed: bool
    detail: str


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8-sig") as stream:
        return json.load(stream)


def schema_validation_errors(instance: Any, schema: dict[str, Any]) -> list[str]:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [
        f"{'.'.join(str(part) for part in error.absolute_path) or '<root>'}: {error.message}"
        for error in sorted(validator.iter_errors(instance), key=lambda item: list(item.absolute_path))
    ]


def expected_domain(ability_id: str) -> str | None:
    if isinstance(ability_id, str) and len(ability_id) >= 2:
        prefix = ability_id[:2]
        if prefix in ALL_DOMAINS:
            return prefix
    return None


def validate_catalog(catalog: Any, schema: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if not isinstance(catalog, list):
        return ["ability_catalog must be a JSON array"]

    ids = [item.get("ability_id") for item in catalog if isinstance(item, dict)]
    if len(catalog) != 39:
        errors.append(f"ability count must be 39, got {len(catalog)}")
    if set(ids) != FROZEN_ID_SET:
        missing = sorted(FROZEN_ID_SET - set(ids))
        extra = sorted(set(ids) - FROZEN_ID_SET)
        errors.append(f"frozen ID mismatch; missing={missing}, extra={extra}")
    duplicates = sorted(ability_id for ability_id, count in Counter(ids).items() if count > 1)
    if duplicates:
        errors.append(f"duplicate ability_id values: {duplicates}")

    for index, item in enumerate(catalog):
        if not isinstance(item, dict):
            errors.append(f"catalog[{index}] is not an object")
            continue
        ability_id = item.get("ability_id")
        domain = item.get("domain_code")
        architecture = item.get("architecture_type")
        required_domain = expected_domain(ability_id)
        if domain != required_domain:
            errors.append(
                f"{ability_id}: domain_code must be {required_domain!r}, got {domain!r}"
            )
        required_architecture = (
            "cross_domain_module" if domain == "WB" else "operational_domain"
        )
        if architecture != required_architecture:
            errors.append(
                f"{ability_id}: architecture_type must be {required_architecture!r}, "
                f"got {architecture!r}"
            )

    errors.extend(f"schema: {message}" for message in schema_validation_errors(catalog, schema))
    return errors


def iter_ability_references(value: Any, path: str = "<root>") -> Iterable[tuple[str, str]]:
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}"
            if key in ABILITY_REFERENCE_KEYS:
                candidates = child if isinstance(child, list) else [child]
                for candidate in candidates:
                    if isinstance(candidate, str):
                        yield child_path, candidate
            yield from iter_ability_references(child, child_path)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from iter_ability_references(child, f"{path}[{index}]")


def validate_ability_references(documents: Iterable[Any], valid_ids: set[str]) -> list[str]:
    errors: list[str] = []
    for document_index, document in enumerate(documents):
        for location, ability_id in iter_ability_references(
            document, f"document[{document_index}]"
        ):
            if ability_id not in valid_ids:
                errors.append(f"{location}: unknown ability_id {ability_id!r}")
    return errors


def _flatten_records(value: Any) -> Iterable[dict[str, Any]]:
    if isinstance(value, dict):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from _flatten_records(item)


def validate_state_initialization(
    profiles: Iterable[dict[str, Any]],
    skill_states: Iterable[dict[str, Any]],
    learning_events: Iterable[dict[str, Any]],
) -> list[str]:
    errors: list[str] = []
    profile_by_student = {
        item.get("student_id"): item
        for item in profiles
        if isinstance(item.get("student_id"), str)
    }
    evidence_pairs: set[tuple[str, str]] = set()
    for event in learning_events:
        student_id = event.get("student_id")
        for ability_id in event.get("ability_ids", []):
            if isinstance(student_id, str) and isinstance(ability_id, str):
                evidence_pairs.add((student_id, ability_id))

    for state in skill_states:
        student_id = state.get("student_id")
        ability_id = state.get("ability_id")
        pair = (student_id, ability_id)
        profile = profile_by_student.get(student_id)
        if profile is None:
            errors.append(f"{student_id}/{ability_id}: missing student_profile")
        elif profile.get("baseline_status") == "unknown":
            errors.append(
                f"{student_id}/{ability_id}: baseline_status=unknown cannot have skill_state"
            )
        if state.get("evidence_count", 0) < 1:
            errors.append(f"{student_id}/{ability_id}: evidence_count must be at least 1")
        if pair not in evidence_pairs:
            errors.append(
                f"{student_id}/{ability_id}: skill_state has no matching learning_event"
            )
    return errors


def _runtime_json_paths(project_root: Path) -> list[Path]:
    paths: list[Path] = []
    for relative in ("data/students", "data/tasks", "data/sessions", "data/examples"):
        folder = project_root / relative
        if folder.exists():
            paths.extend(sorted(folder.rglob("*.json")))
    return paths


def run_project_validation(project_root: Path = PROJECT_ROOT) -> list[CheckResult]:
    schema_dir = project_root / "schemas"
    master_dir = project_root / "data" / "master"
    catalog_path = master_dir / "ability_catalog.v1.1.json"
    version_path = master_dir / "master_data_version.json"
    ability_schema_path = schema_dir / "ability_catalog.schema.json"

    catalog = load_json(catalog_path) if catalog_path.exists() else None
    ability_schema = load_json(ability_schema_path) if ability_schema_path.exists() else {}
    ids = [item.get("ability_id") for item in catalog or [] if isinstance(item, dict)]

    results: list[CheckResult] = []
    results.append(CheckResult("A", "ability_catalog exists", catalog_path.exists(), str(catalog_path)))
    results.append(
        CheckResult("B", "ability count is 39", isinstance(catalog, list) and len(catalog) == 39, f"count={len(catalog) if isinstance(catalog, list) else 'invalid'}")
    )
    results.append(
        CheckResult("C", "IDs equal frozen list", set(ids) == FROZEN_ID_SET and len(ids) == 39, f"unique={len(set(ids))}")
    )
    duplicates = sorted(key for key, count in Counter(ids).items() if count > 1)
    results.append(CheckResult("D", "no duplicate ability_id", not duplicates, f"duplicates={duplicates}"))

    domain_errors = [
        item.get("ability_id")
        for item in catalog or []
        if isinstance(item, dict) and item.get("domain_code") != expected_domain(item.get("ability_id"))
    ]
    results.append(CheckResult("E", "domain_code matches ability_id", not domain_errors, f"errors={domain_errors}"))

    architecture_errors = [
        item.get("ability_id")
        for item in catalog or []
        if isinstance(item, dict)
        and item.get("architecture_type")
        != ("cross_domain_module" if item.get("domain_code") == "WB" else "operational_domain")
    ]
    results.append(CheckResult("F", "architecture_type is correct", not architecture_errors, f"errors={architecture_errors}"))
    wb_errors = [
        item.get("ability_id")
        for item in catalog or []
        if isinstance(item, dict)
        and item.get("domain_code") == "WB"
        and item.get("architecture_type") != "cross_domain_module"
    ]
    results.append(CheckResult("G", "WB is cross_domain_module", not wb_errors, f"errors={wb_errors}"))
    operational_errors = [
        item.get("ability_id")
        for item in catalog or []
        if isinstance(item, dict)
        and item.get("domain_code") in OPERATIONAL_DOMAINS
        and item.get("architecture_type") != "operational_domain"
    ]
    results.append(CheckResult("H", "other domains are operational_domain", not operational_errors, f"errors={operational_errors}"))

    schema_errors: list[str] = []
    schema_paths = sorted(schema_dir.glob("*.schema.json"))
    for path in schema_paths:
        try:
            schema = load_json(path)
            Draft202012Validator.check_schema(schema)
        except (json.JSONDecodeError, OSError, SchemaError) as exc:
            schema_errors.append(f"{path.name}: {exc}")
    results.append(CheckResult("I", "all JSON Schemas are valid", len(schema_paths) == 9 and not schema_errors, f"schemas={len(schema_paths)}, errors={schema_errors}"))

    catalog_schema_errors = (
        validate_catalog(catalog, ability_schema)
        if catalog is not None and ability_schema
        else ["catalog or schema missing"]
    )
    results.append(CheckResult("J", "ability_catalog passes schema", not catalog_schema_errors, f"errors={catalog_schema_errors}"))

    documents: list[Any] = []
    load_errors: list[str] = []
    for path in sorted(master_dir.glob("*.json")) + _runtime_json_paths(project_root):
        if path in {catalog_path, version_path}:
            continue
        try:
            documents.append(load_json(path))
        except (json.JSONDecodeError, OSError) as exc:
            load_errors.append(f"{path}: {exc}")
    reference_errors = load_errors + validate_ability_references(documents, FROZEN_ID_SET)
    results.append(CheckResult("K", "cross-table ability references are valid", not reference_errors, f"errors={reference_errors}"))

    student_schema_path = schema_dir / "student_profile.schema.json"
    student_schema = load_json(student_schema_path) if student_schema_path.exists() else {}
    student_props = student_schema.get("properties", {})
    student_pattern = student_props.get("student_id", {}).get("pattern", "")
    privacy_ok = (
        student_schema.get("additionalProperties") is False
        and "real_name" not in student_props
        and student_pattern.startswith("^STU-")
    )
    results.append(CheckResult("L", "student_id is pseudonymized by contract", privacy_ok, f"pattern={student_pattern!r}"))

    baseline_schema = student_props.get("baseline_status", {})
    baseline_ok = (
        "unknown" in baseline_schema.get("enum", [])
        and baseline_schema.get("default") == "unknown"
    )
    results.append(CheckResult("M", "baseline_status allows and defaults to unknown", baseline_ok, str(baseline_schema)))

    runtime_records: list[dict[str, Any]] = []
    for document in documents:
        runtime_records.extend(_flatten_records(document))
    profiles = [item for item in runtime_records if "baseline_status" in item]
    states = [item for item in runtime_records if "skill_state" in item]
    events = [item for item in runtime_records if "event_id" in item and "ability_ids" in item]
    state_errors = validate_state_initialization(profiles, states, events)
    skill_schema = load_json(schema_dir / "skill_state.schema.json")
    minimum = skill_schema.get("properties", {}).get("evidence_count", {}).get("minimum")
    no_unknown_to_s0 = minimum == 1 and not state_errors
    results.append(CheckResult("N", "unknown cannot initialize S0", no_unknown_to_s0, f"runtime_errors={state_errors}, evidence_minimum={minimum}"))

    version_ok = False
    version_detail = "missing"
    if version_path.exists():
        try:
            version = load_json(version_path)
            policy = version.get("breaking_change_policy", "")
            version_ok = all(
                key in version
                for key in (
                    "schema_version",
                    "ability_catalog_version",
                    "created_at",
                    "status",
                    "breaking_change_policy",
                )
            ) and "永久主键" in policy and "不得" in policy
            version_detail = f"status={version.get('status')}, catalog={version.get('ability_catalog_version')}"
        except (json.JSONDecodeError, OSError) as exc:
            version_detail = str(exc)
    results.append(CheckResult("O", "master_data_version exists and freezes IDs", version_ok, version_detail))
    return results


def main() -> int:
    results = run_project_validation()
    for result in results:
        label = "PASS" if result.passed else "FAIL"
        print(f"[{label}] {result.code}. {result.name}: {result.detail}")
    passed = all(result.passed for result in results)
    print(f"\nP0-2 DATA CONTRACT VALIDATION: {'PASS' if passed else 'FAIL'}")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())

"""Validate the P0-3B human definition decisions and draft catalog."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
V11_PATH = PROJECT_ROOT / "data/master/ability_catalog.v1.1.json"
MASTER_VERSION_PATH = PROJECT_ROOT / "data/master/master_data_version.json"
DRAFT_PATH = PROJECT_ROOT / "data/master/_draft/ability_catalog.v1.2.candidate.json"
DECISIONS_PATH = PROJECT_ROOT / "data/master/_draft/definition_review_decisions.v1.0.json"
REVIEW_PATH = PROJECT_ROOT / "docs/acceptance/P0-3A_17_DEFINITION_REVIEW.md"

EXPECTED_V11_SHA256 = "A8C0031EE5DE5A30F3CC4C98AF0BAB030C25DBF1DE0CC7F93DD4DF466CBD6EDC"
EXPECTED_MASTER_VERSION_SHA256 = "F6AF22EF484DB0EF154DC45FEF787611E2A550800242526A27CB922372ABBF62"

APPROVE_AS_IS_IDS = {
    "CL02",
    "PO02",
    "PO04",
    "WR02",
    "WR04",
    "WR05",
    "OC01",
    "OC02",
    "MC01",
    "MC03",
}

REVISED_DEFINITIONS = {
    "CL04": "能够在文言文本中依据人物事件、因果关系和原文证据，解释内容主旨、人物态度或作者立场，并在陌生文言文本中独立完成同类理解与评价。",
    "PO01": "能够依据语意处理古诗词的朗读节奏，并结合关键字词、景物、动作和时空信息复原基本情境，建构连贯画面。",
    "PO03": "能够结合诗词语境，辨析关键字词或表达手法形成的具体意义，并解释其对整体表达和审美效果的作用。",
    "WR03": "能够依据写作目的和立意，选择、取舍真实、相关、具体且有代表性的素材与细节，并说明其对中心的支撑作用。",
    "WR06": "能够提出并限定观点，选择、核验和解释相关证据，形成回应反例与条件限制的论证，并在写作与修订中对事实准确性和原创表达承担责任。",
    "OC03": "能够围绕真实问题设计检索或调查，识别并交叉核验原始来源，采集、整合和解释信息或数据，说明其偏差、不确定性与适用边界，并形成可追溯的跨学科成果进行呈现和答辩。",
    "MC02": "能够监控自己的理解与作答过程，依据初答、证据和反馈定位信息、证据、推理或表达等主要错因，并据此自主修订和调整策略。",
}

DECISION_IDS = APPROVE_AS_IS_IDS | set(REVISED_DEFINITIONS)


@dataclass(frozen=True)
class Check:
    number: int
    name: str
    passed: bool
    detail: str


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8-sig") as stream:
        return json.load(stream)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def by_id(records: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {record["ability_id"]: record for record in records}


def extract_review_definitions() -> dict[str, str]:
    text = REVIEW_PATH.read_text(encoding="utf-8-sig")
    definitions: dict[str, str] = {}
    for ability_id in DECISION_IDS:
        pattern = re.compile(
            rf"(?ms)^## {re.escape(ability_id)} .*?^- 候选 definition：\*\*(.*?)\*\*"
        )
        match = pattern.search(text)
        if match:
            definitions[ability_id] = match.group(1).strip()
    return definitions


def main() -> int:
    v11 = load_json(V11_PATH)
    draft = load_json(DRAFT_PATH)
    decisions = load_json(DECISIONS_PATH)
    review_definitions = extract_review_definitions()

    v11_ids = [item["ability_id"] for item in v11]
    draft_ids = [item["ability_id"] for item in draft]
    v11_map = by_id(v11)
    draft_map = by_id(draft)
    null_ids = {item["ability_id"] for item in v11 if item["definition"] is None}
    original_ids = set(v11_ids) - null_ids

    checks: list[Check] = []
    checks.append(Check(1, "candidate catalog has 39 abilities", len(draft) == 39, f"count={len(draft)}"))
    checks.append(Check(2, "candidate IDs exactly match v1.1", draft_ids == v11_ids, f"ids={len(draft_ids)}"))
    duplicates = sorted(key for key, count in Counter(draft_ids).items() if count > 1)
    checks.append(Check(3, "candidate has no duplicate IDs", not duplicates, f"duplicates={duplicates}"))

    filled = sorted(ability_id for ability_id in null_ids if draft_map[ability_id]["definition"] is not None)
    checks.append(Check(4, "all 17 former null definitions are filled", len(null_ids) == 17 and len(filled) == 17, f"filled={len(filled)}/17"))

    changed_originals = sorted(
        ability_id
        for ability_id in original_ids
        if draft_map[ability_id]["definition"] != v11_map[ability_id]["definition"]
    )
    checks.append(Check(5, "22 original definitions are byte-for-byte equal as strings", len(original_ids) == 22 and not changed_originals, f"changed={changed_originals}"))

    as_is_errors = sorted(
        ability_id
        for ability_id in APPROVE_AS_IS_IDS
        if draft_map[ability_id]["definition"] != review_definitions.get(ability_id)
    )
    checks.append(Check(6, "10 APPROVE_AS_IS definitions equal P0-3A review", len(review_definitions) == 17 and not as_is_errors, f"errors={as_is_errors}"))

    revised_errors = sorted(
        ability_id
        for ability_id, expected in REVISED_DEFINITIONS.items()
        if draft_map[ability_id]["definition"] != expected
    )
    checks.append(Check(7, "7 revised definitions exactly equal human text", not revised_errors, f"errors={revised_errors}"))

    decision_ids = [item.get("ability_id") for item in decisions]
    required_fields = {
        "ability_id",
        "original_definition",
        "candidate_definition",
        "approved_definition",
        "human_decision",
        "decision_type",
        "keep_needs_review",
        "reviewer_role",
        "reviewed_at",
        "review_notes",
    }
    structural_errors = [
        item.get("ability_id")
        for item in decisions
        if set(item) != required_fields
        or item.get("original_definition") is not None
        or not item.get("review_notes")
        or item.get("candidate_definition") != review_definitions.get(item.get("ability_id"))
        or item.get("approved_definition") != draft_map.get(item.get("ability_id"), {}).get("definition")
        or item.get("reviewer_role") != "project_owner_review"
        or item.get("reviewed_at") != "2026-08-17"
    ]
    decisions_ok = (
        len(decisions) == 17
        and set(decision_ids) == DECISION_IDS
        and len(set(decision_ids)) == 17
        and not structural_errors
    )
    checks.append(Check(8, "machine-readable decision file has 17 valid records", decisions_ok, f"errors={structural_errors}"))

    human_errors = sorted(item.get("ability_id") for item in decisions if item.get("human_decision") != "APPROVE")
    checks.append(Check(9, "all human_decision values are APPROVE", not human_errors, f"errors={human_errors}"))

    decision_counts = Counter(item.get("decision_type") for item in decisions)
    decision_types_ok = decision_counts == Counter({"APPROVE_AS_IS": 10, "REVISE_AND_APPROVE": 7})
    per_id_type_ok = all(
        item.get("decision_type")
        == ("APPROVE_AS_IS" if item.get("ability_id") in APPROVE_AS_IS_IDS else "REVISE_AND_APPROVE")
        for item in decisions
    )
    checks.append(Check(10, "decision types are exactly 10 + 7", decision_types_ok and per_id_type_ok, str(dict(decision_counts))))

    keep_errors = sorted(item.get("ability_id") for item in decisions if item.get("keep_needs_review") is not True)
    checks.append(Check(11, "all decisions keep needs_review", not keep_errors, f"errors={keep_errors}"))

    draft_review_errors = sorted(item["ability_id"] for item in draft if item.get("needs_review") is not True)
    checks.append(Check(12, "all 39 candidate records keep needs_review=true", not draft_review_errors, f"errors={draft_review_errors}"))

    assessment_changes = sorted(
        ability_id
        for ability_id in v11_ids
        if draft_map[ability_id].get("assessment_focus") != v11_map[ability_id].get("assessment_focus")
    )
    checks.append(Check(13, "assessment_focus is unchanged", not assessment_changes, f"changes={assessment_changes}"))

    evidence_changes = sorted(
        ability_id
        for ability_id in v11_ids
        if draft_map[ability_id].get("evidence_requirements") != v11_map[ability_id].get("evidence_requirements")
    )
    checks.append(Check(14, "evidence_requirements is unchanged", not evidence_changes, f"changes={evidence_changes}"))

    v11_hash = sha256(V11_PATH)
    checks.append(Check(15, "formal ability_catalog.v1.1.json hash is unchanged", v11_hash == EXPECTED_V11_SHA256, v11_hash))

    version_hash = sha256(MASTER_VERSION_PATH)
    checks.append(Check(16, "master_data_version.json hash is unchanged", version_hash == EXPECTED_MASTER_VERSION_SHA256, version_hash))

    private_files = sorted(
        str(path.relative_to(PROJECT_ROOT))
        for path in (PROJECT_ROOT / "data/students").rglob("*")
        if path.is_file() and path.name != ".gitkeep"
    )
    checks.append(Check(17, "no real student data was created", not private_files, f"files={private_files}"))

    immutable_changes: list[str] = []
    for ability_id in v11_ids:
        original = {key: value for key, value in v11_map[ability_id].items() if key != "definition"}
        candidate = {key: value for key, value in draft_map[ability_id].items() if key != "definition"}
        if original != candidate:
            immutable_changes.append(ability_id)
    checks.append(Check(18, "all non-definition fields are unchanged", not immutable_changes, f"changes={immutable_changes}"))

    for check in checks:
        status = "PASS" if check.passed else "FAIL"
        print(f"[{status}] {check.number}. {check.name}: {check.detail}")

    passed = all(check.passed for check in checks)
    print(f"\nP0-3B DEFINITION DECISIONS VALIDATION: {'PASS' if passed else 'FAIL'}")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())

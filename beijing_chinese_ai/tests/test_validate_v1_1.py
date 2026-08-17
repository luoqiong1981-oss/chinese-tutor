from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from validate_v1_1 import (  # noqa: E402
    FROZEN_ID_SET,
    load_json,
    validate_ability_references,
    validate_catalog,
    validate_state_initialization,
)


class ValidateV11Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.catalog = load_json(PROJECT_ROOT / "data/master/ability_catalog.v1.1.json")
        cls.catalog_schema = load_json(PROJECT_ROOT / "schemas/ability_catalog.schema.json")
        cls.student_schema = load_json(PROJECT_ROOT / "schemas/student_profile.schema.json")
        cls.skill_schema = load_json(PROJECT_ROOT / "schemas/skill_state.schema.json")
        cls.fixture_dir = PROJECT_ROOT / "tests/fixtures"

    def test_01_all_39_abilities_exist(self) -> None:
        self.assertEqual(39, len(self.catalog))
        self.assertEqual(FROZEN_ID_SET, {item["ability_id"] for item in self.catalog})
        self.assertEqual([], validate_catalog(self.catalog, self.catalog_schema))

    def test_02_removing_one_ability_fails(self) -> None:
        modified = copy.deepcopy(self.catalog[:-1])
        self.assertTrue(validate_catalog(modified, self.catalog_schema))

    def test_03_adding_fortieth_ability_fails(self) -> None:
        modified = copy.deepcopy(self.catalog)
        extra = copy.deepcopy(modified[-1])
        extra["ability_id"] = "ZZ99"
        extra["domain_code"] = "ZZ"
        modified.append(extra)
        self.assertTrue(validate_catalog(modified, self.catalog_schema))

    def test_04_duplicate_ability_id_fails(self) -> None:
        modified = copy.deepcopy(self.catalog)
        modified[1]["ability_id"] = modified[0]["ability_id"]
        self.assertTrue(validate_catalog(modified, self.catalog_schema))

    def test_05_wrong_wb_architecture_fails(self) -> None:
        modified = copy.deepcopy(self.catalog)
        wb = next(item for item in modified if item["ability_id"] == "WB01")
        wb["architecture_type"] = "operational_domain"
        self.assertTrue(validate_catalog(modified, self.catalog_schema))

    def test_06_rd_cannot_be_cross_domain_module(self) -> None:
        modified = copy.deepcopy(self.catalog)
        rd = next(item for item in modified if item["ability_id"] == "RD01")
        rd["architecture_type"] = "cross_domain_module"
        self.assertTrue(validate_catalog(modified, self.catalog_schema))

    def test_07_unknown_baseline_status_is_valid(self) -> None:
        profile = load_json(self.fixture_dir / "student_profile_unknown.json")
        errors = list(
            Draft202012Validator(
                self.student_schema, format_checker=FormatChecker()
            ).iter_errors(profile)
        )
        self.assertEqual([], errors)

    def test_08_untested_s0_initialization_fails(self) -> None:
        profile = load_json(self.fixture_dir / "student_profile_unknown.json")
        state = load_json(self.fixture_dir / "skill_state_untested_s0.json")
        state_schema_errors = list(
            Draft202012Validator(
                self.skill_schema, format_checker=FormatChecker()
            ).iter_errors(state)
        )
        rule_errors = validate_state_initialization([profile], [state], [])
        self.assertTrue(state_schema_errors)
        self.assertTrue(rule_errors)

    def test_09_unknown_cross_table_ability_reference_fails(self) -> None:
        invalid_document = {"ability_ids": ["RD01", "ZZ99"]}
        errors = validate_ability_references([invalid_document], FROZEN_ID_SET)
        self.assertTrue(errors)


if __name__ == "__main__":
    unittest.main()

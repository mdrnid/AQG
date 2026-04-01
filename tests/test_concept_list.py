"""
Tests untuk concept_list.py
"""
from src.dataset.concept_list import CONCEPTS, get_concepts_for_module, get_all_concepts


class TestConceptList:
    def test_all_modules_present(self):
        expected_modules = [
            "01-berkenalan-dengan-python",
            "02-berinteraksi-dengan-data",
            "03-ekspresi",
            "04-aksi-sekuensial",
            "05-control-flow",
            "06-array",
            "07-matriks",
            "08-subprogram",
            "09-oop",
            "10-style-guide",
            "11-unit-testing",
        ]
        for mod in expected_modules:
            assert mod in CONCEPTS, f"Modul '{mod}' tidak ada di CONCEPTS"

    def test_each_module_has_concepts(self):
        for module, concepts in CONCEPTS.items():
            assert len(concepts) > 0, f"Modul '{module}' tidak punya konsep"

    def test_get_concepts_for_module_returns_list(self):
        result = get_concepts_for_module("01-berkenalan-dengan-python")
        assert isinstance(result, list)
        assert len(result) > 0

    def test_get_concepts_for_unknown_module_returns_empty(self):
        result = get_concepts_for_module("99-tidak-ada")
        assert result == []

    def test_get_all_concepts_no_duplicates(self):
        all_concepts = get_all_concepts()
        assert len(all_concepts) == len(set(all_concepts)), "Ada duplikat di get_all_concepts()"

    def test_get_all_concepts_not_empty(self):
        assert len(get_all_concepts()) > 0

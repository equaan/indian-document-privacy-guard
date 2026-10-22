from app.modules.ner_engine import NEREngine, _is_valid_aadhaar
from app.modules.redaction_engine import RedactionEngine


def test_indian_pii_patterns_and_aadhaar_safeguard():
    engine = NEREngine(use_spacy=False)
    text = "PAN ABCDE1234F Mobile +91 9876543210 UPI student@okaxis Student ID CSE-2026-42 Aadhaar 234567890123"
    types = {entity.entity_type for entity in engine.detect_entities(text)}

    assert {"PAN_NUMBER", "PHONE", "UPI_ID", "STUDENT_ID"} <= types
    assert "AADHAAR" not in types
    assert not _is_valid_aadhaar("234567890123")


def test_export_metadata_never_contains_original_pii(tmp_path):
    output = tmp_path / "metadata.json"
    metadata = [{"original_text": "ABCDE1234F", "entity_type": "PAN_NUMBER"}]

    assert RedactionEngine().export_redacted("PAN: [PAN_NUMBER]", metadata, "json", str(output))
    assert "ABCDE1234F" not in output.read_text(encoding="utf-8")

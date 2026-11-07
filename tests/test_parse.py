import json
import pathlib
import sys
from datetime import datetime

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "app"))
from managebac import parse_classes, parse_tasks  # noqa: E402

HTML = (pathlib.Path(__file__).parent / "fixture_maths.html").read_text()
BASE = "https://theislandprivateschool.managebac.com"


def test_classes():
    cls = parse_classes(HTML)
    assert [c["id"] for c in cls] == ["13056535", "13062669", "13121264"]
    assert cls[0]["short"] == "Maths TLF"
    assert cls[1]["short"] == "Physical and health education (PHE)"
    assert cls[2]["short"] == "Wellbeing Miss Anna"


def test_tasks():
    c = parse_classes(HTML)[0]
    res = parse_tasks(HTML, c, BASE, today=datetime(2026, 11, 7))
    t = {x["title"]: x for x in res["tasks"]}
    assert len(res["tasks"]) == 7
    assert res["terms"]["selected"] == "238489"

    s = t["Trigonometry unit Summative assessment"]
    assert s["kind"] == "summative"
    assert s["date"] == "2026-10-16T16:15"
    assert s["grade"]["type"] == "graded"
    assert [(k["letter"], k["score"], k["max"]) for k in s["grade"]["criteria"]] == [
        ("A", 7, 8), ("B", 7, 8), ("C", 6, 8), ("D", 7, 8)]
    assert s["grade"]["criteria"][3]["name"] == "Applying mathematics in real-life contexts"
    assert s["comment"] == "You use a good range of methods."
    assert s["url"] == BASE + "/student/classes/13056535/core_tasks/49227638"

    p = t["Parameters"]
    assert p["grade"]["points"] == {"label": "Local Points", "score": 8, "max": 8}
    assert p["status"] == "Submitted" and p["status_hint"] == "12 hours early"
    assert p["kind"] == "formative"

    g = t["Trigonometry functions graphs TEST"]
    assert g["comment"].startswith("Q1: 1.75/2")
    assert "\n" in g["comment"]

    assert t["Parameters test"]["grade"] == {"type": "none", "text": "Not Assessed Yet"}
    assert t["End of term summative"]["grade"]["text"] == "N/A"
    assert t["End of term summative"]["date"] == "2026-11-27T17:55"
    assert t["Dot product of vectors"]["grade"]["text"] == "Complete"
    assert t["Dot product of vectors"]["status"] == "Pending"
    assert t["Beginning of the year diagnostic"]["status_hint"] == "6 hours late"
    assert t["Beginning of the year diagnostic"]["date"].startswith("2026-09-04")


if __name__ == "__main__":
    test_classes()
    test_tasks()
    c = parse_classes(HTML)[0]
    print(json.dumps(parse_tasks(HTML, c, BASE)["tasks"][4], indent=1, ensure_ascii=False))
    print("OK")

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "app"))
from materials import asset_id_from_attachment, parse_task_detail, parse_unit_popup, parse_units  # noqa: E402

BASE = "https://theislandprivateschool.managebac.com"
ATT = "/attachments/eyJfcmFpbHMiOnsiZGF0YSI6ImdpZDovL21hbmFnZWJhYy9Bc3NldC8xOTYzOTEzNTA_ZXhwaXJlc19pbiIsInB1ciI6ImRlZmF1bHQifX0=--e395415ebfc1f2a3a3d3fd926dec9c900e271058"

TASK = f"""<main><div class='core-task-show m-0'>
<a href="/student/classes/13056535/units/2103923/presentations#show_at_a_glance">Spatial Reasoning: Trigonometry</a>
<div class='fusion-section-content core-task-details mt-0 pt-2'><div class='h4'>Description</div>
<div class="show-more"><div class="fix-body-margins redactor-styles fr-view fr-element" style="padding:0"><p><br></p><p>HOMEWORK:</p>
<p>Please solve problems 19 &amp; 20 <a href="https://docs.google.com/document/d/abc/edit">doc</a> <script>x()</script></p>
<p><a href="{ATT}" class="fr-file" data-name="TLF10_Parameters.pdf"><span><span class="fr-inner">TLF10_Parameters.pdf</span><span class="fr-file-size">24.47 KB</span></span></a></p></div></div></div>
<div class='resource-container'><div class='resource fileslibrary'><div class='fileslibrary'><div class='file'><div class='flex flex-start'><div class='cell stretch'>
<a class="file-name" href="https://cdn.ca.managebac.com/uploads/asset/file/194448603/HT-angular-velocity.pdf?Expires=1&amp;Signature=x">HT-angular-velocity.pdf</a></div></div></div></div></div></div>
<table><tbody><tr class="file" id="asset_1"><td><div class="title"><div class="details"><a href="https://cdn.ca.managebac.com/uploads/asset/file/1/img_1.jpg">img_1.jpg</a></div></div></td></tr></tbody></table>
</div></main>"""

UNITS = """<div class='unit-component unit w-100 current'><p class='h4'><a href="/student/classes/1/units/2030255/presentations">Quadratic Functions &amp; Parameters</a></p>
<span class='label label-start'><span>StartsW1 Nov</span></span><div class='unit-duration'>4 Weeks</div></div>
<div class='unit-component unit w-100'><p class='h4'><a href="/student/classes/1/units/7/presentations">Vectors</a></p></div>
<div class='unit-component unit w-100 current'><p class='h4'><a href="/student/classes/1/units/2030255/presentations">Quadratic Functions &amp; Parameters</a></p></div>"""

POPUP = """<div>Unit</div><div>Back to the beginning</div><div>Last updated on Jan 27</div><div>Subjects:Extended Mathematics</div>
<h4>Global Context</h4><p>Personal and cultural expression</p><h4>Key Concepts</h4><p>Form is the shape.</p>
<h4>Statement of Inquiry</h4><p>Generalizing patterns can lead to better models.</p>
<h4>Inquiry Questions</h4><div>Factual</div><div>How does the discriminant work?</div><div>Debatable</div><div>Is maths invented?</div>"""


def test_all():
    assert asset_id_from_attachment(ATT) == "196391350"
    d = parse_task_detail(TASK, BASE)
    assert d["unit_id"] == "2103923"
    names = [f["name"] for f in d["files"]]
    assert names == ["TLF10_Parameters.pdf", "HT-angular-velocity.pdf"], names
    assert d["files"][0]["asset"] == "196391350" and d["files"][0]["kind"] == "pdf"
    assert d["files"][0]["size"] == "24.47 KB"
    assert d["links"][0]["kind"] == "gdoc"
    assert "<script" not in d["description_html"] and "HOMEWORK" in d["description_html"]
    assert "TLF10_Parameters.pdf" not in d["description_html"]
    assert 'target="_blank"' in d["description_html"]
    u = parse_units(UNITS)
    assert [x["id"] for x in u] == ["2030255", "7"] and u[0]["current"] and not u[1]["current"]
    assert u[0]["start"] == "W1 Nov" and u[0]["duration"] == "4 Weeks"
    p = parse_unit_popup(POPUP)
    assert p["Statement of Inquiry"] == ["Generalizing patterns can lead to better models."]
    assert p["Inquiry Questions"] == ["Factual: How does the discriminant work?", "Debatable: Is maths invented?"]
    assert "Subjects" not in p


if __name__ == "__main__":
    test_all()
    print("OK")

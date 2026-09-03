"""
materials_data.py
------------------
Single source of truth for every study-material link scattered across the
app's pages (Semester 1/2/3, Data Science, Resume Building, Home/Syllabus).

Each entry is a plain dict so it's trivial to keep in sync whenever a page
adds/removes a `st.link_button`. The ASUR search page imports MATERIALS
and the helper functions below instead of re-parsing the pages.

Fields on every entry:
    title      -> display name of the resource
    url        -> Google Drive (or other) link
    semester   -> "Semester 1" | "Semester 2" | "Semester 3" | "Data Science"
                  | "Resume Building" | "General"
    subject    -> subject/category within that semester
    kind       -> "file" | "folder"  (inferred from the Drive URL shape)
    type       -> resource type, e.g. "Notes", "Book", "Question Paper", ...
    tags       -> extra free-text keywords to help fuzzy search
"""

from __future__ import annotations
from typing import List, Dict, Optional
import difflib


def _kind(url: str) -> str:
    if "/drive/folders/" in url:
        return "folder"
    return "file"


MATERIALS: List[Dict] = [
    # ---------------------------------------------------------------- Home
    {
        "title": "Detailed M.Tech QROR Syllabus",
        "url": "https://drive.google.com/file/d/1otS_-835q4W_EuDuWLtTTGohF-d21Wzk/view?usp=sharing",
        "semester": "General",
        "subject": "Syllabus",
        "type": "Syllabus",
        "tags": "syllabus course structure curriculum",
    },

    # ------------------------------------------------------------ Semester 1
    {
        "title": "RMMR Table",
        "url": "https://drive.google.com/file/d/1GxYgJQlY4sl6XDwmna01JFAVojprTuF5/view?usp=drive_link",
        "semester": "Semester 1", "subject": "RMMR Table", "type": "Reference Table",
        "tags": "rmmr table statistical tables",
    },
    {
        "title": "QMS Study Material",
        "url": "https://drive.google.com/drive/folders/1AYiY3CMUkNWluAnP9BhMmZkx5RRZciwD?usp=sharing",
        "semester": "Semester 1", "subject": "QMS", "type": "Notes",
        "tags": "quantitative management systems qms",
    },
    {
        "title": "QMS Assignment",
        "url": "https://drive.google.com/drive/folders/1oWbDYyQ_ExKCuGF-B7aWfkh68MlCYllM?usp=sharing",
        "semester": "Semester 1", "subject": "QMS", "type": "Assignment",
        "tags": "qms assignment homework",
    },
    {
        "title": "QMS Material 2023",
        "url": "https://drive.google.com/drive/folders/1mgSCHIr_hpSfhd2BbMrfTnhRPZeaGUQj?usp=sharing",
        "semester": "Semester 1", "subject": "QMS", "type": "Notes",
        "tags": "qms 2023 archive",
    },
    {
        "title": "QMS Add/Access New Material",
        "url": "https://drive.google.com/drive/folders/1r9UOJEWtTibl7Y1sloyYXATPMMOJ0G_B?usp=sharing",
        "semester": "Semester 1", "subject": "QMS", "type": "Notes",
        "tags": "qms shared drive contribute",
    },
    {
        "title": "Examination Papers [Old]",
        "url": "https://drive.google.com/drive/folders/1OU3Q5o9s0GYnd54FA3mV-ZDmTt32bX0e?usp=sharing",
        "semester": "Semester 1", "subject": "Examination Papers", "type": "Question Paper",
        "tags": "old previous year papers sem1",
    },
    {
        "title": "Mid Sem Papers [New]",
        "url": "https://drive.google.com/file/d/1mRHT-HpOKgi-Aj--hniZX7eStJO5Ghu1/view?usp=sharing",
        "semester": "Semester 1", "subject": "Examination Papers", "type": "Question Paper",
        "tags": "mid semester exam paper sem1",
    },
    {
        "title": "End Sem Papers [New]",
        "url": "https://drive.google.com/file/d/1F8mSRi7oYQyI-PCqSyPIaDFP7dJkhkWp/view?usp=sharing",
        "semester": "Semester 1", "subject": "Examination Papers", "type": "Question Paper",
        "tags": "end semester final exam paper sem1",
    },
    {
        "title": "Probability Notes",
        "url": "https://drive.google.com/drive/folders/18SWl8nmu-TUET0ox2UiINcAw3d-X1Pg8?usp=sharing",
        "semester": "Semester 1", "subject": "Probability", "type": "Notes",
        "tags": "probability theory notes",
    },
    {
        "title": "Probability Book",
        "url": "https://drive.google.com/file/d/1ies89poEi_FhOsVpw1HfGwqwsZ5ro5yK/view?usp=sharing",
        "semester": "Semester 1", "subject": "Probability", "type": "Book",
        "tags": "probability textbook",
    },
    {
        "title": "Probability Notes (Soumyadeep Mondal)",
        "url": "https://drive.google.com/file/d/1AMBY_s25YHV_klT8A_-xboX90U_-nPWP/view?usp=sharing",
        "semester": "Semester 1", "subject": "Probability", "type": "Notes",
        "tags": "probability soumyadeep mondal handwritten notes",
    },
    {
        "title": "Statistical Method 1 Notes",
        "url": "https://drive.google.com/drive/folders/1EkesCgrU8dyRuIMuadtYVLqx8jwguN4l?usp=sharing",
        "semester": "Semester 1", "subject": "Statistical Method 1", "type": "Notes",
        "tags": "sm1 statistical methods",
    },
    {
        "title": "Complete SM1 Notes [Latest]",
        "url": "https://drive.google.com/file/d/1-_cU7ygW_aObGqoaRZAFW9eTsWMGJKZP/view?usp=sharing",
        "semester": "Semester 1", "subject": "Statistical Method 1", "type": "Notes",
        "tags": "sm1 complete latest",
    },
    {
        "title": "Operations Research Material (SKD Sir)",
        "url": "https://drive.google.com/file/d/1pesNRIg-LOrhmUmxmFrYDzr9qP13gEf4/view?usp=sharing",
        "semester": "Semester 1", "subject": "Operations Research", "type": "Notes",
        "tags": "or skd sir operations research",
    },
    {
        "title": "Operations Research Material (KK Sir)",
        "url": "https://drive.google.com/drive/folders/16KjUsw_BoQIzOkxTMrtMqfte5uqYFb0r?usp=sharing",
        "semester": "Semester 1", "subject": "Operations Research", "type": "Notes",
        "tags": "or kk sir operations research",
    },
    {
        "title": "Linear Algebra Book",
        "url": "https://drive.google.com/file/d/1bz0m8nciWSvWyuVsy04gmucDPbOzeFaY/view",
        "semester": "Semester 1", "subject": "Operations Research", "type": "Book",
        "tags": "linear algebra textbook or",
    },
    {
        "title": "Programming & Data Structures Material (UB Sir)",
        "url": "https://drive.google.com/drive/folders/1E7lieYsGwp8UXsHXrogh0818iwuMlj6d?usp=drive_link",
        "semester": "Semester 1", "subject": "Programming and Data Structures", "type": "Notes",
        "tags": "pds programming data structures ub sir",
    },
    {
        "title": "Programming & Data Structures Assignment (UB Sir)",
        "url": "https://drive.google.com/drive/folders/1hDBmVECWWDnEhggZtHbTsev8jjKXgUfE?usp=sharing",
        "semester": "Semester 1", "subject": "Programming and Data Structures", "type": "Assignment",
        "tags": "pds assignment ub sir coding",
    },

    # ------------------------------------------------------------ Semester 2
    {
        "title": "SQC Study Material (Compiled by Prakash Kumar)",
        "url": "https://drive.google.com/file/d/1nnIxDBcuXPNKgi-dOdZDpf5FaqOwMnn5/view?usp=sharing",
        "semester": "Semester 2", "subject": "SQC", "type": "Notes",
        "tags": "statistical quality control sqc prakash kumar",
    },
    {
        "title": "SQC Quiz",
        "url": "https://drive.google.com/file/d/1OPrGzX0tiWjG29rc07XztYRYZ7iR1-7M/view?usp=sharing",
        "semester": "Semester 2", "subject": "SQC", "type": "Quiz",
        "tags": "sqc quiz practice",
    },
    {
        "title": "SQC Lecture-wise Notes",
        "url": "https://drive.google.com/drive/folders/1rnlw7uOY9-B2Wvjy1LWqFANEyefQSNPN?usp=sharing",
        "semester": "Semester 2", "subject": "SQC", "type": "Notes",
        "tags": "sqc lecture wise notes",
    },
    {
        "title": "RMMR Table",
        "url": "https://drive.google.com/file/d/1GxYgJQlY4sl6XDwmna01JFAVojprTuF5/view?usp=drive_link",
        "semester": "Semester 2", "subject": "RMMR Table", "type": "Reference Table",
        "tags": "rmmr table statistical tables",
    },
    {
        "title": "Examination Papers [Old]",
        "url": "https://drive.google.com/drive/folders/1OU3Q5o9s0GYnd54FA3mV-ZDmTt32bX0e?usp=sharing",
        "semester": "Semester 2", "subject": "Examination Papers", "type": "Question Paper",
        "tags": "old previous year papers sem2",
    },
    {
        "title": "Mid Sem Papers [New]",
        "url": "https://drive.google.com/file/d/1L1ah2nSwfExuZDQpVtQoVkbcnbux_ruu/view?usp=sharing",
        "semester": "Semester 2", "subject": "Examination Papers", "type": "Question Paper",
        "tags": "mid semester exam paper sem2",
    },
    {
        "title": "End Sem Papers [New]",
        "url": "https://drive.google.com/file/d/1CORRJ2dNQck7of-wQiVvO27Grtc-GNKE/view?usp=sharing",
        "semester": "Semester 2", "subject": "Examination Papers", "type": "Question Paper",
        "tags": "end semester final exam paper sem2",
    },
    {
        "title": "Stochastic Processes Notes (Sumit Kr Gupta)",
        "url": "https://drive.google.com/file/d/1BsEoA4EyWQdj8lo5wa8tsBN1KbPV0oPY/view?usp=sharing",
        "semester": "Semester 2", "subject": "Stochastic Processes", "type": "Notes",
        "tags": "stochastic processes sumit kr gupta",
    },
    {
        "title": "Stochastic Processes Notes (Soumyadeep Mondal)",
        "url": "https://drive.google.com/file/d/1d0weHrafTONxKm2pgQc1gtgRNWzuVwgT/view?usp=sharing",
        "semester": "Semester 2", "subject": "Stochastic Processes", "type": "Notes",
        "tags": "stochastic processes soumyadeep mondal",
    },
    {
        "title": "Stochastic Processes Digital Notes",
        "url": "https://drive.google.com/drive/folders/1XIJPCLtu8J8WrSXrCpXx_16mViIWAnrN?usp=sharing",
        "semester": "Semester 2", "subject": "Stochastic Processes", "type": "Notes",
        "tags": "stochastic processes digital notes",
    },
    {
        "title": "Reliability Notes (Soumyadeep Mondal)",
        "url": "https://drive.google.com/file/d/1gHiVCOTznLRFLDEuuEpsLEqeEzV-gYCy/view?usp=sharing",
        "semester": "Semester 2", "subject": "Reliability", "type": "Notes",
        "tags": "reliability soumyadeep mondal",
    },
    {
        "title": "Reliability Digital Notes",
        "url": "https://drive.google.com/drive/folders/1UAC9V3l0irJy8UnxiQuzt68714hRXcZI?usp=sharing",
        "semester": "Semester 2", "subject": "Reliability", "type": "Notes",
        "tags": "reliability digital notes",
    },
    {
        "title": "Reliability End Sem '23 Paper",
        "url": "https://drive.google.com/file/d/1_7_kJobSaHOLtr_OJL5LAhC1QwlO503L/view?usp=sharing",
        "semester": "Semester 2", "subject": "Reliability", "type": "Question Paper",
        "tags": "reliability end sem 2023 paper",
    },
    {
        "title": "Reliability Notes (Sumit Kr Gupta)",
        "url": "https://drive.google.com/file/d/16wjkhSdc3Q1upUrbYgiymyXWTNUL-5iD/view?usp=sharing",
        "semester": "Semester 2", "subject": "Reliability", "type": "Notes",
        "tags": "reliability sumit kr gupta",
    },
    {
        "title": "Reliability Notes (Prakash Kumar)",
        "url": "https://drive.google.com/file/d/1Qv2AgKjpIoSrhxO61l45i7TDUxmaUN1c/view?usp=sharing",
        "semester": "Semester 2", "subject": "Reliability", "type": "Notes",
        "tags": "reliability prakash kumar",
    },
    {
        "title": "Applied Statistics & Probability for Engineers [Book]",
        "url": "https://drive.google.com/file/d/1zl1Pr1vzxL50-hCxC8erNuqiWMkNuXku/view?usp=sharing",
        "semester": "Semester 2", "subject": "Statistical Method 2", "type": "Book",
        "tags": "applied statistics probability engineers textbook sm2",
    },
    {
        "title": "Hypothesis Testing Notes",
        "url": "https://drive.google.com/drive/folders/1sJWCY9wsFlnJksUnzMt2pXRMSC-ZahSO?usp=sharing",
        "semester": "Semester 2", "subject": "Statistical Method 2", "type": "Notes",
        "tags": "hypothesis testing sm2",
    },
    {
        "title": "ANOVA Notes",
        "url": "https://drive.google.com/drive/folders/1vy_669nBzsQdUBTsm8hv9LKW_Iuo8OFN?usp=sharing",
        "semester": "Semester 2", "subject": "Statistical Method 2", "type": "Notes",
        "tags": "anova analysis of variance sm2",
    },
    {
        "title": "Simple Linear Regression Notes",
        "url": "https://drive.google.com/drive/folders/1JtGStvIyrjN37Wdklth76jBNWHOGLwH6?usp=sharing",
        "semester": "Semester 2", "subject": "Statistical Method 2", "type": "Notes",
        "tags": "slr simple linear regression sm2",
    },
    {
        "title": "Multiple Linear Regression Notes",
        "url": "https://drive.google.com/drive/folders/19yOCk-F_ZBll16CbGlmfwfDJ3Su8ft1q?usp=sharing",
        "semester": "Semester 2", "subject": "Statistical Method 2", "type": "Notes",
        "tags": "mlr multiple linear regression sm2",
    },
    {
        "title": "ANCOVA Notes",
        "url": "https://drive.google.com/drive/folders/1UQsOjw7l2Wso6W4h6AnIgCDmy6pOwX1Y?usp=sharing",
        "semester": "Semester 2", "subject": "Statistical Method 2", "type": "Notes",
        "tags": "ancova sm2",
    },
    {
        "title": "NPT Notes",
        "url": "https://drive.google.com/drive/folders/1Yfgi4So82e8SYVXLal-4NBbxMOuSXkoE?usp=sharing",
        "semester": "Semester 2", "subject": "Statistical Method 2", "type": "Notes",
        "tags": "npt non-parametric tests sm2",
    },
    {
        "title": "IEM Material Before Mid Sem (KK Sir)",
        "url": "https://drive.google.com/drive/folders/1KuRRgp-U6ymxQzB9zSNSPoRyQI6ThUax?usp=sharing",
        "semester": "Semester 2", "subject": "IEM", "type": "Notes",
        "tags": "iem industrial engineering management kk sir",
    },
    {
        "title": "IEM Mid Sem Paper",
        "url": "https://drive.google.com/file/d/1KIxPTu0px4THDmA4EZ_Ft86w-PmonltD/view?usp=sharing",
        "semester": "Semester 2", "subject": "IEM", "type": "Question Paper",
        "tags": "iem mid sem paper",
    },
    {
        "title": "IEM Complete Notes (KK Sir)",
        "url": "https://drive.google.com/file/d/1zWDk6OliPUgnq_FFmwPkYkDptI6BOXMi/view?usp=sharing",
        "semester": "Semester 2", "subject": "IEM", "type": "Notes",
        "tags": "iem complete notes kk sir",
    },

    # ------------------------------------------------------------ Semester 3
    {
        "title": "Mid Sem Papers [New]",
        "url": "https://drive.google.com/file/d/1vuO_BLW8CaQOG0WP1QD6yXArQ08g9IKF/view?usp=sharing",
        "semester": "Semester 3", "subject": "Examination Papers", "type": "Question Paper",
        "tags": "mid semester exam paper sem3",
    },
    {
        "title": "End Sem Papers [New]",
        "url": "https://drive.google.com/file/d/1GYFlYqzq3_i_-8ip6HQz20TVctEdXx_7/view?usp=sharing",
        "semester": "Semester 3", "subject": "Examination Papers", "type": "Question Paper",
        "tags": "end semester final exam paper sem3",
    },
    {
        "title": "Six Sigma Material",
        "url": "https://drive.google.com/drive/folders/1TYK0ZDAxQbcemu9KB6owts6AEY9L2YnF?usp=sharing",
        "semester": "Semester 3", "subject": "Six Sigma", "type": "Notes",
        "tags": "six sigma quality",
    },
    {
        "title": "AMA Book",
        "url": "https://drive.google.com/file/d/10_hHk0NmSVAJUWvNVWduwapujwNNRxxG/view?usp=sharing",
        "semester": "Semester 3", "subject": "Advanced Multivariate Analysis", "type": "Book",
        "tags": "advanced multivariate analysis ama textbook",
    },
    {
        "title": "AMA Complete Notes",
        "url": "https://drive.google.com/file/d/1JTWZFjCDjI7l60N1QrYYZlAAPOVTl7c3/view?usp=sharing",
        "semester": "Semester 3", "subject": "Advanced Multivariate Analysis", "type": "Notes",
        "tags": "advanced multivariate analysis ama complete notes",
    },
    {
        "title": "Reliability-II Material (Upto Mid Sem)",
        "url": "https://drive.google.com/file/d/1w3dEgUc7cGFuusZiatTxnJNpY0v3xfjC/view?usp=sharing",
        "semester": "Semester 3", "subject": "Reliability - II", "type": "Notes",
        "tags": "reliability 2 upto midsem",
    },
    {
        "title": "Reliability-II Material (After Mid Sem)",
        "url": "https://drive.google.com/file/d/12N1Gg704l5kukpBmiGRCON8oLUG_22WC/view?usp=sharing",
        "semester": "Semester 3", "subject": "Reliability - II", "type": "Notes",
        "tags": "reliability 2 after midsem",
    },
    {
        "title": "Reliability-II Complete Notes",
        "url": "https://drive.google.com/file/d/1bd3y5hHJQ1Bnp0BCYSRIKi3vp-3sl4RG/view?usp=sharing",
        "semester": "Semester 3", "subject": "Reliability - II", "type": "Notes",
        "tags": "reliability 2 complete notes",
    },
    {
        "title": "Operations Research Material",
        "url": "https://drive.google.com/file/d/144Al12hnk9xqM321vAtr5a3zrgZ1G3e_/view?usp=sharing",
        "semester": "Semester 3", "subject": "Operations Research", "type": "Notes",
        "tags": "operations research sem3",
    },
    {
        "title": "Bazaraa Book",
        "url": "https://drive.google.com/file/d/1vGIR58UuETrEj-BkNrroW1Zj2OLWUHXW/view?usp=sharing",
        "semester": "Semester 3", "subject": "Operations Research", "type": "Book",
        "tags": "bazaraa nonlinear programming textbook or",
    },
    {
        "title": "Operations Research Notes",
        "url": "https://drive.google.com/file/d/1MFGB8f9VAcPddv9N8JDd3qtJouR-ERRk/view?usp=sharing",
        "semester": "Semester 3", "subject": "Operations Research", "type": "Notes",
        "tags": "or notes sem3",
    },
    {
        "title": "RMMR Table",
        "url": "https://drive.google.com/file/d/1GxYgJQlY4sl6XDwmna01JFAVojprTuF5/view?usp=drive_link",
        "semester": "Semester 3", "subject": "RMMR Table", "type": "Reference Table",
        "tags": "rmmr table statistical tables",
    },

    # -------------------------------------------------------------- Data Science
    {
        "title": "Data Science Books (Compiled by Soubhik Bhattacharya)",
        "url": "https://drive.google.com/drive/folders/1tMlOwyXzpiiSWmvlP-X7HSrc4dxBi0YJ?usp=sharing",
        "semester": "Data Science", "subject": "ML Books", "type": "Book",
        "tags": "data science ml books soubhik bhattacharya compiled",
    },
    {
        "title": "Interview Questions PDF",
        "url": "https://drive.google.com/file/d/1JJ0Co6YTXa8qMFAjqKVTkp8WzTz33JpL/view?usp=sharing",
        "semester": "Data Science", "subject": "Interview Prep", "type": "Question Bank",
        "tags": "interview questions data science placement",
    },
    {
        "title": "Extra Interview Questions & Important PDFs",
        "url": "https://drive.google.com/drive/folders/1dysGAdEkuO8TdDVZXn5vQws-o5HmPZjl?usp=sharing",
        "semester": "Data Science", "subject": "Interview Prep", "type": "Question Bank",
        "tags": "extra interview questions important pdfs placement",
    },
    {
        "title": "Pandas Practice",
        "url": "https://drive.google.com/file/d/1onfaw-0pA2fhCNccBLggoZlm53BjJ4FV/view?usp=sharing",
        "semester": "Data Science", "subject": "Pandas", "type": "Practice Set",
        "tags": "pandas practice python data science",
    },

    # -------------------------------------------------------------- Resume Building
    {
        "title": "Overleaf Resume Template",
        "url": "https://drive.google.com/file/d/1bhrEj7RR-omwHE-T0c_yfA0_DsqERn2h/view?usp=sharing",
        "semester": "Resume Building", "subject": "Resume Template", "type": "Template",
        "tags": "resume template overleaf latex",
    },
]

# Normalize kind + build a lowercase searchable blob once, up front.
for _m in MATERIALS:
    _m["kind"] = _kind(_m["url"])
    _m["_haystack"] = " ".join([
        _m["title"], _m["subject"], _m["semester"], _m["type"], _m.get("tags", "")
    ]).lower()


def get_semesters() -> List[str]:
    order = ["General", "Semester 1", "Semester 2", "Semester 3", "Data Science", "Resume Building"]
    present = {m["semester"] for m in MATERIALS}
    return [s for s in order if s in present]


def get_subjects(semesters: Optional[List[str]] = None) -> List[str]:
    pool = MATERIALS if not semesters else [m for m in MATERIALS if m["semester"] in semesters]
    return sorted({m["subject"] for m in pool})


def get_types(semesters: Optional[List[str]] = None, subjects: Optional[List[str]] = None) -> List[str]:
    pool = MATERIALS
    if semesters:
        pool = [m for m in pool if m["semester"] in semesters]
    if subjects:
        pool = [m for m in pool if m["subject"] in subjects]
    return sorted({m["type"] for m in pool})


def _score(query: str, entry: Dict) -> float:
    """Higher is better. Combines substring match with fuzzy ratio."""
    q = query.lower().strip()
    if not q:
        return 1.0
    hay = entry["_haystack"]
    if q in hay:
        # Prefer matches that occur in the title itself, and earlier matches.
        title_hit = q in entry["title"].lower()
        return 2.0 + (1.0 if title_hit else 0.0)
    # Fuzzy fallback for typos / partial words
    ratio = difflib.SequenceMatcher(None, q, hay).ratio()
    title_ratio = difflib.SequenceMatcher(None, q, entry["title"].lower()).ratio()
    return max(ratio, title_ratio)


def search(
    query: str = "",
    semesters: Optional[List[str]] = None,
    subjects: Optional[List[str]] = None,
    types: Optional[List[str]] = None,
    min_score: float = 0.4,
) -> List[Dict]:
    """Return matching materials, best matches first."""
    pool = MATERIALS
    if semesters:
        pool = [m for m in pool if m["semester"] in semesters]
    if subjects:
        pool = [m for m in pool if m["subject"] in subjects]
    if types:
        pool = [m for m in pool if m["type"] in types]

    if not query.strip():
        return sorted(pool, key=lambda m: (m["semester"], m["subject"], m["title"]))

    scored = [(_score(query, m), m) for m in pool]
    scored = [(s, m) for s, m in scored if s >= min_score]
    scored.sort(key=lambda pair: pair[0], reverse=True)
    return [m for _, m in scored]

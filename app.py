import streamlit as st
from pathlib import Path
import json


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="ResearchGapAI",
    page_icon="🔬",
    layout="wide"
)


# ==========================================
# PATH
# ==========================================

BASE_DIR = Path(__file__).resolve().parent

FINAL_GAP_FILE = (
    BASE_DIR
    / "data"
    / "final_gap"
    / "final_research_gap.json"
)

REPORT_FILE = (
    BASE_DIR
    / "data"
    / "final_gap"
    / "final_research_gap_report.txt"
)


# ==========================================
# LOAD FINAL RESULT
# ==========================================

def load_final_gap():

    if not FINAL_GAP_FILE.exists():
        return None

    with open(
        FINAL_GAP_FILE,
        "r",
        encoding="utf-8"
    ) as f:
        return json.load(f)


data = load_final_gap()


# ==========================================
# HEADER
# ==========================================

st.title("🔬 ResearchGapAI")

st.subheader(
    "Intelligent Research Gap Identification System"
)

st.write(
    "An NLP-based system that analyzes research literature, "
    "detects potential research gaps, identifies semantic themes, "
    "and validates gaps across multiple papers."
)

st.divider()


# ==========================================
# ERROR CHECK
# ==========================================

if data is None:

    st.error(
        "Final research gap data was not found."
    )

    st.info(
        "Run the ResearchGapAI pipeline before launching the dashboard."
    )

    st.stop()


# ==========================================
# KEY METRICS
# ==========================================

st.header("Research Gap Analysis")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "Cluster",
        data.get("cluster_id", "N/A")
    )

with col2:
    st.metric(
        "Gap Score",
        data.get("gap_score", "N/A")
    )

with col3:
    st.metric(
        "Similarity",
        data.get(
            "semantic_similarity",
            "N/A"
        )
    )

with col4:
    st.metric(
        "Supporting Papers",
        data.get(
            "supporting_paper_count",
            "N/A"
        )
    )

with col5:
    st.metric(
        "Confidence",
        data.get(
            "confidence",
            "N/A"
        )
    )


st.divider()


# ==========================================
# VALIDATION STATUS
# ==========================================

st.header("Validation Status")

validation = data.get(
    "validation",
    "UNKNOWN"
)

if validation == "VALIDATED":

    st.success(
        f"✓ Research Gap {validation}"
    )

else:

    st.warning(
        f"Research Gap Status: {validation}"
    )


# ==========================================
# RESEARCH GAP
# ==========================================

st.header("Identified Research Gap")

st.info(
    data.get(
        "research_gap",
        "No research gap available."
    )
)


# ==========================================
# RESEARCH THEME
# ==========================================

st.header("Research Theme")

st.write(
    data.get(
        "research_theme",
        "No theme available."
    )
)


# ==========================================
# VALIDATION REASON
# ==========================================

st.header("Why Was This Gap Validated?")

st.write(
    data.get(
        "validation_reason",
        "No validation explanation available."
    )
)


# ==========================================
# SUPPORTING PAPERS
# ==========================================

st.header("Supporting Research Papers")

papers = data.get(
    "supporting_papers",
    []
)

if papers:

    for i, paper in enumerate(
        papers,
        start=1
    ):

        st.write(
            f"**{i}.** {paper}"
        )

else:

    st.write(
        "No supporting papers available."
    )


# ==========================================
# RESEARCH DIRECTION
# ==========================================

st.header("Potential Research Direction")

st.success(
    data.get(
        "potential_research_direction",
        "No research direction available."
    )
)


# ==========================================
# TECHNICAL EVIDENCE
# ==========================================

with st.expander(
    "View Technical Validation Evidence"
):

    st.write(
        f"**Cluster ID:** "
        f"{data.get('cluster_id')}"
    )

    st.write(
        f"**Gap Score:** "
        f"{data.get('gap_score')}"
    )

    st.write(
        f"**Semantic Similarity:** "
        f"{data.get('semantic_similarity')}"
    )

    st.write(
        f"**Supporting Papers:** "
        f"{data.get('supporting_paper_count')}"
    )

    st.write(
        f"**Validation:** "
        f"{data.get('validation')}"
    )

    st.write(
        f"**Confidence:** "
        f"{data.get('confidence')}"
    )


# ==========================================
# REPORT DOWNLOAD
# ==========================================

st.divider()

st.header("Research Gap Report")

if REPORT_FILE.exists():

    with open(
        REPORT_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        report = f.read()

    st.download_button(
        label="Download Research Gap Report",
        data=report,
        file_name="ResearchGapAI_Report.txt",
        mime="text/plain"
    )

    with st.expander(
        "Preview Full Report"
    ):

        st.text(report)

else:

    st.warning(
        "Report file not found."
    )


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "ResearchGapAI | NLP-based Automated Research Gap Identification"
)
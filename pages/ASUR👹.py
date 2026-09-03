import streamlit as st
from material_data import MATERIALS, get_semesters, search

TYPE_ICONS = {
    "Notes": "📝",
    "Book": "📚",
    "Question Paper": "📄",
    "Assignment": "🧾",
    "Quiz": "❓",
    "Reference Table": "📊",
    "Question Bank": "💼",
    "Practice Set": "💻",
    "Template": "🎓",
    "Syllabus": "📘",
}


def main():
    st.set_page_config(
        page_title="ASUR - Material Search",
        page_icon="👹",
        layout="centered",
        initial_sidebar_state="auto",
        menu_items=None,
    )

    st.title("👹 A.S.U.R.")
    st.caption("Search every study material link in the QROR Study Hub - notes, books, papers, assignments, and more  in one place.")
    st.sidebar.success("SELECT THE PAGE ABOVE")

    st.info(
        f"Indexing **{len(MATERIALS)}** + resources across "
        f"{len(get_semesters())} sections. This searches titles/subjects/tags — "
        "it opens the original Google Drive link, it doesn't search text *inside* the PDFs.",
        icon="ℹ️",
    )

    # ---------------------------------------------------------------- Search
    query = st.text_input(
        "Search",
        placeholder="e.g. reliability notes, RMMR table, probability book...",
        label_visibility="collapsed",
    )

    results = search(query)

    st.write("")

    # ---------------------------------------------------------------- Results
    if not results:
        st.warning("No matching material found. Try a shorter or different keyword.", icon="🤷")
        return

    if query.strip():
        st.markdown(f"**{len(results)} result(s)** for *\"{query}\"*")
    else:
        st.markdown(f"**{len(results)} resource(s)** in total")

    for m in results:
        icon = TYPE_ICONS.get(m["type"], "🔗")
        kind_label = "📁 Folder" if m["kind"] == "folder" else "📄 File"
        with st.container(border=True):
            c1, c2 = st.columns([5, 2])
            with c1:
                st.markdown(f"**{icon} {m['title']}**")
                st.caption(f"{m['semester']} • {m['subject']} • {m['type']} • {kind_label}")
            with c2:
                st.link_button("Open ↗", url=m["url"], use_container_width=True)

    st.divider()
    st.caption("⚠️ **Disclaimer:** All shared materials are for educational use only. Copyright belongs to the original owners.")


if __name__ == "__main__":
    main()

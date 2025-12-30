import streamlit as st

st.set_page_config(page_title="Nanoparticle Design Decision Engine")

st.title("Nanoparticle Design Decision Engine")
st.write(
    "Answer a few questions about your goals and tumor conditions, "
    "and this tool will recommend a nanoparticle design with tradeoffs explained."
)

st.header("Design Goals")
targeting = st.slider("How important is targeting the tumor?", 0, 10, 7)
safety = st.slider("How important is minimizing side effects?", 0, 10, 8)
circulation = st.slider("How important is long circulation time?", 0, 10, 6)

st.header("Tumor & Drug Constraints")
acidic = st.checkbox("Tumor is acidic")
immune_sensitive = st.checkbox("Patient is immune-sensitive")
fragile_drug = st.checkbox("Drug is fragile")

st.header("Recommended Design")

size = "80–100 nm"
coating = "Standard polymer coating"
release = "Passive diffusion"

if circulation >= 7:
    coating = "PEG coating (long circulation)"

if immune_sensitive:
    coating = "PEG coating (immune stealth)"

if acidic:
    release = "pH-triggered release"

if targeting >= 7:
    size = "100–130 nm"

st.markdown(f"""
### 🧬 Suggested Nanoparticle Design
- **Size:** {size}  
- **Surface coating:** {coating}  
- **Release strategy:** {release}
""")

st.markdown("### Why this design?")
st.write(
    "This recommendation balances your stated priorities. "
    "Changes in size affect circulation and penetration, "
    "surface coatings influence immune clearance, "
    "and release strategies control where and when the drug activates."
)

import streamlit as st
import matplotlib.pyplot as plt
from matplotlib_venn import venn3





# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="SetLab",
    page_icon="∪",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background-color: #0b1020;
    color: white;
}

[data-testid="stSidebar"] {
    background-color: #11182d;
}

[data-testid="stSidebar"] h1 {
    color: white;
}

.hero {
    background: linear-gradient(135deg, #1d4ed8, #7c3aed);
    padding: 45px;
    border-radius: 22px;
    margin-bottom: 30px;
}

.hero-title {
    font-size: 48px;
    font-weight: 800;
    color: white;
}

.hero-subtitle {
    font-size: 20px;
    color: #e5e7eb;
}

.card {
    background-color: #151d35;
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #263250;
    margin-bottom: 20px;
}

.card-title {
    font-size: 24px;
    font-weight: 700;
    color: white;
}

.card-text {
    color: #cbd5e1;
    font-size: 16px;
    line-height: 1.6;
}

.result-card {
    background-color: #151d35;
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #263250;
    min-height: 120px;
}

.result-title {
    color: #94a3b8;
    font-size: 15px;
}

.result-value {
    color: white;
    font-size: 24px;
    font-weight: 700;
}

.formula {
    background-color: #111827;
    padding: 18px;
    border-radius: 12px;
    font-size: 22px;
    text-align: center;
    margin: 15px 0;
    border: 1px solid #334155;
}

.section-label {
    color: #818cf8;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 2px;
}

.footer {
    text-align: center;
    color: #64748b;
    margin-top: 50px;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# FUNCTIONS
# =========================================================

def convert_to_set(text):
    try:
        return set(
            int(x.strip())
            for x in text.split(",")
            if x.strip()
        )
    except ValueError:
        return set()


def format_set(value):
    if not value:
        return "∅"

    return "{ " + ", ".join(map(str, sorted(value))) + " }"


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("∪ SetLab")

    st.caption("Interactive Set Learning Platform")

    st.divider()

    page = st.radio(
        "Navigation",
        [
            "🏠 Home",
            "🔢 Set Operations",
            "⭕ Venn Visualizer",
            "📚 Laws of Sets"
        ]
    )

    st.divider()


# =========================================================
# HOME
# =========================================================

if page == "🏠 Home":

    st.markdown(
        """
        <div class="hero">
            <div class="hero-title">Interactive SetLab</div>
            <div class="hero-subtitle">
                Explore set operations, visualize relationships,
                and verify important laws of sets interactively.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.header("What is SetLab?")

    st.write(
        "SetLab is an interactive learning platform that helps "
        "students understand set theory using calculations, "
        "Venn diagrams, and set laws."
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.subheader("🔢 Set Operations")

        st.write(
            "Perform union, intersection, difference, "
            "and complement operations on three sets."
        )

    with col2:

        st.subheader("⭕ Venn Diagram")

        st.write(
            "Visualize relationships between three sets "
            "and highlight the selected regions."
        )

    with col3:

        st.subheader("📚 Laws of Sets")

        st.write(
            "Verify important laws such as associative, "
            "distributive, complement, and De Morgan's laws."
        )

    st.header("How to use SetLab")

    st.write("**1. Enter your sets**")
    st.write(
        "Provide the Universal Set and sets A, B and C."
    )

    st.write("**2. Perform operations**")
    st.write(
        "Select the operation you want to calculate."
    )

    st.write("**3. Visualize the result**")
    st.write(
        "Use the Venn Visualizer to understand the operation."
    )

    st.write("**4. Verify set laws**")
    st.write(
        "Check whether important laws of sets hold true."
    )


# =========================================================
# SET OPERATIONS
# =========================================================

elif page == "🔢 Set Operations":

    st.markdown(
        '<div class="section-label">CALCULATION</div>',
        unsafe_allow_html=True
    )

    st.header("Set Operations")

    st.write(
        "Enter the Universal Set and three sets "
        "to perform different set operations."
    )

    col1, col2 = st.columns(2)

    with col1:

        U_input = st.text_input(
            "Universal Set (U)",
            "1,2,3,4,5,6,7,8"
        )

        A_input = st.text_input(
            "Set A",
            "1,2,3,4"
        )

    with col2:

        B_input = st.text_input(
            "Set B",
            "3,4,5,6"
        )

        C_input = st.text_input(
            "Set C",
            "2,3,5,7"
        )

    if st.button(
        "Generate Sets",
        use_container_width=True
    ):

        U = convert_to_set(U_input)
        A = convert_to_set(A_input)
        B = convert_to_set(B_input)
        C = convert_to_set(C_input)

        st.session_state["U"] = U
        st.session_state["A"] = A
        st.session_state["B"] = B
        st.session_state["C"] = C

    if "U" in st.session_state:

        U = st.session_state["U"]
        A = st.session_state["A"]
        B = st.session_state["B"]
        C = st.session_state["C"]

        st.subheader("Current Sets")

        set_col1, set_col2, set_col3, set_col4 = st.columns(4)

        with set_col1:
            st.info("U = " + format_set(U))

        with set_col2:
            st.info("A = " + format_set(A))

        with set_col3:
            st.info("B = " + format_set(B))

        with set_col4:
            st.info("C = " + format_set(C))

        st.subheader("Select Operation")

        operation = st.selectbox(
            "Choose an operation:",
            [
                "Union (A ∪ B)",
                "Union (A ∪ C)",
                "Union (B ∪ C)",
                "Union (A ∪ B ∪ C)",

                "Intersection (A ∩ B)",
                "Intersection (A ∩ C)",
                "Intersection (B ∩ C)",
                "Intersection (A ∩ B ∩ C)",

                "Difference (A − B)",
                "Difference (A − C)",
                "Difference (B − A)",
                "Difference (B − C)",
                "Difference (C − A)",
                "Difference (C − B)",

                "Complement (A')",
                "Complement (B')",
                "Complement (C')"
            ]
        )

        # =================================================
        # CALCULATION
        # =================================================

        if operation == "Union (A ∪ B)":

            result = A | B

            formula = "A ∪ B"

            explanation = (
                "The union of A and B contains every element "
                "that belongs to A, B, or both."
            )

        elif operation == "Union (A ∪ C)":

            result = A | C

            formula = "A ∪ C"

            explanation = (
                "The union of A and C contains every element "
                "that belongs to A, C, or both."
            )

        elif operation == "Union (B ∪ C)":

            result = B | C

            formula = "B ∪ C"

            explanation = (
                "The union of B and C contains every element "
                "that belongs to B, C, or both."
            )

        elif operation == "Union (A ∪ B ∪ C)":

            result = A | B | C

            formula = "A ∪ B ∪ C"

            explanation = (
                "The union of A, B and C contains every element "
                "that belongs to at least one of the three sets."
            )

        elif operation == "Intersection (A ∩ B)":

            result = A & B

            formula = "A ∩ B"

            explanation = (
                "The intersection of A and B contains only "
                "the elements common to both sets."
            )

        elif operation == "Intersection (A ∩ C)":

            result = A & C

            formula = "A ∩ C"

            explanation = (
                "The intersection of A and C contains only "
                "the elements common to both sets."
            )

        elif operation == "Intersection (B ∩ C)":

            result = B & C

            formula = "B ∩ C"

            explanation = (
                "The intersection of B and C contains only "
                "the elements common to both sets."
            )

        elif operation == "Intersection (A ∩ B ∩ C)":

            result = A & B & C

            formula = "A ∩ B ∩ C"

            explanation = (
                "The intersection of A, B and C contains only "
                "the elements common to all three sets."
            )

        elif operation == "Difference (A − B)":

            result = A - B

            formula = "A − B"

            explanation = (
                "A − B contains the elements that are in A "
                "but not in B."
            )

        elif operation == "Difference (A − C)":

            result = A - C

            formula = "A − C"

            explanation = (
                "A − C contains the elements that are in A "
                "but not in C."
            )

        elif operation == "Difference (B − A)":

            result = B - A

            formula = "B − A"

            explanation = (
                "B − A contains the elements that are in B "
                "but not in A."
            )

        elif operation == "Difference (B − C)":

            result = B - C

            formula = "B − C"

            explanation = (
                "B − C contains the elements that are in B "
                "but not in C."
            )

        elif operation == "Difference (C − A)":

            result = C - A

            formula = "C − A"

            explanation = (
                "C − A contains the elements that are in C "
                "but not in A."
            )

        elif operation == "Difference (C − B)":

            result = C - B

            formula = "C − B"

            explanation = (
                "C − B contains the elements that are in C "
                "but not in B."
            )

        elif operation == "Complement (A')":

            result = U - A

            formula = "A'"

            explanation = (
                "The complement of A contains all elements "
                "of the Universal Set that are not in A."
            )

        elif operation == "Complement (B')":

            result = U - B

            formula = "B'"

            explanation = (
                "The complement of B contains all elements "
                "of the Universal Set that are not in B."
            )

        else:

            result = U - C

            formula = "C'"

            explanation = (
                "The complement of C contains all elements "
                "of the Universal Set that are not in C."
            )

        st.subheader("Result")

        col1, col2 = st.columns(2)

        with col1:

            st.markdown("### Operation")

            st.info(formula)

        with col2:

            st.markdown("### Answer")

            st.success(format_set(result))

        st.markdown("### Explanation")

        st.info(explanation)


# =========================================================
# VENN VISUALIZER
# =========================================================

elif page == "⭕ Venn Visualizer":

    st.markdown(
        '<div class="section-label">VISUALIZATION</div>',
        unsafe_allow_html=True
    )

    st.header("Interactive Venn Diagram")

    st.write(
        "Choose an operation to highlight the matching regions. "
        "Each region displays its actual elements, and the rectangle "
        "represents the Universal Set."
    )

    if "U" not in st.session_state:

        st.warning(
            "Please go to Set Operations and "
            "click Generate Sets first."
        )

    else:

        U = st.session_state["U"]
        A = st.session_state["A"]
        B = st.session_state["B"]
        C = st.session_state["C"]

        # Keep the diagram mathematically consistent with the universe.
        outside_universe = (A | B | C) - U
        if outside_universe:
            st.warning(
                "Some elements in A, B or C are not in U: "
                + format_set(outside_universe)
                + ". For a valid set diagram, each of A, B and C "
                "should be a subset of U."
            )

        operation = st.selectbox(
            "Choose an operation:",
            [
                "Union (A ∪ B)",
                "Union (A ∪ C)",
                "Union (B ∪ C)",
                "Union (A ∪ B ∪ C)",
                "Intersection (A ∩ B)",
                "Intersection (A ∩ C)",
                "Intersection (B ∩ C)",
                "Intersection (A ∩ B ∩ C)",
                "Difference (A − B)",
                "Difference (A − C)",
                "Difference (B − A)",
                "Difference (B − C)",
                "Difference (C − A)",
                "Difference (C − B)",
                "Complement (A')",
                "Complement (B')",
                "Complement (C')"
            ]
        )

        # Calculate the operation result and explanation.
        if operation == "Union (A ∪ B)":
            result = A | B
            explanation = "All elements that belong to A, B, or both."
            selected_regions = ["100", "010", "110", "101", "011", "111"]

        elif operation == "Union (A ∪ C)":
            result = A | C
            explanation = "All elements that belong to A, C, or both."
            selected_regions = ["100", "001", "110", "101", "011", "111"]

        elif operation == "Union (B ∪ C)":
            result = B | C
            explanation = "All elements that belong to B, C, or both."
            selected_regions = ["010", "001", "110", "101", "011", "111"]

        elif operation == "Union (A ∪ B ∪ C)":
            result = A | B | C
            explanation = "All elements that belong to at least one of the three sets."
            selected_regions = ["100", "010", "001", "110", "101", "011", "111"]

        elif operation == "Intersection (A ∩ B)":
            result = A & B
            explanation = "Elements common to both A and B."
            selected_regions = ["110", "111"]

        elif operation == "Intersection (A ∩ C)":
            result = A & C
            explanation = "Elements common to both A and C."
            selected_regions = ["101", "111"]

        elif operation == "Intersection (B ∩ C)":
            result = B & C
            explanation = "Elements common to both B and C."
            selected_regions = ["011", "111"]

        elif operation == "Intersection (A ∩ B ∩ C)":
            result = A & B & C
            explanation = "Elements common to all three sets."
            selected_regions = ["111"]

        elif operation == "Difference (A − B)":
            result = A - B
            explanation = "Elements in A that are not in B."
            selected_regions = ["100", "101"]

        elif operation == "Difference (A − C)":
            result = A - C
            explanation = "Elements in A that are not in C."
            selected_regions = ["100", "110"]

        elif operation == "Difference (B − A)":
            result = B - A
            explanation = "Elements in B that are not in A."
            selected_regions = ["010", "011"]

        elif operation == "Difference (B − C)":
            result = B - C
            explanation = "Elements in B that are not in C."
            selected_regions = ["010", "110"]

        elif operation == "Difference (C − A)":
            result = C - A
            explanation = "Elements in C that are not in A."
            selected_regions = ["001", "011"]

        elif operation == "Difference (C − B)":
            result = C - B
            explanation = "Elements in C that are not in B."
            selected_regions = ["001", "101"]

        elif operation == "Complement (A')":
            result = U - A
            explanation = "Elements of U that are outside A."
            selected_regions = ["010", "001", "011"]

        elif operation == "Complement (B')":
            result = U - B
            explanation = "Elements of U that are outside B."
            selected_regions = ["100", "001", "101"]

        else:
            result = U - C
            explanation = "Elements of U that are outside C."
            selected_regions = ["100", "010", "110"]

        left, right = st.columns([1.55, 1])

        with left:
            # Region contents: 100=A only, 010=B only, 001=C only,
            # 110=A∩B only, 101=A∩C only, 011=B∩C only, 111=all three.
            region_elements = {
                "100": A - (B | C),
                "010": B - (A | C),
                "001": C - (A | B),
                "110": (A & B) - C,
                "101": (A & C) - B,
                "011": (B & C) - A,
                "111": A & B & C,
            }

            # Use a fixed three-circle geometry so an empty set does not
            # cause matplotlib_venn to hide or reposition a circle.
            from matplotlib.patches import Rectangle

            fig, ax = plt.subplots(figsize=(8.2, 7.2))
            fig.patch.set_facecolor("white")
            ax.set_facecolor("white")

            is_complement = operation.startswith("Complement")
            # The rectangle is the universal set. For complements, tint the
            # whole universe first; circle-region patches are drawn over it.
            universal_box = Rectangle(
                (-0.98, -0.78),
                1.96,
                1.58,
                linewidth=2,
                edgecolor="#222222",
                facecolor="#e8f2ff" if is_complement else "white",
                zorder=0
            )
            ax.add_patch(universal_box)

            # Artificial equal region sizes are used ONLY to keep the three
            # circles in a stable layout. The element labels and operation
            # results below are calculated from the real sets.
            v = venn3(
                subsets=(1, 1, 1, 1, 1, 1, 1),
                set_labels=("Set A", "Set B", "Set C"),
                ax=ax
            )

            # Give every region an opaque neutral base first. This prevents
            # overlapping translucent circle colors from making unrelated
            # regions look highlighted.
            neutral_color = "#e5e7eb"
            highlight_color = "#16a34a"

            for region_id, elements in region_elements.items():
                label = v.get_label_by_id(region_id)
                if label is not None:
                    label.set_text(
                        ", ".join(map(str, sorted(elements))) if elements else ""
                    )
                    label.set_fontsize(10)
                    label.set_color("black")
                    label.set_zorder(20)

                patch = v.get_patch_by_id(region_id)
                if patch is not None:
                    patch.set_facecolor(neutral_color)
                    patch.set_edgecolor("white")
                    patch.set_linewidth(1.0)
                    patch.set_alpha(1.0)
                    patch.set_zorder(2)

            # Only regions that belong to the chosen operation are green.
            # Empty regions are not highlighted because they contain no
            # elements from the actual sets.
            if result:
                for region_id in selected_regions:
                    patch = v.get_patch_by_id(region_id)
                    if patch is not None and region_elements[region_id]:
                        patch.set_facecolor(highlight_color)
                        patch.set_alpha(1.0)
                        patch.set_zorder(3)

            # Keep set labels readable and in front of the circles.
            for label_id in ("A", "B", "C"):
                label = v.get_label_by_id(label_id)
                if label is not None:
                    label.set_color("black")
                    label.set_fontsize(11)
                    label.set_zorder(20)

            ax.set_title(
                operation,
                fontsize=17,
                fontweight="bold",
                pad=18,
                color="black"
            )

            # Give the diagram enough space so circles, labels and rectangle
            # remain visible instead of being clipped at the bottom.
            ax.set_xlim(-1.08, 1.08)
            ax.set_ylim(-0.88, 0.90)
            ax.set_aspect("equal", adjustable="box")
            ax.axis("off")

            fig.tight_layout(pad=1.5)
            st.pyplot(fig, use_container_width=True)
            plt.close(fig)

            st.caption(
                "Each number shown inside a region is an actual set element, "
                "not the number of elements in that region."
            )

        with right:
            st.subheader("Selected Operation")
            st.write(operation)

            st.divider()

            st.subheader("Result")
            st.success(format_set(result))

            st.subheader("What does it mean?")
            st.info(explanation)

# =========================================================
# LAWS OF SETS
# =========================================================

elif page == "📚 Laws of Sets":

    st.markdown(
        '<div class="section-label">SET THEORY</div>',
        unsafe_allow_html=True
    )

    st.header("Laws of Sets")

    st.write(
        "Select a law and verify it using sets A, B and C."
    )

    if "U" not in st.session_state:

        st.warning(
            "Please go to Set Operations and "
            "click Generate Sets first."
        )

    else:

        U = st.session_state["U"]
        A = st.session_state["A"]
        B = st.session_state["B"]
        C = st.session_state["C"]

        # -------------------------------------------------
        # SELECT LAW
        # -------------------------------------------------

        law = st.selectbox(
            "Choose a law:",
            [
                "Commutative Law",
                "Associative Law",
                "Distributive Law",
                "Identity Law",
                "Domination Law",
                "Idempotent Law",
                "Complement Law",
                "De Morgan's Law"
            ]
        )

        # =================================================
        # COMMUTATIVE LAW
        # =================================================

        if law == "Commutative Law":

            formula_choice = st.selectbox(
                "Choose formula:",
                [
                    "A ∪ B = B ∪ A",
                    "A ∩ B = B ∩ A",
                    "A ∪ C = C ∪ A",
                    "A ∩ C = C ∩ A",
                    "B ∪ C = C ∪ B",
                    "B ∩ C = C ∩ B"
                ]
            )

            if formula_choice == "A ∪ B = B ∪ A":

                left = A | B
                right = B | A

            elif formula_choice == "A ∩ B = B ∩ A":

                left = A & B
                right = B & A

            elif formula_choice == "A ∪ C = C ∪ A":

                left = A | C
                right = C | A

            elif formula_choice == "A ∩ C = C ∩ A":

                left = A & C
                right = C & A

            elif formula_choice == "B ∪ C = C ∪ B":

                left = B | C
                right = C | B

            else:

                left = B & C
                right = C & B

        # =================================================
        # ASSOCIATIVE LAW
        # =================================================

        elif law == "Associative Law":

            formula_choice = st.selectbox(
                "Choose formula:",
                [
                    "(A ∪ B) ∪ C = A ∪ (B ∪ C)",
                    "(A ∩ B) ∩ C = A ∩ (B ∩ C)"
                ]
            )

            if formula_choice == "(A ∪ B) ∪ C = A ∪ (B ∪ C)":

                left = (A | B) | C
                right = A | (B | C)

            else:

                left = (A & B) & C
                right = A & (B & C)

        # =================================================
        # DISTRIBUTIVE LAW
        # =================================================

        elif law == "Distributive Law":

            formula_choice = st.selectbox(
                "Choose formula:",
                [
                    "A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)",
                    "A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)"
                ]
            )

            if formula_choice == "A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)":

                left = A | (B & C)
                right = (A | B) & (A | C)

            else:

                left = A & (B | C)
                right = (A & B) | (A & C)

        # =================================================
        # IDENTITY LAW
        # =================================================

        elif law == "Identity Law":

            formula_choice = st.selectbox(
                "Choose formula:",
                [
                    "A ∪ ∅ = A",
                    "A ∩ U = A",
                    "B ∪ ∅ = B",
                    "B ∩ U = B",
                    "C ∪ ∅ = C",
                    "C ∩ U = C"
                ]
            )

            if formula_choice == "A ∪ ∅ = A":

                left = A | set()
                right = A

            elif formula_choice == "A ∩ U = A":

                left = A & U
                right = A

            elif formula_choice == "B ∪ ∅ = B":

                left = B | set()
                right = B

            elif formula_choice == "B ∩ U = B":

                left = B & U
                right = B

            elif formula_choice == "C ∪ ∅ = C":

                left = C | set()
                right = C

            else:

                left = C & U
                right = C

        # =================================================
        # DOMINATION LAW
        # =================================================

        elif law == "Domination Law":

            formula_choice = st.selectbox(
                "Choose formula:",
                [
                    "A ∪ U = U",
                    "A ∩ ∅ = ∅",
                    "B ∪ U = U",
                    "B ∩ ∅ = ∅",
                    "C ∪ U = U",
                    "C ∩ ∅ = ∅"
                ]
            )

            if formula_choice == "A ∪ U = U":

                left = A | U
                right = U

            elif formula_choice == "A ∩ ∅ = ∅":

                left = A & set()
                right = set()

            elif formula_choice == "B ∪ U = U":

                left = B | U
                right = U

            elif formula_choice == "B ∩ ∅ = ∅":

                left = B & set()
                right = set()

            elif formula_choice == "C ∪ U = U":

                left = C | U
                right = U

            else:

                left = C & set()
                right = set()

        # =================================================
        # IDEMPOTENT LAW
        # =================================================

        elif law == "Idempotent Law":

            formula_choice = st.selectbox(
                "Choose formula:",
                [
                    "A ∪ A = A",
                    "A ∩ A = A",
                    "B ∪ B = B",
                    "B ∩ B = B",
                    "C ∪ C = C",
                    "C ∩ C = C"
                ]
            )

            if formula_choice == "A ∪ A = A":

                left = A | A
                right = A

            elif formula_choice == "A ∩ A = A":

                left = A & A
                right = A

            elif formula_choice == "B ∪ B = B":

                left = B | B
                right = B

            elif formula_choice == "B ∩ B = B":

                left = B & B
                right = B

            elif formula_choice == "C ∪ C = C":

                left = C | C
                right = C

            else:

                left = C & C
                right = C

        # =================================================
        # COMPLEMENT LAW
        # =================================================

        elif law == "Complement Law":

            formula_choice = st.selectbox(
                "Choose formula:",
                [
                    "A ∪ A' = U",
                    "A ∩ A' = ∅",
                    "B ∪ B' = U",
                    "B ∩ B' = ∅",
                    "C ∪ C' = U",
                    "C ∩ C' = ∅"
                ]
            )

            if formula_choice == "A ∪ A' = U":

                left = A | (U - A)
                right = U

            elif formula_choice == "A ∩ A' = ∅":

                left = A & (U - A)
                right = set()

            elif formula_choice == "B ∪ B' = U":

                left = B | (U - B)
                right = U

            elif formula_choice == "B ∩ B' = ∅":

                left = B & (U - B)
                right = set()

            elif formula_choice == "C ∪ C' = U":

                left = C | (U - C)
                right = U

            else:

                left = C & (U - C)
                right = set()

        # =================================================
        # DE MORGAN'S LAW
        # =================================================

        else:

            formula_choice = st.selectbox(
                "Choose formula:",
                [
                    "(A ∪ B)' = A' ∩ B'",
                    "(A ∩ B)' = A' ∪ B'",
                    "(A ∪ C)' = A' ∩ C'",
                    "(A ∩ C)' = A' ∪ C'",
                    "(B ∪ C)' = B' ∩ C'",
                    "(B ∩ C)' = B' ∪ C'"
                ]
            )

            if formula_choice == "(A ∪ B)' = A' ∩ B'":

                left = U - (A | B)
                right = (U - A) & (U - B)

            elif formula_choice == "(A ∩ B)' = A' ∪ B'":

                left = U - (A & B)
                right = (U - A) | (U - B)

            elif formula_choice == "(A ∪ C)' = A' ∩ C'":

                left = U - (A | C)
                right = (U - A) & (U - C)

            elif formula_choice == "(A ∩ C)' = A' ∪ C'":

                left = U - (A & C)
                right = (U - A) | (U - C)

            elif formula_choice == "(B ∪ C)' = B' ∩ C'":

                left = U - (B | C)
                right = (U - B) & (U - C)

            else:

                left = U - (B & C)
                right = (U - B) | (U - C)

        # =================================================
        # DISPLAY FORMULA
        # =================================================

        st.markdown(
            '<div class="formula">'
            + formula_choice +
            '</div>',
            unsafe_allow_html=True
        )

        # =================================================
        # DISPLAY RESULTS
        # =================================================

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Left Side")

            st.info(
                format_set(left)
            )

        with col2:

            st.subheader("Right Side")

            st.info(
                format_set(right)
            )

        # =================================================
        # VERIFY
        # =================================================

        if left == right:

            st.success(
                "✓ The law is verified! Both sides are equal."
            )

        else:

            st.error(
                "✗ The law is not satisfied for the current sets."
            )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "SetLab • Interactive Set Operations & Visualization"
)


import streamlit as st
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from io import BytesIO
# ==========================================
# CREATE POWERPOINT
# ==========================================

def create_ppt():
    prs = Presentation()

    ppt_file = BytesIO()
    prs.save(ppt_file)
    ppt_file.seek(0)

    return ppt_file
# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="FOMO vs JOMO",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

* {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 15% 20%, rgba(255, 92, 145, 0.12), transparent 30%),
        radial-gradient(circle at 85% 75%, rgba(135, 92, 255, 0.12), transparent 30%),
        #0b0b10;
    color: white;
}

/* Hide Streamlit default elements */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* Navigation */

.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 20px;
    margin-bottom: 35px;
}

.logo {
    font-size: 20px;
    font-weight: 700;
    letter-spacing: 1px;
}

.logo span {
    color: #ff6b9d;
}

/* Main title */

.hero-title {
    text-align: center;
    font-size: 76px;
    font-weight: 700;
    line-height: 1.05;
    margin-top: 40px;
    background: linear-gradient(
        90deg,
        #ff6b9d,
        #c084fc,
        #67e8f9
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    text-align: center;
    font-size: 22px;
    color: #aaa8b8;
    margin-top: 15px;
}

/* Cards */

.card {
    background: rgba(255,255,255,0.045);
    border: 1px solid rgba(255,255,255,0.09);
    border-radius: 24px;
    padding: 35px;
    margin-top: 25px;
    backdrop-filter: blur(15px);
}

.card:hover {
    border: 1px solid rgba(255,255,255,0.18);
}

/* Section title */

.section-title {
    font-size: 48px;
    font-weight: 700;
    margin-top: 20px;
}

.section-subtitle {
    font-size: 20px;
    color: #aaa8b8;
}

/* Big question */

.question {
    font-size: 34px;
    font-weight: 600;
    text-align: center;
    line-height: 1.4;
}

.highlight {
    color: #ff7aa8;
}

.purple {
    color: #c084fc;
}

.blue {
    color: #67e8f9;
}

/* Quotes */

.quote {
    font-size: 28px;
    font-style: italic;
    text-align: center;
    line-height: 1.5;
    padding: 35px;
    color: #eadcff;
}

/* Progress */

.progress-text {
    text-align: center;
    color: #777584;
    font-size: 14px;
    margin-top: 25px;
}

/* Buttons */

.stButton > button {
    border-radius: 14px;
    border: 1px solid rgba(255,255,255,0.12);
    background: rgba(255,255,255,0.06);
    color: white;
    padding: 10px 25px;
    font-weight: 500;
}

.stButton > button:hover {
    border-color: #ff6b9d;
    color: #ff8fb3;
}

/* Big emoji */

.big-emoji {
    text-align: center;
    font-size: 80px;
    margin-bottom: 10px;
}

/* Footer */

.footer {
    text-align: center;
    color: #666575;
    margin-top: 60px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# PRESENTATION DATA
# ==========================================

slides = [
    "INTRO",
    "FOMO",
    "FOMO CYCLE",
    "FEAR OF REGRET",
    "HIGHLIGHT-REEL EFFECT",
    "THE INVISIBLE CROWD"
    "THE PHONE",
    "2-CHOICE EXPERIMENT",
    "SCARCITY EFFECT",
    "MIMETIC THEORY",
    "JOMO",
    "JOMO BENEFITS",
    "JOMO & Self Awareness"
    "FOMO vs JOMO"
    "How can we practice JOMO ",
    "UHV",
    "TAKEAWAY"
]


# ==========================================
# SESSION STATE
# ==========================================

if "slide" not in st.session_state:
    st.session_state.slide = 0


# ==========================================
# NAVIGATION FUNCTION
# ==========================================

def next_slide():
    if st.session_state.slide < len(slides) - 1:
        st.session_state.slide += 1


def previous_slide():
    if st.session_state.slide > 0:
        st.session_state.slide -= 1


# ==========================================
# CURRENT SLIDE
# ==========================================

slide = st.session_state.slide


# ==========================================
# SLIDE 1 — INTRO
# ==========================================

if slide == 0:

    st.markdown(
        '<div class="hero-title">FOMO<br>vs<br>JOMO</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="hero-subtitle">'
        'The Fear of Missing Out vs The Joy of Missing Out'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="card">
            <div class="question">
                What if the best thing you could do today...
                <br><br>
                <span class="highlight">
                was not do what everyone else was doing?
                </span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================
# SLIDE 2 — FOMO
# ==========================================

elif slide == 1:



    st.markdown(
        '<div class="section-title">Meet FOMO.</div>',
        unsafe_allow_html=True
    )

    st.markdown(
    """
    <div class="section-subtitle">
        It doesn't only happen on social media.
    </div>
    """,
    unsafe_allow_html=True
)

    st.markdown(
        """
        <div class="card">

        <p style="font-size:22px;">
        You are sitting at home.
        </p>

        <p style="font-size:22px;">
        Your friends are out.
        </p>

        <p style="font-size:22px;">
        Someone posts a story.
        </p>

        <p style="font-size:22px;">
        You open Instagram.
        </p>

        <br>

        <div class="quote">
        "Why wasn't I there?"
        <br><br>
        "Did I miss something?"
        <br><br>
        "Are they having more fun without me?"
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================
# SLIDE 3 — FOMO CYCLE
# ==========================================

elif slide == 2:

    st.markdown(
        '<div class="section-title">The FOMO Cycle</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'How one simple moment can become a cycle of pressure.'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            """
            <div class="card">
            <h2>👀 SEE</h2>
            <p>
            We see someone else doing something exciting.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="card">
            <h2>🧠 COMPARE</h2>
            <p>
            We compare their experience with our own.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="card">
            <h2>😰 FEEL</h2>
            <p>
            Anxiety, insecurity and pressure appear.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            """
            <div class="card">
            <h2>🏃 REACT</h2>
            <p>
            We act because we are afraid of missing out.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

# ==========================================
# SLIDE 4 — FEAR OF REGRET
# ==========================================

elif slide == 3:

    st.markdown(
        '<div class="section-title">The Fear of Regret</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="card">

        <div class="question">

        What's worse —
        <span class="highlight">missing something</span>,

        <br>

        or finding out later that everyone
        had an amazing time without you?

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    st.markdown(
        """
        <div class="card">

        <h2>🧠 Anticipated Regret</h2>

        <p style="font-size:20px;color:#aaa8b8;">
        Sometimes, we imagine our future selves looking back
        and thinking:
        </p>

        <div class="quote">

        "I should have gone."
        <br><br>

        "I should have bought it."
        <br><br>

        "I should have joined them."

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="card">

        <div class="quote">

        "FOMO isn't always fear of missing the moment.
        <br><br>
        Sometimes, it's fear of regretting
        the decision not to be there."

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )
    # ==========================================
# SLIDE 5 — HIGHLIGHT REEL EFFECT
# ==========================================

elif slide == 4:

    st.markdown(
        '<div class="section-title">The Highlight-Reel Effect</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Social media rarely shows the whole story.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="card">

        <div class="question">

        Think about the last 10 Instagram stories
        you saw today.

        <br><br>

        How many showed someone being bored?

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            <div class="card">

            <h2>📸 What we usually see</h2>

            <p style="font-size:20px;">
            ✈️ Vacations
            </p>

            <p style="font-size:20px;">
            🎉 Parties
            </p>

            <p style="font-size:20px;">
            🍽️ Restaurants
            </p>

            <p style="font-size:20px;">
            🏆 Achievements
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="card">

            <h2>🫥 What we don't see</h2>

            <p style="font-size:20px;">
            😴 Boring afternoons
            </p>

            <p style="font-size:20px;">
            😔 Bad days
            </p>

            <p style="font-size:20px;">
            😐 Ordinary moments
            </p>

            <p style="font-size:20px;">
            😓 Stress and failures
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <div class="card">

        <div class="quote">

        "We aren't comparing lives.
        <br><br>
        We're comparing our reality
        with someone else's highlights."

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )
# ==========================================
# SLIDE 6 — THE INVISIBLE CROWD
# ==========================================

elif slide == 5:

    st.markdown(
        '<div class="section-title">The Invisible Crowd</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Imagine you are alone. Nobody is watching.</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="content-card">
            <h2>Yet you open Instagram...</h2>
            <p>And suddenly, you feel behind.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="quote-card">
            <b>Who made you feel behind?</b><br><br>
            Nobody.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="content-card">
            <h3>🔥 The crowd doesn't have to be present anymore.</h3>
            <p>Your phone brings the crowd into your room.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    # ==========================================
# SLIDE 6 — THE PHONE
# ==========================================

elif slide == 6:

    st.markdown(
        '<div class="section-title">The Phone That Knows Nothing...</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">But Controls Everything</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="quote-card">
            “It doesn't know whether I'm happy.<br>
            It doesn't know whether I'm bored.<br>
            It doesn't even know if I want to check it.”
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            '<div class="mini-card">🔔<br><b>Notifications</b></div>',
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            '<div class="mini-card">⭕<br><b>Stories</b></div>',
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            '<div class="mini-card">💬<br><b>Seen</b></div>',
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            '<div class="mini-card">⌨️<br><b>Typing...</b></div>',
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <div class="content-card">
            <h3>None of them say “You're missing out.”</h3>
            <p>
                But they create just enough uncertainty for our brain to ask:
            </p>
            <h2>“What if?”</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="quote-card">
            Sometimes, “What if?” is enough to make us check.
        </div>
        """,
        unsafe_allow_html=True
    )
    # ==========================================
# SLIDE 7 — 2-CHOICE EXPERIMENT
# ==========================================

elif slide == 7:

    st.markdown(
        '<div class="section-title">The 2-Choice Experiment</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Which would you regret more?</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="content-card">
                <h2>OPTION A</h2>
                <p>
                    🎉 You go to the party.<br><br>
                    It turns out to be... okay.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="content-card">
                <h2>OPTION B</h2>
                <p>
                    🏠 You stay home.<br><br>
                    Tomorrow, you discover it was incredible.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <div class="quote-card">
            Which decision would you regret more?
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="content-card">
            <h3>🧠 Anticipated Regret</h3>
            <p>
                We may not choose what we truly want.<br>
                We choose what protects us from thinking:
            </p>
            <h2>“What if I had gone?”</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="quote-card">
            And that's where FOMO gets powerful.
        </div>
        """,
        unsafe_allow_html=True
    )

    

elif slide == 8:

    st.markdown(
        '<div class="section-title">Why does FOMO work?</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Two psychological ideas help explain it.'
        '</div>',
        unsafe_allow_html=True
    )

    # --------------------------------------
    # SCARCITY EFFECT
    # --------------------------------------

    st.markdown(
        """
        <div class="card">

        <h2>⏳ The Scarcity Effect</h2>

        <p style="font-size:20px;color:#aaa8b8;">
        We tend to value something more when we think
        it is limited or might disappear.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="card">

        <div class="question">

        "If I tell you this pen is available to everyone,
        would you care?"

        <br><br>

        But what if I say...

        <br><br>

        <span class="highlight">
        "This is the last pen.
        You have 10 seconds to decide."
        </span>

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="card">

        <p style="font-size:20px;">

        Suddenly, it becomes more interesting.

        <br><br>

        That's the <span class="highlight">Scarcity Effect.</span>

        <br><br>

        FOMO works similarly.

        When we think we're about to miss an opportunity,
        our brain can make it feel more valuable.

        </p>

        <div class="quote">

        "Sometimes, we don't want the thing.
        <br>
        We just don't want to lose the chance to have it."

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------
    # MIMETIC THEORY
    # --------------------------------------

    st.markdown(
        """
        <div class="card">

        <h2>👥 Mimetic Theory</h2>

        <p style="font-size:20px;color:#aaa8b8;">

        Do we actually want it...

        <br><br>

        or do we want it because
        <span class="highlight">everyone else wants it?</span>

        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            <div class="card">

            <h3>📱 The Phone</h3>

            <p style="font-size:18px;">

            You see your friend buying a particular phone.

            <br><br>

            Suddenly you think:

            <br>

            <span class="highlight">
            "Maybe I need that phone too."
            </span>

            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="card">

            <h3>☕ The Café</h3>

            <p style="font-size:18px;">

            Everyone is going to a particular café.

            <br><br>

            Suddenly you wonder:

            <br>

            <span class="highlight">
            "Why haven't I been there yet?"
            </span>

            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <div class="card">

        <p style="font-size:20px;">

        This connects to a concept called
        <span class="purple">Mimetic Theory</span>,
        proposed by philosopher
        <span class="blue">René Girard.</span>

        <br><br>

        The theory suggests that our desires are often
        influenced by what we see other people desiring.

        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------
    # FOMO CONNECTION
    # --------------------------------------

    st.markdown(
        """
        <div class="card">

        <div class="question">

        Someone else is enjoying something

        <br>
        ↓
        <br>

        We see it

        <br>
        ↓
        <br>

        We assume it must be valuable

        <br>
        ↓
        <br>

        We want to experience it too

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="card">

        <div class="quote">

        So sometimes, FOMO isn't really about
        missing an opportunity.

        <br><br>

        It's about missing something that
        <span class="highlight">
        other people have decided is worth having.
        </span>

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------
    # FINAL QUESTION
    # --------------------------------------

    st.markdown(
        """
        <div class="card">

        <div class="question">

        Is this something I genuinely want...

        <br><br>

        <span class="highlight">
        or is someone else's desire
        teaching me to want it?
        </span>

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

# ==========================================
# SLIDE 10 — JOMO
# ==========================================

elif slide == 9:

    st.markdown(
        '<div class="section-title">The Freedom to Miss Out</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">“Who has cancelled plans… and actually felt relieved?”</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="content-card">
            <h2>JOMO — The Joy of Missing Out</h2>
            <p>
                JOMO is being comfortable — even happy — with choosing
                <b>not</b> to participate when something else matters more to you.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            '<div class="mini-card">🎯<br><b>Choose intentionally</b></div>',
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            '<div class="mini-card">🧠<br><b>Trust your decisions</b></div>',
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            '<div class="mini-card">🌱<br><b>Stop comparing</b></div>',
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            '<div class="mini-card">✋<br><b>Say “No”</b></div>',
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <div class="quote-card">
            <b>JOMO isn't missing out.</b><br>
            It's choosing what matters.
        </div>
        """,
        unsafe_allow_html=True
    )
    # ==========================================
# SLIDE 11 — JOMO BENEFITS
# ==========================================

elif slide == 10:

    st.markdown(
        '<div class="section-title">Psychological Benefits of JOMO</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">What happens when we stop chasing?</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="mini-card">
                🧠<br>
                <b>Less Comparison</b>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="mini-card">
                🕊️<br>
                <b>Reduced Social Pressure</b>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="mini-card">
                🎯<br>
                <b>Better Focus</b>
            </div>
            """,
            unsafe_allow_html=True
        )

    col4, col5 = st.columns(2)

    with col4:
        st.markdown(
            """
            <div class="mini-card">
                🌱<br>
                <b>Greater Contentment</b>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col5:
        st.markdown(
            """
            <div class="mini-card">
                💫<br>
                <b>More Meaningful Experiences</b>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <div class="quote-card">
            Sometimes, doing less of what everyone else is doing
            gives us more space for what actually matters.
        </div>
        """,
        unsafe_allow_html=True
    )
    # ==========================================
# SLIDE 12 — JOMO & SELF-AWARENESS
# ==========================================

elif slide == 11:

    st.markdown(
        '<div class="section-title">JOMO & Self-Awareness</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Knowing yourself before following everyone else.</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="content-card">
                <h3>🧠 SELF-AWARENESS</h3>
                <p>
                    What are my priorities?<br>
                    What genuinely makes me happy?<br>
                    What am I doing just because others are?
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="content-card">
                <h3>🌱 CONTENTMENT</h3>
                <p>
                    Being satisfied with what we have while
                    working toward what we genuinely need.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="content-card">
                <h3>🛑 SETTING BOUNDARIES</h3>
                <p>
                    JOMO gives us the confidence to say
                    <b>“No”</b> without guilt — protecting
                    our time and peace.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="content-card">
                <h3>🤝 UHV CONNECTION</h3>
                <p>
                    JOMO encourages <b>self-awareness, happiness,
                    harmony and meaningful relationships</b> —
                    values at the heart of UHV.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <div class="quote-card">
            “When we understand ourselves, we stop needing
            everyone else to decide for us.”
        </div>
        """,
        unsafe_allow_html=True
    )
    # ==========================================
# SLIDE 13 — HOW CAN WE PRACTICE JOMO?
# ==========================================

elif slide == 12:

    st.markdown(
        '<div class="section-title">How Can We Practice JOMO?</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Small choices that create more space for what matters.</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="mini-card">
                📱<br>
                <b>Take Breaks from Social Media</b>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="mini-card">
                🛑<br>
                <b>Learn to Say No</b>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="mini-card">
                🎯<br>
                <b>Identify Your Priorities</b>
            </div>
            """,
            unsafe_allow_html=True
        )

    col4, col5, col6 = st.columns(3)

    with col4:
        st.markdown(
            """
            <div class="mini-card">
                🧘<br>
                <b>Spend Intentional Time Alone</b>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col5:
        st.markdown(
            """
            <div class="mini-card">
                🪞<br>
                <b>Stop Comparing</b>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col6:
        st.markdown(
            """
            <div class="mini-card">
                🌸<br>
                <b>Enjoy the Present</b>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <div class="quote-card">
            <b>JOMO begins when we stop asking,</b><br>
            “What am I missing?”<br><br>
            and start asking,<br>
            <b>“What matters to me right now?”</b>
        </div>
        """,
        unsafe_allow_html=True
    )
elif slide == 13:

    st.markdown(
        """
        <div class="hero-title">
        Choose.<br>
        Don't chase.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="card">

        <div class="quote">

        "You don't have to experience everything
        to live a meaningful life."

        </div>

        <p style="text-align:center;font-size:22px;">

        Maybe the real freedom isn't having every experience...

        <br><br>

        <span class="highlight">
        It's being okay with choosing your own.
        </span>

        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

# ==========================================
# PRESENTATION NAVIGATION
# ==========================================

st.write("")
st.write("")

# Progress percentage
progress = (slide + 1) / len(slides)

st.progress(progress)

# Navigation area
col1, col2, col3 = st.columns([1, 2, 1])

with col1:

    if slide > 0:

        st.button(
            "← Previous",
            on_click=previous_slide,
            use_container_width=True
        )

with col2:

    st.markdown(
        f"""
        <div class="progress-text">

        <b>{slide + 1}</b>
        &nbsp; / &nbsp;
        <b>{len(slides)}</b>

        <br>

        {slides[slide]}

        </div>
        """,
        unsafe_allow_html=True
    )

with col3:

    if slide < len(slides) - 1:

        st.button(
            "Next →",
            on_click=next_slide,
            use_container_width=True
        )


# ==========================================
# MINI SLIDE INDICATORS
# ==========================================

dots = ""

for i in range(len(slides)):

    if i == slide:
        dots += "● "
    else:
        dots += "○ "

st.markdown(
    f"""
    <div style="
        text-align:center;
        margin-top:15px;
        color:#ff7aa8;
        font-size:13px;
        letter-spacing:3px;
    ">
        {dots}
    </div>
    """,
    unsafe_allow_html=True
)


# ==========================================
# FOOTER
# ==========================================

st.markdown(
    """
    <div class="footer">
        FOMO × JOMO &nbsp; • &nbsp; Universal Human Values
    </div>
    """,
    unsafe_allow_html=True
)
st.download_button(
    label="📥 Download Presentation",
    data=create_ppt(),
    file_name="FOMO_vs_JOMO.pptx",
    mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
)
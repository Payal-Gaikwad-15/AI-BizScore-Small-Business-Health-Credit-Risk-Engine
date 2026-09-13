import base64
import matplotlib.pyplot as plt
import joblib
import pandas as pd
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="AI BizScore: Smart Business Health Engine",
    page_icon="📈",
    layout="wide",
)


# Helper function to convert local background image to base64
def get_base64_of_bin_file(bin_file):
  try:
    with open(bin_file, "rb") as f:
      data = f.read()
    return base64.b64encode(data).decode()
  except FileNotFoundError:
    return None


# Load Local or Fallback Background Image
bg_str = get_base64_of_bin_file("background.png")

if bg_str:
  bg_url = f"data:image/png;base64,{bg_str}"
else:
  # High-resolution dark abstract mesh gradient background fallback
  bg_url = "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1920&auto=format&fit=crop"

# Custom CSS for Deep Dark Theme, Big Cover Background, & Dark KPI Cards
st.markdown(
    f"""
    <style>
    /* Full-bleed, large, fixed background image with dark overlay */
    .stApp {{
        background: linear-gradient(rgba(10, 15, 29, 0.88), rgba(10, 15, 29, 0.88)), 
                    url("{bg_url}");
        background-size: cover !important;
        background-position: center center !important;
        background-repeat: no-repeat !important;
        background-attachment: fixed !important;
        color: #f8fafc;
    }}
    
    /* Darker, High-Contrast Glassmorphic KPI Cards */
    .metric-card {{
        background-color: rgba(15, 23, 42, 0.92);
        border: 1px solid #1e293b;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.5);
        margin-bottom: 12px;
        backdrop-filter: blur(12px);
    }}
    .metric-label {{
        color: #94a3b8;
        font-size: 0.82rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }}
    .metric-value {{
        color: #ffffff !important;
        font-size: 2.2rem;
        font-weight: 800;
        margin-top: 4px;
    }}
    .metric-delta-green {{
        color: #4ade80;
        font-size: 0.85rem;
        font-weight: 700;
        margin-top: 4px;
    }}
    .metric-delta-red {{
        color: #f87171;
        font-size: 0.85rem;
        font-weight: 700;
        margin-top: 4px;
    }}
    
    /* Recommendations Section Styling */
    .recommendation-box {{
        background-color: rgba(15, 23, 42, 0.95);
        border-left: 6px solid #38bdf8;
        border-radius: 10px;
        padding: 22px;
        margin-bottom: 25px;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(12px);
    }}
    
    /* Dark Sidebar */
    div[data-testid="stSidebar"] {{
        background-color: rgba(10, 15, 29, 0.96) !important;
        border-right: 1px solid #1e293b;
    }}
    </style>
""",
    unsafe_allow_html=True,
)

st.title("📈 AI BizScore: Small Business Health & Credit Risk Engine")
st.caption(
    "Automated Financial Health Assessment, Risk Diagnostics & 'What-If'"
    " Growth Simulator"
)


# Load Artifacts
@st.cache_resource
def load_artifacts():
  model = joblib.load("business_model.pkl")
  features = joblib.load("business_features.pkl")
  return model, features


model, features = load_artifacts()

# Sidebar Setup - User Financial Inputs
st.sidebar.header("🏢 Business Financial Parameters")
monthly_revenue = st.sidebar.number_input(
    "Monthly Revenue (₹)",
    min_value=0,
    max_value=20000000,
    value=500000,
    step=25000,
)
operating_costs = st.sidebar.number_input(
    "Monthly Operating Costs (₹)",
    min_value=0,
    max_value=20000000,
    value=300000,
    step=25000,
)
debt_amount = st.sidebar.number_input(
    "Total Business Debt (₹)",
    min_value=0,
    max_value=50000000,
    value=200000,
    step=50000,
)
churn_pct = st.sidebar.slider("Customer Churn Rate (%)", 0.0, 30.0, 5.0)
credit_score = st.sidebar.slider(
    "Owner Credit Score (CIBIL/FICO)", 300, 850, 720
)
pending_invoices = st.sidebar.slider("Overdue Pending Invoices", 0, 50, 3)

# Validation Check for Zero Revenue
if monthly_revenue <= 0:
  st.warning(
      "⚠️ **Monthly Revenue is ₹0 or empty.** Please enter a valid revenue"
      " amount above ₹0 to evaluate business health."
  )
  st.stop()


# Helper function to compute health score safely
def calculate_safe_score(rev, costs, debt, churn, credit, invoices):
  profit = rev - costs
  margin = (profit / rev) * 100 if rev > 0 else 0
  debt_ratio = debt / (rev * 12) if rev > 0 else 0

  profit_comp = min(35, max(0, margin * 1.2))
  debt_comp = min(25, max(0, (1.0 - debt_ratio) * 25))
  credit_comp = min(20, max(0, ((credit - 300) / 550) * 20))
  churn_comp = min(10, max(0, (1.0 - (churn / 30.0)) * 10))
  inv_comp = min(10, max(0, (1.0 - (invoices / 30.0)) * 10))

  score = int(profit_comp + debt_comp + credit_comp + churn_comp + inv_comp)
  return max(5, min(98, score)), profit, margin, debt_ratio


# Primary Score Calculation
(
    health_score,
    monthly_profit,
    profit_margin,
    debt_to_annual_rev,
) = calculate_safe_score(
    monthly_revenue,
    operating_costs,
    debt_amount,
    churn_pct,
    credit_score,
    pending_invoices,
)

# Top Executive Cards (Dark Theme Styled)
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
  st.markdown(
      f"""
        <div class="metric-card">
            <div class="metric-label">Business Health Score</div>
            <div class="metric-value">{health_score} / 100</div>
            <div class="{'metric-delta-green' if health_score >= 50 else 'metric-delta-red'}">
                {'Healthy Standing' if health_score >= 50 else 'Financial Stress'}
            </div>
        </div>
    """,
      unsafe_allow_html=True,
  )

with kpi2:
  if health_score >= 70:
    rating_text, rating_color, delta_msg = (
        "PRIME",
        "metric-delta-green",
        "Low Default Risk",
    )
  elif health_score >= 45:
    rating_text, rating_color, delta_msg = (
        "MODERATE",
        "metric-delta-green",
        "Watchlist Status",
    )
  else:
    rating_text, rating_color, delta_msg = (
        "HIGH RISK",
        "metric-delta-red",
        "Severe Default Risk",
    )

  st.markdown(
      f"""
        <div class="metric-card">
            <div class="metric-label">Financial Rating</div>
            <div class="metric-value">{rating_text}</div>
            <div class="{rating_color}">{delta_msg}</div>
        </div>
    """,
      unsafe_allow_html=True,
  )

with kpi3:
  st.markdown(
      f"""
        <div class="metric-card">
            <div class="metric-label">Monthly Profit</div>
            <div class="metric-value">₹{monthly_profit:,.0f}</div>
            <div class="{'metric-delta-green' if profit_margin >= 15 else 'metric-delta-red'}">{profit_margin:.1f}% Margin</div>
        </div>
    """,
      unsafe_allow_html=True,
  )

with kpi4:
  st.markdown(
      f"""
        <div class="metric-card">
            <div class="metric-label">Debt-to-Revenue Ratio</div>
            <div class="metric-value">{debt_to_annual_rev:.2f}x</div>
            <div class="{'metric-delta-green' if debt_to_annual_rev <= 0.25 else 'metric-delta-red'}">
                {'Manageable Leverage' if debt_to_annual_rev <= 0.25 else 'High Debt Burden'}
            </div>
        </div>
    """,
      unsafe_allow_html=True,
  )

st.divider()

# 1. Prescriptive Recommendations (Displayed Before Graph)
st.subheader("🎯 Risk Drivers & Advisory Plan")

if health_score < 45:
  st.error(
      "🚨 **Critical Health Warning:** This business is operating under severe"
      " financial stress."
  )
  st.markdown(
      """
    <div class="recommendation-box">
        <h4 style="color: #f8fafc; margin-bottom: 10px;">📋 Prescriptive Remediation Strategies:</h4>
    """,
      unsafe_allow_html=True,
  )
  if profit_margin < 15:
    st.write(
        "• **Cost Reduction:** Operating expenses consume over 85% of income."
        " Audit monthly overhead immediately."
    )
  if pending_invoices > 8:
    st.write(
        "• **Cash Flow Acceleration:** Overdue invoices are stalling working"
        " capital. Implement early payment discounts."
    )
  if churn_pct > 10:
    st.write(
        "• **Customer Retention:** Churn rate is dangerously high. Launch a"
        " loyalty check-in program."
    )
  if debt_amount > (monthly_revenue * 3):
    st.write(
        "• **Debt Restructuring:** Debt exceeds 3 months of revenue. Refinance"
        " high-interest short-term loans."
    )
  st.markdown("</div>", unsafe_allow_html=True)

elif health_score < 70:
  st.warning(
      "⚡ **Moderate Risk:** Stable operations, but margin for error is"
      " narrow."
  )
  st.markdown(
      """
    <div class="recommendation-box">
        <h4 style="color: #f8fafc; margin-bottom: 10px;">📋 Actionable Guidance:</h4>
        <p>• Build a 60-day cash buffer to manage seasonal revenue drops.</p>
        <p>• Transition key one-time buyers into recurring retainer contracts.</p>
    </div>
    """,
      unsafe_allow_html=True,
  )
else:
  st.success(
      "✅ **Prime Business Standing:** Highly eligible for expansion credit &"
      " credit lines."
  )
  st.markdown(
      """
    <div class="recommendation-box">
        <h4 style="color: #f8fafc; margin-bottom: 10px;">📋 Strategic Growth Opportunities:</h4>
        <p>• Eligible for prime business expansion loans at competitive interest rates.</p>
        <p>• Strong leverage positioning to negotiate better credit terms with supply chain vendors.</p>
    </div>
    """,
      unsafe_allow_html=True,
  )

st.divider()

# 2. Key Model Feature Drivers (Enlarged & Multi-Color Vibrant Bars)
st.subheader("📊 Key Model Feature Drivers")
st.caption("Feature importances driving the machine learning evaluation model")

importances = model.feature_importances_
df_imp = pd.DataFrame({"Metric": features, "Weight": importances}).sort_values(
    "Weight", ascending=True
)

# Figure setup (Large size with transparent dark background)
fig, ax = plt.subplots(figsize=(11, 5))
fig.patch.set_facecolor("none")
ax.set_facecolor("none")

# Multi-color gradient palette for vibrant graph visual
vibrant_colors = [
    "#38bdf8",
    "#818cf8",
    "#c084fc",
    "#f472b6",
    "#fb7185",
    "#34d399",
    "#facc15",
]
colors = [
    vibrant_colors[i % len(vibrant_colors)] for i in range(len(df_imp))
]

bars = ax.barh(
    df_imp["Metric"],
    df_imp["Weight"],
    color=colors,
    height=0.6,
    edgecolor="none",
)

# Labeling values on each bar
for bar in bars:
  width = bar.get_width()
  ax.text(
      width + 0.005,
      bar.get_y() + bar.get_height() / 2,
      f"{width:.3f}",
      ha="left",
      va="center",
      color="#f1f5f9",
      fontsize=10,
      fontweight="bold",
  )

ax.set_xlabel(
    "Relative Importance Weight",
    color="#94a3b8",
    fontsize=11,
    fontweight="bold",
)
ax.tick_params(colors="#f8fafc", labelsize=11)

for spine in ["top", "right", "bottom", "left"]:
  ax.spines[spine].set_color("#334155")

plt.tight_layout()
st.pyplot(fig, use_container_width=True)

st.divider()

# Interactive What-If Growth Simulator
st.subheader("🧪 Interactive 'What-If' Financial Growth Simulator")
st.info(
    "Simulate operational changes (e.g., cutting costs, reducing churn) to see"
    " how your Business Health Score improves live."
)

sim_col1, sim_col2 = st.columns([1, 1])

with sim_col1:
  sim_cost_cut = st.slider(
      "Simulated Monthly Cost Reduction (₹)", 0, 150000, 30000, step=5000
  )

  # Safe Slider Logic for Churn
  max_churn_sim = max(0.1, float(churn_pct))
  sim_churn_reduction = st.slider(
      "Simulated Churn Reduction (% points)",
      0.0,
      max_churn_sim,
      min(3.0, max_churn_sim),
  )

  # Safe Slider Logic for Invoices
  max_inv_sim = max(1, int(pending_invoices))
  sim_invoices_cleared = st.slider(
      "Simulated Overdue Invoices Cleared",
      0,
      max_inv_sim,
      min(5, int(pending_invoices)),
  )

# Safe Simulated Calculation
sim_op_costs = max(0, operating_costs - sim_cost_cut)
sim_churn = max(0.0, churn_pct - sim_churn_reduction)
sim_invoices = max(0, pending_invoices - sim_invoices_cleared)

sim_health_score, _, _, _ = calculate_safe_score(
    monthly_revenue,
    sim_op_costs,
    debt_amount,
    sim_churn,
    credit_score,
    sim_invoices,
)

score_improvement = sim_health_score - health_score

with sim_col2:
  st.markdown("### 📈 Simulation Results")

  st.markdown(
      f"""
        <div class="metric-card">
            <div class="metric-label">New Simulated Health Score</div>
            <div class="metric-value">{sim_health_score} / 100</div>
            <div class="{'metric-delta-green' if score_improvement >= 0 else 'metric-delta-red'}">
                {f'+{score_improvement} Points Improvement' if score_improvement >= 0 else f'{score_improvement} Points Drop'}
            </div>
        </div>
    """,
      unsafe_allow_html=True,
  )

  if sim_health_score >= 70 and health_score < 70:
    st.success(
        "🎉 **Growth Milestone Achieved:** These simulated operational fixes"
        " raise the business into the PRIME credit tier!"
    )
  elif score_improvement > 0:
    st.info(
        f"💡 This optimization plan adds **+{score_improvement} points** to"
        " the score."
    )

###Footer
st.markdown("""
<div style="text-align: center; padding: 40px 20px; color: #b8a8cc; margin-top: 20px; border-top: 2px solid rgba(255, 0, 110, 0.1);">
    <p style="font-size: 0.95em; margin: 0 0 8px 0; font-weight: 600;">
        <span style="background: linear-gradient(135deg, #ff006e, #d60c9a); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">AI BizScore</span> • Small Business Health & Credit Risk Engine
    </p>
    <p style="font-size: 0.85em; margin: 4px 0; color: #9d8baa;">
        📊 Advanced Financial Analysis |  ⚡ Real-Time Updates
    </p>
    <p style="font-size: 0.75em; color: #7d6d96; margin-top: 16px;">
        © 2024 AI BizScore Engine • Built by Payal Gaikwad 
    </p>
</div>
""", unsafe_allow_html=True)
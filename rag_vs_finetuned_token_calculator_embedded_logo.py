
import streamlit as st
import pandas as pd

st.set_page_config(page_title="LLM Token Cost Calculator", layout="centered")

# Embedded CGI logo
def get_logo_html():
    return f'<img src="data:image/jpeg;base64,/9j/4QAYRXhpZgAASUkqAAgAAAAAAAAAAAAAAP/sABFEdWNreQABAAQAAABQAAD/4QMraHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLwA8P3hwYWNrZXQgYmVnaW49Iu+7vyIgaWQ9Ilc1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCI/PiA8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJBZG9iZSBYTVAgQ29yZSA1LjAtYzA2MCA2MS4xMzQ3NzcsIDIwMTAvMDIvMTItMTc6MzI6MDAgICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCBDUzUgTWFjaW50b3NoIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjc3QkZCQzkzNTFGNzExRTI5OTRCRDE2MTUzNUMwNzVEIiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOjc3QkZCQzk0NTFGNzExRTI5OTRCRDE2MTUzNUMwNzVEIj4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6NzdCRkJDOTE1MUY3MTFFMjk5NEJEMTYxNTM1QzA3NUQiIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6NzdCRkJDOTI1MUY3MTFFMjk5NEJEMTYxNTM1QzA3NUQiLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz7/7gAOQWRvYmUAZMAAAAAB/9sAhAACAgICAgICAgICAwICAgMEAwIC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" width="150">'

#st.markdown(get_logo_html(), unsafe_allow_html=True)
st.title("RAG vs Fine-Tuned LLM Token Cost Calculator")

st.markdown("Use this tool to estimate and compare token costs for Retrieval-Augmented Generation (RAG) and Fine-Tuned LLM deployments in enterprise use cases.")

# Token cost database for popular models
model_costs = {
    "GPT-4 (8K)": {"input": 0.03, "output": 0.06},
    "GPT-4 (32K)": {"input": 0.06, "output": 0.12},
    "GPT-3.5-Turbo": {"input": 0.0015, "output": 0.002},
    "Claude 2.1": {"input": 0.008, "output": 0.024},
    "Claude 3 Opus": {"input": 0.015, "output": 0.075},
    "Claude 3 Sonnet": {"input": 0.003, "output": 0.015},
    "Claude 3 Haiku": {"input": 0.00025, "output": 0.00125},
    "Mistral (Open Source)": {"input": 0.0007, "output": 0.0007},
    "Mixtral": {"input": 0.002, "output": 0.002},
    "Command R+": {"input": 0.0003, "output": 0.0008},
    "Gemini 1.5 Flash": {"input": 0.000125, "output": 0.000375},
    "Gemini 1.5 Pro": {"input": 0.0005, "output": 0.0015},
    "LLaMA 3 (70B) Hosted": {"input": 0.002, "output": 0.002},
    "LLaMA 3 (8B) Hosted": {"input": 0.0004, "output": 0.0004},
    "Falcon 180B": {"input": 0.0018, "output": 0.0018},
    "Gemma (Open Source)": {"input": 0.0005, "output": 0.0005},
    "Cohere Command R+": {"input": 0.0003, "output": 0.0008},
    "Groq LLaMA 3": {"input": 0.0002, "output": 0.0002},
    "Groq Mixtral": {"input": 0.0003, "output": 0.0003},
    "Groq Gemma": {"input": 0.0001, "output": 0.0001},
    "PaLM 2": {"input": 0.001, "output": 0.001},
    "Gemini Pro 1.0": {"input": 0.0005, "output": 0.0015},
    "Anthropic Claude Instant": {"input": 0.00163, "output": 0.00551},
    "Azure OpenAI GPT-3.5": {"input": 0.0015, "output": 0.002},
    "Azure OpenAI GPT-4": {"input": 0.03, "output": 0.06}
}

st.sidebar.header("🔧 Input Parameters")

selected_model = st.sidebar.selectbox("Select LLM Model", list(model_costs.keys()))
input_cost = model_costs[selected_model]["input"]
output_cost = model_costs[selected_model]["output"]

st.sidebar.markdown(f"**Input Token Cost**: ${input_cost:.5f} per 1K tokens")
st.sidebar.markdown(f"**Output Token Cost**: ${output_cost:.5f} per 1K tokens")

queries = st.sidebar.number_input("Monthly Query Volume", min_value=1000, value=1000000, step=10000)

st.sidebar.subheader("📄 Avg Tokens per Query")
rag_input_tokens = st.sidebar.number_input("RAG Input Tokens", min_value=0, value=3000, step=100)
rag_output_tokens = st.sidebar.number_input("RAG Output Tokens", min_value=0, value=300, step=50)

ft_input_tokens = st.sidebar.number_input("Fine-Tuned Input Tokens", min_value=0, value=800, step=100)
ft_output_tokens = st.sidebar.number_input("Fine-Tuned Output Tokens", min_value=0, value=300, step=50)

rag_cost_per_query = ((rag_input_tokens / 1000) * input_cost) + ((rag_output_tokens / 1000) * output_cost)
ft_cost_per_query = ((ft_input_tokens / 1000) * input_cost) + ((ft_output_tokens / 1000) * output_cost)

rag_monthly_cost = rag_cost_per_query * queries
ft_monthly_cost = ft_cost_per_query * queries
savings = rag_monthly_cost - ft_monthly_cost

st.subheader("📊 Monthly Cost Comparison")
st.metric("RAG Estimated Monthly Cost", f"${rag_monthly_cost:,.2f}")
st.metric("Fine-Tuned Estimated Monthly Cost", f"${ft_monthly_cost:,.2f}")
st.metric("Estimated Monthly Savings", f"${savings:,.2f}")

st.subheader("📉 Visual Comparison")
cost_data = pd.DataFrame({
    "Approach": ["RAG", "Fine-Tuned"],
    "Monthly Cost ($)": [rag_monthly_cost, ft_monthly_cost]
})
st.bar_chart(cost_data.set_index("Approach"))

st.markdown("---")
st.markdown("Adjust parameters to reflect your real-world scenario and share with clients to demonstrate potential token cost savings using fine-tuned models.")

# Legal disclaimer
st.markdown("---")
st.markdown("©This tool is provided for informational purposes only and does not constitute a commercial offer or technical guarantee. Cost estimates are based on user inputs and public model pricing as of the current date.")

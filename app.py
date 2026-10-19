"""Optional Streamlit viewer; the model remains usable without Streamlit."""
from model.engine import BASE, BEAR, BULL, build, dcf, validate, sensitivity
try:
 import streamlit as st
except ImportError as exc:
 raise SystemExit('Install requirements.txt then run: streamlit run app.py') from exc
st.set_page_config(page_title='Tesla FIN 43900 Project 1',layout='wide')
st.title('Tesla valuation as of October 19 2026')
st.caption('Point-in-time model: Q3 operating statistics are included, Q3 financial results are excluded.')
choice=st.selectbox('Scenario',['Bear','Base','Bull']); scenario={'Bear':BEAR,'Base':BASE,'Bull':BULL}[choice]
rows=build(scenario); value=dcf(rows,scenario.wacc,scenario.terminal_growth)
st.metric('DCF value per share',f"${value['per_share']:,.2f}")
st.write('Observed October 19 market price is pending a dated source, so the app does not state an action.')
st.dataframe([{k:v for k,v in r.items() if k in ('year','revenue','ebit','ni','cfo','capex','fcff','next_cash','assets','liabilities','next_equity')} for r in rows],use_container_width=True)
st.subheader('Validation'); st.write(validate(rows))
st.subheader('WACC and terminal-growth sensitivity'); st.dataframe([{'WACC':w,'g':g,'Value/share':v} for (w,g),v in sensitivity(build(BASE)).items()])

import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.io as pio
from pathlib import Path

PANEL_PATH   = Path('cckp_raw/exposure_panel.csv')
RESULTS_PATH = Path('outputs/exposure_index_results.csv')
OUTPUT_HTML  = Path('outputs/dashboard.html')
INDICATORS   = ['temperature', 'precipitation', 'drought']

C = {
    'temperature':   '#E63946',
    'precipitation': '#4361EE',
    'drought':       '#F4A261',
    'composite':     '#1D3557',
    'bg':            '#F8F9FA',
    'grid':          '#DEE2E6',
    'text':          '#212529',
}

WEIGHTS = {'temperature': 1/3, 'precipitation': 1/3, 'drought': 1/3}

REGIONS = {
    'Netherlands':'Europe','United Kingdom':'Europe','France':'Europe',
    'Germany':'Europe','Belgium':'Europe','Spain':'Europe','Italy':'Europe',
    'Portugal':'Europe','Denmark':'Europe','Sweden':'Europe','Norway':'Europe',
    'Poland':'Europe','Greece':'Europe','Ireland':'Europe',
    'Nigeria':'Africa','Kenya':'Africa','South Africa':'Africa',
    'United States':'Other','Australia':'Other','India':'Other','Brazil':'Other',
}

panel   = pd.read_csv(PANEL_PATH)
results = pd.read_csv(RESULTS_PATH)
results.columns = ['rank','country','composite','temperature','precipitation','drought']
results['region'] = results['country'].map(REGIONS)
raw = panel.groupby('country')[INDICATORS].mean().reset_index()
results = results.merge(raw, on='country', suffixes=('','_raw'))

# ── Chart 1: Composite Score ──────────────────────────────────────────────────
df = results.sort_values('composite')
hover = [
    (
        f"<b>{row['country']}</b><br>"
        f"Rank: {int(row['rank'])} / 21<br>"
        f"Composite score: {row['composite']:.3f}<br>"
        f"&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;<br>"
        f"Temperature (norm.): {row['temperature']:.3f}<br>"
        f"Precipitation (norm.): {row['precipitation']:.3f}<br>"
        f"Drought (norm.): {row['drought']:.3f}<br>"
        f"&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;<br>"
        f"Temperature (°C): {row['temperature_raw']:.1f}<br>"
        f"Precipitation (mm): {row['precipitation_raw']:.1f}<br>"
        f"Drought (days): {row['drought_raw']:.1f}"
    )
    for _, row in df.iterrows()
]

fig1 = go.Figure(go.Bar(
    x=df['composite'], y=df['country'], orientation='h',
    marker=dict(
        color=df['composite'], colorscale='RdYlGn_r', cmin=0, cmax=1,
        colorbar=dict(title='Score', thickness=12, len=0.6),
        line=dict(color='white', width=0.5),
    ),
    hovertemplate='%{customdata}<extra></extra>',
    customdata=hover,
))
fig1.add_vline(
    x=df['composite'].median(), line_dash='dash',
    line_color=C['composite'], line_width=1.5,
    annotation_text=f"Median ({df['composite'].median():.3f})",
    annotation_position='top right', annotation_font_size=10,
)
fig1.update_layout(
    title=dict(
        text='<b>Physical Climate Hazard Exposure Index</b><br><sup>Composite Exposure Score (0 = least exposed, 1 = most exposed)</sup>',
        font_size=16,
    ),
    xaxis=dict(title='', range=[0, 1.05]),
    yaxis=dict(title=''),
    plot_bgcolor=C['bg'], paper_bgcolor=C['bg'],
    font=dict(color=C['text'], family='sans-serif'),
    height=620, margin=dict(l=140, r=80, t=90, b=60),
    hoverlabel=dict(bgcolor='white', font_size=12, bordercolor=C['grid']),
)

# ── Chart 2: Heatmap ──────────────────────────────────────────────────────────
df_heat = results.sort_values('rank')[['country'] + INDICATORS]
z = df_heat[INDICATORS].values
countries_list = df_heat['country'].tolist()
col_labels = ['Temperature', 'Precipitation', 'Drought']
hover_heat = [
    [f'<b>{countries_list[i]}</b><br>{col_labels[j]}: {z[i][j]:.3f}' for j in range(3)]
    for i in range(21)
]

fig2 = go.Figure(go.Heatmap(
    z=z,
    x=col_labels,
    y=countries_list,
    colorscale='YlOrRd', zmin=0, zmax=1,
    text=[[f'{v:.2f}' for v in row] for row in z],
    texttemplate='%{text}', textfont=dict(size=10),
    hovertemplate='%{customdata}<extra></extra>',
    customdata=hover_heat,
    colorbar=dict(title='Norm. exposure', thickness=12, len=0.6),
    xgap=2, ygap=2,
))
fig2.update_layout(
    title=dict(
        text='<b>Normalised Hazard Indicators by Country</b><br>'
             '<sup>Ordered by composite score: most exposed at top</sup>',
        font_size=16,
    ),
    xaxis=dict(side='bottom'), yaxis=dict(autorange='reversed'),
    plot_bgcolor=C['bg'], paper_bgcolor=C['bg'],
    font=dict(color=C['text'], family='sans-serif'),
    height=680, margin=dict(l=140, r=80, t=90, b=60),
    hoverlabel=dict(bgcolor='white', font_size=12),
)

# ── Chart 3: Driver Decomposition ─────────────────────────────────────────────
df_d = results.sort_values('rank', ascending=False)
fig3 = go.Figure()
for ind, color, label in zip(
    INDICATORS,
    [C['temperature'], C['precipitation'], C['drought']],
    ['Temperature', 'Precipitation', 'Drought'],
):
    fig3.add_trace(go.Bar(
        name=label, y=df_d['country'], x=df_d[ind] * WEIGHTS[ind],
        orientation='h',
        marker=dict(color=color, line=dict(color='white', width=0.4)),
        hovertemplate=f'<b>%{{y}}</b><br>{label} contribution: %{{x:.3f}}<extra></extra>',
    ))
fig3.update_layout(
    barmode='stack',
    title=dict(
        text='<b>Hazard Driver Decomposition</b><br>'
             '<sup>What drives each country’s exposure score?</sup>',
        font_size=16,
    ),
    xaxis=dict(title='Contribution to Composite Score'), yaxis=dict(title=''),
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
    plot_bgcolor=C['bg'], paper_bgcolor=C['bg'],
    font=dict(color=C['text'], family='sans-serif'),
    height=620, margin=dict(l=140, r=80, t=100, b=60),
    hoverlabel=dict(bgcolor='white', font_size=12),
)

# ── Chart 4: Sensitivity Analysis ────────────────────────────────────────────
WEIGHT_SCHEMES = {
    'Equal (1/3 each)':          {'temperature': 1/3,  'precipitation': 1/3,  'drought': 1/3},
    'Temperature-heavy (1/2)':   {'temperature': 0.50, 'precipitation': 0.25, 'drought': 0.25},
    'Precipitation-heavy (1/2)': {'temperature': 0.25, 'precipitation': 0.50, 'drought': 0.25},
    'Drought-heavy (1/2)':       {'temperature': 0.25, 'precipitation': 0.25, 'drought': 0.50},
    'No drought (1/2 + 1/2)':    {'temperature': 0.50, 'precipitation': 0.50, 'drought': 0.00},
}
rank_results = {}
for scheme, weights in WEIGHT_SCHEMES.items():
    s = results.copy()
    s['cs'] = sum(s[ind] * w for ind, w in weights.items())
    s = s.sort_values('cs', ascending=False).reset_index(drop=True)
    s['rank_s'] = s.index + 1
    rank_results[scheme] = s.set_index('country')['rank_s']
rank_df = pd.DataFrame(rank_results)
top10 = results.sort_values('rank')['country'].head(10).tolist()
schemes = list(WEIGHT_SCHEMES.keys())

fig4 = go.Figure()
for i, country in enumerate(top10):
    ranks = [rank_df.loc[country, s] for s in schemes]
    fig4.add_trace(go.Scatter(
        x=schemes, y=ranks, mode='lines+markers', name=country,
        line=dict(width=2.5), marker=dict(size=8),
        opacity=1.0 if i < 5 else 0.5,
        hovertemplate=f'<b>{country}</b><br>Scheme: %{{x}}<br>Rank: %{{y}}<extra></extra>',
    ))
fig4.update_layout(
    title=dict(
        text='<b>Sensitivity Analysis: Rank Stability</b><br>'
             '<sup>Top 10 countries under equal weights · Rank 1 = most exposed</sup>',
        font_size=16,
    ),
    xaxis=dict(title='Weighting Scheme', tickangle=-20),
    yaxis=dict(title='Rank (1 = most exposed)', autorange='reversed', tickvals=list(range(1, 22))),
    legend=dict(title='Country'),
    plot_bgcolor=C['bg'], paper_bgcolor=C['bg'],
    font=dict(color=C['text'], family='sans-serif'),
    height=520, margin=dict(l=80, r=160, t=100, b=80),
    hoverlabel=dict(bgcolor='white', font_size=12),
)

# ── Chart 5: Time Trends ──────────────────────────────────────────────────────
trend = panel.groupby('year')[INDICATORS].mean().reset_index()
fig5 = go.Figure()
for ind, color, label in zip(
    INDICATORS,
    [C['temperature'], C['precipitation'], C['drought']],
    ['Temperature (°C)', 'Precipitation (mm)', 'Drought (days)'],
):
    roll = trend[ind].rolling(5, center=True, min_periods=3).mean()
    fig5.add_trace(go.Scatter(
        x=trend['year'], y=trend[ind], mode='lines', name=label,
        line=dict(color=color, width=1.5), opacity=0.5,
        hovertemplate=f'{label}: %{{y:.2f}}<br>Year: %{{x}}<extra></extra>',
        legendgroup=ind, showlegend=False,
    ))
    fig5.add_trace(go.Scatter(
        x=trend['year'], y=roll, mode='lines', name=label,
        line=dict(color=color, width=3),
        hovertemplate=f'{label} (5yr avg): %{{y:.2f}}<br>Year: %{{x}}<extra></extra>',
        legendgroup=ind,
    ))
fig5.update_layout(
    title=dict(
        text='<b>Indicator Trends 2000-2023</b><br>'
             '<sup>Mean across 21 countries · Thin = annual · Thick = 5-year rolling mean</sup>',
        font_size=16,
    ),
    xaxis=dict(title='Year', range=[2000, 2023]),
    yaxis=dict(title='Mean value (raw units)'),
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
    plot_bgcolor=C['bg'], paper_bgcolor=C['bg'],
    font=dict(color=C['text'], family='sans-serif'),
    height=460, margin=dict(l=80, r=80, t=100, b=60),
    hoverlabel=dict(bgcolor='white', font_size=12),
)

# ── Assemble HTML ─────────────────────────────────────────────────────────────
figures = [
    ('Composite Score Ranking',   fig1),
    ('Normalised Hazard Heatmap', fig2),
    ('Driver Decomposition',      fig3),
    ('Sensitivity Analysis',      fig4),
    ('Indicator Trends',          fig5),
]

header = """<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Climate Risk Exposure Index: Dashboard</title>
  <style>
    body  { font-family: sans-serif; background: #F8F9FA; margin: 0; padding: 20px; color: #212529; }
    h1    { color: #1D3557; border-bottom: 3px solid #E63946; padding-bottom: 10px; }
    p.sub { color: #6c757d; font-size: 14px; margin-top: -10px; }
    .chart-wrap { background: white; border-radius: 8px; padding: 10px;
                  margin-bottom: 24px; box-shadow: 0 1px 4px rgba(0,0,0,0.08); }
    .footer { font-size: 12px; color: #adb5bd; text-align: center; margin-top: 40px; }
  </style>
</head>
<body>
<h1>Climate Risk Exposure Index</h1>
<p class="sub">
  <b>Number of countries:</b> 21 &nbsp;·&nbsp;
  <b>Temporal scale:</b> 2000-2023 &nbsp;·&nbsp;
  <b>Hazards:</b> Temperature (°C), Precipitation (mm), Drought (days) &nbsp;·&nbsp;
  <b>Weighting:</b> Equal weighting &nbsp;·&nbsp;
  <b>Source:</b> World Bank CCKP (CC-BY 4.0)
</p>
"""

footer = """
<div class="footer">
  Data: The World Bank, Climate Change Knowledge Portal (CCKP), CC-BY 4.0 &nbsp;|&nbsp;
  Method: OECD/JRC Handbook on Constructing Composite Indicators &nbsp;|&nbsp;
  CSRD (ESRS E1) / TCFD physical-risk demonstration
</div>
</body></html>
"""

html_parts = [header]
include_js = True
for title, fig in figures:
    chart_html = pio.to_html(
        fig, full_html=False,
        include_plotlyjs='cdn' if include_js else False,
        config={'displayModeBar': True, 'scrollZoom': False},
    )
    include_js = False
    html_parts.append(f'<div class="chart-wrap">{chart_html}</div>')
html_parts.append(footer)

OUTPUT_HTML.write_text('\n'.join(html_parts), encoding='utf-8')

content = OUTPUT_HTML.read_text(encoding='utf-8')
print('txx remaining:   ', content.count('txx'))
print('rx5day remaining:', content.count('rx5day'))
print('cdd remaining:   ', content.count('cdd'))
print(f'Saved -> {OUTPUT_HTML}')

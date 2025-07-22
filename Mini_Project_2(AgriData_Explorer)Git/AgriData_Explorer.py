import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Config ---
st.set_page_config(page_title="Agri Data Explorer",page_icon=":seedling:", layout="wide")

st.markdown("<h1 style='color:#00B4D8;'>🌾 Agri Data Explorer</h1>", unsafe_allow_html=True)
st.markdown("Analyze key crop production trends across Indian states and years.")

st.markdown("---")

# Example metrics
#col1, col2, col3 = st.columns(3)
#col1.metric("🌾 Top Rice State", "West Bengal", "↑ 4.2%")
#col2.metric("🌽 Top Wheat State", "Uttar Pradesh", "↓ 1.5%")
#col3.metric("🥜 Oilseed Yield (Best)", "Madhya Pradesh", "↑ 6.1%")


# --- Load Data ---
@st.cache_data
def load_data():
    return pd.read_csv("Data-Science-learning-path\Mini_Project_2(AgriData_Explorer)Git\\agri_data.csv")  

agri_df = load_data()
# ---Dropdown Options ---
chart_options = {
    "Top 7 Rice Producing States": "chart1",
    "Top 5 Wheat Producing States and Their Production Percentages (Bar Chart)": "chart2",
    "Top 5 States in Oilseed Production": "chart3",
    "Top 7 Sunflower Producing States": "chart4",
    "India's Sugarcane Production Over the Last 50 Years": "chart5",
    "Rice vs. Wheat Production Over the Last 50 Years": "chart6",
    "Rice Production in West Bengal by District": "chart7",
    "Top 10 Years of Wheat Production in Uttar Pradesh": "chart8",
    "Millet Production Over the Last 50 Years": "chart9",
    "Sorghum Production (Kharif and Rabi) by Region": "chart10",
    "Top 7 States in Groundnut Production": "chart11",
    "Soybean Production and Yield Efficiency by Top 5 States": "chart12",
    "Oilseed Production Across Major States": "chart13",
    "Impact of Area Cultivated on Rice, Wheat, and Maize Production": "chart14",
    "Rice vs. Wheat Yield Across States": "chart15"
}

# Slightly wider dropdown without using columns
st.markdown("### 📊 Select the Chart to Display")
selected_chart = st.selectbox(
    "",
    list(chart_options.keys()),
    key="chart_selector"
)



# --- Chart 1 Function ---
def chart_1():
    # Top 7 Rice Producing States
    q1_df = agri_df.groupby('State Name')['RICE PRODUCTION (1000 tons)'].sum().sort_values(ascending=False).head(7)

    fig1 = px.bar(
        q1_df,
        x=q1_df.index,
        y='RICE PRODUCTION (1000 tons)',
        title='Top 7 Rice Producing States',
        color=q1_df.index
    )
    fig1.update_layout(
        title_font=dict(color='#FF6F61', size=22),
        xaxis_title=dict(text="State Name", font=dict(color='#999999', size=17)),
        yaxis_title=dict(text="RICE PRODUCTION (1000 tons)", font=dict(color='#999999', size=17)),
        bargap=0.5,
        template="plotly_dark",
        paper_bgcolor="black",
        plot_bgcolor="black",
        shapes=[dict(
            type="rect", xref="paper", yref="paper",
            x0=0, y0=0, x1=1, y1=1,
            line=dict(color="#4d4d4d", width=1),
            layer="below"
        )],
        margin=dict(l=50, r=50, t=80, b=50)
    )
    fig1.update_layout(height=500)  # control height

    st.plotly_chart(fig1, use_container_width=True)

    # Optional: Show data table
    with st.expander("📄 View Raw Data"):
        st.dataframe(q1_df)
        
    # Download button for this chart's data 
    csv_data = q1_df.to_csv(index=False).encode('utf-8')
    st.download_button(
    label="⬇️ Download CSV",
    data=csv_data,
    file_name='Top 7 Rice Producing States data.csv',
    mime='text/csv'
)


# --- Chart 2 Function ---
def chart_2():
    # Top 5 Wheat Producing States with Bar and Pie Chart
    q2_df = agri_df.groupby('State Name')['WHEAT PRODUCTION (1000 tons)'] \
                   .sum().sort_values(ascending=False).head(5)

    # Bar Chart
    fig2 = px.bar(
        q2_df,
        x=q2_df.index,
        y='WHEAT PRODUCTION (1000 tons)',
        title='Top 5 Wheat Producing States (Bar Chart)',
        color=q2_df.index
    )
    fig2.update_layout(
        title_font=dict(color='#FF6F61', size=22),
        xaxis_title=dict(text="State Name", font=dict(color='#999999', size=17)),
        yaxis_title=dict(text="WHEAT PRODUCTION (1000 tons)", font=dict(color='#999999', size=17)),
        bargap=0.6,
        template="plotly_dark",
        paper_bgcolor="black",
        plot_bgcolor="black",
        shapes=[dict(
            type="rect", xref="paper", yref="paper",
            x0=0, y0=0, x1=1, y1=1,
            line=dict(color="#4d4d4d", width=1),
            layer="below"
        )],
        margin=dict(l=50, r=50, t=80, b=50),
        height=500
    )

    st.plotly_chart(fig2, use_container_width=True)

    # Pie Chart Section Title
    st.markdown("### 📊 Wheat Production Share (Pie Chart)")

    # Prepare data for Pie Chart
    q2_df = q2_df.reset_index()

    # Pie Chart
    fig2_1 = px.pie(
        q2_df,
        values='WHEAT PRODUCTION (1000 tons)',
        names='State Name',
        title='Top 5 Wheat Producing States (Pie Chart)',
        hole=0.3
    )
    fig2_1.update_traces(
        textinfo='percent+label'  # Show percent + label on pie
    )
    fig2_1.update_layout(
        title_font=dict(color='#FF6F61', size=22),
        template="plotly_dark",
        paper_bgcolor="black",
        plot_bgcolor="black",
        legend_title_text='State Name',
        shapes=[dict(
            type="path", xref="paper", yref="paper",
            x0=1, y0=1, x1=1, y1=1,
            line=dict(color="#4d4d4d", width=1),
            layer="below"
        )],
        margin=dict(l=50, r=50, t=80, b=50),
        height=450
    )

    st.plotly_chart(fig2_1, use_container_width=True)
        # Download button
    st.download_button(
    label="📥 Download this data as CSV",
    data=q2_df.to_csv(index=False),
    file_name="sugarcane_production_last_50_years.csv",
    mime="text/csv")



# --- Chart 3 Function ---
def chart_3():
    # Oilseed Production by Top 5 States
    q3_df = agri_df.groupby('State Name')['OILSEEDS PRODUCTION (1000 tons)'].sum().sort_values(ascending=False).head(5)

    fig3 = px.bar(
        q3_df,
        x=q3_df.index,
        y='OILSEEDS PRODUCTION (1000 tons)',
        title='Top 5 Oilseed Producing States',
        color=q3_df.index
    )
    fig3.update_layout(
        title_font=dict(color='#FF6F61', size=22),
        xaxis_title=dict(text="State Name", font=dict(color='#999999', size=17)),
        yaxis_title=dict(text="OILSEEDS PRODUCTION (1000 tons)", font=dict(color='#999999', size=17)),
        bargap=0.6,
        template="plotly_dark",
        paper_bgcolor="black",
        plot_bgcolor="black",
        shapes=[dict(
            type="rect", xref="paper", yref="paper",
            x0=0, y0=0, x1=1, y1=1,
            line=dict(color="#4d4d4d", width=1),
            layer="below"
        )],
        margin=dict(l=50, r=50, t=80, b=50)
    )
    fig3.update_layout(height=500)  # control height

    st.plotly_chart(fig3, use_container_width=True)
        # Download button
    st.download_button(
    label="📥 Download this data as CSV",
    data=q3_df.to_csv(index=False),
    file_name="sugarcane_production_last_50_years.csv",
    mime="text/csv")


# --- Chart 4 Function ---
def chart_4():
    # Top 7 Sunflower Producing States
    q4_df = agri_df.groupby('State Name')['SUNFLOWER PRODUCTION (1000 tons)'].sum().sort_values(ascending=False).head(7)

    fig4 = px.bar(
        q4_df,
        x=q4_df.index,
        y='SUNFLOWER PRODUCTION (1000 tons)',
        title='Top 7 Sunflower Producing States',
        color=q4_df.index
    )
    fig4.update_layout(
        title_font=dict(color='#FF6F61', size=22),
        xaxis_title=dict(text="State Name", font=dict(color='#999999', size=17)),
        yaxis_title=dict(text="SUNFLOWER PRODUCTION (1000 tons)", font=dict(color='#999999', size=17)),
        bargap=0.5,
        template="plotly_dark",
        paper_bgcolor="black",
        plot_bgcolor="black",
        shapes=[dict(
            type="rect", xref="paper", yref="paper",
            x0=0, y0=0, x1=1, y1=1,
            line=dict(color="#4d4d4d", width=1),
            layer="below"
        )],
        margin=dict(l=50, r=50, t=80, b=50)
    )
    fig4.update_layout(height=500)  # control height

    st.plotly_chart(fig4, use_container_width=True)
        # Download button
    st.download_button(
    label="📥 Download this data as CSV",
    data=q4_df.to_csv(index=False),
    file_name="sugarcane_production_last_50_years.csv",
    mime="text/csv")


def chart_5():
    # 5. India's Sugarcane Production from Last 50 Years (Line Plot)
    q5_df = agri_df.groupby('Year')['SUGARCANE PRODUCTION (1000 tons)'].sum().reset_index().tail(50)

    fig5 = px.line(
        q5_df,
        x='Year',
        y='SUGARCANE PRODUCTION (1000 tons)',
        title="India's Sugarcane Production (Last 50 Years)",
        labels={
            'Year': 'Year',
            'SUGARCANE PRODUCTION (1000 tons)': 'Production (1000 tons)'
        },
        markers=True,
        color_discrete_sequence=['#00B4D8']
    )

    fig5.update_layout(
        title_font=dict(color='#FF6F61', size=22),
        xaxis_title=dict(text='Year', font=dict(color='#999999', size=17)),
        yaxis_title=dict(text='Production (1000 tons)', font=dict(color='#999999', size=17)),
        hovermode="x unified",
        template="plotly_dark",
        paper_bgcolor="black",
        plot_bgcolor="black",
        shapes=[dict(
            type="rect", xref="paper", yref="paper",
            x0=0, y0=0, x1=1, y1=1,
            line=dict(color="#4d4d4d", width=1),
            layer="below"
        )],
        margin=dict(l=50, r=50, t=80, b=50)
    )

    max_year = q5_df.loc[q5_df['SUGARCANE PRODUCTION (1000 tons)'].idxmax(), 'Year']
    max_val = q5_df['SUGARCANE PRODUCTION (1000 tons)'].max()

    fig5.add_annotation(
        x=max_year,
        y=max_val,
        text="Peak Sugarcane",
        showarrow=True,
        arrowhead=2,
        font=dict(color='white'),
        bgcolor="#333",
        bordercolor="#666",
        borderwidth=1
    )
    fig5.update_layout(height=550)  # control height

    st.plotly_chart(fig5, use_container_width=True)
        # Download button
    st.download_button(
    label="📥 Download this data as CSV",
    data=q5_df.to_csv(index=False),
    file_name="sugarcane_production_last_50_years.csv",
    mime="text/csv"
)



def chart_6():
    # 6. Rice Production Vs Wheat Production (Last 50 Years)
    q6_df = agri_df.groupby('Year')[['RICE PRODUCTION (1000 tons)', 'WHEAT PRODUCTION (1000 tons)']].sum().tail(50).reset_index()

    fig6 = px.line(
        q6_df,
        x='Year',
        y=['RICE PRODUCTION (1000 tons)', 'WHEAT PRODUCTION (1000 tons)'],
        title="Rice vs Wheat Production (Last 50 Years)",
        markers=True
    )

    fig6.update_layout(
        title_font=dict(color='#FF6F61', size=22),
        xaxis_title=dict(text='Year', font=dict(color='#999999', size=17)),
        yaxis_title=dict(text='Production (1000 tons)', font=dict(color='#999999', size=17)),
        legend_title_text='Crop',
        hovermode="x unified",
        template="plotly_dark",
        paper_bgcolor="black",
        plot_bgcolor="black",
        shapes=[dict(
            type="rect", xref="paper", yref="paper",
            x0=0, y0=0, x1=1, y1=1,
            line=dict(color="#4d4d4d", width=1),
            layer="below"
        )],
        margin=dict(l=50, r=50, t=80, b=50)
    )

    max_year_rice = q6_df.loc[q6_df['RICE PRODUCTION (1000 tons)'].idxmax(), 'Year']
    max_val_rice = q6_df['RICE PRODUCTION (1000 tons)'].max()

    fig6.add_annotation(
        x=max_year_rice,
        y=max_val_rice,
        text="Peak Rice",
        showarrow=True,
        arrowhead=2,
        font=dict(color='white'),
        bgcolor="#333",
        bordercolor="#666",
        borderwidth=1
    )

    max_year_wheat = q6_df.loc[q6_df['WHEAT PRODUCTION (1000 tons)'].idxmax(), 'Year']
    max_val_wheat = q6_df['WHEAT PRODUCTION (1000 tons)'].max()

    fig6.add_annotation(
        x=max_year_wheat,
        y=max_val_wheat,
        text="Peak Wheat",
        showarrow=True,
        arrowhead=2,
        ax=80,
        ay=-20,
        font=dict(color='white'),
        bgcolor="#333",
        bordercolor="#666",
        borderwidth=1
    )
    fig6.update_layout(height=550)  # control height

    st.plotly_chart(fig6, use_container_width=True)
        # Download button
    st.download_button(
    label="📥 Download this data as CSV",
    data=q6_df.to_csv(index=False),
    file_name="sugarcane_production_last_50_years.csv",
    mime="text/csv")


def chart_7():
    # 7. Rice Production by West Bengal Districts
    q7_df = agri_df[agri_df['State Name'] == 'West Bengal'].groupby('Dist Name')['RICE PRODUCTION (1000 tons)'].sum().sort_values(ascending=False)

    fig7 = px.bar(
        q7_df,
        x=q7_df.index,
        y='RICE PRODUCTION (1000 tons)',
        title='Rice Production by Districts (West Bengal)',
        color=q7_df.index
    )

    fig7.update_layout(
        title_font=dict(color='#FF6F61', size=22),
        xaxis_title=dict(text='District Name', font=dict(color='#999999', size=17)),
        yaxis_title=dict(text='RICE PRODUCTION (1000 tons)', font=dict(color='#999999', size=17)),
        bargap=0.5,
        template="plotly_dark",
        paper_bgcolor="black",
        plot_bgcolor="black",
        shapes=[dict(
            type="rect", xref="paper", yref="paper",
            x0=0, y0=0, x1=1, y1=1,
            line=dict(color="#4d4d4d", width=1),
            layer="below"
        )],
        margin=dict(l=50, r=50, t=80, b=50)
    )
    fig7.update_layout(height=500)  # control height

    st.plotly_chart(fig7, use_container_width=True)
        # Download button
    st.download_button(
    label="📥 Download this data as CSV",
    data=q7_df.to_csv(index=False),
    file_name="sugarcane_production_last_50_years.csv",
    mime="text/csv")


def chart_8():
    # 8. Top 10 Wheat Production Years from Uttar Pradesh
    q8_df = agri_df[agri_df['State Name'] == 'Uttar Pradesh'].groupby('Year')['WHEAT PRODUCTION (1000 tons)'].sum().sort_values(ascending=False).head(10)

    fig8 = px.bar(
        q8_df,
        x=q8_df.index,
        y='WHEAT PRODUCTION (1000 tons)',
        title='Top 10 Wheat Production Years (Uttar Pradesh)',
        color=q8_df.index
    )

    fig8.update_layout(
        title_font=dict(color='#FF6F61', size=22),
        xaxis_title=dict(text='Year', font=dict(color='#999999', size=17)),
        yaxis_title=dict(text='WHEAT PRODUCTION (1000 tons)', font=dict(color='#999999', size=17)),
        bargap=0.5,
        template="plotly_dark",
        paper_bgcolor="black",
        plot_bgcolor="black",
        shapes=[dict(
            type="rect", xref="paper", yref="paper",
            x0=0, y0=0, x1=1, y1=1,
            line=dict(color="#4d4d4d", width=1),
            layer="below"
        )],
        margin=dict(l=50, r=50, t=80, b=50)
    )
    fig8.update_layout(height=500)  # control height

    st.plotly_chart(fig8, use_container_width=True)
        # Download button
    st.download_button(
    label="📥 Download this data as CSV",
    data=q8_df.to_csv(index=False),
    file_name="sugarcane_production_last_50_years.csv",
    mime="text/csv")


def chart_9():
    # Millet Production (Last 50 Years)
    q9_df = agri_df.groupby('Year')[['PEARL MILLET PRODUCTION (1000 tons)', 'FINGER MILLET PRODUCTION (1000 tons)']].sum().tail(50)

    fig9 = px.line(
        q9_df,
        x=q9_df.index,
        y=['PEARL MILLET PRODUCTION (1000 tons)', 'FINGER MILLET PRODUCTION (1000 tons)'],
        title="Millet Production (Last 50 Years)",
        markers=True
    )

    fig9.update_layout(
        title_font=dict(color='#FF6F61', size=22),
        xaxis_title=dict(text='Year', font=dict(color='#999999', size=17)),
        yaxis_title=dict(text='Production (1000 tons)', font=dict(color='#999999', size=17)),
        legend_title_text='Crop',
        hovermode="x unified",
        template="plotly_dark",
        paper_bgcolor="black",
        plot_bgcolor="black",
        shapes=[dict(
            type="rect", xref="paper", yref="paper",
            x0=0, y0=0, x1=1, y1=1,
            line=dict(color="#4d4d4d", width=1), layer="below"
        )],
        margin=dict(l=50, r=50, t=80, b=50)
    )

    # Annotate peak Pearl Millet
    max_year = q9_df['PEARL MILLET PRODUCTION (1000 tons)'].idxmax()
    max_val = q9_df['PEARL MILLET PRODUCTION (1000 tons)'].max()
    fig9.add_annotation(
        x=max_year, y=max_val,
        text="Peak Pearl Millet", showarrow=True, arrowhead=2,
        font=dict(color='white'), bgcolor="#333",
        bordercolor="#666", borderwidth=1,
    )

    # Annotate peak Finger Millet
    max_year = q9_df['FINGER MILLET PRODUCTION (1000 tons)'].idxmax()
    max_val = q9_df['FINGER MILLET PRODUCTION (1000 tons)'].max()
    fig9.add_annotation(
        x=max_year, y=max_val,
        text="Peak Finger Millet", showarrow=True, arrowhead=2,
        font=dict(color='white'), bgcolor="#333",
        bordercolor="#666", borderwidth=1,
    )

    fig9.update_layout(height=550)  # control height

    st.plotly_chart(fig9, use_container_width=True)
        # Download button
    st.download_button(
    label="📥 Download this data as CSV",
    data=q9_df.to_csv(index=False),
    file_name="sugarcane_production_last_50_years.csv",
    mime="text/csv")


def chart_10():

    #Have a doubt

    #fig10.update_layout(height=500)  # control height

    st.plotly_chart(fig10, use_container_width=True)
        # Download button
    st.download_button(
    label="📥 Download this data as CSV",
    data=q10_df.to_csv(index=False),
    file_name="sugarcane_production_last_50_years.csv",
    mime="text/csv")


def chart_11():
    # Top 7 States for Groundnut Production
    q11_df = agri_df.groupby('State Name')['GROUNDNUT PRODUCTION (1000 tons)'].sum().sort_values(ascending=False).head(7)

    fig11 = px.bar(
        q11_df,
        x=q11_df.index,
        y='GROUNDNUT PRODUCTION (1000 tons)',
        title='Top 7 States for Groundnut Production',
        color=q11_df.index
    )

    fig11.update_layout(
        title_font=dict(color='#FF6F61', size=22),
        xaxis_title=dict(text='State Name', font=dict(color='#999999', size=17)),
        yaxis_title=dict(text='GROUNDNUT PRODUCTION (1000 tons)', font=dict(color='#999999', size=17)),
        bargap=0.7,
        template="plotly_dark",
        paper_bgcolor="black",
        plot_bgcolor="black",
        shapes=[dict(
            type="rect", xref="paper", yref="paper",
            x0=0, y0=0, x1=1, y1=1,
            line=dict(color="#4d4d4d", width=1), layer="below"
        )],
        margin=dict(l=50, r=50, t=80, b=50)
    )
    fig11.update_layout(height=550)  # control height

    st.plotly_chart(fig11, use_container_width=True)
        # Download button
    st.download_button(
    label="📥 Download this data as CSV",
    data=q11_df.to_csv(index=False),
    file_name="sugarcane_production_last_50_years.csv",
    mime="text/csv")


def chart_12():
    # Soybean Production by Top 5 States and Yield Efficiency
    q12_df = agri_df.groupby('State Name')[
        ['SOYABEAN PRODUCTION (1000 tons)', 'SOYABEAN YIELD (Kg per ha)']
    ].sum().sort_values(by='SOYABEAN YIELD (Kg per ha)', ascending=False).head(5)

    fig12 = px.bar(
        q12_df,
        x=q12_df.index,
        y=['SOYABEAN PRODUCTION (1000 tons)', 'SOYABEAN YIELD (Kg per ha)'],
        title='Soybean Production by Top 5 States and Yield Efficiency',
        barmode='group',
        color_discrete_sequence=['#00B4D8', '#F9A825'],
        labels={"variable": "Soyabean Production & Yield"}
    )

    fig12.update_layout(
        title_font=dict(color='#FF6F61', size=22),
        xaxis_title=dict(text='State Name', font=dict(color='#999999', size=17)),
        yaxis_title=dict(text='Production & Yield', font=dict(color='#999999', size=17)),
        bargap=0.6,
        template="plotly_dark",
        paper_bgcolor="black",
        plot_bgcolor="black",
        shapes=[dict(
            type="rect", xref="paper", yref="paper",
            x0=0, y0=0, x1=1, y1=1,
            line=dict(color="#4d4d4d", width=1), layer="below"
        )],
        margin=dict(l=50, r=50, t=80, b=50),
        yaxis=dict(tickmode='linear', dtick=200000),
        height=500
    )

    st.plotly_chart(fig12, use_container_width=True)
        # Download button
    st.download_button(
    label="📥 Download this data as CSV",
    data=q12_df.to_csv(index=False),
    file_name="sugarcane_production_last_50_years.csv",
    mime="text/csv")



def chart_13():
    # Oilseed Production in Major States
    q13_df = agri_df.groupby('State Name')['OILSEEDS PRODUCTION (1000 tons)'].sum().sort_values(ascending=False).head(5)

    fig13 = px.bar(
        q13_df,
        x=q13_df.index,
        y='OILSEEDS PRODUCTION (1000 tons)',
        title='Oilseed Production in Major States',
        color=q13_df.index
    )

    fig13.update_layout(
        width=1000,
        height=600,
        title_font=dict(color='#FF6F61', size=22),
        xaxis_title=dict(text='State Name', font=dict(color='#999999', size=17)),
        yaxis_title=dict(text='OILSEEDS PRODUCTION (1000 tons)', font=dict(color='#999999', size=17)),
        bargap=0.8,
        template="plotly_dark",
        barmode='group',
        paper_bgcolor="black",
        plot_bgcolor="black",
        shapes=[dict(
            type="rect", xref="paper", yref="paper",
            x0=0, y0=0, x1=1, y1=1,
            line=dict(color="#4d4d4d", width=1), layer="below"
        )],
        margin=dict(l=50, r=50, t=80, b=50)
    )
    fig13.update_layout(height=550)  # control height

    st.plotly_chart(fig13, use_container_width=True)
        # Download button
    st.download_button(
    label="📥 Download this data as CSV",
    data=q13_df.to_csv(index=False),
    file_name="sugarcane_production_last_50_years.csv",
    mime="text/csv")

def chart_14():
    # Chart 14: Impact of Area Cultivated on Production (Rice, Wheat, Maize)

    q14_df = agri_df.groupby(['Year', 'State Name'])[
        ['RICE PRODUCTION (1000 tons)', 'RICE YIELD (Kg per ha)',
         'WHEAT PRODUCTION (1000 tons)', 'WHEAT YIELD (Kg per ha)',
         'MAIZE PRODUCTION (1000 tons)', 'MAIZE YIELD (Kg per ha)']
    ].mean().reset_index()

    yearly_df = q14_df.groupby('Year')[
        ['RICE PRODUCTION (1000 tons)', 'WHEAT PRODUCTION (1000 tons)', 'MAIZE PRODUCTION (1000 tons)']
    ].sum().reset_index()

    fig14 = px.line(
        yearly_df,
        x='Year',
        y=['RICE PRODUCTION (1000 tons)', 'WHEAT PRODUCTION (1000 tons)', 'MAIZE PRODUCTION (1000 tons)'],
        title='Impact of Area Cultivated on Production (Rice, Wheat, Maize)',
        labels={'value': 'Production (1000 tons)', 'variable': 'Crop'},
        markers=True
    )

    fig14.update_layout(
        title_font=dict(color='#FF6F61', size=22),
        xaxis_title=dict(text='Year', font=dict(color='#999999', size=17)),
        yaxis_title=dict(text='Production (1000 tons)', font=dict(color='#999999', size=17)),
        template="plotly_dark",
        hovermode="x unified",
        legend_title_text='Crop',
        paper_bgcolor="black",
        plot_bgcolor="black",
        shapes=[dict(
            type="rect", xref="paper", yref="paper",
            x0=0, y0=0, x1=1, y1=1,
            line=dict(color="#4d4d4d", width=1),
            layer="below"
        )],
        margin=dict(l=50, r=50, t=80, b=50)
    )

    for crop in ['RICE PRODUCTION (1000 tons)', 'WHEAT PRODUCTION (1000 tons)', 'MAIZE PRODUCTION (1000 tons)']:
        max_year = yearly_df.loc[yearly_df[crop].idxmax(), 'Year']
        max_val = yearly_df[crop].max()
        fig14.add_annotation(
            x=max_year, y=max_val,
            text=f"Peak {crop.split()[0]}",
            showarrow=True, arrowhead=2,
            font=dict(color='white'),
            bgcolor="#333", bordercolor="#666", borderwidth=1
        )
        fig14.update_layout(height=550)  # control height

    st.plotly_chart(fig14, use_container_width=True)
        # Download button
    st.download_button(
    label="📥 Download this data as CSV",
    data=q14_df.to_csv(index=False),
    file_name="sugarcane_production_last_50_years.csv",
    mime="text/csv")


def chart_15():
    # Chart 15: Rice vs. Wheat Yield Across States

    q15_df = agri_df.groupby('State Name')[
        ['RICE YIELD (Kg per ha)', 'WHEAT YIELD (Kg per ha)']
    ].sum()

    q15_df['Total_Yield'] = q15_df['RICE YIELD (Kg per ha)'] + q15_df['WHEAT YIELD (Kg per ha)']
    q15_df = q15_df.sort_values(by='Total_Yield', ascending=False)

    q15_df_melted = q15_df.drop(columns='Total_Yield').reset_index().melt(
        id_vars='State Name', var_name='Crop', value_name='Yield')

    fig15 = px.bar(
        q15_df_melted,
        x='State Name',
        y='Yield',
        color='Crop',
        barmode='group',
        title='Rice vs. Wheat Yield Across States',
        color_discrete_map={
            'RICE YIELD (Kg per ha)': '#00B4D8',
            'WHEAT YIELD (Kg per ha)': '#F9A825'
        }
    )

    fig15.update_layout(
        title_font=dict(color='#FF6F61', size=22),
        xaxis_title=dict(text='State Name', font=dict(color='#999999', size=17)),
        yaxis_title=dict(text='Yield (Kg per ha)', font=dict(color='#999999', size=17)),
        template="plotly_dark",
        bargap=0.4,
        paper_bgcolor="black",
        plot_bgcolor="black",
        shapes=[dict(
            type="rect", xref="paper", yref="paper",
            x0=0, y0=0, x1=1, y1=1,
            line=dict(color="#4d4d4d", width=1),
            layer="below"
        )],
        margin=dict(l=50, r=50, t=80, b=50),
        yaxis=dict(tickmode='linear', dtick=1000000)
    )
    fig15.update_layout(height=500)  # control height

    st.plotly_chart(fig15, use_container_width=True)
        # Download button
    st.download_button(
    label="📥 Download this data as CSV",
    data=q15_df.to_csv(index=False),
    file_name="sugarcane_production_last_50_years.csv",
    mime="text/csv")


# --- Chart Dispatcher ---
if chart_options[selected_chart] == "chart1":
        # 💎 Rice Metrics Section
    st.markdown("### 📊 Key Metrics – Rice Production")
    st.markdown("##### Last Reported Rice Production by Top 7 States")

# Calculate differences
    top_values = [544232.26, 445597.62, 335040.10, 315185.40, 291201.51, 282532.93, 231759]
    diffs = [round(top_values[0] - v, 2) for v in top_values[1:]]

# Show metrics with changes
    col1, col2, col3 = st.columns(3)
    col1.metric("🥇 West Bengal", "544.2K Tons", "—")
    col2.metric("🥈 Uttar Pradesh", "445.6K Tons", f"↓ {diffs[0]/1000:.1f}K Tons")
    col3.metric("🥉 Punjab", "335.0K Tons", f"↓ {diffs[1]/1000:.1f}K Tons")

    chart_1()


elif chart_options[selected_chart] == "chart2":
    chart_2()
elif chart_options[selected_chart] == "chart3":
    chart_3()
elif chart_options[selected_chart] == "chart4":
    chart_4()
elif chart_options[selected_chart] == "chart5":
    chart_5()
elif chart_options[selected_chart] == "chart6":
    chart_6()
elif chart_options[selected_chart] == "chart7":
    chart_7()
elif chart_options[selected_chart] == "chart8":
    chart_8()
elif chart_options[selected_chart] == "chart9":
    chart_9()
elif chart_options[selected_chart] == "chart10":
    chart_10()
elif chart_options[selected_chart] == "chart11":
    chart_11()
elif chart_options[selected_chart] == "chart12":
    chart_12()
elif chart_options[selected_chart] == "chart13":
    chart_13()
elif chart_options[selected_chart] == "chart14":
    chart_14()
elif chart_options[selected_chart] == "chart15":
    chart_15()


    # Footer
st.markdown("""
    <hr>
    <div style="text-align: center;">
        <p style="font-size: 13px;">🚨 SecureCheck | Built by <strong>Infant Joshva</strong></p>
        <a href="https://github.com/Infant-Joshva" target="_blank" style="text-decoration: none; margin: 0 10px;">🐙 GitHub</a>
        <a href="https://www.linkedin.com/in/infant-joshva" target="_blank" style="text-decoration: none; margin: 0 10px;">🔗 LinkedIn</a>
        <a href="mailto:infantjoshva46@gmail.com" style="text-decoration: none; margin: 0 10px;">📩 Contact</a>
    </div>
""", unsafe_allow_html=True)
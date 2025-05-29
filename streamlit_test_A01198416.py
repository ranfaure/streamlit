import pandas as pd
import streamlit as st

#import database
sellers = pd.read_excel("sellers.xlsx")

# 1. Display the table and filter it by Region.
st.title("SALES INFORMATION") # Site title

st.subheader("INFORMATION") # Name of the first chart
st.dataframe(sellers) # Show the chart

st.subheader("REGION FILTER") #Name of the second chart
reg_selected = st.selectbox("CHOOSE REGION", sellers["REGION"].unique()) # Shows the region filter
sellers_fil = sellers[sellers["REGION"] == reg_selected] # Creating a filtered database
st.dataframe(sellers_fil) # Show the updated df

# 2. Display graphs of Units Sold, Total Sales, and Average Sales.
import altair as alt

# Units Sold
st.subheader("UNITS SOLD PER SELLER")
bar_US = alt.Chart(sellers_fil).mark_bar(color='white').encode( x = "NOMBRE:N", y = "UNIDADES VENDIDAS:Q",
    tooltip = ["NOMBRE", "UNIDADES VENDIDAS"]).properties(width = 400) # Chart properties
st.altair_chart(bar_US) # Chart display

st.subheader("TOTAL SALES")
bar_TS = alt.Chart(sellers_fil).mark_bar(color='purple').encode(x="NOMBRE:N", y="VENTAS TOTALES:Q",
    tooltip=["NOMBRE", "VENTAS TOTALES"]).properties(width=600) # Chart properties
st.altair_chart(bar_TS) # Chart display

st.subheader("AVERAGE SALES IN REGION")
avg = sellers_fil["VENTAS TOTALES"].mean() # AVG calculation
st.metric(label=f"AVG SALES IN REGION: {reg_selected}", value=f"${avg:,.2f}") # Region name and AVG sales



# 3. Display data for a specific vendor.
sellers["NOMBRE COMPLETO"] = sellers["NOMBRE"] + " " + sellers["APELLIDO"]

st.title("VENDOR SALES") #Title of the section

st.subheader("VENDOR")#Title of the subsection
sel_vendor = st.selectbox("CHOOSE VENDOR", sellers["NOMBRE COMPLETO"].unique()) # Selecting vendor

vendor_info= sellers[sellers["NOMBRE COMPLETO"] == sel_vendor]  # Data filtered by vendor

# Display the seller's info
st.write(f"INFORMATION OF **{sel_vendor}**")
st.dataframe(vendor_info)

us = vendor_info["UNIDADES VENDIDAS"].sum() #Information of each column
ts = vendor_info["VENTAS TOTALES"].sum()

st.write(f"**UNIDADES VENDIDAS:** {us}") # Display of information from the vendor
st.write(f"**VENTAS TOTALES:** ${ts:,.2f}")
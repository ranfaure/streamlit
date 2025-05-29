import pandas as pd
import streamlit as st
import altair as alt

# Exploration and formating
df = pd.read_excel("sellers.xlsx")
print(df.head())

#Display the table filtered by regions

st.title("Sales") #Title of the page

st.subheader("Full table") #Title of the first table in the page
st.dataframe(df) #Shows the table with the dataframe

st.subheader("Filter by region") #Title of the second table in the page
selected_region = st.selectbox("Pick a region", df["REGION"].unique()) #Displays the region picker
df_filtered = df[df["REGION"] == selected_region] #Aplies the filter in real time
st.dataframe(df_filtered) #Show the filtered dataframe

# Display graphs of Units Sold, Total Sales, and Average Sales.

# Bar graph for Units sold per seller
st.subheader("Units Sold per Seller")
bar_units = alt.Chart(df_filtered).mark_bar(color='aquamarine').encode(
    x = "NOMBRE:N",
    y = "UNIDADES VENDIDAS:Q",
    tooltip = ["NOMBRE", "UNIDADES VENDIDAS"] 
).properties(width = 600) # Specifying the properties of the chart, x and y axis names and size of the chart
st.altair_chart(bar_units) # Displays the chart

st.subheader("Total Sales per Seller")
bar_sales = alt.Chart(df_filtered).mark_bar(color='green').encode(
    x="NOMBRE:N",
    y="VENTAS TOTALES:Q",
    tooltip=["NOMBRE", "VENTAS TOTALES"]
).properties(width=600) # Specifying the properties of the chart, x and y axis names, and bar and chart characteristics.
st.altair_chart(bar_sales) # Displays the chart

st.subheader("Average Sales in Region")
avg_sales = df_filtered["VENTAS TOTALES"].mean() #Calculates the average sales of the region
st.metric(label=f"Average Sales in {selected_region}", value=f"${avg_sales:,.2f}") #Displays the name of the region and the value of its avg sales

#Created a new column to facilitate selection
df["NOMBRE COMPLETO"] = df["NOMBRE"] + " " + df["APELLIDO"]

# Specific seller information

st.title("Sales Dashboard")

st.subheader("Vendors")
selected_vendor = st.selectbox("Choose a vendor", df["NOMBRE COMPLETO"].unique()) #Using the information on the full name column to give options

# Filter data for the selected seller
vendor_data = df[df["NOMBRE COMPLETO"] == selected_vendor]

# Display the seller's infoo
st.write(f"Data for **{selected_vendor}**")
st.dataframe(vendor_data)

# Show metrics for the selected seller
units_sold = vendor_data["UNIDADES VENDIDAS"].sum() #Creating the variables for each metric
total_sales = vendor_data["VENTAS TOTALES"].sum()

st.write(f"**UNIDADES VENDIDAS:** {units_sold}") #Displaying the metrics
st.write(f"**VENTAS TOTALES:** ${total_sales:,.2f}")

#Thank you :)
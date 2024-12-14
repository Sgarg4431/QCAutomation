import streamlit as st
import pandas as pd
from datetime import datetime

st.title("QCing the Processed Sales File")

uploaded_file1 = st.file_uploader("Upload your processed CSV file here", type=["csv","tsv"])
uploaded_file2 = st.file_uploader("Upload your CSV file here", type=["csv","tsv"])

def processedFile(uploaded_file1,uploaded_file2):
    if uploaded_file1 and uploaded_file2:
        df=pd.read_csv(uploaded_file1,sep='\t')
        df_sales=pd.read_csv(uploaded_file2,sep='\t')
        

        # Overall Quantity
        print("Checking the Overall Quantity...")
        mask_qty=(df["quantity"]>=0)
        mask_qty2=(df_sales["quantity"]>=0)
        filtered_df_qty=df.loc[mask_qty]
        filtered_df_qty_sales=df_sales.loc[mask_qty2]
        total_qty=filtered_df_qty["quantity"].sum()
        total_qty_sales=filtered_df_qty_sales["quantity"].sum()
        print(f"Overall quantity is {total_qty}")   
        st.text(f"The Overall quantity sum in processed file is {total_qty}")
        st.text(f"The Overall quantity sum is {total_qty_sales}")

        # Checking for particular day
        print("Checking for particular day...")
        df["day"] = pd.to_datetime(df["day"])
        df["day"] = df['day'].dt.strftime('%Y-%m-%d')
        df_sales["day"] = pd.to_datetime(df_sales["day"])
        df_sales["day"] = df_sales['day'].dt.strftime('%Y-%m-%d')
        random_day=df["day"].sample(n=1).iloc[0]
        st.text(f"Checking for particular day...{random_day}")
        mask_day=(df["day"]==random_day) & (df["quantity"]>=0)
        mask_day2=(df_sales["day"]==random_day) & (df_sales["quantity"]>=0)
        filtered_df_day=df.loc[mask_day]
        filtered_df_day_sales=df_sales.loc[mask_day2]
        total_qty_day=filtered_df_day["quantity"].sum()
        total_qty_day_sales=filtered_df_day_sales["quantity"].sum()
        print(f"The sum of quantity in processed file at date ${random_day} is ${total_qty_day}")
        st.text(f"The sum of quantity at {random_day} in processed file is {total_qty_day}")
        st.text(f"The sum of quantity at {random_day} is {total_qty_day_sales}")
        
        # Checking for particular ean
        random_ean=df["ean"].sample(n=1).iloc[0]
        st.text(f"Checking for ean...{random_ean}")
        mask_ean=(df["ean"]==random_ean) & (df["quantity"]>=0)
        mask_ean2=(df_sales["ean"]==random_ean) & (df_sales["quantity"]>=0)
        filtered_df_ean=df.loc[mask_ean]
        filtered_df_ean_sales=df_sales.loc[mask_ean2]
        total_qty_ean=filtered_df_ean["quantity"].sum()
        total_qty_ean_sales=filtered_df_ean_sales["quantity"].sum()
        st.text(f"The sum of quantity for ean {random_ean} in processed file is {total_qty_ean}")
        st.text(f"The sum of quantity for ean {random_ean} is {total_qty_ean_sales}")

        # Checking for one channel
        random_channel=df["channel"].sample(n=1).iloc[0]
        st.text(f"Checking for channel...{random_channel}")
        mask_channel=(df["channel"]==random_channel) & (df["quantity"]>=0)
        mask_channel_sales=(df_sales["channel"]==random_channel) & (df_sales["quantity"]>=0)
        filtered_df_channel=df.loc[mask_channel]
        filtered_df_channel_sales=df_sales.loc[mask_channel_sales]
        total_qty_channel=filtered_df_channel["quantity"].sum()
        total_qty_channel_sales=filtered_df_channel_sales["quantity"].sum()
        st.text(f"The sum of quantity for ean {random_channel} in processed file is {total_qty_channel}")
        st.text(f"The sum of quantity for ean {random_channel} is {total_qty_channel_sales}")

        # Checking for one day and one ean 
        random_value_day=df["day"].sample(n=1).iloc[0]
        random_value_ean=df["ean"].sample(n=1).iloc[0]
        st.text(f"Checking for day:{random_value_day} and for ean:{random_value_ean} ")
        mask_final=(df["day"]==random_value_day) & (df["ean"]==random_value_ean) & (df["quantity"]>=0)
        mask_final_sales=(df_sales["day"]==random_value_day) & (df_sales["ean"]==random_value_ean) & (df_sales["quantity"]>=0)
        filtered_df_final=df.loc[mask_final]
        filtered_df_final_sales=df_sales.loc[mask_final_sales]
        total_qty_final=filtered_df_final["quantity"].sum()
        total_qty_final_sales=filtered_df_final_sales["quantity"].sum()
        st.text(f"The sum of quantity on {random_value_day} and for ean {random_value_ean} in processed file is {total_qty_final}")
        st.text(f"The sum of quantity on {random_value_day} and for ean {random_value_ean} is {total_qty_final_sales}")




    else:
        st.info("Please upload the valid CSV or TSV file")


processedFile(uploaded_file1,uploaded_file2)


# Exploratory Data Analysis (EDA) for Customer Loans in Finance
--------------------------------------------------------

# Overview
You currently work for a large financial institution, where managing loans is a critical component of business operations.

To ensure informed decisions are made about loan approvals and risk is efficiently managed, your task is to gain a comprehensive understanding of the loan portfolio data.

Your task is to perform exploratory data analysis on the loan portfolio, using various statistical and data visualisation techniques to uncover patterns, relationships, and anomalies in the loan data.

This information will enable the business to make more informed decisions about loan approvals, pricing, and risk management.

By conducting exploratory data analysis on the loan data, you aim to gain a deeper understanding of the risk and return associated with the business' loans.

Ultimately, your goal is to improve the performance and profitability of the loan portfolio.


# Table of Contents
1. [Installation Instructions](#Installation-Instructions)
2. [File Structure of the Project](#File-Structure-of-the-Project)
3. [Data Dictionary](#Data-Dictionary)
4. [License Information](#License-Information)


# Installation Instructions
Clone the repo and use Python to run the programs and files.

1. To clone the repository to your local machine:
   ```bash
   git clone https://github.com/lusl007/exploratory-data-analysis---customer-loans-in-finance929.git

2. Run the file 'db_utils.py' to get the csv file containing the loan payments data


# File Structure of the Project
- credentials.yaml - contains database credentials to connect to the database with web services
- db_utils.py - contains classes to
- data_transform.py - 
- EDA_Analysis.ipynb - 


# Data Dictionary
Below is a summary and description of all columns in the loan payments file:

- `id`: Unique id of the loan
- `member_id`: Id of the member to took out the loan
- `loan_amount`: Amount of loan the applicant received
- `funded_amount`: The total amount committed to the loan at that point in time
- `funded_amount_inv`: The total amount committed by investors for that loan at that point in time
- `term`: The number of monthly payments for the loan
- `int_rate (APR)`: Annual (APR) interest rate of the loan
- `instalment`: The monthly payment owned by the borrower. This is inclusive of the interest.
- `grade`: Loan company (LC) assigned loan grade
- `sub_grade`: LC assigned loan sub grade
- `employment_length`: Employment length in years
- `home_ownership`: The home ownership status provided by the borrower
- `annual_inc`: The annual income of the borrower
- `verification_status`: Indicates whether the borrowers income was verified by the LC or the income source was verified
- `issue_date`: Issue date of the loan
- `loan_status`: Current status of the loan
- `payment_plan`: Indicates if a payment plan is in place for the loan. Indication borrower is struggling to pay.
- `purpose`: A category provided by the borrower for the loan request
- `dti`: A ratio calculated using the borrower's total monthly debt payments on the total debt obligations, excluding mortgage and the requested LC loan, divided by the borrower’s self-reported monthly income
- `delinq_2yr`: The number of 30+ days past-due payments in the borrower's credit file for the past 2 years
- `earliest_credit_line`: The month the borrower's earliest reported credit line was opened
- `inq_last_6mths`: The number of inquiries in past 6 months (excluding auto and mortgage inquiries)
- `mths_since_last_record`: The number of months' since the last public record
- `open_accounts`: The number of open credit lines in the borrower's credit file
- `total_accounts`: The total number of credit lines currently in the borrower's credit file
- `out_prncp`: Remaining outstanding principal for total amount funded
- `out_prncp_inv`: Remaining outstanding principal for portion of total amount funded by investors
- `total_payment`: Payments received to date for total amount funded
- `total_rec_int`: Interest received to date
- `total_rec_late_fee`: Late fees received to date
- `recoveries`: Post charge off gross recovery
- `collection_recovery_fee`: Post charge off collection fee
- `last_payment_date`: Date on which last month payment was received
- `last_payment_amount`: Last total payment amount received
- `next_payment_date`: Next scheduled payment date
- `last_credit_pull_date`: The most recent month LC pulled credit for this loan
- `collections_12_mths_ex_med`: Number of collections in 12 months' excluding medical collections
- `mths_since_last_major_derog`: Months' since most recent 90-day or worse rating
- `policy_code`: Publicly available policy_code=1 new products not publicly available policy_code=2
- `application_type`: Indicates whether the loan is an individual application or a joint application with two co-borrowers


# License Information
Licensed under the [MIT](https://github.com/lusl007/hangman591/blob/main/LICENSE) license.

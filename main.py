# Import libraries
from sklearn.exceptions import DataConversionWarning
from scripts import pre_processing as prep
from scripts import exploration as exp
import pandas as pd
import warnings
import math

# Ignore warnings for automatic data conversion
warnings.simplefilter(action='ignore', category=DataConversionWarning)

# Import the data and read from Excel file
df = pd.read_csv('banking_campaign.csv')


# Perform binarisation for 'marital'
binarised_marital = prep.binarise_marital(df['marital'])


# Perform binarisation for 'job'
binarised_job = prep.binarise_job(df['job'])


# Create a combined data frame of pre-processed data for analysis
processed_df = pd.DataFrame({
    'Married': binarised_marital['married'],
    'Single': binarised_marital['single'],
    'Divorced': binarised_marital['divorced'],
    'Admin': binarised_job['admin'],
    'Blue-Collar': binarised_job['blue-collar'],
    'Entrepreneur': binarised_job['entrepreneur'],
    'Housemaid': binarised_job['housemaid'],
    'Management': binarised_job['management'],
    'Retired': binarised_job['retired'],
    'Self-Employed': binarised_job['self-employed'],
    'Services': binarised_job['services'],
    'Student': binarised_job['student'],
    'Technician': binarised_job['technician'],
    'Unemployed': binarised_job['unemployed'],
})

# Combine the original data to the processed data for analysis
concatenated_df = pd.concat([df, processed_df], axis=1, sort=False)

# Display a correlation matrix
exp.correlation_matrix(concatenated_df)

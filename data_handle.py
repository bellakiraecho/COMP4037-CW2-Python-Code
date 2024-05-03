import pandas as pd

# Load
data = pd.read_csv('Results_21Mar2022.csv')

# select
columns_of_interest = [
    'mean_ghgs', 'mean_land', 'mean_watscar', 'mean_eut',
    'mean_ghgs_ch4', 'mean_ghgs_n2o', 'mean_bio', 'mean_watuse', 'mean_acid',
    'sex', 'diet_group', 'age_group'
]
data = data[columns_of_interest]

# divide
grouped_data = data.groupby(['sex', 'diet_group', 'age_group'])

# calculate
statistics = grouped_data.agg({
    'mean_ghgs': ['mean', 'median', 'min', 'max'],
    'mean_land': ['mean', 'median', 'min', 'max'],
    'mean_watscar': ['mean', 'median', 'min', 'max'],
    'mean_eut': ['mean', 'median', 'min', 'max'],
    'mean_ghgs_ch4': ['mean', 'median', 'min', 'max'],
    'mean_ghgs_n2o': ['mean', 'median', 'min', 'max'],
    'mean_bio': ['mean', 'median', 'min', 'max'],
    'mean_watuse': ['mean', 'median', 'min', 'max'],
    'mean_acid': ['mean', 'median', 'min', 'max']
})

# change name
statistics.reset_index(inplace=True)

# regroup name
statistics.columns = ['_'.join(col).strip() if col[1] else col[0] for col in statistics.columns.values]

# save
statistics.to_csv('output.csv', index=False)

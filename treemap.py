import pandas as pd
import plotly.express as px

# Load data
data = pd.read_csv('output.csv')

# a bug from data handle, never mind :)
data.iloc[:, 3:] = data.iloc[:, 3:].apply(lambda x: x / 12)

# in order to make firgue readable
data['mean_watscar_mean'] = data['mean_watscar_mean'] / 1000
data['mean_bio_mean'] = data['mean_bio_mean'] / 10
data['mean_watuse_mean'] = data['mean_watuse_mean'] / 100
data['mean_ghgs_ch4_mean'] = data['mean_ghgs_ch4_mean'] * 10
data['mean_ghgs_n2o_mean'] = data['mean_ghgs_n2o_mean'] * 10

# better name
indicators = {
    'mean_ghgs_mean': 'GHG Mean',
    'mean_land_mean': 'Land Use Mean',
    'mean_watscar_mean': 'Water Scarcity Mean',
    'mean_eut_mean': 'Eutrophication Mean',
    'mean_ghgs_ch4_mean': 'GHG CH4 Mean',
    'mean_ghgs_n2o_mean': 'GHG N2O Mean',
    'mean_bio_mean': 'Biodiversity Mean',
    'mean_watuse_mean': 'Water Use Mean',
    'mean_acid_mean': 'Acidity Mean'
}

# which creat treemap
def create_treemap(data, top_level):
    path_data = pd.DataFrame()
    for key, name in indicators.items():
        data[name] = name + ': ' + data[key].round(2).astype(str)
        data[name + '_Path'] = data[top_level] + '/' + name
        temp_df = pd.DataFrame({
            'Top Level': data[top_level],  # make it same color
            'Path': data[name + '_Path'],
            'Value': data[key]
        })
        path_data = pd.concat([path_data, temp_df], ignore_index=True)

    fig = px.treemap(path_data, path=['Top Level', 'Path'], values='Value', color='Top Level',
                     color_discrete_map={"(?)": 'lightgrey'},
                     color_discrete_sequence=px.colors.qualitative.Pastel)
    fig.update_layout(
        margin=dict(t=50, l=25, r=25, b=25),
        font=dict(size=35, family="Arial, sans-serif")  # set font size
    )
    fig.update_traces(
        textinfo="label",
        textfont_size=35
    )
    fig.show()

# creat treemap sexaul
create_treemap(data, 'sex')

# creat treemap diet_group
create_treemap(data, 'diet_group')

# creat treemap age_group
create_treemap(data, 'age_group')
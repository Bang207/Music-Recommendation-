import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

df = pd.read_csv("data.csv", encoding="windows-1252", low_memory=False)

# Cleaning df
df.dropna(axis=1, thresh=1000, inplace=True)
df = df.drop(df.columns[[1, 7, 8, 10, 13]], axis=1)  # Remove irrelevant features
df['popularity'] = pd.to_numeric(df['popularity'], errors='coerce')
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
X = df.iloc[:, [0, 1, 3, 4, 5, 6, 7, 8, 10, 12]]  # This contains all our features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # We have now scaled our df to reduce the impact of outliers

recommender = NearestNeighbors(n_neighbors=11).fit(X_scaled)  # Training the model
distances, indices = recommender.kneighbors(X_scaled)
output = pd.DataFrame(indices)
output['name'] = df.iloc[:, 9]
output['artist'] = df.iloc[:, 2]


def getSong_recommendations(song, artist):
	recommendations = output.loc[(output.name == song) & (output.artist == artist), (output.columns != 'name') &
	                             (output.columns != 'artist')]

	return df.loc[list(recommendations.values[0])[1:], ['artists', 'name', 'release_date']]


if __name__ == '__main__':
	print(getSong_recommendations("Payphone", "['Maroon 5', 'Wiz Khalifa']"))

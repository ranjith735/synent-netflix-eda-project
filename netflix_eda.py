import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# LOAD DATASET
# =========================
df = pd.read_csv(
    r"C:\Users\RANJITH\Downloads\archive\netflix_titles.csv"
)

# =========================
# DISPLAY DATA
# =========================
print("First 5 Rows:")
print(df.head())

print("\nColumn Names:")
print(df.columns)

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# =========================
# DATA CLEANING
# =========================
df.drop_duplicates(inplace=True)

df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna(df["rating"].mode()[0])

# Convert date column
df["date_added"] = pd.to_datetime(
    df["date_added"],
    errors="coerce"
)

# =========================
# SUMMARY STATISTICS
# =========================
print("\nSummary Statistics:")
print(df.describe(include="all"))

# =========================
# VISUALIZATION 1
# Movies vs TV Shows
# =========================
plt.figure(figsize=(6, 4))

sns.countplot(
    x="type",
    data=df
)

plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")

plt.show()

# =========================
# VISUALIZATION 2
# Top Countries
# =========================
top_countries = df["country"].value_counts().head(10)

plt.figure(figsize=(12, 5))

top_countries.plot(kind="bar")

plt.title("Top 10 Countries")
plt.xlabel("Country")
plt.ylabel("Count")

plt.xticks(rotation=45)

plt.show()

# =========================
# VISUALIZATION 3
# Ratings Distribution
# =========================
plt.figure(figsize=(10, 6))

sns.countplot(
    y="rating",
    data=df,
    order=df["rating"].value_counts().index
)

plt.title("Ratings Distribution")

plt.show()

# =========================
# VISUALIZATION 4
# Content Added Over Years
# =========================
df["year_added"] = df["date_added"].dt.year

plt.figure(figsize=(12, 6))

sns.countplot(
    x="year_added",
    data=df,
    order=sorted(df["year_added"].dropna().unique())
)

plt.xticks(rotation=90)

plt.title("Content Added Over Years")

plt.show()

# =========================
# VISUALIZATION 5
# Top Genres
# =========================
genres = df["listed_in"].str.split(
    ", ",
    expand=True
).stack()

plt.figure(figsize=(12, 6))

genres.value_counts().head(10).plot(
    kind="bar"
)

plt.title("Top 10 Genres")

plt.xticks(rotation=45)

plt.show()

print("\nEDA Completed Successfully!")
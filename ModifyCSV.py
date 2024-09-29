import pandas as pd

# Load CSV file
df = pd.read_csv("Project_1\\Project_1_Intro_To_ML_02450\\Data\\Sport car price.csv")

# Define the car manufacturer country mapping
manufacturer_country = {
    'Porsche': 'Germany',
    'Audi': 'Germany',
    'BMW': 'Germany',
    'Mercedes-Benz': 'Germany',
    'Mercedes-AMG': 'Germany',
    'Lamborghini': 'Italy',
    'Ferrari': 'Italy',
    'Maserati': 'Italy',
    'Pagani': 'Italy',
    'Alfa Romeo': 'Italy',
    'Pininfarina': 'Italy',
    'Nissan': 'Japan',
    'Lexus': 'Japan',
    'Subaru': 'Japan',
    'Acura': 'Japan',
    'Toyota': 'Japan',
    'Mazda': 'Japan',
    'Aston Martin': 'UK',
    'Jaguar': 'UK',
    'Lotus': 'UK',
    'McLaren': 'UK',
    'Bentley': 'UK',
    'Rolls-Royce': 'UK',
    'Ariel': 'UK',
    'TVR': 'UK',
    'Ultima': 'UK',
    'Chevrolet': 'USA',
    'Ford': 'USA',
    'Dodge': 'USA',
    'Tesla': 'USA',
    'Shelby': 'USA',
    'Bugatti': 'France',
    'Alpine': 'France',
    'Koenigsegg': 'Sweden',
    'Polestar': 'Sweden',
    'Rimac': 'Croatia',
    'W Motors': 'UAE',
    'Kia': 'South Korea',
}

print(f"There are: {len(df['Car Make'])} cars in the dataset")

df['Country'] = df['Car Make'].map(manufacturer_country)

print(f"There are: {len(df['Country'])} cars in the new dataset")

df.to_csv('car_data_with_country.csv', index=False)

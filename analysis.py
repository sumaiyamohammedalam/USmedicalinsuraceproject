# Import necessary library
import csv

# -----------------------------
# Step 1: Load the CSV dataset
# -----------------------------
insurance_data = []

with open('insurance.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Convert numerical values to floats or ints
        row_data = {
            'age': int(row['age']),
            'sex': row['sex'],
            'bmi': float(row['bmi']),
            'children': int(row['children']),
            'smoker': row['smoker'],
            'region': row['region'],
            'charges': float(row['charges'])
        }
        insurance_data.append(row_data)

# -----------------------------
# Step 2: Define analysis functions
# -----------------------------
def average_charge(data):
    """Calculate the average insurance charge."""
    total = sum(row['charges'] for row in data)
    return total / len(data)

def average_charge_by_smoker(data):
    """Calculate average charges for smokers and non-smokers."""
    smokers = [row['charges'] for row in data if row['smoker'] == 'yes']
    non_smokers = [row['charges'] for row in data if row['smoker'] == 'no']
    return {
        "smokers": sum(smokers)/len(smokers) if smokers else 0,
        "non_smokers": sum(non_smokers)/len(non_smokers) if non_smokers else 0
    }

def average_charge_by_region(data):
    """Calculate average charges for each region."""
    region_totals = {}
    region_counts = {}
    for row in data:
        region = row['region']
        region_totals[region] = region_totals.get(region, 0) + row['charges']
        region_counts[region] = region_counts.get(region, 0) + 1
    return {region: region_totals[region]/region_counts[region] for region in region_totals}

def correlation_bmi_charges(data):
    """Calculate correlation between BMI and charges."""
    n = len(data)
    mean_bmi = sum(row['bmi'] for row in data) / n
    mean_charges = sum(row['charges'] for row in data) / n
    
    numerator = sum((row['bmi'] - mean_bmi)*(row['charges'] - mean_charges) for row in data)
    denominator = (sum((row['bmi'] - mean_bmi)**2 for row in data) * sum((row['charges'] - mean_charges)**2 for row in data)) ** 0.5
    return numerator / denominator if denominator != 0 else 0

# -----------------------------
# Step 3: Optional class-based approach
# -----------------------------
class InsuranceDataset:
    def __init__(self, data):
        self.data = data
    
    def average_charge(self):
        return sum(row['charges'] for row in self.data) / len(self.data)
    
    def average_charge_by_smoker(self):
        smokers = [row['charges'] for row in self.data if row['smoker'] == 'yes']
        non_smokers = [row['charges'] for row in self.data if row['smoker'] == 'no']
        return {
            "smokers": sum(smokers)/len(smokers) if smokers else 0,
            "non_smokers": sum(non_smokers)/len(non_smokers) if non_smokers else 0
        }
    
    def average_charge_by_region(self):
        region_totals = {}
        region_counts = {}
        for row in self.data:
            region = row['region']
            region_totals[region] = region_totals.get(region, 0) + row['charges']
            region_counts[region] = region_counts.get(region, 0) + 1
        return {region: region_totals[region]/region_counts[region] for region in region_totals}

    def correlation_bmi_charges(self):
        n = len(self.data)
        mean_bmi = sum(row['bmi'] for row in self.data) / n
        mean_charges = sum(row['charges'] for row in self.data) / n
        
        numerator = sum((row['bmi'] - mean_bmi)*(row['charges'] - mean_charges) for row in self.data)
        denominator = (sum((row['bmi'] - mean_bmi)**2 for row in self.data) * sum((row['charges'] - mean_charges)**2 for row in self.data)) ** 0.5
        return numerator / denominator if denominator != 0 else 0

# -----------------------------
# Step 4: Run analyses
# -----------------------------
# Using functions
print("Average insurance charge:", average_charge(insurance_data))
print("Average charge by smoker:", average_charge_by_smoker(insurance_data))
print("Average charge by region:", average_charge_by_region(insurance_data))
print("Correlation between BMI and charges:", correlation_bmi_charges(insurance_data))

# Using class
dataset = InsuranceDataset(insurance_data)
print("\n[Class-based approach]")
print("Average insurance charge:", dataset.average_charge())
print("Average charge by smoker:", dataset.average_charge_by_smoker())
print("Average charge by region:", dataset.average_charge_by_region())
print("Correlation between BMI and charges:", dataset.correlation_bmi_charges())

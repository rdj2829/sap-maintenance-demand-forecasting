import pandas as pd
import numpy as np
from datetime import timedelta, date

def generate_mock_sap_logs(num_days=1095, num_skus=50):
    """Generates 3+ years of daily maintenance usage logs."""
    
    print("Generating synthetic SAP maintenance logs...")
    dates = [date(2021, 1, 1) + timedelta(days=i) for i in range(num_days)]
    
    # Industrial/Mechanical SKUs to simulate a real maintenance environment
    sku_prefixes = ['Air_Filter_Eco', 'Hydraulic_Valve', 'O_Ring_Seal', 'Synthetic_Oil_Drum', 'Sensor_Assy']
    skus = [f"{np.random.choice(sku_prefixes)}_{i:03d}" for i in range(1, num_skus + 1)]
    
    data = []
    for d in dates:
        for sku in skus:
            # Simulate baseline usage with some random noise and seasonal spikes
            base_usage = np.random.poisson(lam=2)
            is_high_season = 1 if d.month in [6, 7, 12] else 0  # Summer and Year-end maintenance
            
            usage = base_usage + (np.random.randint(2, 5) * is_high_season)
            
            data.append({
                'Date': d,
                'SKU': sku,
                'Quantity_Used': usage,
                'Stock_Level': np.random.randint(10, 500) # Mock stock level
            })
            
    df = pd.DataFrame(data)
    
    # Exporting using openpyxl to mimic SAP Excel extracts
    output_path = 'data/raw_sap_export.xlsx'
    df.to_excel(output_path, index=False, engine='openpyxl')
    print(f"✅ Mock data generated successfully at: {output_path}")

if __name__ == "__main__":
    generate_mock_sap_logs()

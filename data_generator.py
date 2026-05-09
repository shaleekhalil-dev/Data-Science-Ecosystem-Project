import pandas as pd
import numpy as np

def generate_consumer_data(n_users=500):
    np.random.seed(42)
    
    data = {
        'UserID': range(1001, 1001 + n_users),
        'Age': np.random.randint(18, 65, size=n_users),
        'SessionDuration_Min': np.random.uniform(1, 60, size=n_users).round(2),
        'PagesVisited': np.random.randint(1, 25, size=n_users),
        'DeviceType': np.random.choice(['Mobile', 'Desktop', 'Tablet'], size=n_users),
        'LastPurchaseDaysAgo': np.random.randint(0, 365, size=n_users)
    }
    
    df = pd.DataFrame(data)
    
    # محاكاة منطق التنبؤ: احتمالية الشراء تزداد مع زيادة وقت الجلسة وعدد الصفحات
    # نستخدم دالة sigmoid بسيطة لتحديد احتمالية التحويل (Conversion)
    prob = 1 / (1 + np.exp(-(0.1 * df['SessionDuration_Min'] + 0.2 * df['PagesVisited'] - 5)))
    df['Conversion'] = np.random.binomial(1, prob)
    
    df.to_csv('data/consumer_behavior_data.csv', index=False)
    print(f"Consumer behavior data for {n_users} users generated in data/ folder.")

if __name__ == "__main__":
    generate_consumer_data()
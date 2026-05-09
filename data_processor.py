import pandas as pd

def process_ecosystem_data():
    # تحميل البيانات
    df = pd.read_csv('data/consumer_behavior_data.csv')
    
    # 1. تقسيم الأعمار إلى فئات (Bining)
    bins = [18, 30, 45, 65]
    labels = ['Young (18-30)', 'Adult (31-45)', 'Senior (46-65)']
    df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)
    
    # 2. حساب معدل التحويل حسب نوع الجهاز
    device_conversion = df.groupby('DeviceType')['Conversion'].mean() * 100
    
    # 3. حساب معدل التحويل حسب الفئة العمرية
    age_conversion = df.groupby('AgeGroup')['Conversion'].mean() * 100
    
    # 4. إحصائيات عامة
    total_users = len(df)
    overall_conversion = df['Conversion'].mean() * 100
    avg_session = df['SessionDuration_Min'].mean()
    
    summary_report = f"""
    Consumer Behavior & Ecosystem Analysis
    ======================================
    Total Users Analyzed: {total_users}
    Overall Conversion Rate: {overall_conversion:.2f}%
    Average Session Duration: {avg_session:.2f} minutes
    
    Conversion Rate by Device Type:
    {device_conversion.to_string()}
    
    Conversion Rate by Age Group:
    {age_conversion.to_string()}
    """
    
    # حفظ الملخص
    with open('outputs/ecosystem_summary.txt', 'w', encoding='utf-8') as f:
        f.write(summary_report)
    
    print("Data processing complete. Insights generated in outputs/ folder.")

if __name__ == "__main__":
    process_ecosystem_data()
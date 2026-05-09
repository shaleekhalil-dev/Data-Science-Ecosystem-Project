import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_visualizations():
    # تحميل البيانات
    df = pd.read_csv('data/consumer_behavior_data.csv')
    
    # تحديد تنسيق الرسوم
    sns.set_theme(style="whitegrid")
    
    # الرسم الأول: معدل التحويل حسب نوع الجهاز (Bar Chart)
    plt.figure(figsize=(10, 6))
    device_data = df.groupby('DeviceType')['Conversion'].mean().reset_index()
    sns.barplot(x='DeviceType', y='Conversion', data=device_data, palette='magma')
    plt.title('Conversion Rate by Device Type')
    plt.ylabel('Conversion Rate (Percentage)')
    plt.xlabel('Device Type')
    plt.savefig('figures/device_conversion.png')
    plt.close()
    
    # الرسم الثاني: العلاقة بين مدة الجلسة والتفاعل (Scatter Plot)
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='SessionDuration_Min', y='PagesVisited', hue='Conversion', 
                    data=df, alpha=0.7, palette={1: 'green', 0: 'red'})
    plt.title('Session Duration vs Pages Visited (Colored by Conversion)')
    plt.xlabel('Session Duration (Minutes)')
    plt.ylabel('Number of Pages Visited')
    plt.legend(title='Converted', labels=['No', 'Yes'])
    plt.savefig('figures/behavior_scatter.png')
    plt.close()
    
    print("Visualizations created successfully in figures/ folder.")

if __name__ == "__main__":
    create_visualizations()
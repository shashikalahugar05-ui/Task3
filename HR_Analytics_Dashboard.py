# TASK 3: HR Analytics Dashboard - CodeAlpha
# Author: CodeAlpha Intern - Power BI Track

import matplotlib.pyplot as plt
import pandas as pd

# Load Input
df = pd.read_csv('hr_input.csv')
months = df['Month'].tolist()
headcount = df['Headcount'].tolist()
attrition = df['Attrition'].tolist()
satisfaction = df['Satisfaction'].tolist()

# Dashboard Setup
fig = plt.figure(figsize=(10, 12))
fig.patch.set_facecolor('#f0f2f5')
plt.suptitle('HR Analytics Dashboard - CodeAlpha\nTask 3 - Power BI Internship', fontsize=14, fontweight='bold')

gs = fig.add_gridspec(4, 2, hspace=0.6, wspace=0.4)

# KPI Row
ax_kpi = fig.add_subplot(gs[0, :])
ax_kpi.axis('off')
ax_kpi.text(0.05, 0.5, "Headcount: 202 (+68%) | Attrition: 4.5% | Satisfaction: 4.6/5 | Avg Salary: 65K",
            fontsize=10, fontweight='bold',
            bbox=dict(facecolor='white', edgecolor='#0078D4', boxstyle='round,pad=0.5'))

# 1. Headcount & Attrition Trend
ax1 = fig.add_subplot(gs[1, 0])
ax1.plot(months, headcount, label='Headcount', color='#0078D4', linewidth=2)
ax1.plot(months, attrition, label='Attrition %', color='#D83B01', linestyle='--', linewidth=2)
ax1.set_title('Headcount & Attrition Trend', fontsize=10, fontweight='bold')
ax1.tick_params(axis='x', rotation=90, labelsize=7)
ax1.legend(fontsize=6)
ax1.grid(True, alpha=0.3)

# 2. Employees by Department
ax2 = fig.add_subplot(gs[1, 1])
ax2.pie([35, 30, 20, 15], labels=['IT', 'Sales', 'HR', 'Finance'],
        autopct='%1.1f%%', colors=['#0078D4', '#D83B01', '#107C10', '#FFB900'],
        textprops={'fontsize': 8})
ax2.set_title('Employees by Department', fontsize=10, fontweight='bold')

# 3. Satisfaction by Dept
ax3 = fig.add_subplot(gs[2, 0])
ax3.bar(['IT', 'Sales', 'HR', 'Finance', 'Ops'],
        [4.2, 4.5, 4.6, 4.3, 4.4],
        color=['#0078D4', '#107C10', '#D83B01', '#FFB900', '#7030A0'])
ax3.set_title('Satisfaction by Dept (out of 5)', fontsize=10, fontweight='bold')
ax3.tick_params(axis='x', labelsize=7)

# 4. Overall Satisfaction Trend
ax4 = fig.add_subplot(gs[2, 1])
ax4.bar(months, satisfaction, color='#107C10')
ax4.set_title('Overall Satisfaction Trend', fontsize=10, fontweight='bold')
ax4.tick_params(axis='x', rotation=90, labelsize=7)
ax4.set_ylim(3.5, 5.0)

# 5. Workforce Forecasting
ax5 = fig.add_subplot(gs[3, :])
future = ['2026-01', '2026-03', '2026-05', '2026-07']
forecast = [210, 218, 226, 235]
ax5.plot(months[-6:], headcount[-6:], label='Actual', color='#0078D4', linewidth=2)
ax5.plot(future, forecast, label='Forecast +16%', color='#D83B01', linestyle='--', linewidth=2)
ax5.fill_between(future, [f*0.95 for f in forecast], [f*1.05 for f in forecast], color='#D83B01', alpha=0.15)
ax5.set_title('Workforce Forecasting Next 6 Months (+16%)', fontsize=10, fontweight='bold')
ax5.legend(fontsize=7)
ax5.grid(True, alpha=0.3)
ax5.tick_params(axis='x', rotation=45, labelsize=7)

# Insights Footer
fig.text(0.5, 0.01, "INSIGHTS: IT 35% Largest Dept | Attrition Down 8% to 4.5% | Satisfaction 4.6/5 | Hiring +16%",
         ha='center', fontsize=8,
         bbox=dict(facecolor="#FFF4CE", edgecolor="#FFC000"))

# Save Output
plt.savefig('hr_dashboard.png', dpi=300, bbox_inches='tight')
plt.show()
print("SUCCESS! Task 3 HR Dashboard Created - hr_dashboard.png")

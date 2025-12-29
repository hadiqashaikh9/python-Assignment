import matplotlib.pyplot as plt

activities = ['Social Media', 'Study', 'Gaming', 'Videos', 'Other']
hours = [3, 5, 2, 4, 1]

plt.pie(hours, labels=activities, autopct='%1.1f%%', startangle=90)
plt.title('Daily Screen Time of a User')
plt.show()

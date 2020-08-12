# Officer Deshaun
plt.plot(deshaun.day_of_week, deshaun.hours_worked, label='Deshaun')

# Add a label to Aditya's plot
plt.plot(aditya.day_of_week, aditya.hours_worked, label='Aditya')

# Add a label to Mengfei's plot
plt.plot(mengfei.day_of_week, mengfei.hours_worked, label='Mengfei')

# Add a command to make the legend display
plt.legend()

# Display plot
plt.show()


# Lines
plt.plot(deshaun.day_of_week, deshaun.hours_worked, label='Deshaun')
plt.plot(aditya.day_of_week, aditya.hours_worked, label='Aditya')
plt.plot(mengfei.day_of_week, mengfei.hours_worked, label='Mengfei')

# Add a title
plt.title("Officers Spent Time")

# Add y-axis label
plt.ylabel("Hours Worked")

# Legend
plt.legend()
# Display plot
plt.show()


# Create plot
plt.plot(six_months.month, six_months.hours_worked)

# Add annotation "Missing June data" at (2.5, 80)
plt.text(2.5, 80, "Missing June data")

# Display graph
plt.show()

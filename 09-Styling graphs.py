# Change the color of Phoenix to `"DarkCyan"`
plt.plot(data["Year"], data["Phoenix Police Dept"], label="Phoenix", color="DarkCyan")

# Make the Los Angeles line dotted
plt.plot(data["Year"], data["Los Angeles Police Dept"], label="Los Angeles", linestyle=':')

# Add square markers to Philedelphia
plt.plot(data["Year"], data["Philadelphia Police Dept"], label="Philadelphia", marker='s')

# Add a legend
plt.legend()

# Display the plot
plt.show()


# Change the style to fivethirtyeight
plt.style.use('fivethirtyeight')

# Plot lines
plt.plot(data["Year"], data["Phoenix Police Dept"], label="Phoenix")
plt.plot(data["Year"], data["Los Angeles Police Dept"], label="Los Angeles")
plt.plot(data["Year"], data["Philadelphia Police Dept"], label="Philadelphia")

# Add a legend
plt.legend()

# Display the plot
plt.show()


# Change the style to ggplot
plt.style.use('ggplot')

# Plot lines
plt.plot(data["Year"], data["Phoenix Police Dept"], label="Phoenix")
plt.plot(data["Year"], data["Los Angeles Police Dept"], label="Los Angeles")
plt.plot(data["Year"], data["Philadelphia Police Dept"], label="Philadelphia")

# Add a legend
plt.legend()

# Display the plot
plt.show()


# Choose any of the styles
print(plt.style.available)

plt.style.use('fivethirtyeight')

# Plot lines
plt.plot(data["Year"], data["Phoenix Police Dept"], label="Phoenix")
plt.plot(data["Year"], data["Los Angeles Police Dept"], label="Los Angeles")
plt.plot(data["Year"], data["Philadelphia Police Dept"], label="Philadelphia")

# Add a legend
plt.legend()

# Display the plot
plt.show()


# x should be ransom.letter and y should be ransom.frequency
plt.plot(ransom.letter, ransom.frequency,
         # Label should be "Ransom"
         label="Ransom",
         # Plot the ransom letter as a dotted gray line
         linestyle=':', color='gray')

# Display the plot
plt.show()


# Plot each line
plt.plot(ransom.letter, ransom.frequency,
         label='Ransom', linestyle=':', color='gray')

# X-values should be suspect1.letter
# Y-values should be suspect1.frequency
# Label should be "Fred Frequentist"
plt.plot(suspect1.letter, suspect1.frequency, label="Fred Frequentist")

# Display the plot
plt.show()


# Plot each line
plt.plot(ransom.letter, ransom.frequency,
         label='Ransom', linestyle=':', color='gray')
plt.plot(suspect1.letter, suspect1.frequency,
         label='Fred Frequentist')

# X-values should be suspect2.letter
# Y-values should be suspect2.frequency
# Label should be "Gertrude Cox"
plt.plot(suspect2.letter, suspect2.frequency, label="Gertrude Cox")

# Display plot
plt.show()


# Plot each line
plt.plot(ransom.letter, ransom.frequency,
         label='Ransom', linestyle=':', color='gray')
plt.plot(suspect1.letter, suspect1.frequency, label='Fred Frequentist')
plt.plot(suspect2.letter, suspect2.frequency, label='Gertrude Cox')

# Add x- and y-labels
plt.xlabel("Letter")
plt.ylabel("Frequency")

# Add a legend
plt.legend()

# Display plot
plt.show()




# Define variables
GDP_initial = 26  # Initial GDP (in trillion dollars)
tax_rate = 0.30  # 30% tax rate
regulation_impact = 0.05  # Impact of deregulation (5% increase in GDP)
tariff_rate = 0.10  # 10% tariff on imports
business_investment_rate = 0.15  # 15% increase in investment due to tax cuts
gov_spending_rate = 0.20  # Government spending as a percentage of GDP
debt_interest_rate = 0.03  # Interest rate on debt (3%)

# Initial debt and GDP
debt = 36  # Initial debt in trillion dollars
GDP = GDP_initial

# Function to model economic growth with Trumponomics and calculate debt
def trumponomics_with_debt(GDP, tax_rate, regulation_impact, tariff_rate, business_investment_rate, debt, gov_spending_rate, debt_interest_rate):
	# Step 1: Calculate tax revenue (tax rate * GDP)
	tax_revenue = GDP * tax_rate
	
	# Step 2: Government spending (spending rate * GDP)
	government_spending = GDP * gov_spending_rate
	
	# Step 3: If spending exceeds revenue, increase debt
	if government_spending > tax_revenue:
		debt_increase = government_spending - tax_revenue
		debt += debt_increase
	
	# Step 4: Apply interest to the current debt
	debt += debt * debt_interest_rate
	
	# Step 5: Tax cuts and business investment increase GDP
	GDP_after_tax_cut = GDP + (GDP * business_investment_rate)
	
	# Step 6: Deregulation further increases GDP
	GDP_after_deregulation = GDP_after_tax_cut + (GDP_after_tax_cut * regulation_impact)
	
	# Step 7: Tariffs reduce imports but boost domestic production
	GDP_after_tariff = GDP_after_deregulation + (GDP_after_deregulation * tariff_rate)
	
	# Return new GDP and updated debt
	return GDP_after_tariff, debt

# Calculate the new GDP and debt after applying Trumponomics policies
new_GDP, new_debt = trumponomics_with_debt(GDP, tax_rate, regulation_impact, tariff_rate, business_investment_rate, debt, gov_spending_rate, debt_interest_rate)

print(f"New GDP after applying Trumponomics: ${new_GDP:.2f} trillion")
print(f"New debt after applying policies: ${new_debt:.2f} trillion")

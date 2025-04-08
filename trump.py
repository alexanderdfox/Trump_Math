def calculate_us_reciprocal_tariff(partner_tariff_rate, us_import_value, us_export_value):
	"""
	Calculates the U.S. reciprocal tariff based on the USTR formula.
	
	Parameters:
		partner_tariff_rate (float): Partner country's average tariff rate (e.g. 0.10 for 10%)
		us_import_value (float): U.S. import value from the partner country (in USD)
		us_export_value (float): U.S. export value to the partner country (in USD)

	Returns:
		float: The U.S. reciprocal tariff in USD
	"""
	reciprocal_tariff = (partner_tariff_rate / (partner_tariff_rate + 1)) * (us_import_value + us_export_value) - us_import_value
	return reciprocal_tariff


# Approximate real-world data (as of recent estimates)
trade_partners = {
	"Canada": {
		"tariff_rate": 0.035,
		"us_imports": 350_000_000_000,
		"us_exports": 360_000_000_000
	},
	"European Union": {
		"tariff_rate": 0.05,
		"us_imports": 500_000_000_000,
		"us_exports": 450_000_000_000
	},
	"China": {
		"tariff_rate": 0.075,
		"us_imports": 450_000_000_000,
		"us_exports": 150_000_000_000
	},
	"Japan": {
		"tariff_rate": 0.025,
		"us_imports": 135_000_000_000,
		"us_exports": 75_000_000_000
	},
	"Mexico": {
		"tariff_rate": 0.04,
		"us_imports": 400_000_000_000,
		"us_exports": 300_000_000_000
	}
}

# Print results
for country, data in trade_partners.items():
	tariff = calculate_us_reciprocal_tariff(
		data["tariff_rate"],
		data["us_imports"],
		data["us_exports"]
	)
	print(f"{country} — U.S. Reciprocal Tariff: ${tariff:,.2f}")
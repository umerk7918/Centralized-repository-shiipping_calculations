class ShippingCalculator:
    def __init__(self):
        # --- Configuration / Base Rates ---
        # Real-world mein ye values Database se aayengi
        self.BASE_HANDLING_FEE = 50.0  # Fixed charge
        self.RATE_PER_KG = 20.0        # Charge per Kilogram
        self.RATE_PER_KM = 5.0         # Charge per Kilometer
        self.EXPRESS_MULTIPLIER = 1.5  # Express shipping 1.5x mehngi hogi

    def calculate_cost(self, weight_kg, distance_km, method="standard"):
        """
        Calculate total shipping cost based on weight, distance, and method.
        """
        # 1. Validation (Check inputs)
        if weight_kg <= 0 or distance_km <= 0:
            return {"error": "Weight and distance must be greater than zero."}

        # 2. Core Calculation Logic
        weight_cost = weight_kg * self.RATE_PER_KG
        distance_cost = distance_km * self.RATE_PER_KM
        
        subtotal = self.BASE_HANDLING_FEE + weight_cost + distance_cost

        # 3. Apply Shipping Method Logic (Standard vs Express)
        final_total = subtotal
        if method.lower() == "express":
            final_total = subtotal * self.EXPRESS_MULTIPLIER

        # 4. Return Structured Data (JSON friendly format)
        return {
            "status": "success",
            "details": {
                "weight_kg": weight_kg,
                "distance_km": distance_km,
                "method": method,
                "base_fee": self.BASE_HANDLING_FEE,
                "per_kg_cost": weight_cost,
                "per_km_cost": distance_cost
            },
            "total_cost": round(final_total, 2),
            "currency": "INR"
        }

# --- Main Execution (Testing the code) ---
if __name__ == "__main__":
    # Calculator ka object banaya
    calculator = ShippingCalculator()

    print("--- Test 1: Standard Shipping ---")
    quote1 = calculator.calculate_cost(weight_kg=10, distance_km=100, method="standard")
    print(quote1)

    print("\n--- Test 2: Express Shipping (Faster) ---")
    quote2 = calculator.calculate_cost(weight_kg=5, distance_km=50, method="express")
    print(quote2)

from estimator import estimate_event_cost as es

def negotiate_final_cost(cost_details):

    service_items = {
        key: value for key, value in cost_details.items()
        if isinstance(value, dict)
        and 'base_cost' in value and 'flexibility' in value
    }
    discounts = cost_details.get('possible_discounts')

    messages = []
    base_total = cost_details['total_base_cost']
    final_total = 0

    # service-wise negotiation
    for service, details in service_items.items():
        base = details['base_cost']
        flex = details['flexibility']

        # discount based on flexibility
        if flex >= 9:
            discount = 0.15
        elif flex >= 6:
            discount = 0.10
        elif flex >= 3:
            discount = 0.05
        else:
            discount = 0.0

        discount_amount = base * discount
        final_price = base - discount_amount

        final_total += final_price
        messages.append(f"{service}: base Rs.{base} → discount Rs.{round(discount_amount)} (flexibility {flex})")

    # price calculation after global discounts
    active_discounts = [f"{name.replace('_', ' ').title()}: {int(val*100)}%" for name, val in discounts.items() if val > 0]

    global_discount_percent = sum(discounts.values())
    global_discount_amount = final_total * global_discount_percent
    grand_total = final_total - global_discount_amount
    messages.append(f"\nBase Total: Rs.{round(base_total)}")
    messages.append(f"Final Total (After Negotiations): Rs.{round(final_total)}")
    messages.append(f"\nGlobal Discounts Applied ({', '.join(active_discounts) if active_discounts else 'No Global Discounts'}): {int(global_discount_percent * 100)}% → Rs.{round(global_discount_amount)}")
    messages.append(f"\n🧾 Final Estimated Cost: Rs.{round(grand_total)}")

    return messages

# Example usage
if __name__ == "__main__":
    services = ['Venue', 'Catering', 'Photography', 'DJ']
    guests = 100
    estimated_cost = es(services, guests, event_season='off_season', early_booking=True)
    negotiated = negotiate_final_cost(estimated_cost)

    print("\n--- Negotiation Summary ---")
    for msg in negotiated:
        print(msg)
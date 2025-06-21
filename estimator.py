import json

# load data
def load_mock_data(filepath='data/mock_vendor_data.json'):
    with open(filepath, 'r') as file:
        return json.load(file)

# estimated_cost cost for the event based on mock vendor data
def estimate_event_cost(services_selected, guest_count=100, event_season='regular', early_booking=False):
    data = load_mock_data()
    services_data = data['services']
    discounts = data['season_discounts']

    total_base_cost = 0
    estimation = {}

    # store cost and details of every service
    for service in services_selected:
        # load info of the selected service (base price and flexibility)
        service_info = services_data[service]

        # catering cost calculation
        if service == 'Catering':
            base_cost = service_info['base_price_per_person'] * guest_count
        else:
            base_cost = service_info['base_price']

        estimation[service] = {
            'base_cost': base_cost,
            # flexibility = how much you are willing to negotiate (on the scale of 0 to 9)
            # while 0 being non-negotiable and 9 being highly negotiable
            'flexibility': service_info['flexibility']
        }

        total_base_cost += base_cost

    # store cost and discount details
    estimation['total_base_cost'] = total_base_cost
    estimation['early_booking'] = early_booking
    estimation['event_season'] = event_season
    # store global discounts if applicable
    estimation['possible_discounts'] = {
        'early_booking': discounts['early_booking'] if early_booking else 0,
        'off_season': discounts['off_season'] if event_season == 'off_season' else 0,
        'combo_discount': discounts['combo_discount'] if len(services_selected) >= 4 else 0
    }

    return estimation

# run estimator.py
if __name__ == "__main__":
    selected_services = ['Venue', 'Catering', 'Photography']
    print("-------- Event Cost Estimator ---------")

    guests = 100
    result = estimate_event_cost(selected_services, guests, event_season='off_season', early_booking=True)

    print("\n--- Estimation Results ---")
    for key, value in result.items():
        print(f"{key}: {value}")

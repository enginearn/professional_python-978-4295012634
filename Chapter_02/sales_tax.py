#!/bin/bash/env python3

TAX_RATES_BY_STATE = {
    'UT': 0.0685,
    'NV': 0.08,
    'TX': 0.0625,
    'AL': 0.04,
    'CA': 0.0825
}

def add_sales_tax(total, state):
    """Add sales tax to a total."""
    tax_rate = TAX_RATES_BY_STATE[state]
    return total + total * tax_rate

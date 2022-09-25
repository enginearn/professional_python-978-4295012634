#!/usr/bin/env python

from sales_tax import add_sales_tax

def main():
    """Main entry point for the script."""
    total = 100
    state = 'UT'
    total_with_tax = add_sales_tax(total, state)
    print(total_with_tax)

if __name__ == '__main__':
    main()

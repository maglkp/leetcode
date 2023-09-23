import pandas as pd


# 1757. Recyclable and Low Fat Products
def find_products(products: pd.DataFrame) -> pd.DataFrame:
    lf_rec_products = products[(products.low_fats == 'Y') & (products.recyclable == 'Y')]
    return lf_rec_products[['product_id']]

# 183. Customers Who Never Order
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    cust_order = pd.merge(customers, orders, how='left', left_on='id', right_on= 'customerId')
    f = cust_order['id_y'].isna()
    #print(cust_order[['id_y']])
    #print(cust_order['id_y'])
    return cust_order[f][['name']].rename(columns={'name': 'Customers'})

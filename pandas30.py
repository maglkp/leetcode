import pandas as pd


# 1757. Recyclable and Low Fat Products
def find_products(products: pd.DataFrame) -> pd.DataFrame:
    lf_rec_products = products[(products.low_fats == 'Y') & (products.recyclable == 'Y')]
    return lf_rec_products[['product_id']]


# 183. Customers Who Never Order
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    cust_order = pd.merge(customers, orders, how='left', left_on='id', right_on='customerId')
    f = cust_order['id_y'].isna()
    # print(cust_order[['id_y']])
    # print(cust_order['id_y'])
    return cust_order[f][['name']].rename(columns={'name': 'Customers'})


# Article views
def article_views(views: pd.DataFrame) -> pd.DataFrame:
    v = views[(views.author_id == views.viewer_id)]
    v = v.drop_duplicates(subset='author_id')
    v = v.rename(columns={'author_id': 'id'})
    v = v.sort_values(by='id')
    return v[['id']]


# new column
def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    tweets['len'] = tweets.apply(lambda row: len(row.content), axis=1)
    tweets = tweets[(tweets.len > 15)]
    return tweets[['tweet_id']]

# new column, sort, lambda
def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(employee_bonus, axis=1)
    return employees[['employee_id', 'bonus']].sort_values(by='employee_id')

def employee_bonus(row):
    if row['name'][0] != 'M' and row['employee_id'] % 2 == 1:
        return row['salary']
    else:
        return 0

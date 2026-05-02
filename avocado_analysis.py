import pandas as pd

# LOAD DATA
avocado = pd.read_csv('data/avocado.csv', sep='\t')
olive_oil = pd.read_csv('data/olive_oil.csv', sep='\t')
sourdough = pd.read_csv('data/sourdough.csv', sep='\t')

# LOAD CATEGORY FILES
with open("data/relevant_avocado_categories.txt") as f:
    relevant_avocado_categories = f.read().splitlines()

with open("data/relevant_olive_oil_categories.txt") as f:
    relevant_olive_oil_categories = f.read().splitlines()

with open("data/relevant_sourdough_categories.txt") as f:
    relevant_sourdough_categories = f.read().splitlines()

# KEEP ONLY RELEVANT COLUMNS
cols = [
    'code', 'lc', 'product_name_en', 'quantity', 'serving_size',
    'packaging_tags', 'brands', 'brands_tags', 'categories_tags',
    'labels_tags', 'countries', 'countries_tags', 'origins', 'origins_tags'
]

avocado = avocado[cols]
olive_oil = olive_oil[cols]
sourdough = sourdough[cols]

# FUNCTION TO CLEAN AND GET TOP ORIGIN
def get_top_origin(df, relevant_categories):

    # convert categories to list
    df['categories_list'] = df['categories_tags'].str.split(',')

    # remove missing categories
    df = df.dropna(subset=['categories_list'])

    # filter relevant categories (STRICT MATCH like system)
    df = df[
        df['categories_list'].apply(
            lambda x: any(i in relevant_categories for i in x)
        )
    ]

    # keep only UK products
    df_uk = df[df['countries'] == 'United Kingdom']

    # remove missing origins
    df_uk = df_uk[df_uk['origins_tags'].notna()]

    # find most common origin
    top_origin = df_uk['origins_tags'].value_counts().index[0]

    # clean string
    top_origin = top_origin.lstrip("en:")
    top_origin = top_origin.replace('-', ' ')

    return top_origin

# APPLY FUNCTION TO EACH INGREDIENT
top_avocado_origin = get_top_origin(avocado, relevant_avocado_categories)
top_olive_oil_origin = get_top_origin(olive_oil, relevant_olive_oil_categories)
top_sourdough_origin = get_top_origin(sourdough, relevant_sourdough_categories)

# OUTPUT
print(top_avocado_origin)
print(top_olive_oil_origin)
print(top_sourdough_origin)
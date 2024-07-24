import pyspark
import pyspark.sql


def get_product_categories_map(session, products, categories):
    """ Mapping Products and Categories"""
    try:
        products.createOrReplaceTempView("products")
        categories.createOrReplaceTempView("categories")
        query = """
            select
                p.name as product_name,
                c.name as category_name
            from products as p
            left join categories as c on (c.id = p.category_id)
        """
        return session.sql(query)
    finally:
        session.catalog.dropTempView("products")
        session.catalog.dropTempView("categories")


def main():
    """Main function containing the workflow"""
    app_name = "mindbox-pyspark"
    master = "local[*]" # or "yarn" 
    session = pyspark.sql.SparkSession.builder.appName(app_name).master(master).getOrCreate()
    products = session.read.format("parquet").load("/data/products")
    categories = session.read.format("parquet").load("/data/categories")
    result = get_product_categories_map(session, products, categories)
    result.show()


if __name__=="__main__":
    main()

from neo4j import GraphDatabase

class GraphBuilder:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_company(self, name, year_founded, market_categories, country, city,
                       description, homepage, twitter, total_funding=None, number_of_employees=None):
        query = """
        MERGE (c:Company {name: $name})
        SET c.year_founded = $year_founded,
            c.market_categories = $market_categories,
            c.country = $country,
            c.city = $city,
            c.description = $description,
            c.homepage = $homepage,
            c.twitter = $twitter,
            c.total_funding = $total_funding,
            c.number_of_employees = $number_of_employees
        """
        with self.driver.session() as session:
            session.run(query, name=name, year_founded=year_founded,
                        market_categories=market_categories, country=country,
                        city=city, description=description, homepage=homepage,
                        twitter=twitter, total_funding=total_funding,
                        number_of_employees=number_of_employees)

    def create_acquisition(self, acquirer, target, acquisition_id, year, price, status, terms):
        query = """
        MERGE (a:Company {name: $acquirer})
        MERGE (b:Company {name: $target})
        MERGE (a)-[r:ACQUIRED {acquisition_id: $acquisition_id}]->(b)
        SET r.year = $year,
            r.price = $price,
            r.status = $status,
            r.terms = $terms
        """
        with self.driver.session() as session:
            session.run(query, acquirer=acquirer, target=target,
                        acquisition_id=acquisition_id, year=year,
                        price=price, status=status, terms=terms)
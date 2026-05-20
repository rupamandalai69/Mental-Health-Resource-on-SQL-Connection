import mysql.connector


class Database:

    def __init__(self):

        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="mental_health_resources_db"
        )

        self.cursor = self.conn.cursor()

    # ADD RESOURCE
    def insert_resource(self, city, organization, helpline, website, address):

        query = """
        INSERT INTO mental_health_resources
        (city, organization_name, helpline_number, website, address)
        VALUES (%s, %s, %s, %s, %s)
        """

        values = (city, organization, helpline, website, address)

        self.cursor.execute(query, values)

        self.conn.commit()

    # SEARCH RESOURCE
    def search_resource(self, city):

        query = """
        SELECT * FROM mental_health_resources
        WHERE city = %s
        """

        self.cursor.execute(query, (city,))

        return self.cursor.fetchall()

    # VIEW ALL
    def view_all_resources(self):

        query = """
        SELECT * FROM mental_health_resources
        """

        self.cursor.execute(query)

        return self.cursor.fetchall()

    # DELETE RESOURCE
    def delete_resource(self, resource_id):

        query = """
        DELETE FROM mental_health_resources
        WHERE resource_id = %s
        """

        self.cursor.execute(query, (resource_id,))

        self.conn.commit()

    # UPDATE RESOURCE
    def update_resource(self, city, organization, helpline,
                        website, address, resource_id):

        query = """
        UPDATE mental_health_resources
        SET city=%s,
            organization_name=%s,
            helpline_number=%s,
            website=%s,
            address=%s
        WHERE resource_id=%s
        """

        values = (
            city,
            organization,
            helpline,
            website,
            address,
            resource_id
        )

        self.cursor.execute(query, values)

        self.conn.commit()
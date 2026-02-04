from model.artist import Artist

from database.DB_connect import DBConnect

class DAO:

    @staticmethod
    def get_all_roles():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor()
        query = """ select distinct role from authorship"""
        cursor.execute(query)

        for row in cursor:
            ruolo = str(row[0]).strip("(),'")
            result.append(ruolo)

        cursor.close()
        conn.close()
        return result


    @staticmethod
    def get_artists_by_role(role):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """ select a.artist_id, a.name , count(*) as p
                    from artists a, authorship au, objects o
                    where au.role = %s and au.object_id = o.object_id and o.curator_approved = 1
                    group by a.artist_id , a.name """

        cursor.execute(query, (role,))
        for row in cursor:
            result.append(Artist(id = row['artist_id'], name=row['name'], produttivita = row['p']))
        return result

    @staticmethod
    def get_nodes(role):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """ select distinct a.artist_id  
                    from artists a, authorship au , objects o 
                    where o.curator_approved = 1 and a.artist_id = au.artist_id 
                      and o.object_id = au.object_id and au.role = %s  """
        cursor.execute(query, (role,))
        for row in cursor:
            result.append(row['artist_id'])
        return result

    @staticmethod
    def get_index(artisti):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """ select a.artist_id, a.name"""


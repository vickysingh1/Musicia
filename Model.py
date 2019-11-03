import cx_Oracle


class Model:

    def __init__(self):
        self.song_dict = {}
        self.db_status = True
        self.conn = None
        self.cur = None
        try:
            self.conn =cx_Oracle.connect("mouzikka/music@127.0.0.1/xe")
            print("Connected successfully to the DB")
            self.cur = self.conn.cursor()
            print("cursor Opened")

        except cx_Oracle.DatabaseError as ex:
            print("DB Error:",ex)
            self.db_status = False

    def get_db_status(self):
        return self.db_status

    def close_db_connection(self):
        if self.cur is not None:
            self.cur.close()
            print("Cursor closed successfully")
        if self.conn is not None:
            self.conn.close()
            print("Disconnected successfully from the DB")

    def add_song(self,song_name,song_path):
        self.song_dict[song_name]=song_path
        print("song added:",song_name)
    def get_song_path(self,song_name):
        return self.song_dict[song_name]
    def remove_song(self,song_name):
        self.song_dict.pop(song_name)
        print("song removed:", song_name)



obj=Model()
obj.close_db_connection()
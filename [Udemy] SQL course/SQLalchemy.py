# SQLAlchemy
import sqlalchemy
engine = sqlalchemy.create_engine("sqlite:///movie_library.db")
connection = engine.connect()
metadata = sqlalchemy.MetaData()
movies = sqlalchemy.Table(
    "Movies", metadata, autoload=True, autoload_with=engine)

# selecting all the records in the DB
query = sqlalchemy.select([movies])
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()

# all records
# print(result_set)

# ----------------Filter Results
query = sqlalchemy.select([movies]).where(
    movies.columns.Director == "Russo Brothers")
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
# print(result_set)

# ---------------Inserting Records
query = movies.insert().values(Title="The Lion King",
                               Director="Jon Favreau", Year=2019)
connection.execute(query)
query = sqlalchemy.select([movies])
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
# print(result_set)

# -------------Filtering  Results
query = sqlalchemy.select([movies]).where(movies.columns.Year >= 2015)
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
# print(result_set)

query = sqlalchemy.select([movies]).where(movies.columns.Year <= 2015)
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
print(result_set)

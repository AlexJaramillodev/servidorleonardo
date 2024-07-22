from sqlalchemy import create_engine,MetaData

motorBD = create_engine("mysql+pymysql://root:root@localhost:3306/leonardodb")

metaDatos = MetaData()

conexion = motorBD.connect()
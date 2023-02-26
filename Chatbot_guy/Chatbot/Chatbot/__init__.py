import pymysql
pymysql.version_info= (1, 3, 13, "final", 0)
print(pymysql.__file__)
pymysql.install_as_MySQLdb()
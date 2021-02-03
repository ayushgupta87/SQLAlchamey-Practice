from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer

engine = create_engine('sqlite:///college.db', echo=True)
meta = MetaData()
students = Table('students', meta,
                 Column('id', Integer, primary_key=True),
                 Column('name', String),
                 Column('lastname', String),)
meta.create_all(engine)

insert = students.insert()
delete = students.delete()
update = students.update()
select = students.select()


conn=engine.connect()

# reterive from 'WHERE'
std= select.where(students.c.name=='Tanvi')
result=conn.execute(std)
for row in result:
    for item in row:
        print(item)

# Insert into db
result1=conn.execute(insert, name='Hello', lastname='haha')

# Update into db
result2=update.where(students.c.name == 'ye b change').values(name='change')
conn.execute(result2)

# Delete into db
result3=delete.where(students.c.name == 'change')
conn.execute(result3)

from app import db, Comment

db.session.add(Comment(
    url='http://ctf.csaw.io/',
    x=0,
    y=0,
    creator='admin',
    comment='This is where all the cool kids hang out',
))
db.session.commit()

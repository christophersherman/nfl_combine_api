from helpers.open_sql_connection import engine
from sqlalchemy import Column, Integer, String, PrimaryKeyConstraint, Numeric
from flask import Flask, request, jsonify
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


app = Flask(__name__)


Base = declarative_base()

class DraftEntry(Base):
    __tablename__ = 'drafts'
    name = Column(String)
    position = Column(String)
    college = Column(String)          
    height= Column(Numeric(6,2))             
    weight= Column(Numeric(6,2))                 
    fourty= Column(Numeric(6,2), nullable=True)         
    vertical =Column(Numeric(6,2), nullable=True) 
    bench   = Column(Integer, nullable=True) 
    broadjmp = Column(Numeric(6,2), nullable=True) 
    threecone = Column(Numeric(6,2), nullable=True) 
    shuttle =Column(Numeric(6,2), nullable=True) 

    def __init__(self, **kwargs):
        super(DraftEntry, self).__init__(**kwargs)


    __table_args__ = (
        PrimaryKeyConstraint(name, position, college),
        {},
    )

def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))

    return d

def getFromDB(query, session): #name = query_parameters.get('name')

    #change query to something cleaner
    queryString = "SELECT * FROM draft_results.drafts WHERE "
    
    
    if 'name' in query: 
        result = session.query(DraftEntry).filter_by(name=query.get("name")).all()
    
    result_dict = []

    if len(result) == 0:
        return "<h1>Name not found</h1>"
    for row in result:
        result_dict.append(row2dict(row))
        
    
    return (jsonify(result_dict))

       

@app.route('/', methods=['GET'])
def home():
    return "<h1>NFL Combine API</h1> <br></br> <p> try hitting api/players with a 'name' </p>"




@app.route('/api/players', methods=['GET'])
def api_filter():
    query_parameters = request.args
    Session = sessionmaker(bind = engine)
    session = Session()

    result = getFromDB(query_parameters, session)
    return result

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)

    

from flask import Flask, request
from flask.ext.restful import Resource, Api
app = Flask(__name__)
api = Api(app)


def filecheck():
    try:
        with open('superheros.json'):
            print ''
    except IOError:
        superheros=open('superheros.json', 'w')
        batman=         {
                            "name": "Batman",
                            "real_name": "Bruce Wayne",
                            "appearance_date": "05-1939",
                            "web_page": "http://en.wikipedia.org/wiki/Batman"
                        }
        spiderman=     {
                            "name": "Spiderman",
                            "real_name": "Peter Parker",
                            "appearance_date": "08-1962",
                            "web_page": "http://en.wikipedia.org/wiki/Spider-Man"
                        }
        superheros.append([batman])
        superheros.append([spiderman])
#        json.dump(batman, superheros)
        superheros.close()







def datecheck(appearance_date):
    if len(appearance_date)!=7:
        print 'nieprawidlowa dlugosc daty'
        return False
    elif not appearance_date[:2].isdigit():
        if int(appearance_date[:2])>12 or int(appearance_date[:2])<1:
            print 'nieprawidlowy miesiac (1-12)'
            return False
        print 'miesiac powinien byc liczba'
        return False
    elif appearance_date[2]!='-':
        print 'po miesiacu nalezy wstawic znak "-"'
        return False
    elif not appearance_date[3:].isdigit():
        print 'rok powinien byc liczba'
        return False
    else:
        return True

def sitecheck(www):
    if len(www)<11:
        return False
    elif www[:8]!='http://' and www[:9]!='https://':
        return False
    elif '.' not in www:
        return False
    else:
        return True







class superhero(Resource):
    def get(self, superhero_id):
        superheros=open('superheros.json', 'r')
        superheros.close()
        return {'superhero_id': superheros[superhero_id]},'OK',200

    def put(self, superhero_id):
        superheros=open('superheros.json', 'w')
        if superhero_id not in superheros:
            return {'not found'},404
        else:
            if len(['name'])>20:
                return {'name':'name too long' },400
            elif len(['real_name'])>50:
                return {'real_name':'real_name too long'},400
            elif datecheck(['appearance_date'])!=True:
                return {'appearance_date':'invalid date format'},400
            elif sitecheck(['web_page'])!=True:
                return {'web_page':'invalid web_page address'},400
            else:
                for i in superheros:
                    if i==superhero_id:
                        i['name']=request.form['name']
                        i['real_name']=request.form['real_name']
                        i['appearance_date']=request.form['appearance_date']
                        i['web_page']=request.form['web_page']
                superheros.close()
                return {'OK'},200

    def delete(self, superhero_id):
        superheros=open('superheros.json', 'w')
        for i in superheros:
            if i==superhero_id:
                del superheros[i]
                superheros.close()
                return{'no content'},204




class superheros(Resource):
    def post(self):
        superheros=open('superheros.json', 'r')
        if ['name'] in superheros:
            return {'name':'superhero already exists'},400
        elif len(['name'])>20:
            return {'name':'name too long' },400
        elif len(['real_name'])>50:
            return {'real_name':'real_name too long'},400
        elif datecheck(['appearance_date'])!=True:
            return {'appearance_date':'invalid date format'},400
        elif sitecheck(['web_page'])!=True:
            return {'web_page':'invalid web_page address'},400
        else:
            superhero = {
                        'name':request.form['name'],
                        'real_name':request.form['real_name'],
                        'appearance_date':request.form['appearance_date'],
                        'web_page':request.form['web_page'],
                        }
            superheros.append(superhero)
            superheros.close()
            return {'created'},201
    def get(self):
        superheros=open('superheros.json', 'r')
        superheros.close()
        return superheros,200



filecheck()



api.add_resource(superheros, '/superheros')
api.add_resource(superhero, '/superheros/<string:superhero_id>')



if __name__ == '__main__':
    app.run(debug=True)

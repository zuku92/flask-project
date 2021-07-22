from flask import Flask,render_template, url_for, request, redirect        # flask bibliotekidan imports uketebt Flask klass, render_template, url_for, request, funqciebs
from flask_sqlalchemy import SQLAlchemy                                 # imports uketebs flask_sqlalchemy bibliotekidan klass SQLAlchemy
from datetime import datetime                                           #imports vuktebt datetime biliotekidan datetime klass


app=Flask(__name__)                                               # vqmnit 'app' obieqts Flask klasis bazaze(parametrad vutitebt __main__),rac nishnavs rom es faili 'app.py' iqneba ziritadi faili
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///flask.db'       #'app' obieqtshi mivmartavt 'config'(list) obieqts, romelshic aris elementi 'SQLAlALCHEMY_DATABASE_URI' da mas vanichebt monacemta bazis tips,saxels da gafartoebas
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False               # vtishavt arasachiro chanawers config failshi(romelsac mxardachera uwkdeba)
db=SQLAlchemy(app)                                                # vqmnit 'db' obieqts 'SQLAlchemy' klasis safuzvelze da konstruqtorshi gadavcemt 'app' obieqts, romelic sheqmnilia Flask klasis bazaze


class Article(db.Model):                                     #vqmnit class 'Article' romelsac konstruqtorshi gadavcemt 'db' obieqts(anu veubnebit rom clasma monacemebi unda miigos memkvidreobit 'db' obieqtidan)
    id = db.Column(db.Integer, primary_key=True)             #vqmnit 'id' obieqts, mivmartavt 'db' obieqts da veubnebit rom sheqmnas chanaweri bazashi 'int' tipis, romelic unda iyos unikaluri(ar ganmeordes)
    title = db.Column(db.String(100), nullable=False)        #vqmnit 'title' obieqts, mivmartavt 'db' obieqts da veubnebit rom sheqmnas chanaweri bazashi 'str' tipis 100 simolos moculobit, romelic ar unda iyos cariel
    intro = db.Column(db.String(300), nullable=False)        #vqmnit 'intro' obieqts, mivmartavt 'db' obieqts da veubnebit rom sheqmnas chanaweri bazashi 'str' tipis 300 simolos moculobit, romelic ar unda iyos cariel
    text = db.Column(db.Text, nullable=False)                #vqmnit 'text' obieqts, mivmartavt 'db' obieqts da veubnebit rom sheqmnas chanaweri bazashi 'text' tipis , romelic ar unda iyos cariel
    date = db.Column(db.DateTime, default=datetime.utcnow)   #vqmnit 'Datetime' obieqts, mivmartavt 'db' obieqts da veubnebit rom sheqmnas chanaweri bazashi 'Datetime' tipis, romelsac default mnishvneloba eqneba mimdinare tarigi da dro

    def __repr__(self):                                  # classhi vizaxebt chashenebul funqcia __repr__, romelshic vabrunebt chanawers '<Article %r>' %self.id
        return '<Article %r>' % self.id                  # am chanawerit veubnebit rom roca avirchevt romelime obieqts class Article bazaze, am klasidan mogvecodeba tviton es obieqti(chanaweri bazidan) da id identifikatoric
                                                         # amis shemdeg unda gadavidet terminalidan interaqtiul rejimshi 'python' brzanebit da shevqmnat monacemta baza
                                                         # brzanebebi:
                                                         # 1. from app import db - app.py failidan imports uketebt 'db' obieqts
                                                         # 2. db.create_all() - mivmartavt db obieqts da veubnebit rom sheqmnas monacemta baza




@app.route('/')                                    # vqmnit dekoratorebs da 'route' funqciit vamocmebt URL misamartebs
@app.route('/home')
def index():                                      # vizaxebt funqcia render-templates da gadavcemt html shablons

    return render_template("index.html")           # romlebic imyofeba templates katalogshi


@app.route('/about')
def about():

    return render_template("about.html")



@app.route('/create-article',methods=['POST','GET'])                      # vqmnit axal rout-s saidanac moxdeba statiebis damateba monacemta bazashi, vutitebt rom metodma monacemebi unda miigos rogorc Post aseve Get
def create_article():                                                     # vamowmebt ra tipis monacemebia gadmocemuli metodshi
    if request.method =='POST':                                           #tu POST metoditaa vqmnit title,intro da text obieqtebs da matshi vinaxavt formidan migebul monacemebs

        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        article = Article(title=title, intro=intro, text=text)            # vqmnit article obieqts Article klasis bazaze da amit formidan migebul da shenaxul  monacemebs gadavcemt Article class, anu klasshi arsebul chanawerebshi vcert migebul monacemebs
        try:                                                              # viyenebt try: except: konstruqcias,
                                                                          # mivmartavt db obieqtshi session.add metods da argumentad gadavcemt  article obieqts
            db.session.add(article)                                       # anu es metodi monacemta bazashi daamatebs article chanacers
            db.session.commit()                                           # mivmartavs commit() metods rac monacemebs sheinaxavs bazashi
            return redirect('/posts')                                      # chanaweris damatebis shemdeg redirect() metodit vamisamartebt mtavar gverdze


        except:                                                           # ru ar daemata chanaceri bazashi gamogvaqvs shetkobineba

            return 'სტატიის დამატების შეცდომა..!'


    else:
        return render_template("create-article.html")                     #tu GET metoditaa gamogvaqvs create-article.html shabloni


@app.route('/posts')
def posts():                                                        #postebis gamosatanad vqmnit axal routs da post.html shablons templates katalogshi
    articles =Article.query.order_by(Article.date.desc()).all()      #vqmnit articles obieqts da vanichebt bazidan camogebul monacemebs
    return render_template("posts.html", articles=articles)         #bazidan monacemebi mogvaqvs shemdegnairad:
                                                                    #mivmartavt Article moduls(class) vizaxebt 'query' metods rmelic moitxovs chanacerebs bazidan
                                                                    # sgemdeg 'order_by(Article.data.desc())' metodit vaxarisxebt migebul monacemebs tarigis mixedvit, desc() metodit axal tarigs valagebt tavshi zvels boloshi
                                                                    # da boloshi utitebt 'all()' metods romelic camoigebs mtlian chanawers bazidan
                                                                    # bolos render_template metodit migebul+daxarisxebul monacemebs,romlebic inaxeba articles obieqtshi
                                                                    # gadavcemt 'posts.html' shablonshi, saxelit 'articles'
                                                                    # 'articles' saxelit mivmartavt am obieqts 'posts.html' shablonshi

@app.route('/posts/<int:id>')                                      # postis sruli teqstis gamotana: amistvis vqmnit axal rout() funqcias
def post_detail(id):                                               # romelshic gavakontrolebt postis ID-s da amis mixedvit gadavalt shesabamisi postis srul teqstze
    article =Article.query.get(id)                                 # vqmnit obieqts 'article' vizaxebt Article moduls + query metods romelic mimartavs bazas da get(id) metods romelsac gadavcemt postis ID-s da is camogebs chanacerebs ID -s mixedvit
    return render_template("post_detail.html", article=article)    # vabrunebt 'post_detail.html' shablons da masshi gadavcemt 'article' obieqts romelshic inaxeba ID -s mixedvit chanacerebi




                                                     # postis washlis realizacia
@app.route('/posts/<int:id>/del')                    # vqmnit axal rout() funqcias, romelsac gadavcemt cashashleli postis 'id'-s
def post_delete(id):                                 # vqmnit 'article' obieqts da masshi vinaxavt: vizaxebt 'Article' moduls + mivmartavt 'query' metods + get_or_404(id) metods
    article =Article.query.get_or_404(id)            # romelsac gadavcemt  postis 'id'-s, anu am id-s safuzvelze camoigebs bazidan shesabamis chanawerebs
    try:                                             # viyenebt try: except: konstruqcias, romelic daichers shecdomas tu bazastan kavshirshi moxdeba shecdoma
        db.session.delete(article)                   # mivmartavt 'db' obieqts(masshi inaxeba bazis monacemebi)+session metods romelic daamyarebs sesias bazastan+ delete(article)
        db.session.commit()                          # metods romelsac gadavcemt 'article' obieqts sadac shevinaxet cashashleli postis monacemebi, romelic cashlis chanawers bazashi
        return redirect('/posts')                    # db.session.commit()  sheinaxavs cvlilebas bazashi da shemdeg 'redirect()' metodit vamosamartebt 'posts' shblonze
    except:                                          # tu ar damyarda kavshi bazastan gamogvaqvs shetkobineba amaze
        return 'პოსტის წაშლის შეცდომა'


                                                    # postis redaqtirebis realizacia:
                                                    # rout() funqciashi gadavcemt dasaredaqtirebeli postis 'id'-s, romelic igzavneba 'post_detail.html'-dan

@app.route('/posts/<int:id>/update',methods=['POST','GET'])
def post_update(id):                                              # funqciashi gadavcemt migebul 'id'-s
    article = Article.query.get(id)                               # vqmnit 'article' obieqts 'Article' klasis bazaze, masshi vizaxebt 'query' metods mivmartavt bazas da 'get' metods gadavcemt id-s
    if request.method =='POST':                                  # vamowmebt formidan gadmogzavnis metods tu aris POST

        article.title = request.form['title']                    # formidan migebul monacemebs vcert zvel chanacerebshi
        article.intro = request.form['intro']
        article.text = request.form['text']

        try:                                                    # try: except: konstruqcia bazastan kavshiris shecdomis dasafiqsireblad tu arsebobs

            db.session.commit()                                 # tu damyarda kavshi bazastan mivmartavs 'db' obieqts, session metods
            return redirect('/posts')                          # da commit metodit vinaxavt cvlilebas bazashi


        except:

            return 'სტატიის რედაქტირების შეცდომა..!'

    else:                                                              # winaagmdeg shemtxvevashi mivmartavt 'Article' moduls, query metods, get(id) metods romelsac gadavcemt postis id-s
                                                                       # motxovnas vinaxavt 'article' obieqtshi da gadavcemt render_template funqciashi
        return render_template('post_update.html', article=article)    # am chanawerit aketebs: roca gavxsnit posts dasaredaqtireblad formashi iqneba bazidan camogebuli postis monacemebi anu forma ar iqneba carieli






@app.route('/admin')
def admin():

    return render_template("admin.html")





@app.route('/mycv')
def my_cv():

    return render_template("my_cv.html")





@app.route('/user/<string:name>/<int:id>')          # tu gvinda route funqciashi gadavamocmot ramodenime parametri
def user(name,id):                                  # URL misamartis garda momxmareblis saxeli da identifikatori magalitad
    return 'user page: '+name+'-'+str(id)          # rout-shi utitebt aset chanawers <string:name>, <int:id>


if __name__=='__main__':           # vamocmebt es faili 'app.py' tu aris rogorc mtavari faili(aqedan tu eshveba proeqti), tu moxda misi importi
    app.run(debug=True)            # 'run' metodit vushvebt lokalur servers








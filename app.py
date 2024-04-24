from flask import Flask, render_template, url_for, flash, redirect, request

from form import RegistrationForm, LoginForm

app = Flask(__name__)
app.secret_key = 'a6821e9fe9574ecd4cb17d9444dde328'
app.config['SECRET KEY'] = 'a6821e9fe9574ecd4cb17d9444dde328'
posts = [
    {
        'author': 'Jayden Briggs-Belt',
        'title': 'Playlist 1',
        'content': 'Playlist 1 Content',
        'date_posted': 'April 21,2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Playlist 2',
        'content': 'Playlist 2 Content',
        'date_posted': 'April 22,2018'
    }

]


@app.route('/')
@app.route('/home')
def home():  # put application's code here
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():  # put application's code here
    return render_template('about.html', title='About')

@app.route('/Recommender')
def Recommender():
    return render_template('Recommender.html', title='Ready To Listen?')

@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        return render_template('data.html', form_data=form_data)


@app.route('/register', methods=['Get','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login',methods=['Get','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'jabri32@morgan.edu' and form.password.data == 'JKBB2303':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)

from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import SendMessageForm

USER = {'username': 'willy'}
MESSAGES = []
# MESSAGES = [
#         {
#             'author': {'username': 'John'},
#             'body': 'Beautiful day in Portland!'
#         },
#         {
#             'author': {'username': 'Susan'},
#             'body': 'The Avengers movie was so cool!'
#         }
#     ]

@app.route('/')
@app.route('/home')
def home():
    user = USER
    messages = MESSAGES
    form = SendMessageForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('base.html', user=user, messages=messages, form=form)
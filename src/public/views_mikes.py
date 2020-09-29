"""

"""
import math
from flask import Blueprint, render_template
from .forms import LogUserForm, secti, masoform, formmikes, advancedform, octoform
from ..data.database import db
from ..data.models import LogUser


from .views import blueprint


@blueprint.route('/vystup_mikes', methods=['GET'])
def Vypis_mikes():
    pole = [0, 1], [2, 3], [20, 30]
    pole[0][1] = 10 + 1
    return render_template('public/vystup_mikes.tmpl', data=pole)


@blueprint.route('/formular_mikes', methods=['GET', 'POST'])
def Formular_mikes():
    form = formmikes()
    if form.validate_on_submit():
        '''vypocet data'''

        return str(form.a.data * form.b.data)
    return render_template("public/formular_mikes.tmpl", form=form)

@blueprint.route('/advancedform',methods=['GET','POST'])
def formular():
    form = advancedform()
    if form.validate_on_submit():
        if form.oo.data == "2" and form.obrazec.data == "1":
            hodnota=str(form.a.data*form.a.data)
            return render_template("public/vystuphodnoty.tmpl", hodnota = hodnota)
        if form.oo.data == "2" and form.obrazec.data == "2":
            hodnota=str(form.a.data*form.b.data)
            return render_template("public/vystuphodnoty.tmpl", hodnota = hodnota)
        if form.oo.data == "2" and form.obrazec.data == "3":
            return str(((form.a.data)*math.sqrt(form.a.data*form.a.data-(form.c.data*form.c.data)/2))/2)
        if form.oo.data == "1" and form.obrazec.data == "1":
            return str(4*form.a.data)
        if form.oo.data == "1" and form.obrazec.data == "2":
            return str((form.a.data+form.b.data)*2)
        if form.oo.data == "1" and form.obrazec.data == "3":
            return str(form.a.data+form.b.data+form.c.data)
        else:
            return "spatne"
    return render_template ('public/advancedform.tmpl',form = form)


@blueprint.route("/simple_chart")
def chart():
    legend = 'Monthly Data'
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    return render_template('public/graf.tmpl', values=values, labels=labels, legend=legend)



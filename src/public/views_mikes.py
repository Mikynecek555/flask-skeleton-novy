"""

"""
from flask import Blueprint, render_template
from .forms import LogUserForm, secti, masoform, formmikes, advancedform
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
    if form.validate_csrf_data():
        if form.oo.data == 1 and form.obrazec.data == 1:
            return str(form.a.data*form.a.data)
        if form.oo.data == 1 and form.obrazec.data == 2:
            return str(form.a.data*form.b.data)
        if form.oo.data == 1 and form.obrazec.data == 3:
            return str(form.a.data*form.a.data)
        if form.oo.data == 2 and form.obrazec.data == 1:
            return str(4*form.a.data)
        if form.oo.data == 2 and form.obrazec.data == 2:
            return str((form.a.data+form.b.data)*2)
        if form.oo.data == 2 and form.obrazec.data == 3:
            return str(form.a.data+form.b.data+form.c.data)
    return render_template ('public/advancedform.tmpl',form = form)

from flask_admin.contrib.sqla import ModelView


class UserView(ModelView):
    column_display_pk = True
    column_list = ('id', 'email', 'group')
    column_labels = {'id': 'Id', 'email': 'Email', 'group': 'Group'}
    form_excluded_columns = ['electives']

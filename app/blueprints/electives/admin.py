from flask_admin.contrib.sqla import ModelView


class ElectiveDistributionView(ModelView):
    column_list = ('elective', 'user')
    column_labels = {'elective': 'Elective', 'user': 'User'}

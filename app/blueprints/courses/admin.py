from flask_admin.contrib.sqla import ModelView


class GroupView(ModelView):
    column_display_pk = True
    form_excluded_columns = ['users', 'courses']


class CourseDistributionView(ModelView):
    column_display_pk = True
    column_list = ('course', 'group')
    column_labels = {'course': 'Course', 'group': 'Group'}

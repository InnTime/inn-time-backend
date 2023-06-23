from flask_admin.contrib.sqla import ModelView


class CourseDistributionView(ModelView):
    column_display_pk = True
    column_list = ('course', 'group')
    column_labels = {'course': 'Course', 'group': 'Group'}

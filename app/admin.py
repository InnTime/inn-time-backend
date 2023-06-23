from flask_admin.contrib.sqla import ModelView


class AdminView(ModelView):
    column_display_pk = True

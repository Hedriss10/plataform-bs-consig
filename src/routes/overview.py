from flask import Blueprint , render_template
from flask_login import login_required
from src.models.user import User
from flask_login import current_user, login_required


bp_overview = Blueprint("overview", __name__, template_folder="templates")


@bp_overview.route("/home")
@login_required
def home():
    """Function for process overview system"""
    return render_template("partials/dashboard.html")


@bp_overview.context_processor
def inject_user():
    return dict(current_user=current_user)


@bp_overview.route("/profile")
@login_required
def profile():
    user_id = current_user.id
    user = User.query.filter_by(user_identification=user_id).first()
    return render_template("user/profile.html", users=user)
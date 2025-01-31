from flask import Blueprint, render_template
from ckan.plugins import toolkit as tk

from ckanext.collection import shared

twdh_reports = Blueprint("twdh_reports", __name__, template_folder="templates")


def reports():
    collection = shared.get_collection("twdh-users", None)
    return render_template("reports/reports.html", collection=collection.serializer.serialize())


twdh_reports.add_url_rule("/ckan-admin/reports", "reports", reports)
# twdh_reports.add_url_rule("/api/util/collection/twdh-users/render", "user_report", user_report)


def get_blueprint():
    return twdh_reports

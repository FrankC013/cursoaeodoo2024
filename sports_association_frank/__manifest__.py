# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Sport Association Frank",
    "summary": "Manage sports association members, teams and events",
    "version": "17.0.1.0.0",
    "category": "Sports",
    "author": "<Frank>, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "base",
    ],
    "data": [
        "data/sport_license_data.xml",
        "security/groups.xml",
        "security/ir.model.access.csv",
        "views/sport_license_views.xml",
        "views/sport_issue_views.xml",
        "views/sport_menuitems.xml",
    ],
}
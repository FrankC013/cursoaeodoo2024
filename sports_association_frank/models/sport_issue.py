from odoo import models, fields

class SportIssue(models.Model):
    _name = "sport.issue"
    _description = "Sport Issue"

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
    date = fields.Date(string="Date")
    assistance = fields.Boolean(string="Assistance", help="Show if the issue has assistance")
    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("open", "Open"),
            ("done", "Done"),
        ],
        string="State",
        default="draft",
    )
    priority = fields.Selection(
        selection=[
            ("1", "Low"),
            ("2", "Medium"),
            ("3", "High"),
        ],
    )        

    def name_get(self):
        result = []
        for rec in self:
            # primero nombre y despues si existe la fecha añadirla
            name = rec.name
            if rec.date:
                name = f"{name} - ({rec.date})"
            result.append((rec.id, name))
        return result

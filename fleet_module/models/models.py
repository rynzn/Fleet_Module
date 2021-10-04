# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class VehicleFeeltRequest(models.Model):
    _inherit = 'vehicle.fleet.request'

    vehicles_color = fields.Char(related="vehicle_id.color", store="True")
    employees_identification_num = fields.Char(related="employee_id.identification_id")

    start_date = fields.Datetime(
        string='Start Date',
        default=fields.datetime.now()
    )
    end_date = fields.Datetime(
        string="End Date",
        default=fields.datetime.now() + timedelta(hours=24)
    )
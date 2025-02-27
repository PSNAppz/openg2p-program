from odoo.tests.common import TransactionCase


class TestG2PProgramRegistrantInfo(TransactionCase):
    def setUp(self):
        super().setUp()
        self.program = self.env["g2p.program"].create(
            {
                "name": "Test Program",
            }
        )
        self.partner = self.env["res.partner"].create(
            {
                "name": "Test Partner",
            }
        )
        self.g2p_program_registrant_info = self.env["g2p.program.registrant_info"]

        reg_info_model = self.env["ir.model"].search([("model", "=", "g2p.program.registrant_info")])
        self.env["ir.model.fields"].create(
            {
                "name": "x_field1",
                "ttype": "integer",
                "model": "g2p.program.registrant_info",
                "model_id": reg_info_model.id,
                "store": True,
                "depends": "program_registrant_info",
                "compute": 'for rec in self: rec["x_field1"] = 10',
            }
        )
        self.env["ir.model.fields"].create(
            {
                "name": "x_field2",
                "ttype": "float",
                "model": "g2p.program.registrant_info",
                "model_id": reg_info_model.id,
                "store": True,
                "depends": "program_registrant_info",
                "compute": 'for rec in self: rec["x_field2"] = 10',
            }
        )
        self.program_reg_info = self.g2p_program_registrant_info.create(
            {
                "registrant_id": self.partner.id,
                "program_id": self.program.id,
                "program_registrant_info": {"id": "123"},
                "x_field1": 10,
                "x_field2": 10,
            }
        )
        self.program_pmt_params = self.env["g2p.proxy_means_test_params"].create(
            [
                {
                    "pmt_field": "x_field1",
                    "pmt_weightage": 0.5,
                    "program_id": self.program.id,
                },
                {
                    "pmt_field": "x_field2",
                    "pmt_weightage": 0.3,
                    "program_id": self.program.id,
                },
            ]
        )

    def test_compute_pmt_score(self):
        self.program_reg_info._compute_pmt_score()
        self.assertAlmostEqual(8.0, 8.0)

    def test_delete_related_proxy_means_params(self):
        self.program_reg_info.delete_related_proxy_means_params("x_field1")
        self.assertTrue(param.id not in self.program_pmt_params.ids for param in self.program_pmt_params)

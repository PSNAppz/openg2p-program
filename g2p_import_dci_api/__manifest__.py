{
    "name": """OpenG2P Import: DCI API""",
    "summary": """RESTful API routes for OpenG2P""",
    "category": "",
    "version": "15.0.1.1.0",
    "author": "OpenG2P",
    "development_status": "Alpha",
    "external_dependencies": {"python": ["PyLD", "pyjwt>=2.4.0"]},
    "website": "https://openg2p.org",
    "license": "LGPL-3",
    "depends": [
        "base",
        "g2p_programs",
        "g2p_registry_base",
        "g2p_registry_individual",
        "spp_registry_data_source",
    ],
    "data": [
        "security/fetch_social_registry_security.xml",
        "security/ir.model.access.csv",
        "views/fetch_social_registry_beneficiary_views.xml",
    ],
    "application": True,
    "auto_install": False,
    "installable": True,
}

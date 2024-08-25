from flask import Blueprint
from controllers.bfhl_get import bfhl_get
from controllers.bfhl_post import bfhl_post

router = Blueprint("router", __name__)

router.add_url_rule("/bfhl", "bfhl_get", bfhl_get, methods=["GET"])
router.add_url_rule("/bfhl", "bfhl_post", bfhl_post, methods=["POST"])

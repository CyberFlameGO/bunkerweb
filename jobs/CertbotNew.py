from Job import Job

class CertbotNew(Job) :

	def __init__(self, redis_host=None, copy_cache=False, domain="", email="", staging=False) :
		name = "certbot-new"
		data = ["certbot", "certonly", "--webroot", "-w", "/opt/bunkerized-nginx/acme-challenge", "-n", "-d", domain, "--email", email, "--agree-tos"]
		if staging :
			data.append("--staging")
		type = "exec"
		super().__init__(name, data, filename=None, redis_host=redis_host, type=type, copy_cache=copy_cache)

from app.services.providers.base import Provider

class GcpProvider(Provider):
    name = "gcp"

    async def provision(self, spec):
        print("Provisioning GCP resource")
        return {"id": "gcp-123"}

    async def update(self, resource_id, spec):
        print(f"Updating GCP resource {resource_id}")
        return {"id": resource_id}

    async def destroy(self, resource_id):
        print(f"Destroying GCP resource {resource_id}")

    async def cost_estimate(self, spec):
        return {"cost": "90 USD"}

    async def validate(self, spec):
        print("Validating GCP spec")

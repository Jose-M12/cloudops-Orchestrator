from app.services.providers.base import Provider

class AzureProvider(Provider):
    name = "azure"

    async def provision(self, spec):
        print("Provisioning Azure resource")
        return {"id": "azure-123"}

    async def update(self, resource_id, spec):
        print(f"Updating Azure resource {resource_id}")
        return {"id": resource_id}

    async def destroy(self, resource_id):
        print(f"Destroying Azure resource {resource_id}")

    async def cost_estimate(self, spec):
        return {"cost": "120 USD"}

    async def validate(self, spec):
        print("Validating Azure spec")

from app.services.providers.base import Provider

class AwsProvider(Provider):
    name = "aws"

    async def provision(self, spec):
        print("Provisioning AWS resource")
        return {"id": "aws-123"}

    async def update(self, resource_id, spec):
        print(f"Updating AWS resource {resource_id}")
        return {"id": resource_id}

    async def destroy(self, resource_id):
        print(f"Destroying AWS resource {resource_id}")

    async def cost_estimate(self, spec):
        return {"cost": "100 USD"}

    async def validate(self, spec):
        print("Validating AWS spec")

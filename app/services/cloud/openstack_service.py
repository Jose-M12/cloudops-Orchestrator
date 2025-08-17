from app.services.providers.base import Provider

class OpenStackProvider(Provider):
    name = "openstack"

    async def provision(self, spec):
        print("Provisioning OpenStack resource")
        return {"id": "openstack-123"}

    async def update(self, resource_id, spec):
        print(f"Updating OpenStack resource {resource_id}")
        return {"id": resource_id}

    async def destroy(self, resource_id):
        print(f"Destroying OpenStack resource {resource_id}")

    async def cost_estimate(self, spec):
        return {"cost": "50 USD"}

    async def validate(self, spec):
        print("Validating OpenStack spec")

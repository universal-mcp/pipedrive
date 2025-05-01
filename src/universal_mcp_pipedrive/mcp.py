
from universal_mcp.servers.server import SingleMCPServer
from universal_mcp.integrations.agentr import AgentRIntegration
from universal_mcp.stores.store import EnvironmentStore

from universal_mcp_pipedrive.app import PipedriveApp

env_store = EnvironmentStore()
integration_instance = AgentRIntegration(name="pipedrive", store=env_store)
app_instance = PipedriveApp(integration=integration_instance)

mcp = SingleMCPServer(
    app_instance=app_instance,
)

if __name__ == "__main__":
    mcp.run()



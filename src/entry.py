from workers import Response, WorkerEntrypoint

class Default(WorkerEntrypoint):
    async def fetch(self, request, env, ctx):
        return await env.ASSETS.fetch(request) 
        
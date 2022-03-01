# -*- mode: Python -*-

version_settings(constraint='>=0.22.1')
load('ext://pack', 'pack')
docker_compose('docker-compose.yml')

pack('myapp',
  builder="paketobuildpacks/builder:full",
  live_update=[
    sync('.', '/workspace'),
  ]
)

curl -X PUT -H "Content-Type: application/json" http://localhost:9200/_cluster/settings?pretty  -d' { "transient": { "cluster.routing.allocation.disk.watermark.low": "1gb", "cluster.routing.allocation.disk.watermark.high": "1mb", "cluster.routing.allocation.disk.watermark.flood_stage": "1mb", "cluster.info.update.interval": "1m"}}'
curl -X PUT -H "Content-Type: application/json" http://localhost:9200/_all/_settings -d '{"index.blocks.read_only_allow_delete": null}'


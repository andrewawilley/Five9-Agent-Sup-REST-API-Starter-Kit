# Websocket behavior during an MGR Event
When an MGR event is triggered, there will be a websocket eventId: 70 with an eventReason: "STARTED"

Subsequently, there will be eventId: 1002, eventReason: "Domain Migrated, please use MetadatAPI to reload client"

The "payload" object for that message will contain the new metadata.  Here is the sample websocket message:
    
    {
        "context": {
            "eventId": "1002",
            "eventReason": "Domain Migrated, please use MetadataAPI to reload client.",
            "messageId": "106595212",
            "userId": "3578927",
            "correlationId": "5eff49b1-9f50-4d60-8bcd-61a6fcc8c278",
            "userName": "awilley@aw_tam",
            "timeStamp": 1661875378672,
            "tenantId": "131792",
            "broadCast": false
        },
        "payLoad": {
            "freedomUrl": "https://app.five9.com",
            "dataCenters": [
                {
                    "name": "Santa Clara Data Center",
                    "uiUrls": [
                        {
                            "host": "app-scl.five9.com",
                            "port": "443",
                            "routeKey": "SCLjUI96e6",
                            "version": "13.0.42"
                        }
                    ],
                    "apiUrls": [
                        {
                            "host": "app-scl.five9.com",
                            "port": "443",
                            "routeKey": "SCLjAPI013",
                            "version": "13.0.42"
                        }
                    ],
                    "loginUrls": [
                        {
                            "host": "app-scl.five9.com",
                            "port": "443",
                            "routeKey": "SCLLGNYoI4",
                            "version": "13.0.42"
                        }
                    ],
                    "active": true
                }
            ]
        }
    }

Finally you will receive eventId: 73, eventReason: "COMPLETED" when the MGR is done.  After that point, that websocket will no longer receive any "real" data.  The original host will still respond to "PING" requests, but will otherwise be dead.

    {
        "context": {
            "eventId": "73",
            "eventReason": "COMPLETED",
            "messageId": "106595273",
            "userId": null,
            "correlationId": "96a67bfd-9204-4c37-848f-39b57ded933a",
            "userName": null,
            "timeStamp": 1661875379045,
            "tenantId": "131792",
            "broadCast": true
        },
        "payLoad": "IDLE_MAINTENANCE"
    }

At this point, use the updated metadata from the payload to re-initialize the websocket and update the API method URLs with the updated location information.


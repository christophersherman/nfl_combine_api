# nfl_combine_api

Really simple get API for NFL combine statistics for players in the last ~20 years. Built for future reference 

## description
reference title
## usage 

Hosted on free AWS VPC EC2 <-> RDS  
ec2-3-26-166-9.ap-southeast-2.compute.amazonaws.com   
   
  
## GET  
### GET /api/players  


**Parameters**

|          Name | Required |  Type   | Description                                                                                                                                                           |
| -------------:|:--------:|:-------:| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|     `name` | required | string  | The name of the player who's draft-stats you require <br/><br/> needs to be exact                                                                     |
|                                                                      |

**Response**
```
// Johnny Football
[
    {
        "bench": "0",
        "broadjmp": "113.00",
        "college": "Texas A&M",
        "fourty": "4.68",
        "height": "6.00",
        "name": "Johnny Manziel",
        "position": "QB",
        "shuttle": "4.03",
        "threecone": "6.75",
        "vertical": "31.50",
        "weight": "207"
    }
]
```
## Help

PR's welcome but its just a quick and dirty flask project
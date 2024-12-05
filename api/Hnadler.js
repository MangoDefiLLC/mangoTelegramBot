const axios = require("axios")

/**this Class will handle interaction with tgBot server*/
// Not in uses. Not working.

class Handler {

    constructor(ServerEndpoint){
        this.endpoint = ServerEndpoint
    }

    async call(OBJ){
        try{
            console.log(this.endpoint)
            const response = await axios.post(`${this.endpoint}${OBJ.route}`,
            {
                params:OBJ.param,
            })
            return response.data
        } catch(e){
            console.log('CALL TO RPC FAILED\n\n',e)
        }
    }
    async tokenInfo(tokenAddress){
        let r = await this.call(
            {
            route:'/tokenInfo',
            param : tokenAddress
        })
        return r
    }
}
module.exports={Handler}
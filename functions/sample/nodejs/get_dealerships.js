/**
  *
  * main() will be run when you invoke this action
  *
  * @param Cloud Functions actions accept a single parameter, which must be a JSON object.
  *
  * @return The output of this action, which must be a JSON object.
  *
  */
 const Cloudant = require('@cloudant/cloudant');


function main(params) {  
     secret={ 
    "COUCH_URL": "https://e03960c7-5bd1-47b3-aa1a-eed32cbb0cc7-bluemix.cloudantnosqldb.appdomain.cloud",
    "IAM_API_KEY": "DfzOwkwtYdDS38XjyotiB9c12ezmP7zY9Idjh16U90E9",
    "COUCH_USERNAME": "e03960c7-5bd1-47b3-aa1a-eed32cbb0cc7-bluemix"
    };
    console.log(params);
    return new Promise(function (resolve, reject) {  
        const Cloudant = require('@cloudant/cloudant');  
        const cloudant = Cloudant({  
            url: secret.COUCH_URL,  
            plugins: {iamauth: {iamApiKey:secret.IAM_API_KEY}}  
        });  
        const dealershipDb = cloudant.use('dealerships');  
        if (params.state) {  
            // return dealership with this state  
            dealershipDb.find({ 
                "selector": { 
                "state": { 
                "$eq": params.state} } }, function (err, result) {  
                if (err) {
                    console.log("🚀 ~ file: index.js ~ line 20 ~ err", err)  
                    reject(err);
                }
                let code=200;
                if (result.docs.length==0) {
                    code= 404;
                }
                resolve({
                    statusCode: code,
                    headers: { 'Content-Type': 'application/json' },  
                    body: result
                });  
            });  
        } 
        else if (params.id) {  
            id=parseInt(params.dealerId)
          // return dealership with this state  
            dealershipDb.find({selector: {id:parseInt(params.id)}}, function (err, result) {  
                if (err) {
                    console.log("🚀 ~ file: index.js ~ line 20 ~ err", err)  
                    reject(err);  
                }  
                let code=200;  
                if (result.docs.length==0) {  
                    code= 404;
                }  
                resolve({
                    statusCode: code,  
                    headers: { 'Content-Type': 'application/json' },  
                    body: result  
                });  
            });  
        } 
        else {
            // return all documents  
            dealershipDb.list({ include_docs: true }, function (err, result) {  
                if (err) {  
                    console.log("🚀 ~ file: index.js ~ line 35 ~ err", err)  
                    reject(err);
                }
                resolve({
                    statusCode: 200,
                    headers: { 'Content-Type': 'application/json' },
                    body: result
                });
            });
        }
    });

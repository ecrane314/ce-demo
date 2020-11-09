// gs://dataflow-templates/2020-07-20-00_RC00/GCS_Text_to_BigQuery
// ce-demo2:bq_demo


function transform(line) {
    var values = line.split(',');
    
    var obj = new Object();
    obj.location = values[0];
    obj.name = values[1];
    obj.age = values[2];
    obj.color = values[3];
    obj.coffee = values[4];
    var jsonString = JSON.stringify(obj);
    
    return jsonString;
    }

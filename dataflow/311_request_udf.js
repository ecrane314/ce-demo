// gs://dataflow-templates/latest/GCS_Text_to_BigQuery
// risky, but everygreen
// ce-demo2:bq_demo


function transform(line) {
    var values = line.split(',');
    
    var obj = new Object();
    obj.unique_key = values[0];
    obj.complaint_type = values[1];
    obj.complaint_description = values[2];
    obj.owning_department = values[3];
    obj.source = values[4];
    obj.status = values[5];
    obj.status_change_date = values[6];
    obj.created_date = values[7];
    obj.last_update_date = values[8];
    obj.close_date = values[9];
    obj.incident_address = values[10];
    obj.street_number = values[11];
    obj.street_name = values[12];
    obj.city = values[13];
    obj.incident_zip = values[14];
    obj.county = values[15];
    obj.latitude = values[16];
    obj.longitude = values[17];
    var jsonString = JSON.stringify(obj);
    
    return jsonString;
    }

function filter_ops(){
            
        var table = document.getElementById('master_table');
        var rows_num = table.rows.length;
    
        if(document.getElementById("ops_select").value == "all"){
                var j;
                for(j = 0; j<rows_num-1; j++){
                    var chck_id = "chck_" + String(j);
                    if (!document.getElementById(chck_id).checked){
                        document.getElementById(chck_id).checked = true;
                        check_it(j);
                    }
                }
                document.getElementById("kpis_ops").style.display = "none";
                document.getElementById("kpis_all").style.display = "block";
        }else{
                var operator = String(document.getElementById("ops_select").value);
                
                if(operator.includes("&")){
                    operator = operator.split("&")[0];
                }
                
                var i;
                for(i = 0; i<rows_num-1; i++){
                        
                        console.log(String(table.rows[i+1].cells[2].innerHTML));
                        if(String(table.rows[i+1].cells[2].innerHTML).includes(operator)){
                                var chck_id = "chck_" + String(i);
                                if (!document.getElementById(chck_id).checked){
                                    document.getElementById(chck_id).checked = true;
                                    check_it(i);
                                }
                        }else{
                            var chck_id = "chck_" + String(i);
                            if (document.getElementById(chck_id).checked){
                                document.getElementById(chck_id).checked = false;
                                check_it(i);
                    }
                        } 
                }
                                             
                document.getElementById("ops_spaces").innerHTML = String(space_v);
                
                var price_hour_out = String(hour_v) + " " + String(currency) + " | " + String(hour_v_we) + " " + String(currency);
                var day_hour_out = String(day_v) + " " + String(currency) + " | " + String(day_v_we) + " " + String(currency);
                document.getElementById("ops_hour").innerHTML = price_hour_out;
                document.getElementById("ops_day").innerHTML = day_hour_out;
                
                document.getElementById("kpis_all").style.display = "none";
                document.getElementById("kpis_ops").style.display = "block";
        }
}
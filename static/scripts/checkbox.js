function get_change(idx,variant){
                var table = document.getElementById('master_table');
                var str = (table.rows[idx+1].cells[2+variant].innerHTML).split(" ")[0];
                var change = Number(str);

                return change;
            }

            function recalculate(value, count, change, q_value, count_q, uncheck) {
                if(change > 0){
                    var total = Number(value) * count;
                    if (uncheck == 1){
                        count = count + 1;
                        total = total + change;
                    }else{
                        count = count - 1;
                        total = total - change;
                    }
                    if(count>0){
                        value = Math.round(total / count * 100)/100;
                    }else{
                        value = 0;
                    }

                    var q_total = Number(q_value) * count_q;
                    if (uncheck == 1){
                        count_q = count_q + 1;
                        q_total = q_total + change;
                    }else{
                        count_q = count_q - 1;
                        q_total = q_total - change;
                    }
                    
                    if(count_q>0){
                        q_value = Math.round(q_total / count_q * 100)/100;
                    }else{
                        q_value = 0;
                    }

                    return [value, count, q_value, count_q];
                }else{
                    return [value, count, q_value, count_q];
                }
            }


            function checkbox(idx,mid,isqpark) {

                hour_ch = get_change(idx,3);
                day_ch = get_change(idx,4);
                hourwe_ch = get_change(idx,5);
                daywe_ch = get_change(idx,6);
                space_ch = get_change(idx,1);

                var chck_id = "chck_" + String(idx);

                if (document.getElementById(chck_id).checked){
                    var uncheck = 1;
                    mid.setOpacity(1.0);
                }else{
                    var uncheck = 0;
                    mid.setOpacity(0.5);
                }

                if(isqpark == 1){
                    var hour_calc = recalculate(hour_v,count_v1,hour_ch,hour_q_v,count_q_v1,uncheck);
                        hour_v = hour_calc[0];
                        count_v1 = hour_calc[1];
                        hour_q_v = hour_calc[2];
                        count_q_v1 = hour_calc[3];
                    var day_calc = recalculate(day_v,count_v2,day_ch,day_q_v,count_q_v2,uncheck);
                        day_v = day_calc[0];
                        count_v2 = day_calc[1];
                        day_q_v = day_calc[2];
                        count_q_v2 = day_calc[3];
                    var hourwe_calc = recalculate(hour_v_we,count_v3,hourwe_ch,hour_q_v_we,count_q_v3,uncheck);
                        hour_v_we = hourwe_calc[0];
                        count_v3 = hourwe_calc[1];
                        hour_q_v_we = hourwe_calc[2];
                        count_q_v3 = hourwe_calc[3];
                    var daywe_calc = recalculate(day_v_we,count_v4,daywe_ch,day_q_v_we,count_q_v4,uncheck);
                        day_v_we = daywe_calc[0];
                        count_v4 = daywe_calc[1];
                        day_q_v_we = daywe_calc[2];
                        count_q_v4 = daywe_calc[3];
                    if (!isNaN(space_ch)){
                        if (uncheck == 1){
                            space_v = space_v + space_ch;
                            space_q_v = space_q_v + space_ch;
                        }else{
                            space_v = space_v - space_ch;
                            space_q_v = space_q_v - space_ch;
                        }
                    }
                }else{
                    var hour_calc = recalculate(hour_v,count_v1,hour_ch,hour_nq_v,count_nq_v1,uncheck);
                        hour_v = hour_calc[0];
                        count_v1 = hour_calc[1];
                        hour_nq_v = hour_calc[2];
                        count_nq_v1 = hour_calc[3];
                    var day_calc = recalculate(day_v,count_v2,day_ch,day_nq_v,count_nq_v2,uncheck);
                        day_v = day_calc[0];
                        count_v2 = day_calc[1];
                        day_nq_v = day_calc[2];
                        count_nq_v2 = day_calc[3];
                    var hourwe_calc = recalculate(hour_v_we,count_v3,hourwe_ch,hour_nq_v_we,count_nq_v3,uncheck);
                        hour_v_we = hourwe_calc[0];
                        count_v3 = hourwe_calc[1];
                        hour_nq_v_we = hourwe_calc[2];
                        count_nq_v3 = hourwe_calc[3];
                    var daywe_calc = recalculate(day_v_we,count_v4,daywe_ch,day_nq_v_we,count_nq_v4,uncheck);
                        day_v_we = daywe_calc[0];
                        count_v4 = daywe_calc[1];
                        day_nq_v_we = daywe_calc[2];
                        count_nq_v4 = daywe_calc[3];
                    if (!isNaN(space_ch)){
                        if (uncheck == 1){
                            space_v = space_v + space_ch;
                            space_nq_v = space_nq_v + space_ch;
                        }else{
                            space_v = space_v - space_ch;
                            space_nq_v = space_nq_v - space_ch;
                        }
                    }
                }
                var space_per_q = Math.round(space_q_v / space_v * 1000) / 10;
                var space_per_nq = Math.round(space_nq_v / space_v * 1000) / 10;
                    
                var hour_out = String(hour_v) + " " + String(currency) + " | " + String(hour_v_we) + " " + String(currency);
                var day_out = String(day_v) + " " + String(currency) + " | " + String(day_v_we) + " " + String(currency);
                var hour_q_out = "Q-Park:  " + String(hour_q_v) + " " + String(currency) + " | " + String(hour_q_v_we) + " " + String(currency);
                var hour_nq_out = "Others:  " + String(hour_nq_v) + " " + String(currency) + " | " + String(hour_nq_v_we) + " " + String(currency);
                var day_q_out = "Q-Park:  " + String(day_q_v) + " " + String(currency) + " | " + String(day_q_v_we) + " " + String(currency);
                var day_nq_out = "Others:  " + String(day_nq_v) + " " + String(currency) + " | " + String(day_nq_v_we) + " " + String(currency);
                
                var space_out = String(space_v);
                var space_q_out = "Q-Park:  " + String(space_q_v) + " (" + String(space_per_q) + " %)";
                var space_nq_out = "Others:  " + String(space_nq_v) + " (" + String(space_per_nq) + " %)";

                document.getElementById("hour_h3").innerHTML = hour_out;
                document.getElementById("day_h3").innerHTML = day_out;
                document.getElementById("size_h3").innerHTML = space_out;
                document.getElementById("hour_q").innerHTML = hour_q_out;
                document.getElementById("day_q").innerHTML = day_q_out;
                document.getElementById("size_q").innerHTML = space_q_out;
                document.getElementById("hour_nq").innerHTML = hour_nq_out;
                document.getElementById("day_nq").innerHTML = day_nq_out;
                document.getElementById("size_nq").innerHTML = space_nq_out;

            }
                    
            function check_it(id){
                    var marker_id = "marker" + String(id);
                    var marker = window[marker_id];
                    var name = String(document.getElementById('master_table').rows[id].cells[2].innerHTML);
                    if (name.includes("Q-Park")){
                            var isqp = 1;
                    }else{
                            var isqp = 0;
                    }
                    checkbox(id,marker,isqp);
            }
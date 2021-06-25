function get_coordinates(){
                var coords = String(dragable.getLatLng());
                var res = coords.split("(");
                var res2 = res[1].split(",");
                var res3 = res2[1].split(" ");
                var res4 = res3[1].split(")");
                var lat = res2[0];
                var lon = res4[0];
                document.getElementById("latbox").value = lat;
                document.getElementById("lonbox").value = lon;
            }
function highlight_standard(id, number) {
                    id.setIcon(yIcon);
                    var iconn_str = new L.standardIcon({number: number});
                    setTimeout(function() {id.setIcon(iconn_str);}, 1000);
            }
            function highlight_qpark(id, number) {
                    id.setIcon(yIcon);
                    var iconn_str = new L.qparkIcon({number: number});
                    setTimeout(function() {id.setIcon(iconn_str);}, 1000);
            }
            function highlight_main(id, number) {
                    id.setIcon(yIcon);
                    var iconn_str = new L.maincompIcon({number: number});
                    setTimeout(function() {id.setIcon(iconn_str);}, 1000);
            }
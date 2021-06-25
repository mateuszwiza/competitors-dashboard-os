var locIcon = new L.Icon({
              iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-green.png',
              shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
              iconSize: [25, 41],
              iconAnchor: [12, 41],
              popupAnchor: [1, -34],
              shadowSize: [41, 41]
            });

            var yIcon = new L.Icon({
              iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-yellow.png',
              shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
              iconSize: [25, 41],
              iconAnchor: [12, 41],
              popupAnchor: [1, -34],
              shadowSize: [41, 41]
            });
    
            L.standardIcon = L.Icon.extend({
        	options: {
            iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-grey.png',
            number: '',
            shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
            iconSize: [25, 41], //new L.Point(25, 41),
        		iconAnchor: [12, 41], //new L.Point(12, 41),
        		popupAnchor: [1, -34], //new L.Point(1, -34),
                shadowSize: [41, 41],
        		className: 'leaflet-div-icon'
        	},
        
        	createIcon: function () {
        		var div = document.createElement('div');
        		var img = this._createImg(this.options['iconUrl']);
        		var numdiv = document.createElement('div');
        		numdiv.setAttribute ( "class", "number" );
        		numdiv.innerHTML = this.options['number'] || '';
        		div.appendChild ( img );
        		div.appendChild ( numdiv );
        		this._setIconStyles(div, 'icon');
        		return div;
        	},
        
        	//you could change this to add a shadow like in the normal marker if you really wanted
        	createShadow: function () {
        		return null;
        	}
            });
    
            L.qparkIcon = L.Icon.extend({
        	options: {
            iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-red.png',
            number: '',
            shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
            iconSize: [25, 41], //new L.Point(25, 41),
        		iconAnchor: [12, 41], //new L.Point(12, 41),
        		popupAnchor: [1, -34], //new L.Point(1, -34),
                shadowSize: [41, 41],
        		className: 'leaflet-div-icon'
        	},
        
        	createIcon: function () {
        		var div = document.createElement('div');
        		var img = this._createImg(this.options['iconUrl']);
        		var numdiv = document.createElement('div');
        		numdiv.setAttribute ( "class", "number" );
        		numdiv.innerHTML = this.options['number'] || '';
        		div.appendChild ( img );
        		div.appendChild ( numdiv );
        		this._setIconStyles(div, 'icon');
        		return div;
        	},
        
        	//you could change this to add a shadow like in the normal marker if you really wanted
        	createShadow: function () {
        		return null;
        	}
            });
    
            L.maincompIcon = L.Icon.extend({
        	options: {
            iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-black.png',
            number: '',
            shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
            iconSize: [25, 41], //new L.Point(25, 41),
        		iconAnchor: [12, 41], //new L.Point(12, 41),
        		popupAnchor: [1, -34], //new L.Point(1, -34),
                shadowSize: [41, 41],
        		className: 'leaflet-div-icon'
        	},
        
        	createIcon: function () {
        		var div = document.createElement('div');
        		var img = this._createImg(this.options['iconUrl']);
        		var numdiv = document.createElement('div');
        		numdiv.setAttribute ( "class", "number" );
        		numdiv.innerHTML = this.options['number'] || '';
        		div.appendChild ( img );
        		div.appendChild ( numdiv );
        		this._setIconStyles(div, 'icon');
        		return div;
        	},
        
        	//you could change this to add a shadow like in the normal marker if you really wanted
        	createShadow: function () {
        		return null;
        	}
            });
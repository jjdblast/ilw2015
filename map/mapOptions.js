var mapOptions = {
				zoom: 1,
				center: new google.maps.LatLng(55.94, -3.2),
				mapTypeId: google.maps.MapTypeId.ROADMAP
			};
			
var styles = [
{
stylers: [
	{ hue: "#67D167" },
	{ saturation: -20 }
]
},
{
featureType: "road",
elementType: "geometry",
stylers: [
	{ lightness: 100 },
	{ visibility: "simplified" }
]
},
{
featureType: "road",
elementType: "labels",
stylers: [
	{ visibility: "off" }
]
}
];
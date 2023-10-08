import React, { useState, useEffect } from "react";
import { useMapEvents } from "react-leaflet";

const useGeoLocation = () => {
  const [position, setPosition] = useState<LatLng>();
  const map = useMapEvents({
    click() {
      map.locate();
    },
    locationfound(e) {
      setPosition(e.latlng);
      map.flyTo(e.latlng, map.getZoom());
    },
  });

  return position;
};
const GetLocation = () => {
  const map = useMapEvents({
    click: (e) => {
      console.log(e.latlng);
    },
  });
  return null;
};
export default useGeoLocation;

// source: https://github.com/codegeous/react-component-depot/blob/master/src/hooks/useGeoLocation.js

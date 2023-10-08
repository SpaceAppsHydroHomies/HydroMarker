import { useEffect, useRef, useState } from "react";
import { motion } from "framer-motion";
import { RxDoubleArrowDown, RxEnterFullScreen } from "react-icons/rx";
import {
  MapContainer,
  TileLayer,
  Marker,
  Popup,
  useMapEvents,
  useMap,
} from "react-leaflet";
import "leaflet/dist/leaflet.css";
import "leaflet-geosearch/dist/geosearch.css";
import { marker } from "leaflet";

const GetLocation = (longlati: any, setLonglati: any) => {
  const map = useMapEvents({
    click: (e) => {
      map.flyTo(e.latlng, map.getZoom());
      console.log(e.latlng);
      setLonglati(e.latlng);
    },
  });
  return null;
};

const Map = (longlati: any) => {
  const mapRef = useRef(null);
  const [center, setCenter] = useState<LatLng>({
    lat: 37.719,
    lng: -97.293,
  });

  const [isExpanded, setIsExpanded] = useState(true);
  const [isFullScreen, setIsFullScreen] = useState(false);

  useEffect(() => {
    const map = mapRef.current;
    // @ts-ignore
    map?.invalidateSize();
  }, [isFullScreen]);

  return (
    <motion.div
      layout
      className="w-auto h-auto absolute bottom-5 right-5 md:right-72 bg-slate-600 rounded-xl"
      data-expanded={isExpanded}
    >
      <motion.div
        layout
        className="w-auto h-auto flex items-center justify-end"
      >
        <motion.div
          layout
          className="w-auto flex items-center p-2 gap-2 cursor-pointer"
        >
          <motion.div
            className="flex g-2 items-center"
            onClick={() => setIsExpanded(!isExpanded)}
          >
            <motion.h1 className="text-xl font-bold ">Map</motion.h1>
            <RxDoubleArrowDown size={22} />
          </motion.div>
          {isExpanded && (
            <motion.div onClick={() => setIsFullScreen(!isFullScreen)}>
              <RxEnterFullScreen size={22} />
            </motion.div>
          )}
        </motion.div>
      </motion.div>
      {isExpanded && (
        <motion.div
          layout
          className={`${
            isFullScreen ? "z-50 w-[70vw] h-[70vh]" : "w-64 h-64"
          } pb-2 px-2`}
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.2 }}
        >
          <MapContainer
            center={longlati.longlati}
            zoom={13}
            ref={mapRef}
            className="w-full h-full rounded-xl"
          >
            <TileLayer
              attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
              url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
            <Marker position={longlati.longlati} draggable={false}>
              <Popup>marked here!</Popup>
            </Marker>
            <GetLocation longlati={longlati} />
          </MapContainer>
        </motion.div>
      )}
    </motion.div>
  );
};

export default Map;
